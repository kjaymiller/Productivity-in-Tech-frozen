Title: Become a PIT Member ❤️
slug: memberships

<div class="box">
<blockquote class="blockquote text-center">
<p class="font-italic">
"I wanted to <b>focus</b> on my career. I knew I wasn't very proactive or productive in that area so I thought a productivity coach sounded practical. I knew Jay was passionate about this from listening to his podcast for so long. That and unlike some of the other coaches I looked into, I could actually afford his coaching."
</p>
- Chris J. - PIT Premium Member since 2015
</blockquote>
</div>

<h2 class="is-primary is-subtitle is-2">
Productivity in Tech is a <span class="has-text-weight-semi-bold is-italic">Member-Supported</span> Company. 
</h2>

<p class="subtitle is-4">
While the business does make some revenue from consulting, and helping developers get their content to you,
we cannot continue to grow the community and the services we offer without support from community members like you!  </p> 

<div class="columns is-centered">
<div class="column is-half box section">
<h2 class="is-subtitle has-text-primary">Get access to:</h2>
<ul class="list-group list-group-flush my-3">
<li class="list-group-item">Priority Access to the PIT Mastermind Group</li>
<li class="list-group-item">Access to the bonus PIT Podcast Feed</li>
<li class="list-group-item">PIT Premium Newsletter</li>
</ul>
</div>

<div class="my-3 column">
<!-- Load Stripe.js on your website. -->
<script src="https://js.stripe.com/v3"></script>

<!-- Create a button that your customers click to complete their purchase. Customize the styling to suit your branding. -->
<button
class="button is-primary-outline"
id="checkout-button-5d0bd868f033bf667526053f"
role="link">
Subscribe $10/Month
</button>

<button
class='button is-primary-outline'
id="checkout-button-pit-annual"
role="link">
Subscribe $100/Year
</button>
</div>
</div>

<script>
var stripe = Stripe('pk_live_kDLC8qiW74z3zUMfXQBjEfjD');
var monthlyCheckout = document.getElementById('checkout-button-5d0bd868f033bf667526053f');
monthlyCheckout.addEventListener('click', function () {
// When the customer clicks on the button, redirect
// them to Checkout.
stripe.redirectToCheckout({items: [{plan: '5d0bd868f033bf667526053f', quantity: 1}],

// Do not rely on the redirect to the successUrl for fulfilling
// purchases, customers may not always reach the success_url after
// a successful payment.
// Instead use one of the strategies described in
// https://stripe.com/docs/payments/checkout/fulfillment
successUrl: 'https://productivityintech.com',
cancelUrl: 'https://productivityintech.com',
})
.then(function (result) {
if (result.error) {
// If `redirectToCheckout` fails due to a browser or network
// error, display the localized error message to your customer.
var displayError = document.getElementById('error-message');
displayError.textContent = result.error.message;
}
});
});
</script>


<script>
var annualButton= document.getElementById('checkout-button-pit-annual');
annualButton.addEventListener('click', function () {
// When the customer clicks on the button, redirect
// them to Checkout.
stripe.redirectToCheckout({
items: [{plan: 'pit-annual', quantity: 1}],

// Do not rely on the redirect to the successUrl for fulfilling
// purchases, customers may not always reach the success_url after
// a successful payment.
// Instead use one of the strategies described in
// https://stripe.com/docs/payments/checkout/fulfillment
successUrl: 'https://productivityintech.com/',
cancelUrl: 'https://productivityintech.com/',
})
.then(function (result) {
if (result.error) {
// If `redirectToCheckout` fails due to a browser or network
// error, display the localized error message to your customer.
var displayError = document.getElementById('error-message');
displayError.textContent = result.error.message;
}
});
});
</script>
<div id="error-message" class="text-danger"></div>
</div>
