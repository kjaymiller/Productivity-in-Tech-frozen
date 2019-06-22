Title: Become a PIT Member ❤️
slug: memberships

<h2 class="">
<span class="text-primary">Productivity in Tech</span> is a <em>Member-Supported</em> Company. 
</h2>

<p class='lead my-4'>
While the business does make some revenue from consulting, coaching and speaking, we cannot continue to grow the community and the services we offer without support from the community members like you! 
</p>

<div class="jumbotron bg-transparent border border-primary">
<h2 class="text-primary">Get access to:</h2>
<div class="col-md-6 my-3 text-centered">

<ul class="list-group list-group-flush my-3">
<li class="list-group-item">Priority Access to the PIT Mastermind Group</li>
<li class="list-group-item">Access to the bonus PIT Podcast Feed</li>
<li class="list-group-item">PIT Premium Newsletter</li>
</ul>

<div class="row justify-content-around">
<!-- Load Stripe.js on your website. -->
<script src="https://js.stripe.com/v3"></script>

<!-- Create a button that your customers click to complete their purchase. Customize the styling to suit your branding. -->
<button
	class="btn btn-primary"
  id="checkout-button-5d0bd868f033bf667526053f"
  role="link">
Subscribe $10/Month
</button>

<button
	class='btn btn-primary'
  id="checkout-button-pit-annual"
  role="link">
Subscribe $100/Year
</button>


<script>
  var stripe = Stripe('pk_live_kDLC8qiW74z3zUMfXQBjEfjD');
  var monthlyCheckout = document.getElementById('checkout-button-5d0bd868f033bf667526053f');
  monthlyCheckout.addEventListener('click', function () {
    // When the customer clicks on the button, redirect
    // them to Checkout.
    stripe.redirectToCheckout({
      items: [{plan: '5d0bd868f033bf667526053f', quantity: 1}],

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
