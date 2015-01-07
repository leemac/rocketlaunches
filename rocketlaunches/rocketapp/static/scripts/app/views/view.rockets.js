define([
	'backbone',
	'marionette',
	'app/views/view.rocket.grid',
	'app/collections/rocket',
	'text!app/templates/rockets.html'
	], function(Backbone, Marionette, GridView, RocketCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function () {
				return viewHtml;
			},
			tagName: 'div',
			regions: {
				gridRegion: "#grid-rockets"
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