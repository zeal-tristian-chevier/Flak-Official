const cards = document.querySelectorAll('.card-animate')

window.addEventListener('scroll', checkCards)

function checkCards() {
    const trigger = window.innerHeight

    cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top
        let currentCard = 
        cardTop < trigger ?  
        card.classList.remove('hide') : 
        card.classList.add('hide')
        return currentCard
    })
}