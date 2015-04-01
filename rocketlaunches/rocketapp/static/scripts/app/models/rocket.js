define(['backbone', 'moment'], function(Backbone){

	Rocket = Backbone.Model.extend({
		url: function () {
			if(this.id)
				return "api/rockets/?id=" + this.id;

			return "api/rockets/";
		}
	});

	return Rocket;
});