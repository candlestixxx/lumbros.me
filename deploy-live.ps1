# ==============================================================================
# Live Deploy Script: Local Workspace -> GitHub -> Hetzner Production
# ==============================================================================
param(
    [string]$Message = "Update lumbros.me production deployment"
)

Write-Host "==> [1/4] Checking local Git status..." -ForegroundColor Cyan
git add -A

$status = git status --porcelain
if ($status) {
    Write-Host "==> [2/4] Committing changes..." -ForegroundColor Yellow
    git commit -m $Message
} else {
    Write-Host "==> [2/4] No local file changes to commit." -ForegroundColor DarkGray
}

Write-Host "==> [3/4] Pushing to GitHub (origin/main)..." -ForegroundColor Cyan
git push origin main

Write-Host "==> [4/4] Deploying live to Hetzner (/var/www/lumbros.me)..." -ForegroundColor Green
ssh hetzner "cd /var/www/lumbros.me && git fetch origin main && git reset --hard origin/main && cp /var/www/lumbros.me/deploy/spectrum-engine.js /var/www/lumbros.me/spectrum-engine.js && cp /var/www/lumbros.me/deploy/nginx_lumbros.me.conf /etc/nginx/sites-available/lumbros.me && chown -R www-data:www-data /var/www/lumbros.me && if [ -f /var/www/lumbros.me/deploy/deploy_page.py ]; then python3 /var/www/lumbros.me/deploy/deploy_page.py; fi && sudo -u www-data wp --path=/var/www/lumbros.me cache flush && nginx -t && systemctl reload nginx"

Write-Host "`n✔ LIVE DEPLOYMENT COMPLETE: https://lumbros.me is up to date!" -ForegroundColor Green
