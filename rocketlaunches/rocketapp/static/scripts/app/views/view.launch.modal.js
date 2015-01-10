define([
	'backbone',
	'marionette',
	'app/common/events',
	'text!app/templates/modals/launch_edit.html'
	], function(Backbone, Marionette, events, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: _.template(viewHtml),
			tagName: 'div',
			initialize: function (){
				console.log('im here!')
			},
			onRender: function (){
				console.log('i rendered!')
			}
		});

		return View;
	});