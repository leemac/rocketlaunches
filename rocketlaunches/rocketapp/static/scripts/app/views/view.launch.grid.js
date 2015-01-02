define([
	'jquery',
	'backbone',
	'marionette',
	'app/collections/launch',
	'app/views/view.launch.row',
	'text!app/templates/launch.grid.html',
	'bootstrap',
	'vendor/jquery.fancybox.pack',
	'vendor/jquery.fancybox.media'
	], function($, Backbone, Marionette, LaunchCollection, LaunchRowView, viewHtml){

		GridView = Backbone.Marionette.CompositeView.extend({
			template: function () {
				return _.template(viewHtml);
			},
			tagName: 'div',
			onRender: function () {
				var ref = this;

				var collection = new LaunchCollection();
				collection.fetch({
					success: function (collection, response, options) {
						_.each(collection.models, function(model) {

							model.launch_date_human = Helpers.convert_to_human(model.launch_date);

							var rowView = new LaunchRowView({
								model: model
							});

							ref.$el.find("table.launches").append(rowView.render().el);
						});

						ref.$el.find(".video-link").each(function () {
							var hostname = new URL($(this).attr("href")).hostname;

							var provider = "";

							switch(hostname)
							{
								case "www.youtube.com":
								provider = "youtube";
								break;
							}

							$(this).html("<img src='static/images/video_providers/" + provider + ".png' style='width: 30px' title='Click to watch this launch!' />");
						});

						$(".fancybox").fancybox({
							helpers : {
								media: true
							},
							youtube : {
								autoplay: 1
							}
						});

						$('[data-toggle="tooltip"]').tooltip();
					},
					error: function (collection, response, options) {

					}
				});

			}
		});

return GridView;
});