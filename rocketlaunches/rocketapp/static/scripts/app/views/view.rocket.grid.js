define([
	'jquery',
	'backbone',
	'marionette',
	'app/views/view.rocket.row',
	'text!app/templates/rocket.grid.html',
	'bootstrap',
	'vendor/jquery.fancybox.pack',
	'vendor/jquery.fancybox.media'
	], function($, Backbone, Marionette, ChildView, viewHtml){

		GridView = Backbone.Marionette.CompositeView.extend({
			template: function() {
				return viewHtml;
			},
			childView: ChildView,
			childViewContainer: "tbody"
		});

	return GridView;
});