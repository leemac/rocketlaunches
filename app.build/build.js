({
	baseUrl: '../rocketlaunches/rocketapp/static/scripts',
    paths: {
		jquery: 'vendor/jquery',
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
	    }
  	},
    name: "main",
    out: "../rocketlaunches/rocketapp/static/scripts/app.deploy/app.js",
    removeCombined: true
})