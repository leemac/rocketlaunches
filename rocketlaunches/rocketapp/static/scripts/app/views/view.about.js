define([
	'backbone',
	'marionette',
	'text!app/templates/about.html'
	], function(Backbone, Marionette, viewHtml){

		AboutView = Backbone.Marionette.LayoutView.extend({
			template: function () {
				return viewHtml;
			},
			tagName: 'div'
		});

		return AboutView;
	});