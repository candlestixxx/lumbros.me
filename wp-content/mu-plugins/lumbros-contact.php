<?php
/**
 * Plugin Name: Lumbros Network Uplink & Contact Handler
 * Description: Handles networking inquiries, storing them in WordPress and relaying to UnitedBeatsLLC@gmail.com.
 * Version: 1.0.0
 * Author: Lumbros Kourlos & Robert Matthew Pelloni
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

add_action( 'rest_api_init', function () {
    register_rest_route( 'lumbros/v1', '/contact', array(
        'methods'             => 'POST',
        'callback'            => 'lumbros_handle_contact_submission',
        'permission_callback' => '__return_true',
    ) );
} );

add_action( 'wp_ajax_nopriv_lumbros_contact', 'lumbros_ajax_contact_submission' );
add_action( 'wp_ajax_lumbros_contact', 'lumbros_ajax_contact_submission' );

function lumbros_process_contact_data( $params ) {
    $name    = isset( $params['name'] ) ? sanitize_text_field( trim( $params['name'] ) ) : 'Anonymous Explorer';
    $email   = isset( $params['email'] ) ? sanitize_email( trim( $params['email'] ) ) : '';
    $phone   = isset( $params['phone'] ) ? sanitize_text_field( trim( $params['phone'] ) ) : 'Not provided';
    $role    = isset( $params['role'] ) ? sanitize_text_field( trim( $params['role'] ) ) : 'Inquirer / Creator';
    $message = isset( $params['message'] ) ? sanitize_textarea_field( trim( $params['message'] ) ) : '';

    if ( empty( $email ) || ! is_email( $email ) ) {
        return array(
            'success' => false,
            'message' => 'Please provide a valid email address so we can establish a quantum uplink.',
        );
    }

    $timestamp = current_time( 'mysql' );
    $ip        = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( $_SERVER['REMOTE_ADDR'] ) : 'Unknown';

    $inquiry = array(
        'timestamp' => $timestamp,
        'name'      => $name,
        'email'     => $email,
        'phone'     => $phone,
        'role'      => $role,
        'message'   => $message,
        'ip'        => $ip,
    );

    // 1. Store inside WordPress options table for persistent audit log
    $stored = get_option( 'lumbros_network_inquiries', array() );
    if ( ! is_array( $stored ) ) {
        $stored = array();
    }
    array_unshift( $stored, $inquiry );
    // Keep last 100 entries
    if ( count( $stored ) > 100 ) {
        $stored = array_slice( $stored, 0, 100 );
    }
    update_option( 'lumbros_network_inquiries', $stored, false );

    // 2. Dispatch email to UnitedBeatsLLC@gmail.com
    $to      = 'UnitedBeatsLLC@gmail.com';
    $subject = "[lumbros.me Uplink] New Network Inquiry from {$name} ({$role})";
    
    $body  = "=== LUMBROS.ME NETWORK TRANSMISSION ===\n\n";
    $body .= "Timestamp : {$timestamp}\n";
    $body .= "Sender    : {$name}\n";
    $body .= "Email     : {$email}\n";
    $body .= "Phone     : {$phone}\n";
    $body .= "Role/Field: {$role}\n";
    $body .= "Client IP : {$ip}\n\n";
    $body .= "--- MESSAGE / INQUIRY ---\n";
    $body .= ( ! empty( $message ) ? $message : "[No written message provided - Direct Networking Signal]" ) . "\n\n";
    $body .= "========================================\n";
    $body .= "Sent from HyperNexus VRL-1 node: lumbros.me\n";

    $headers = array(
        'From: lumbros.me Terminal <noreply@lumbros.me>',
        'Reply-To: ' . $email,
        'Content-Type: text/plain; charset=UTF-8',
    );

    @wp_mail( $to, $subject, $body, $headers );

    return array(
        'success'   => true,
        'message'   => 'SIGNAL TRANSMITTED // UPLINK SYNCHRONIZED TO UNITED BEATS & WORDPRESS RECORD.',
        'timestamp' => $timestamp,
    );
}

function lumbros_handle_contact_submission( WP_REST_Request $request ) {
    $params = $request->get_json_params();
    if ( empty( $params ) ) {
        $params = $request->get_body_params();
    }
    $result = lumbros_process_contact_data( $params );
    return new WP_REST_Response( $result, $result['success'] ? 200 : 400 );
}

function lumbros_ajax_contact_submission() {
    $result = lumbros_process_contact_data( $_POST );
    if ( $result['success'] ) {
        wp_send_json_success( $result );
    } else {
        wp_send_json_error( $result );
    }
}
