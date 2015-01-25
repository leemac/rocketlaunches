require.config({
	paths: {
		jquery: 'vendor/jquery',
		datetimepicker: 'vendor/bootstrap.datetimepicker',
		underscore: 'vendor/underscore',
		backbone: 'vendor/backbone',
		marionette: 'vendor/backbone.marionette',
		moment: 'vendor/moment',
		text: "vendor/text"
	},
	shim: {
	    underscore: {
	      	exports: "_"
	    },
	    backbone: {
	      	deps: ["jquery", "underscore"],
	      	exports: "Backbone"
	    },
	    datetimepicker : {
		    deps: ["jquery", "bootstrap"]
		}
  	}
});

require(['app',], function(App){
  App.start();
});