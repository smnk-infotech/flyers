# Script to update navigation menu and buttons across HTML files
param(
    [string]$WorkingDir = "c:\Users\smnk2\Downloads\flyers"
)

$files = @(
    "About Us – Flyers Charitable Trust.html",
    "Services – Flyers Charitable Trust.html",
    "Gallery – Flyers Charitable Trust.html",
    "Donation – Flyers Charitable Trust.html",
    "Contact US – Flyers Charitable Trust.html"
)

$oldMenu = @'
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link">About Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services – Flyers Charitable Trust.html" class="elementor-item menu-link">Services</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-561"><a href="Donation – Flyers Charitable Trust.html" class="elementor-item menu-link">Donation</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery – Flyers Charitable Trust.html" class="elementor-item menu-link">Gallery</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-359"><a href="Contact US – Flyers Charitable Trust.html" class="elementor-item menu-link">Contact Us</a></li>
'@

$newMenu = @'
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link elementor-item-anchor">About Us</a>
<ul class="sub-menu elementor-nav-menu--dropdown">
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#know-us" class="elementor-sub-item menu-link">Know Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#our-story" class="elementor-sub-item menu-link">Our Story & Team</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#milestone" class="elementor-sub-item menu-link">Milestone</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#our-partners" class="elementor-sub-item menu-link">Our Partners</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#transparency" class="elementor-sub-item menu-link">Transparency</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#testimonial" class="elementor-sub-item menu-link">Testimonial</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="Contact US – Flyers Charitable Trust.html" class="elementor-sub-item menu-link">Contact Us</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services – Flyers Charitable Trust.html" class="elementor-item menu-link">Programs</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-561"><a href="Services – Flyers Charitable Trust.html#impact" class="elementor-item menu-link">Impact</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery – Flyers Charitable Trust.html" class="elementor-item menu-link">Gallery</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-362"><a href="Services – Flyers Charitable Trust.html#volunteer" class="elementor-item menu-link">Volunteer</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-363"><a href="Services – Flyers Charitable Trust.html#csr" class="elementor-item menu-link">CSR</a></li>
'@

$oldMenuTabindex = $oldMenu -replace 'class="elementor-item menu-link">', 'class="elementor-item menu-link" tabindex="-1">'
$newMenuTabindex = $newMenu -replace 'class="elementor-item menu-link">', 'class="elementor-item menu-link" tabindex="-1">' -replace 'class="elementor-sub-item menu-link">', 'class="elementor-sub-item menu-link" tabindex="-1">'

foreach ($file in $files) {
    $filePath = Join-Path $WorkingDir $file
    if (Test-Path $filePath) {
        Write-Host "Processing $file..." -ForegroundColor Cyan
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        # Replace menu instances (both with and without tabindex)
        $content = $content -replace [regex]::Escape($oldMenu), $newMenu
        $content = $content -replace [regex]::Escape($oldMenuTabindex), $newMenuTabindex
        
        # Replace Corporate Portal button text
        $content = $content -replace 'Corporate Portal', 'Donate Now'
        
        # Replace user-circle icon with heart icon
        $content = $content -replace 'fa-user-circle', 'fa-heart'
        
        # Replace portal login links with donation page
        $content = $content -replace '/portal/login\?redirect=/', 'Donation – Flyers Charitable Trust.html'
        
        Set-Content $filePath -Value $content -Encoding UTF8 -NoNewline
        Write-Host "✓ Updated $file" -ForegroundColor Green
    } else {
        Write-Host "✗ File not found: $file" -ForegroundColor Red
    }
}

Write-Host "`nAll files processed!" -ForegroundColor Green
