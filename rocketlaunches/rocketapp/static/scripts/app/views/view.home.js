define([
	'backbone',
	'marionette',
	'app/models/launch',
	'app/views/view.launch.grid',
	'app/collections/launch',
	'text!app/templates/home.html'
	], function(Backbone, Marionette, Launch, GridView, LaunchCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function() {
				return viewHtml;
			},
			tagName: 'div',
			regions: {
				upcomingRegion: "#grid-upcoming",
				pastRegion: "#grid-past"
			},
			onRender: function () {
				this.renderUpcomingLaunches();
				this.renderPastLaunches();				
			},
			renderUpcomingLaunches: function () {
				var launchCollection = new LaunchCollection();
				
				var ref = this;

				launchCollection.fetch({
					data: $.param({ type: 'upcoming'}),
					success: function () {
						ref.$el.find(".spinner-upcoming").hide();
						var gridView = new GridView({
							collection: launchCollection
						});

						ref.upcomingRegion.show(gridView);
					}
				});
			},
			renderPastLaunches: function () {
				var launchCollection = new LaunchCollection();
				
				var ref = this;

				launchCollection.fetch({
					data: $.param({ type: 'past'}),
					success: function () {
						ref.$el.find(".spinner-past").hide();
						var gridView = new GridView({ 
							isPast: true,
							collection: launchCollection
						});

						ref.pastRegion.show(gridView);
					}
				});
			}
		});

		return View;
	});