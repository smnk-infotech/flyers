# Fix asset path references in HTML files to use the corrected directory names
# Replace the garbled character sequence with the correct en-dash

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$siteRoot = Split-Path $root

$htmlFiles = Get-ChildItem -Path $siteRoot -Filter *.html -File | Where-Object { $_.Name -notlike '*_files*' }

# Use hex escape for the problematic characters
$badChars = [char]0xE2 + [char]0x80 + [char]0x9C  # â€œ (UTF-8 bytes as Windows-1252)
$correctChar = [char]0x2013  # En dash –

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding utf8
    
    $newContent = $content.Replace($badChars, $correctChar)
    
    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding utf8 -NoNewline
        Write-Host "Fixed asset paths in: $($file.Name)" -ForegroundColor Green
    }
}

Write-Host "`nAsset path fix complete." -ForegroundColor Cyan
