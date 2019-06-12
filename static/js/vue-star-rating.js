Vue.component('star-item', {
	props: ['starData', 'star', 'toggle'],
	template: '<i v-bind:class="star" @click="toggle(star)" @mouseover="toggle(star)"></i>',
})

var app = new Vue({
	el: '#starRating',
	data: function () {
		return {
			starData: 0,
			stars: [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}].map(function(e) {
				return {
					'id': e.id,
					'far': true,
					'fas': false,
					'fa-2x': true,
					'fa-star': true,
					'text-warning': true,
					'mx-1': true
					}
				})
			}
		},

	methods: {
		toggle: function (star) {
			this.stars.forEach(function (e) {
        starData = star.id
        console.log()
				if (e.id <= star.id) {
					e.far = false
					e.fas = true
			}

			else {
				e.far = true
				e.fas = false
				}
			this.starData = star.id
			})
		}
	},

computed: {
	star_message: function () {
    console.log(this.starData)
		switch (this.starData) {
			case 1:
				return {
					class: 'text-danger',
					text: "This wasn't great at all!"
				}
				break;

			case 2:
			return {
				class: 'text-warning',
				text: 'I got very little out of it'
			}
			break;

			case 3:
			return {
				class: 'text-secondary',
				text: 'I got something out of it, but I was hoping for more'
			}
			break;

			case 4:
			return {
				class:"text-info",
				text: 'The coaching was helpful. I definitely got something out of it'
			}
			break;

			case 5:
			return {
				class:"text-success",
				text: 'OMG! This was amazing! I can\'t wait to do future sessions and learn more!'
			}
			break;

			default :
				return {
					class:"text-secondary",
					text: 'Give us your overall star Rating'
					}
				}
		}
	}
})
