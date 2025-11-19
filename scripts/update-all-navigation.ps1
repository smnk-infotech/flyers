# Update Navigation Menu on All Pages
# This script updates the navigation menu structure across all HTML pages

$pages = @(
    "About Us – Flyers Charitable Trust.html",
    "Services – Flyers Charitable Trust.html",
    "Gallery – Flyers Charitable Trust.html",
    "Donation – Flyers Charitable Trust.html",
    "Contact US – Flyers Charitable Trust.html"
)

$oldMenuPattern = @'
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-351"><a href="Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html" class="elementor-item menu-link">Home</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link">About Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services – Flyers Charitable Trust.html" class="elementor-item menu-link">Services</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-561"><a href="Donation – Flyers Charitable Trust.html" class="elementor-item menu-link">Donation</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery – Flyers Charitable Trust.html" class="elementor-item menu-link">Gallery</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-359"><a href="Contact US – Flyers Charitable Trust.html" class="elementor-item menu-link">Contact Us</a></li>
'@

$newMenuPattern = @'
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-351"><a href="Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html" class="elementor-item menu-link">Home</a></li>
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

$oldButtonPattern = @'
<span class="elementor-button-text">Corporate Portal</span>
'@

$newButtonPattern = @'
<span class="elementor-button-text">Donate Now</span>
'@

$oldButtonLink = '/portal/login'
$newButtonLink = 'Donation – Flyers Charitable Trust.html'

$oldButtonIcon = 'fa-user-circle'
$newButtonIcon = 'fa-heart'

foreach ($page in $pages) {
    $filePath = Join-Path $PSScriptRoot "..\$page"
    
    if (Test-Path $filePath) {
        Write-Host "Updating $page..." -ForegroundColor Cyan
        
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        # Update menu structure
        $content = $content -replace [regex]::Escape($oldMenuPattern), $newMenuPattern
        
        # Update button text
        $content = $content -replace [regex]::Escape($oldButtonPattern), $newButtonPattern
        
        # Update button link
        $content = $content -replace [regex]::Escape($oldButtonLink), $newButtonLink
        
        # Update button icon
        $content = $content -replace [regex]::Escape($oldButtonIcon), $newButtonIcon
        
        Set-Content $filePath $content -Encoding UTF8 -NoNewline
        
        Write-Host "✓ $page updated successfully" -ForegroundColor Green
    } else {
        Write-Host "✗ File not found: $page" -ForegroundColor Red
    }
}

Write-Host "`n✓ All pages updated successfully!" -ForegroundColor Green
Write-Host "Updated features:" -ForegroundColor Yellow
Write-Host "  - Navigation menu with About Us dropdown" -ForegroundColor White
Write-Host "  - Replaced 'Corporate Portal' with 'Donate Now' button" -ForegroundColor White
Write-Host "  - Updated menu items: Home, About Us, Programs, Impact, Gallery, Volunteer, CSR" -ForegroundColor White
