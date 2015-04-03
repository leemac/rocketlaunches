({
	baseUrl: '../rocketlaunches/rocketapp/static/scripts',
    paths: {
		jquery: 'vendor/jquery',
		countdown: "vendor/countdown",
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
	    jquery: {
	      	exports: "$"
	    },
	    countdown: {
	      	exports: "countdown"
	    },
	    backbone: {
	      	deps: ["jquery", "underscore"],
	      	exports: "Backbone"
	    },
	    datetimepicker : {
		    deps: ["jquery", "bootstrap"]
		}
  	},
    name: "main",
    out: "../rocketlaunches/rocketapp/static/scripts/app.deploy/app.js",
    removeCombined: true
})