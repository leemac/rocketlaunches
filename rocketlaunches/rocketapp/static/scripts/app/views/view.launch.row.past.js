define([
	'marionette',
	'text!app/templates/launch.row.past.html'
	], function(Marionette, ViewHtml){

		LaunchRowView = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: 'tr'
		});

		return LaunchRowView;
	});