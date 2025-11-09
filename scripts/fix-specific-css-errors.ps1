# Fix specific CSS errors at reported line numbers
$file = 'About Us – Flyers Charitable Trust .html'

Write-Host "Reading file..." -ForegroundColor Cyan
$content = Get-Content $file -Raw -Encoding UTF8

Write-Host "Applying fixes..." -ForegroundColor Cyan

# Fix all CSS variable syntax issues
$content = $content -replace '([a-z-]+):\(--([a-z-]+[^)]*)\)', '$1:var(--$2)'

# Add standard properties for vendor prefixes
$content = $content -replace '(-webkit-appearance:[^;]+;)', '$1appearance:none;'
$content = $content -replace '(-webkit-backface-visibility:[^;]+;)', '$1backface-visibility:hidden;'
$content = $content -replace '(-ms-touch-action:[^;]+;)', '$1touch-action:manipulation;'
$content = $content -replace '(-webkit-filter:[^;]+;)', '$1filter:inherit;'

# Remove empty rulesets
$content = $content -replace '\{\s*\}', ''

Write-Host "Writing fixed content..." -ForegroundColor Cyan
Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline

Write-Host "Done! File has been fixed." -ForegroundColor Green
Write-Host "Please close and reopen the file in your IDE." -ForegroundColor Yellow
