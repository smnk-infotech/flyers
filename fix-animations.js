// Fix for Elementor animations in static export
document.addEventListener('DOMContentLoaded', function() {
    // Remove elementor-invisible class from all elements to make them visible
    const invisibleElements = document.querySelectorAll('.elementor-invisible');
    invisibleElements.forEach(function(element) {
        element.classList.remove('elementor-invisible');
    });
    
    // Add animation classes to elements that should animate
    const elementsToAnimate = document.querySelectorAll('[data-settings*="_animation"]');
    elementsToAnimate.forEach(function(element) {
        const settings = element.getAttribute('data-settings');
        if (settings) {
            try {
                const settingsObj = JSON.parse(settings.replace(/&quot;/g, '"'));
                if (settingsObj._animation) {
                    element.classList.add('animated', settingsObj._animation);
                }
            } catch (e) {
                // If parsing fails, skip
            }
        }
    });
    
    // Trigger counter animations
    const counters = document.querySelectorAll('.elementor-counter-number');
    counters.forEach(function(counter) {
        const targetValue = parseInt(counter.getAttribute('data-to-value')) || 0;
        const duration = parseInt(counter.getAttribute('data-duration')) || 2000;
        const startValue = parseInt(counter.getAttribute('data-from-value')) || 0;
        
        let currentValue = startValue;
        const increment = (targetValue - startValue) / (duration / 16); // 60fps
        
        const updateCounter = function() {
            currentValue += increment;
            if ((increment > 0 && currentValue < targetValue) || (increment < 0 && currentValue > targetValue)) {
                counter.textContent = Math.round(currentValue);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = targetValue;
            }
        };
        
        updateCounter();
    });
});
