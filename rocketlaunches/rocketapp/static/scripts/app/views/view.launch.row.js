define([
	'marionette',
	'app/common/events',
	'text!app/templates/launch.row.html'
	], function(Marionette, events, ViewHtml){

		LaunchRowView = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: 'tr',
			events: {
				"click .btn-edit" : "editLaunchClick"
			},
			editLaunchClick: function()
			{
				events.trigger('launch:edit', this.model);
			}
		});

		return LaunchRowView;
	});