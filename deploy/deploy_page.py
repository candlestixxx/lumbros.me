import os
import subprocess

def deploy_single_page(slug, title, filename):
    base_dir = '/var/www/lumbros.me/deploy'
    if not os.path.exists(base_dir):
        base_dir = os.path.abspath(os.path.dirname(__file__))

    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_html = f.read()

    block_content = f"<!-- wp:html -->\n{raw_html}\n<!-- /wp:html -->"
    tmp_path = f"/tmp/wp_block_{slug}.txt"
    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(block_content)

    # Check if page exists
    cmd_check = [
        'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
        'post', 'list', '--post_type=page', f'--name={slug}', '--field=ID'
    ]
    res_check = subprocess.run(cmd_check, capture_output=True, text=True)
    existing_id = res_check.stdout.strip()

    if existing_id:
        print(f"Updating existing Page [{slug}] (ID: {existing_id})")
        cmd = [
            'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
            'post', 'update', existing_id, tmp_path,
            f'--post_title={title}'
        ]
        subprocess.run(cmd, check=True)
        return existing_id
    else:
        print(f"Creating new Page [{slug}]")
        cmd = [
            'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
            'post', 'create', tmp_path,
            '--post_type=page',
            f'--post_title={title}',
            f'--post_name={slug}',
            '--post_status=publish',
            '--porcelain'
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        new_id = res.stdout.strip()
        print(f"Created Page [{slug}] with ID: {new_id}")
        return new_id

# 1. Front Page (nexus)
front_id = deploy_single_page('nexus', 'UNITED BEATS // HYPERNEXUS NEXUS', 'homepage.html')

# 2. Public Sector Page
public_id = deploy_single_page('public', 'UNITED BEATS // PUBLIC SECTOR // ROTATING PROJECTS', 'public.html')

# 3. Private Sector Page
private_id = deploy_single_page('private', 'UNITED BEATS // PRIVATE SECTOR // CLASSIFIED VAULT', 'private.html')

# 4. Live Posts Diary Page
posts_id = deploy_single_page('posts', 'UNITED BEATS // LIVE POSTS // TRANSMISSION DIARY', 'posts.html')

# Configure static front page
subprocess.run(['sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me', 'option', 'update', 'show_on_front', 'page'], check=True)
subprocess.run(['sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me', 'option', 'update', 'page_on_front', front_id], check=True)

# Also update sample post 1 as well for complete consistency
cmd_post1 = [
    'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
    'post', 'update', '1', '/tmp/wp_block_nexus.txt',
    '--post_title=UNITED BEATS // HYPERNEXUS NEXUS'
]
subprocess.run(cmd_post1, check=True)

# Flush rewrite rules so /posts/, /public/, /private/ permalinks work immediately
subprocess.run(['sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me', 'rewrite', 'flush'], check=True)

# Export updated database
subprocess.run([
    'sudo', '-u', 'www-data', 'wp', '--path=/var/www/lumbros.me',
    'db', 'export', '/var/www/lumbros.me/deploy/database.sql'
], check=True)

print("SUCCESS: Front Page, Public, Private, and Posts pages deployed and database exported!")
