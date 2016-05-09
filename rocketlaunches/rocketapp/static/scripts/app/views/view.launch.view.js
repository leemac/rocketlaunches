define([
	'backbone',
	'marionette',
	'text!app/templates/launches.view.html'
	], function(Backbone, Marionette, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: _.template(viewHtml),
			tagName: 'div',
			initialize: function () {
				//this.render();
			}
		});

		return View;
	});