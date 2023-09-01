let slideIndex = 0;
showSlides();

function showSlides () {
    let slides= document.getElementsByClassName('myslides');
    let dots = document.getElementsByClassName('dot');

    for (let i =0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }

    slideIndex++;
    
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(' active', '')
    }

    slides[slideIndex - 1].style.display = 'block';
    dots[slideIndex - 1].className += ' active';

    setTimeout(showSlides, 3000);
}



function generateStarRating(rating, container) {
    const maxStars= 5;
    const starIcon= '★';

    for (let i = 1; i <= maxStars; i++) {
        const star= document.createElement('span');
        star.textContent = i <= rating ? starIcon : '☆';
        container.appendChild(star);
    }
}


const postElements= document.querySelectorAll('.post');
postElements.forEach(function (postElement) {
    const rating = parseFloat(postElement.getAttribute('data-rating'));
    const starRatingsContainer = postElement.querySelector('.star-ratings');
    generateStarRating(rating, starRatingsContainer);
});