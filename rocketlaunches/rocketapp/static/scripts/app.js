define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/views/view.app'
], function(Backbone, Marionette, events, AppView){


  	RocketApp = new Marionette.Application();

	RocketApp.addRegions({
		appRegion: "#app"
	});

	RocketApp.addInitializer(function(options){
		var appView = new AppView();
		RocketApp.appRegion.show(appView);

		Backbone.history.start(); 
	});

	return RocketApp;
});