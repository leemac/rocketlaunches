define(['backbone', 'moment'], function(Backbone){

	Helpers = {
		convert_to_human: function (date)
		{
			return moment(date).fromNow();
		},
		daysBetween: function (date1, date2)
		{
			var diff = Math.abs(date1.getTime() - date2.getTime());
			return diff / (1000 * 60 * 60 * 24);
		}
	}

	Launch = Backbone.Model.extend({
		initialize: function(){
			this.refreshCustomProperties();
		},
		url: function () {
			return "api/launches/"
		},
	  	validate: function (attrs) {
	        if (!attrs.launch_date) {
	            return 'Please provide a Launch Date';
	        }

	        if (!attrs.rocket) {
	            return 'Please provide a Rocket';
	        }

	        if (!attrs.status) {
	            return 'Please provide a Status';
	        }

	        if (!attrs.orbit) {
	            return 'Please provide an Orbit';
	        }

	        if (!attrs.country) {
	            return 'Please provide a Country';
	        }
	    },
		refreshCustomProperties: function () {		
			var launch_date = this.get("launch_date");

			if(launch_date)	{
				this.set("launch_date_human", Helpers.convert_to_human(launch_date));
				this.set("launch_date_formatted", moment(launch_date).format('MMMM Do YYYY [at] h:mm:ss a'));
				this.set("launch_date_time", moment(launch_date).format('hh:mm'));
				this.set("launch_date_date", moment(launch_date).format('MM/DD/YYYY'));

				var now = new Date();
				var then = new Date(launch_date);
				if(now < then) {
					var daysFromNow = Helpers.daysBetween(then, now);

					if(daysFromNow <= 5)
						this.set("is_close", true);
					else						
						this.set("is_close", false);
				}
				else
					this.set("is_close", false);

			}
		}
	});

	return Launch;
});