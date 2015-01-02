define(['backbone', 'app/models/launch',], function(Backbone, Launch){
	LaunchCollection = Backbone.Collection.extend({
		model: Launch,
		url: function () {
			return "api/launches"
		}
	});

	return LaunchCollection;
});