import os
import subprocess

html_path = '/var/www/lumbros.me/deploy/homepage.html'
if not os.path.exists(html_path):
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'homepage.html'))

with open(html_path, 'r', encoding='utf-8') as f:
    raw_html = f.read()

block_content = f"<!-- wp:html -->\n{raw_html}\n<!-- /wp:html -->"

with open('/tmp/wp_block_content.txt', 'w', encoding='utf-8') as f:
    f.write(block_content)

# Check if front page already exists
cmd_check = [
    'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
    'post', 'list', '--post_type=page', '--name=nexus', '--field=ID'
]
res_check = subprocess.run(cmd_check, capture_output=True, text=True)
existing_id = res_check.stdout.strip()

if existing_id:
    print(f"Updating existing Page ID: {existing_id}")
    cmd = [
        'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
        'post', 'update', existing_id, '/tmp/wp_block_content.txt',
        '--post_title=UNITED BEATS // HYPERNEXUS NEXUS'
    ]
    subprocess.run(cmd, check=True)
    post_id = existing_id
else:
    cmd = [
        'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
        'post', 'create', '/tmp/wp_block_content.txt',
        '--post_type=page',
        '--post_title=UNITED BEATS // HYPERNEXUS NEXUS',
        '--post_name=nexus',
        '--post_status=publish',
        '--porcelain'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    post_id = res.stdout.strip()
    print(f"Created new Page ID: {post_id}")

# Configure static front page
subprocess.run(['sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me', 'option', 'update', 'show_on_front', 'page'], check=True)
subprocess.run(['sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me', 'option', 'update', 'page_on_front', post_id], check=True)

# Also update sample post 1 as well for complete consistency
cmd_post1 = [
    'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
    'post', 'update', '1', '/tmp/wp_block_content.txt',
    '--post_title=UNITED BEATS // HYPERNEXUS NEXUS'
]
subprocess.run(cmd_post1, check=True)

# Export updated database
subprocess.run([
    'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
    'db', 'export', '/var/www/lumbros.me/deploy/database.sql'
], check=True)

print("SUCCESS: Front Page and Post 1 updated and database exported!")
