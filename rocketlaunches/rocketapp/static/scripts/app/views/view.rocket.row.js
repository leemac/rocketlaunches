define([
	'marionette',
	'text!app/templates/rocket.row.html'
	], function(Marionette, ViewHtml){

		View = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: 'tr'
		});

		return View;
	});