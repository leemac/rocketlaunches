define([
	'jquery',
	'backbone',
	'marionette',
	'app/views/view.launch.row',
	'app/views/view.launch.row.past',
	'text!app/templates/launch.grid.html',
	'text!app/templates/launch.grid.past.html',
	'bootstrap',
	'vendor/jquery.fancybox.pack',
	'vendor/jquery.fancybox.media'
	], function($, Backbone, Marionette, LaunchRowView, LaunchRowViewPast, viewHtml, viewPastHtml){

		GridView = Backbone.Marionette.CompositeView.extend({
			getChildView: function () {
				if(this.options.isPast)
					return LaunchRowViewPast;
				else
					return LaunchRowView;
			},
			initialize: function(options) {
			    this.options = options;

			    if(this.options.isPast)
					this.template = _.template(viewPastHtml);
				else
					this.template = _.template(viewHtml);

			    _.bindAll(this, 'render');
			},
			childViewContainer: "div",
			onRender: function () {
				this.$el.find(".video-link").fancybox({
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