define(['backbone', 'moment'], function(Backbone){

	Rocket = Backbone.Model.extend({
		url: function () {
			return "api/rockets/" + this.id
		}
	});

	return Rocket;
});