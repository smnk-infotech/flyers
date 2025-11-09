# Fix CSS parsing errors in HTML files
# This script fixes malformed CSS variable syntax

$htmlFiles = Get-ChildItem -Path "c:\Users\smnk2\Downloads\flyers" -Filter "*.html" -File

foreach ($file in $htmlFiles) {
    Write-Host "Processing: $($file.Name)"
    
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $modified = $false
    
    # Fix: background-color:(--ast-global-dark-bg-style) -> background-color:var(--ast-global-dark-bg-style)
    if ($content -match 'background-color:\(--ast-') {
        $content = $content -replace 'background-color:\(--ast-([^)]+)\)', 'background-color:var(--ast-$1)'
        $modified = $true
    }
    
    # Fix: background:(--ast-...) -> background:var(--ast-...)
    if ($content -match 'background:\(--ast-') {
        $content = $content -replace 'background:\(--ast-([^)]+)\)', 'background:var(--ast-$1)'
        $modified = $true
    }
    
    # Fix: color:(--ast-...) -> color:var(--ast-...)
    if ($content -match 'color:\(--ast-') {
        $content = $content -replace 'color:\(--ast-([^)]+)\)', 'color:var(--ast-$1)'
        $modified = $true
    }
    
    # Fix: border-color:(--ast-...) -> border-color:var(--ast-...)
    if ($content -match 'border-color:\(--ast-') {
        $content = $content -replace 'border-color:\(--ast-([^)]+)\)', 'border-color:var(--ast-$1)'
        $modified = $true
    }
    
    # Fix any other CSS properties with malformed var syntax
    if ($content -match ':\(--[a-z]') {
        $content = $content -replace ':\(--([a-z][^)]+)\)', ':var(--$1)'
        $modified = $true
    }
    
    # Add standard properties for vendor prefixes
    # -webkit-appearance -> appearance
    if ($content -match '-webkit-appearance:' -and $content -notmatch 'appearance:(?!.*-webkit)') {
        $content = $content -replace '(-webkit-appearance:[^;]+;)', '$1appearance:none;'
        $modified = $true
    }
    
    # -webkit-backface-visibility -> backface-visibility
    if ($content -match '-webkit-backface-visibility:' -and $content -notmatch 'backface-visibility:(?!.*-webkit)') {
        $content = $content -replace '(-webkit-backface-visibility:[^;]+;)', '$1backface-visibility:hidden;'
        $modified = $true
    }
    
    # -ms-touch-action -> touch-action
    if ($content -match '-ms-touch-action:' -and $content -notmatch 'touch-action:(?!.*-ms)') {
        $content = $content -replace '(-ms-touch-action:[^;]+;)', '$1touch-action:manipulation;'
        $modified = $true
    }
    
    # -webkit-filter -> filter
    if ($content -match '-webkit-filter:' -and $content -notmatch 'filter:(?!.*-webkit)') {
        $content = $content -replace '(-webkit-filter:[^;]+;)', '$1filter:inherit;'
        $modified = $true
    }
    
    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Host "  Fixed CSS errors in $($file.Name)" -ForegroundColor Green
    } else {
        Write-Host "  No CSS errors found in $($file.Name)" -ForegroundColor Yellow
    }
}

Write-Host "`nDone! All HTML files have been processed." -ForegroundColor Cyan
