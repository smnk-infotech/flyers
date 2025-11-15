# Fix all external flyerstrust.org links to use local files
# This script updates navigation links to work with local file structure

$htmlFiles = @(
    "About Us – Flyers Charitable Trust.html",
    "About-Us.html",
    "Contact US – Flyers Charitable Trust.html",
    "Donation – Flyers Charitable Trust.html",
    "Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html",
    "Gallery – Flyers Charitable Trust.html",
    "Services – Flyers Charitable Trust.html",
    "index.html"
)

Write-Host "Fixing external links to flyerstrust.org..." -ForegroundColor Cyan

foreach ($file in $htmlFiles) {
    $filePath = Join-Path $PSScriptRoot $file
    
    if (Test-Path $filePath) {
        Write-Host "Processing: $file" -ForegroundColor Yellow
        
        $content = Get-Content $filePath -Raw -Encoding UTF8
        $originalContent = $content
        
        # Fix navigation menu links
        $content = $content -replace 'href="https://flyerstrust\.org/"', 'href="Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html"'
        $content = $content -replace 'href="https://www\.flyerstrust\.org/"', 'href="Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html"'
        
        $content = $content -replace 'href="https://flyerstrust\.org/about/"', 'href="About Us – Flyers Charitable Trust.html"'
        $content = $content -replace 'href="https://www\.flyerstrust\.org/about/"', 'href="About Us – Flyers Charitable Trust.html"'
        
        $content = $content -replace 'href="https://flyerstrust\.org/services/"', 'href="Services – Flyers Charitable Trust.html"'
        $content = $content -replace 'href="https://www\.flyerstrust\.org/services/"', 'href="Services – Flyers Charitable Trust.html"'
        
        $content = $content -replace 'href="https://flyerstrust\.org/donation/"', 'href="Donation – Flyers Charitable Trust.html"'
        $content = $content -replace 'href="https://www\.flyerstrust\.org/donation/"', 'href="Donation – Flyers Charitable Trust.html"'
        
        $content = $content -replace 'href="https://flyerstrust\.org/gallery/"', 'href="Gallery – Flyers Charitable Trust.html"'
        $content = $content -replace 'href="https://www\.flyerstrust\.org/gallery/"', 'href="Gallery – Flyers Charitable Trust.html"'
        
        $content = $content -replace 'href="https://flyerstrust\.org/contact/"', 'href="Contact US – Flyers Charitable Trust.html"'
        $content = $content -replace 'href="https://www\.flyerstrust\.org/contact/"', 'href="Contact US – Flyers Charitable Trust.html"'
        
        # Fix skip to content links
        $content = $content -replace 'href="https://www\.flyerstrust\.org/[^"]*#content"', 'href="#content"'
        
        # Remove external canonical, RSS feed, and API links (keep them but make them non-functional)
        $content = $content -replace '<link rel="canonical" href="https://www\.flyerstrust\.org/[^"]*">', '<link rel="canonical" href="#">'
        $content = $content -replace '<link rel="shortlink" href="https://www\.flyerstrust\.org/[^"]*">', '<link rel="shortlink" href="#">'
        
        if ($content -ne $originalContent) {
            Set-Content -Path $filePath -Value $content -Encoding UTF8 -NoNewline
            Write-Host "  ✓ Updated successfully" -ForegroundColor Green
        } else {
            Write-Host "  - No changes needed" -ForegroundColor Gray
        }
    } else {
        Write-Host "  ✗ File not found: $file" -ForegroundColor Red
    }
}

Write-Host "`nLink fixing complete!" -ForegroundColor Green
Write-Host "All navigation links now point to local files." -ForegroundColor Cyan
