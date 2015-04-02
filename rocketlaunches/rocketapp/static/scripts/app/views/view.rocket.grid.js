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
			template: _.template(viewHtml),
			childView: ChildView,
			childViewContainer: "div"
		});

	return GridView;
});