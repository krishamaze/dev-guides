/**
 * Shared JavaScript for guide pages
 */

/**
 * Copies code from a code block to the clipboard
 * @param {HTMLElement} btn The button that was clicked
 */
function copyCode(btn) {
    const codeBlock = btn.closest('.code-block') || btn.closest('pre');
    const codeElement = codeBlock.querySelector('code');
    const code = codeElement.textContent;
    const originalText = btn.textContent;

    navigator.clipboard.writeText(code).then(() => {
        btn.textContent = '✓ Copied!';
        btn.classList.add('copied');

        setTimeout(() => {
            btn.textContent = originalText;
            btn.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

/**
 * Initialize Table of Contents highlighting using IntersectionObserver
 */
function initTOCHighlighting() {
    const sections = document.querySelectorAll('section[id]');
    const tocLinks = document.querySelectorAll('.toc-list a');

    if (sections.length === 0 || tocLinks.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '-10% 0px -70% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                tocLinks.forEach(link => {
                    link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
}

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    initTOCHighlighting();
});
