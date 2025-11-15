# Removes remote WordPress srcset attributes so images use local copies
# Idempotent: safe to run multiple times
$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent
$files = Get-ChildItem -Path $root -Recurse -Filter *.html

$pattern = "(\s)srcset=(`"|')https://(www\.)?flyerstrust\.org[^`"']*(`"|')"
$replacements = 0

foreach ($file in $files) {
    $content = Get-Content -Raw -LiteralPath $file.FullName -Encoding UTF8
    $newContent = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, '$1')

    if ($newContent -ne $content) {
        Set-Content -LiteralPath $file.FullName -Value $newContent -Encoding UTF8
        Write-Host "Updated: $($file.FullName)"
        $replacements++
    }
}

Write-Host "Files updated: $replacements"
