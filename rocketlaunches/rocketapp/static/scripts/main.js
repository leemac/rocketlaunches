require.config({
	paths: {
		jquery: 'vendor/jquery',
		bootstrap: 'vendor/bootstrap',
		datetimepicker: 'vendor/bootstrap.datetimepicker',
		countdown: "vendor/countdown",
		underscore: 'vendor/underscore',
		backbone: 'vendor/backbone',
		marionette: 'vendor/backbone.marionette',
		moment: 'vendor/moment',
		text: "vendor/text",
		fancybox : 'vendor/jquery.fancybox.pack',
    	fancyboxmedia: 'vendor/jquery.fancybox.media'
	},
	shim: {
	    underscore: {
	      	exports: "_"
	    }, 
	    jquery: {
	      	exports: "$"
	    },
	    countdown: {
	      	exports: "countdown"
	    },
     	moment: {
	      	exports: "moment"
	    },
     	fancybox: {
		    deps: ["jquery"],
	      	exports: "fancybox"
	    },
	    fancyboxmedia: {
		    deps: ["jquery"]
	    },
	    backbone: {
	      	deps: ["jquery", "underscore"],
	      	exports: "Backbone"
	    },

	    bootstrap : {
		    deps: ["jquery"]
		},
	    datetimepicker : {
		    deps: ["jquery", "bootstrap"]
		}
  	}
});

require(['app'], function(App){
  App.start();
});