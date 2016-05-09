define(['backbone', 'app/models/rocket',], function(Backbone, Rocket){
	LaunchCollection = Backbone.Collection.extend({
		model: Rocket,
		url: function () {
			return "api/rockets"
		}
	});

	return LaunchCollection;
});