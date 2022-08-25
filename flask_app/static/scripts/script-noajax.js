let stripe = Stripe(checkout_public_key)

let btn = document.querySelector('#checkoutbtn')
console.log('hello')
btn.addEventListener('click', e => {
    stripe.redirectToCheckout({
        sessionId: checkout_session_id
    }).then(function (result) {

    })
})