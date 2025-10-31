# Style Guide and Design System

## Typography

### Fonts
1. **Primary Font: Inter**
   - Regular (400)
   - Semi-bold (600)
   - Used for body text and general content

2. **Heading Font: Plus Jakarta Sans**
   - Semi-bold (600)
   - Used for all headings (h1-h6)

### Font Sizes
- H1: 64px (3.556rem)
- H2: 48px (2.667rem)
- H3: 24px (1.333rem)
- H4: 20px (1.111rem)
- H5: 18px (1rem)
- H6: 15px (0.833rem)
- Body: 18px (1rem)

## Color Palette

### Primary Colors
- Primary Blue: #060097
- Accent Purple: #c10fff
- Accent Yellow: #ffcd57

### Text Colors
- Heading Text: #1e293b
- Body Text: #67768e

### Background Colors
- Primary Background: #FFFFFF
- Secondary Background: #F2F5F7
- Tertiary Background: #f9f6fe

### UI Colors
- Border Color: var(--ast-border-color)
- Input Background: #F9FAFB
- Code Block Background: #ECEFF3

## Spacing System

### Padding
- Container XLG: 3em
- Container LG: 3em
- Container SLG: 2em
- Container MD: 3em
- Container SM: 3em
- Container XS: 2.4em
- Container XXS: 1.8em

### Margins
- Default Block Margin: 24px
- Widget Margin: 1.25em
- Header Elements: 10px

## UI Components

### Buttons
```css
Border Radius: 50px
Padding: 20px 40px
Font Size: 20px
Line Height: 1em
Font Weight: 600
```

### Forms
- Input Padding: 10px
- Border Style: Dotted
- Focus State: Outlined

### Cards
- Border Radius: 4px
- Box Shadow: 0px 0px 4px 0 #00000057

## Responsive Breakpoints

### Desktop
- Normal: 1200px+
- Narrow: 750px max-width

### Tablet
- Max-width: 921px
- Font Size: 102.6%

### Mobile
- Max-width: 544px
- Font Size: 102.6%

## Animation Guidelines

### Transitions
- Duration: 0.2s
- Timing: Linear
- Properties: all

### Hover States
- Links: Color change
- Buttons: Background color change
- Cards: Shadow adjustment

## Layout Rules

### Container Widths
- Normal: 1200px
- Narrow: 750px
- Full Width: 100%

### Grid System
- Column Gap: 20px
- Row Gap: 20px
- Responsive Adjustments

## Media Guidelines

### Images
- Aspect Ratio: 16:9 (featured images)
- Format: WebP preferred
- Lazy Loading: Enabled

### Icons
- Font Awesome integration
- Custom icon sets
- SVG preferred

## Accessibility

### Focus States
- Visible outline
- Color contrast compliance
- Keyboard navigation support

### Text Contrast
- WCAG 2.1 AA compliance
- Minimum contrast ratio: 4.5:1
