# Fix asset path references in HTML files
# Replace garbled character sequences with correct en-dash in asset paths

$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$siteRoot = Split-Path $root

$htmlFiles = Get-ChildItem -Path $siteRoot -Filter *.html -File | Where-Object { $_.Name -notlike '*_files*' }

foreach ($file in $htmlFiles) {
    $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
    $content = [System.Text.Encoding]::UTF8.GetString($bytes)
    
    # Replace the specific bad sequence: 0xC3 0xA2 0xE2 0x82 0xAC 0xE2 0x80 0x9C (â€")
    # with proper en-dash: 0xE2 0x80 0x93 (–)
    $pattern = [regex]'Charitable Trust \xC3\xA2\xE2\x82\xAC\xE2\x80\x9C Flyers Charitable Trust'
    $replacement = 'Charitable Trust – Flyers Charitable Trust'
    
    if ($content -match $pattern) {
        $newContent = $pattern.Replace($content, $replacement)
        $newBytes = [System.Text.Encoding]::UTF8.GetBytes($newContent)
        [System.IO.File]::WriteAllBytes($file.FullName, $newBytes)
        Write-Host "Fixed: $($file.Name)" -ForegroundColor Green
    }
}

Write-Host "`nPath encoding fix complete." -ForegroundColor Cyan
