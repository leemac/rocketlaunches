define([
	'backbone',
	'marionette',
	'text!app/templates/rocket.html'
	], function(Backbone, Marionette, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: _.template(viewHtml),
			tagName: 'div'
		});

		return View;
	});