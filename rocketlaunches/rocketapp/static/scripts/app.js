define([
	'backbone',
	'marionette',
	'app/views/view.app'
], function(Backbone, Marionette, AppView){
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