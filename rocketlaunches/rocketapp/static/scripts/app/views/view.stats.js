define([
	'backbone',
	'marionette',
	'vendor/chart.min',
	'text!app/templates/stats.html'
	], function(Backbone, Marionette, Chart, viewHtml){

		AboutView = Backbone.Marionette.LayoutView.extend({
			template: function () {
				return viewHtml;
			},
			tagName: 'div'
		});

		return AboutView;
	});