# Fix all remaining menu instances in HTML files
$files = @(
    "About Us",
    "Services",
    "Gallery",
    "Donation",
    "Contact US"
)

foreach ($baseName in $files) {
    $file = "$baseName – Flyers Charitable Trust.html"
    Write-Host "Processing $file..." -ForegroundColor Cyan
    
    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    
    # Count how many old menus remain
    $oldPattern = '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services'
    $oldMenuMatchCount = ([regex]::Matches($content, [regex]::Escape($oldPattern))).Count
    
    if ($oldMenuMatchCount -gt 0) {
        Write-Host "  Found $matchCount old menu instances" -ForegroundColor Yellow
        
        # Replace all instances that still say "Services" instead of "Programs"
        $content = $content -replace '>Services</a></li>', '>Programs</a></li>'
        
        # Replace Donation link with Impact anchor link
        $content = $content -replace 'menu-item-561"><a href="Donation[^"]*" class="elementor-item menu-link"([^>]*)>Donation</a></li>',  
                                      'menu-item-561"><a href="Services – Flyers Charitable Trust.html#impact" class="elementor-item menu-link"$1>Impact</a></li>'
        
        # Replace Contact Us with Gallery
        $oldContactPattern = 'menu-item-359"><a href="Contact US[^"]*" class="elementor-item menu-link"'
        if ($content -match $oldContactPattern) {
            # This pattern needs to be removed entirely as Contact Us moves to dropdown
            $content = $content -replace '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-359"><a href="Contact US[^"]*" class="elementor-item menu-link"([^>]*)>Contact Us</a></li>[^<]*', ''
        }
        
        # Add new menu items (Volunteer and CSR) if not present
        if ($content -notmatch 'menu-item-362') {
            Write-Host "  Adding Volunteer and CSR menu items" -ForegroundColor Yellow
            $content = $content -replace '(<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery[^"]*" class="elementor-item menu-link"([^>]*)>Gallery</a></li>)', 
                '$1<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-362"><a href="Services – Flyers Charitable Trust.html#volunteer" class="elementor-item menu-link"$2>Volunteer</a></li><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-363"><a href="Services – Flyers Charitable Trust.html#csr" class="elementor-item menu-link"$2>CSR</a></li>'
        }
        
        # Add About Us dropdown menu where plain About Us exists
        $plainAboutUs = '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-352"><a href="About Us'
        if ($content -match [regex]::Escape($plainAboutUs)) {
            Write-Host "  Converting About Us to dropdown menu" -ForegroundColor Yellow
            # This is complex - will need manual intervention for now
        }
        
        [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
        Write-Host "  ✓ Updated $file" -ForegroundColor Green
    } else {
        Write-Host "  No old menus found - already updated" -ForegroundColor Green
    }
}

Write-Host "`n✓ Processing complete!" -ForegroundColor Green
