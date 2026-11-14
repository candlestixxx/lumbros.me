# lumbros.me

Production WordPress deployment for [lumbros.me](https://lumbros.me).

## Status

**Active Production WordPress Site.** Mirrored directly from the Hetzner production server (`5.161.250.43`).

## Stack & Architecture

- **CMS**: WordPress 7.1.4
- **Host**: Hetzner Cloud (`5.161.250.43`, Ubuntu 24.04 LTS)
- **Web Server**: Nginx with HTTP/2 and Let's Encrypt TLS
- **PHP**: PHP 8.4-FPM (`unix:/run/php/php8.4-fpm.sock`)
- **Database**: MySQL / MariaDB (`lumbros_wp`)
- **Active Theme**: `twentytwentyfive`
- **Deployment**: Git-synchronized deployment in `/var/www/lumbros.me`

## Project Structure

- `wp-admin/`, `wp-includes/`, `wp-content/`: WordPress core, themes, plugins, and uploads
- `wp-config.php`: WordPress configuration and database connectivity
- `deploy/`:
  - `database.sql`: Production database dump
  - `nginx_lumbros.me.conf`: Production Nginx virtual host configuration
  - `deploy.sh`: Automated pull, permission normalization, and Nginx reload script
  - `DEPLOY.md`: Hetzner deployment documentation and SSH runbook

## Deployment

Refer to [`deploy/DEPLOY.md`](deploy/DEPLOY.md) for full server access runbooks and maintenance instructions.

To deploy or update on Hetzner:
```bash
ssh hetzner "bash /var/www/lumbros.me/deploy/deploy.sh"
```

## Links

- Live Site: [https://lumbros.me](https://lumbros.me)
- Repository: [https://github.com/candlestixxx/lumbros.me](https://github.com/candlestixxx/lumbros.me)
