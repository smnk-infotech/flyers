# Fix asset path references in HTML files to use the corrected directory names
# The directories use en-dash (–) but HTML references contain garbled â€" sequence

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$siteRoot = Split-Path $root

$htmlFiles = Get-ChildItem -Path $siteRoot -Filter *.html -File | Where-Object { $_.Name -notlike '*_files*' }

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding utf8
    
    # Replace the garbled â€" with the correct en-dash – in all _files paths
    $newContent = $content -replace 'â€"', '–'
    
    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding utf8 -NoNewline
        Write-Host "Fixed asset paths in: $($file.Name)" -ForegroundColor Green
    }
}

Write-Host "`nAsset path fix complete." -ForegroundColor Cyan
