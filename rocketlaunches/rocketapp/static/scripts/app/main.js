require.config({
	paths: {
		jquery: 'vendor/jquery',
		bootstrap: 'vendor/bootstrap.min',
		fancyboxmedia: 'vendor/jquery.fancybox.media',
		fancyboxpack: 'vendor/jquery.fancybox.pack',
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
	    bootstrap: {
	      	deps: ["jquery"]
	    },
	    fancyboxmedia: {
	      	deps: ["jquery"]
	    },
	    fancyboxpack: {
	      	deps: ["jquery"]
	    }
  	}
});

require(['app'], function(App){
  	App.initialize();	
});