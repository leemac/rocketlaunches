define([
	'marionette',
	'countdown',
	'app/common/events',
	'text!app/templates/launch.row.details.html'
	], function(Marionette, countdown, EventBus, ViewHtml){

		View = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: function () {
				return "div";
			},
			events: {

			},
			initialize: function (options) {
 				this.options = options || {};

 				this.model = this.options.model;

 				this.render();
			},			
			render: function () {
				this.$el.html(this.template(this.model.toJSON()));
			}
		});

		return View;
	});