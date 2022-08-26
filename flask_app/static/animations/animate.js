const cards = document.querySelectorAll('.card-animate')

if(screen.width > 1024){
window.addEventListener('scroll', checkCards)
}

function checkCards() {
    
    const trigger = window.innerHeight + 200;
    
        cards.forEach(card => {
            const cardTop = card.getBoundingClientRect().top
            let currentCard = 
            cardTop > trigger ?  
            card.classList.remove('animate__backInRight') : 
            card.classList.add('animate__backInRight')
            return currentCard
        })
    }