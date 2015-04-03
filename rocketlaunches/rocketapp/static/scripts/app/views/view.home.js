define([
	'backbone',
	'marionette',
	'app/models/launch',
	'app/common/events',
	'app/views/view.launch.grid',
	'app/collections/launch',
	'text!app/templates/home.html'
	], function(Backbone, Marionette, Launch, EventBus, GridView, LaunchCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function() {
				return _.template(viewHtml);
			},
			tagName: 'div',
			regions: {
				upcomingRegion: "#grid-upcoming"
			},
			events: {
				"click .btn-add-launch" : "addLaunchClick"
			},
			addLaunchClick: function()
			{
				EventBus.trigger('launch:add');
			},
			onRender: function () {		
				this.refreshGrids();
				EventBus.on('launch:edited', this.refreshGrids, this);			
			},
			refreshGrids: function (){
				this.renderUpcomingLaunches();
			},
			renderUpcomingLaunches: function () {
				var launchCollection = new LaunchCollection();
				
				var ref = this;

				launchCollection.fetch({
					data: $.param({ type: 'upcoming'}),
					success: function () {
						ref.$el.find(".loader").hide();
						var gridView = new GridView({
							collection: launchCollection
						});

						ref.upcomingRegion.show(gridView);
					}
				});
			}
		});

		return View;
	});