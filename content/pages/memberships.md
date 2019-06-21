Title: Become a PIT Member ❤️
slug: memberships

<h2 class="">
<span class="text-primary">Productivity in Tech</span> is a <em>Member-Supported Company</em>. 
</h2>

<p class='lead my-3'>
While the business does make some revenue from consulting, coaching and speaking, we cannot continue to grow the community and the services we offer without support from the community members like you! 
</p>

<div class="jumbotron bg-transparent border border-primary">
<h2>Your PIT Premium Membership gets you access to:</h2>
<div class="col-md-6 my-3 text-centered">
<ul class="list-group list-group-flush">
<li class="list-group-item">Priority Access to the PIT Mastermind Group</li>
<li class="list-group-item">Access to the bonus PIT Podcast Feed</li>
<li class="list-group-item">PIT Premium Newsletter</li>
</ul>

<!-- <a class="btn btn-primary btn-lg text-white" href="https://productivityintech.memberful.com/checkout?plan=21849"> -->
<!-- <a class="btn btn-primary btn-lg text-white" href="https://productivityintech.memberful.com/checkout?plan=36786"> -->

<div class="row justify-content-around my-3">
<!-- Monthly Subscribe Button - triggers modal -->
<button type="button"
	class="btn btn-primary"
	data-toggle="modal"
	data-target="#modal-monthly">
Subscribe $10/month
</button>

<!-- Annual Subscribe Button - triggers modal -->
<button type="button"
	class="btn btn-primary"
	data-toggle="modal"
	data-target="#modal-annual">
Subscribe $100/year
</button>
</div>
</div>

<!-- Membership JS - Place Ahead of Modals -->
<!-- Stripe and ServiceBot JS -->
<script src="https://js.stripe.com/v3/"></script>
<script src="https://servicebot.io/js/servicebot-embed.js" type="text/javascript"></script>
<!-- End Membership JS -->

<!--Monthly Modal -->
<div class="modal fade" tabindex="-1" id="modal-monthly" role="dialog">
<div class="modal-dialog bg-white" id="srf-monthly" role="document"></div>
<script  type="text/javascript">
Servicebot.init({
templateId : 2,
url : "https://members.productivityintech.com",
selector : document.getElementById('srf-monthly'),
handleResponse : (response) => {
},
type: "request",
spk: "pk_live_kDLC8qiW74z3zUMfXQBjEfjD",
hideSummary: true, // Hides the summary on the side
forceCard : true, //set to true if you want credit card to be a required field for the customer
setPassword : true, //set to true if you want customer to fill out a password
})
</script>

<!-- Modal -->
<div class="modal fade" tabindex="-1" id="modal-annual" role="dialog">
<div class="modal-dialog bg-white" id="srf-annual" role="document"></div>
<script  type="text/javascript">
Servicebot.init({
templateId : 3,
url : "https://members.productivityintech.com",
selector : document.getElementById('srf-annual'),
handleResponse : (response) => {
},
type: "request",
spk: "pk_live_kDLC8qiW74z3zUMfXQBjEfjD",
hideSummary: true, // Hides the summary on the side
forceCard : true, //set to true if you want credit card to be a required field for the customer
setPassword : true, //set to true if you want customer to fill out a password
})
</script>

