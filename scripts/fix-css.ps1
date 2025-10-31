Param(
    [switch]$WhatIf
)

# Fix invalid CSS var usage in inline styles across all HTML files.
# Replaces: background-color:(--ast-global-dark-bg-style)
# With:     background-color:var(--ast-global-dark-bg-style)

$ErrorActionPreference = 'Stop'

$pattern = 'background-color:\(--ast-global-dark-bg-style\)'
$replacement = 'background-color:var(--ast-global-dark-bg-style)'

$files = Get-ChildItem -Path "$PSScriptRoot\.." -Filter '*.html' -Recurse
if (-not $files) {
    Write-Host "No HTML files found to patch." -ForegroundColor Yellow
    exit 0
}

foreach ($file in $files) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    if ($content -match $pattern) {
        Write-Host "Patching: $($file.FullName)" -ForegroundColor Cyan

        if (-not $WhatIf) {
            # Backup once per file
            $backup = "$($file.FullName).bak"
            if (-not (Test-Path $backup)) {
                Copy-Item -LiteralPath $file.FullName -Destination $backup
            }

            $new = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, $replacement)
            Set-Content -LiteralPath $file.FullName -Value $new -NoNewline
        }
    }
}

Write-Host "Done. Use -WhatIf to preview without changing files." -ForegroundColor Green
