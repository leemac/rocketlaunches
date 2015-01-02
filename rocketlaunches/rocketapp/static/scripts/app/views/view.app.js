define([
	'backbone',
	'marionette',
	'app/views/view.home',
	'app/views/view.about',
	'text!app/templates/app.html'
	], function(Backbone, Marionette, HomeView, AboutView, appHtml){

		AppRouter = Backbone.Router.extend({
			routes: { 
				'' : 'home', 
				'about': 'about' 
			} 
		}); 

		AppView = Backbone.Marionette.LayoutView.extend({
			template: function () {
				return appHtml;
			},
			tagName: 'div',
			regions: {    
				contentRegion: "#content"

			},
			initialize: function () {
				this.router = new AppRouter();

				var ref = this;

				this.router.on('route:home', function(actions) {        
					var view = new HomeView();
					ref.contentRegion.show(view);
				});

				this.router.on('route:about', function(actions) {        
					var view = new AboutView();
					ref.contentRegion.show(view);
				});
			}
		});

		return AppView;
	});