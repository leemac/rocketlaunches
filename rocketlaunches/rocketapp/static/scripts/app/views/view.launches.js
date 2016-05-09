define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/views/view.launch.grid',
	'app/collections/launch',
	'text!app/templates/launches.html'
	], function(Backbone, Marionette, EventBus, GridView, LaunchCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function() {
				return _.template(viewHtml);
			},
			tagName: 'div',
			regions: {
				upcomingRegion: "#grid-upcoming",
				pastRegion: "#grid-past"
			},		
			events: {
				"click .btn-add-launch" : "addLaunchClick"
			},	
			addRocketClick: function()
			{
				EventBus.trigger('launch:add');
			},
			onRender: function () {
				this.refreshGrids();
			},
			refreshGrids: function (){
				this.renderPastLaunches();	
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