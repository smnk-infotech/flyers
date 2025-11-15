# Cleans stray 'e=' lines and empty CSS rules in all HTML files
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent
$files = Get-ChildItem -Path $root -Recurse -Filter *.html
$changed = 0
foreach ($f in $files) {
  $text = Get-Content -Raw -LiteralPath $f.FullName -Encoding UTF8
  $orig = $text
  # Remove lines that are exactly 'e=' (with surrounding whitespace)
  $text = [Regex]::Replace($text, '(?m)^\s*e=\s*$(\r?\n)?', '')
  # Remove empty CSS rules: selector { } or selector { /* comments only */ }
  $text = [Regex]::Replace($text, '(?s)[^{]+\{\s*(?:/\*.*?\*/\s*)*\}', { param($m)
      # Keep only rules that contained at least one colon inside braces; otherwise drop
      if ($m.Value -match ':') { $m.Value } else { '' }
    })
  if ($text -ne $orig) {
    Set-Content -LiteralPath $f.FullName -Value $text -Encoding UTF8
    Write-Host "Cleaned: $($f.FullName)"
    $changed++
  }
}
Write-Host "HTML files cleaned: $changed"