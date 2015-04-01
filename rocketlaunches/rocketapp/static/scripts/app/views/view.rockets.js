define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/views/view.rocket.grid',
	'app/collections/rocket',
	'text!app/templates/rockets.html'
	], function(Backbone, Marionette, EventBus, GridView, RocketCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function() {
				return _.template(viewHtml);
			},
			tagName: 'div',
			regions: {
				gridRegion: "#grid-rockets"
			},		
			events: {
				"click .btn-add-rocket" : "addRocketClick"
			},	
			addRocketClick: function()
			{
				EventBus.trigger('rocket:add');
			},
			onRender: function () {
				var collection = new RocketCollection();
				
				var ref = this;

				collection.fetch({
					success: function () {
						ref.$el.find(".spinner").hide();
						var gridView = new GridView({
							collection: collection
						});

						ref.gridRegion.show(gridView);
					}
				});
			},
		});

		return View;
	});