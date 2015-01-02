define([
	'jquery',
	'backbone',
	'marionette',
	'app/collections/launch',
	'app/views/view.launch.row',
	'bootstrap'
	], function($, Backbone, Marionette, LaunchCollection, LaunchRowView){

		GridView = Backbone.Marionette.CollectionView.extend({
			childView: LaunchRowView,
			childViewContainer: "tbody"
		});

	return GridView;
});