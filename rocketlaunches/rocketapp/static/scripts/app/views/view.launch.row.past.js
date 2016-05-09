define([
	'marionette',
	'app/common/events',
	'text!app/templates/launch.row.past.html'
	], function(Marionette, EventBus, ViewHtml){

		LaunchRowView = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: 'div',
			events: {
				"click .btn-edit" : "editLaunchClick",
				"click .listing" : "openClick"
			},
			initialize: function () {
				EventBus.on('launch:edited:' + this.model.id, this.render, this.model);
			},
			openClick: function () {
				location.href = "#/launches/" + this.model.get("id");
			},
			editLaunchClick: function()
			{
				EventBus.trigger('launch:edit', this.model);
			}
		});

		return LaunchRowView;
	});