define(['backbone', 'moment'], function(Backbone){
	Helpers = {
		convert_to_human: function (date)
		{
			return moment(date, "YYYY-MM-DD h:mm:ss a").fromNow();
		}
	}

	Launch = Backbone.Model.extend({
		initialize: function(){
			var launch_date = this.get("launch_date");

			if(launch_date)
				this.set("launch_date_human", Helpers.convert_to_human(launch_date));
		}
	});

	return Launch;
});