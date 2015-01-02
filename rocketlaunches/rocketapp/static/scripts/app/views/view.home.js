define([
	'backbone',
	'marionette',
	'app/views/view.launch.grid',
	'text!app/templates/home.html'
	], function(Backbone, Marionette, GridView, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function() {
				return viewHtml;
			},
			tagName: 'div',
			regions: {
				gridRegion: "#grid-launches"
			},
			onRender: function () {
				var gridView = new GridView();
				this.gridRegion.show(gridView);
			}
		});

		return View;
	});