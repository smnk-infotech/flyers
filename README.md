# Flyers Charitable Trust Website

This is the official website for the Flyers Charitable Trust, a non-governmental organization based in Coimbatore, Tamil Nadu, India. The website is a professional, corporate-style platform that provides information about the trust's activities, services, and ways to get involved.

## 🌐 Live Website
**Production URL:** https://flyerscharitabletrust-site.web.app

## 📋 Organization Details
- **Name:** Flyers Charitable Trust
- **Location:** Coimbatore, Tamil Nadu, India
- **Purpose:** NGO focused on Child Welfare, Women Empowerment, Education, Healthcare, and Community Development
- **Type:** Static Website (WordPress/Elementor Export)

## 🎨 Design & Branding

### Color Palette
- **Primary Blue:** `#060097` (--ast-global-color-0)
- **Accent Purple:** `#c10fff` (--ast-global-color-1)
- **Heading Text:** `#1e293b` (--ast-global-color-2)
- **Body Text:** `#67768e` (--ast-global-color-3)
- **Light Background:** `#f9f6fe` (--ast-global-color-4)
- **White:** `#FFFFFF` (--ast-global-color-5)
- **Light Gray:** `#F2F5F7` (--ast-global-color-6)
- **Accent Yellow:** `#ffcd57` (--ast-global-color-7)

### Typography
- **Headings:** Plus Jakarta Sans (600 weight)
- **Body Text:** Inter
- **Base Font Size:** 18px (112.5%)

### Theme
- **WordPress Theme:** Astra
- **Page Builder:** Elementor Pro 3.29.2
- **Design Style:** Modern, clean, corporate

## ✅ Completed Features

### Core Pages (Fully Implemented)
1. **Home Page** - `Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html`
   - Hero section with banner
   - Mission and vision statements
   - Impact metrics (counters with animations)
   - Quick links and call-to-action buttons
   - Photo slider/carousel
   - Testimonials section
   
2. **About Us Page** - `About Us – Flyers Charitable Trust.html`
   - Detailed history and mission
   - Vision and objectives
   - Team profiles with photos
   - Trust information
   
3. **Services Page** - `Services – Flyers Charitable Trust.html`
   - Child Welfare programs
   - Women Empowerment initiatives
   - Education projects
   - Healthcare services
   - Community development
   
4. **Donation Page** - `Donation – Flyers Charitable Trust.html`
   - Multiple payment options
   - Donation forms
   - Tax benefit information
   - Secure transaction details
   
5. **Gallery Page** - `Gallery – Flyers Charitable Trust.html`
   - Event photo albums
   - Image carousels
   - Organized by activities
   
6. **Contact Page** - `Contact US – Flyers Charitable Trust.html`
   - Contact form (Name, Email, Phone, Message)
   - Embedded Google Maps
   - Address and contact details
   - Social media integration

### Design Features
- ✅ Fully responsive design (mobile, tablet, desktop)
- ✅ Professional corporate styling
- ✅ Consistent branding across all pages
- ✅ Custom animations (fadeIn, zoomIn, slideIn effects)
- ✅ Interactive counters with smooth number transitions
- ✅ Image carousels and sliders
- ✅ Icon boxes with hover effects
- ✅ Social media icons with links
- ✅ WhatsApp and phone call integration

### Technical Implementation
- ✅ **Hosting:** Firebase Hosting
- ✅ **SSL/HTTPS:** Enabled via Firebase
- ✅ **Security Headers:** Configured (X-Frame-Options, CSP, HSTS)
- ✅ **Animation System:** Custom JavaScript solution (`fix-animations.js`)
- ✅ **Performance:** Optimized images and assets
- ✅ **Accessibility:** Semantic HTML, proper heading structure
- ✅ **Cross-browser Compatibility:** Chrome, Firefox, Safari, Edge

### Custom Solutions Implemented
1. **Animation Fix** (`fix-animations.js`)
   - Resolves Elementor animation issues in static export
   - Removes `elementor-invisible` class on page load
   - Parses `data-settings` attributes for animation classes
   - Smooth counter animations with requestAnimationFrame
   - Applied to all pages

2. **Firebase Configuration** (`firebase.json`)
   - Security headers (X-Frame-Options: SAMEORIGIN)
   - Content Security Policy
   - HSTS enforcement
   - Clean URL structure

3. **Redirect Setup** (`index.html`)
   - Automatic redirect to main homepage
   - Proper HTML5 structure
   - Meta viewport for mobile responsiveness

## 📁 File Structure
```
flyers/
├── index.html                          # Redirect to homepage
├── fix-animations.js                   # Custom animation handler
├── firebase.json                       # Firebase hosting config
├── Flyers Charitable Trust – [...].html  # Homepage
├── About Us – [...].html               # About page
├── Services – [...].html               # Services page
├── Donation – [...].html               # Donation page
├── Gallery – [...].html                # Gallery page
├── Contact US – [...].html             # Contact page
├── [Page Name]_files/                  # Page-specific assets
│   ├── CSS files (*.css)
│   ├── JavaScript files (*.js)
│   ├── Images
│   └── Fonts
├── images/                             # Shared images
└── README/                             # Documentation assets
```

## 🚀 Deployment

### Deployment Platform
- **Service:** Firebase Hosting
- **Project ID:** flyerscharitabletrust-site
- **Total Files Deployed:** 1,149 files

### Deployment Commands
```bash
# Deploy to Firebase
firebase deploy --only hosting

# Local testing
python -m http.server 8000
```

### Deployment History
- **Initial Deployment:** 1,148 files
- **Animation Fix Update:** 1,149 files (added fix-animations.js)
- **Status:** ✅ Successfully deployed and live

## 🔧 Technical Stack

### Frontend
- HTML5
- CSS3 (with CSS Grid and Flexbox)
- Vanilla JavaScript
- Elementor CSS framework
- Astra theme styles

### Build Tools
- WordPress (source)
- Elementor Page Builder (design)
- Static export (production)

### Hosting & Infrastructure
- Firebase Hosting
- Firebase CLI
- Git version control
- GitHub repository

## 📊 Website Features Status

### Implemented ✅
- [x] Responsive design (mobile, tablet, desktop)
- [x] Professional corporate styling
- [x] Hero sections with banners
- [x] Mission and vision statements
- [x] Impact metrics with animated counters
- [x] Quick links and CTAs
- [x] Photo sliders/carousels
- [x] Detailed about section
- [x] Services/projects listings
- [x] Donation page with payment info
- [x] Gallery with albums
- [x] Contact form
- [x] Embedded Google Maps
- [x] Social media integration
- [x] Footer with quick links
- [x] WhatsApp integration
- [x] Custom animations
- [x] Fast loading optimized images
- [x] SSL/HTTPS security
- [x] Security headers

### In Progress / Future Enhancements 🚧
- [ ] SEO optimization (meta tags, schema.org)
- [ ] Google Analytics integration
- [ ] Live chat functionality
- [ ] Event calendar
- [ ] Blog/News section
- [ ] Newsletter signup
- [ ] Member login portal
- [ ] Downloadable resources (brochures, reports)
- [ ] Video testimonials
- [ ] Press releases section
- [ ] Corporate partnerships page
- [ ] Volunteer application forms
- [ ] Privacy policy page
- [ ] Terms & conditions page
- [ ] Multi-language support

## 🐛 Known Issues & Fixes

### Fixed Issues ✅
1. **404 Error on Homepage**
   - **Problem:** Firebase expected `index.html` but homepage had different filename
   - **Solution:** Created redirect `index.html` with meta refresh
   - **Status:** ✅ Resolved

2. **HTML Validation Errors**
   - **Problem:** Missing viewport meta tag and lang attribute
   - **Solution:** Added proper HTML5 structure to index.html
   - **Status:** ✅ Resolved

3. **Elementor Animations Not Working**
   - **Problem:** Static export missing JavaScript for scroll-triggered animations
   - **Solution:** Created custom `fix-animations.js` to manually trigger animations
   - **Status:** ✅ Resolved

4. **CSS Variable Syntax Error**
   - **Problem:** `background-color:(--ast-global-dark-bg-style)` missing `var()`
   - **Solution:** Documented in copilot-instructions.md for future fixes
   - **Status:** ⚠️ Documented (run fix-css.ps1 script if available)

## 📝 Development Notes

### Important Considerations
1. **Do not refactor Elementor class names** - These are auto-generated and required for styling
2. **Special characters in filenames** - Main files use em dash (–) character
3. **Page-specific assets** - Each HTML page has corresponding `*_files/` directory
4. **Animation dependencies** - All pages require `fix-animations.js` before closing `</body>` tag

### Browser Compatibility
- ✅ Chrome/Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🔐 Security Features
- HTTPS enforced via Firebase Hosting
- X-Frame-Options: SAMEORIGIN (prevents clickjacking)
- Content Security Policy headers
- HTTP Strict Transport Security (HSTS)
- Secure payment gateway integration

## 📞 Contact & Support
For website updates or technical support, please contact the website administrator or refer to the contact information on the live website.

---

**Last Updated:** November 15, 2025  
**Version:** 1.1.0  
**Status:** ✅ Live in Production
