define([
	'marionette',
	'app/common/events',
	'text!app/templates/launch.row.past.html'
	], function(Marionette, EventBus, ViewHtml){

		LaunchRowView = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: 'tr',
			events: {
				"click .btn-edit" : "editLaunchClick"
			},
			initialize: function () {
				EventBus.on('launch:edited:' + this.model.id, this.render, this.model);
			},
			editLaunchClick: function()
			{
				EventBus.trigger('launch:edit', this.model);
			}
		});

		return LaunchRowView;
	});