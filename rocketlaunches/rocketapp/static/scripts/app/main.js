require.config({
	paths: {
		jquery: 'vendor/jquery',
		underscore: 'vendor/underscore',
		backbone: 'vendor/backbone',
		marionette: 'vendor/backbone.marionette'
	},
	shim: {
	    underscore: {
	      	exports: "_"
	    },
	    backbone: {
	      	deps: ["jquery", "underscore"],
	      	exports: "Backbone"
	    },
	    marionette: {
	      	deps: ["backbone"],
	      	exports: "Marionette"
	    },
  	}
});

require(['app',], function(App){
  App.initialize();
});