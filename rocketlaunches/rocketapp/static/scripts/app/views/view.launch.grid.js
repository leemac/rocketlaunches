define([
	'jquery',
	'backbone',
	'marionette',
	'app/views/view.launch.row',
	'text!app/templates/launch.grid.html',
	'bootstrap',
	'vendor/jquery.fancybox.pack',
	'vendor/jquery.fancybox.media'
	], function($, Backbone, Marionette, LaunchRowView, viewHtml){

		GridView = Backbone.Marionette.CompositeView.extend({
			template: function() {
				return viewHtml;
			},
			childView: LaunchRowView,
			childViewContainer: "tbody",
			onRender: function () {
				this.$el.find(".fancybox").fancybox({
					helpers : {
						media: true
					},
					youtube : {
						autoplay: 1
					}
				});

				this.$el.find('[data-toggle="tooltip"]').tooltip();
			}
		});

	return GridView;
});