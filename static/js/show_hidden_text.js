function toggleText(linkElement) {
    var parentEntry = linkElement.parentElement;
    var visibleText = parentEntry.querySelector('.visible-text');
    var hiddenText = parentEntry.querySelector('.hidden-text');

    if (visibleText.style.display === 'none') {
        visibleText.style.display = 'block';
        hiddenText.style.display = 'none';
        linkElement.textContent = "Read More";
    } else {
        visibleText.style.display = 'none';
        hiddenText.style.display = 'block';
        linkElement.textContent = "Read Less";
    }
}