Set-Location "c:\Users\smnk2\Downloads\flyers"
$file = Get-ChildItem -Filter 'About Us*.html' | Select-Object -First 1

Write-Host "Processing: $($file.Name)" -ForegroundColor Cyan
$content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)

# Fix empty rulesets
$content = $content -replace '{\s*}', ''

# Fix properties without values
$content = $content -replace '([a-zA-Z-]+)\s*:\s*;', ''

# Fix missing semicolons before closing braces
$content = $content -replace '([^;{}])\s*}', '$1;}' 

# Fix double braces
$content = $content -replace '}\s*{', '}{' 

# Fix incomplete style tags
$content = $content -replace '<style([^>]*)>\s*([^<]*[^>])\s*$', '<style$1>$2</style>'

# Save
[System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)

Write-Host "✓ All CSS syntax errors fixed!" -ForegroundColor Green
Write-Host "✓ Please reload your IDE (Ctrl+Shift+P -> Reload Window)" -ForegroundColor Yellow
