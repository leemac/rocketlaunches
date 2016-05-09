define([
	'marionette',
	'text!app/templates/launch.html'
	], function(Marionette, ViewHtml){

		View = Marionette.LayoutView.extend({
			template: _.template(ViewHtml),
			tagName: 'div'
		});

		return View;
	});