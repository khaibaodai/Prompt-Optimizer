// Main JavaScript file for Prompt Optimizer

document.addEventListener('DOMContentLoaded', function() {
    // Auto-resize textarea based on content
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });

    // Show loading state on form submission
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.innerHTML = `
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>Optimizing...</span>
            `;
        });
    }

    // Automatically scroll to results when they appear
    const resultSection = document.getElementById('optimized-prompt');
    if (resultSection) {
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
});