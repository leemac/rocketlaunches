define([
	'backbone',
	'marionette',
	'app/models/rocket',
	'app/views/view.home',
	'app/views/view.rockets',
	'app/views/view.rocket',
	'app/views/view.about',
	'app/views/view.stats',
	'text!app/templates/app.html'
	], function(Backbone, Marionette, Rocket, HomeView, RocketsView, RocketView, AboutView, StatsView, appHtml){

		AppRouter = Backbone.Router.extend({
			routes: { 
				'' : 'home',
				'rockets' : 'rockets', 
				'rockets/:id' : 'rockets_view', 
				'stats' : 'stats', 
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

				this.router.on('route:rockets', function(actions) {      
					var view = new RocketsView();
					ref.contentRegion.show(view);
				});

				this.router.on('route:rockets_view', function(id) {      
					
					var launch = new Rocket({id : id});
					
					launch.fetch({
						success: function () {
							var view = new RocketView({ model : launch});
							ref.contentRegion.show(view);
						}
					});
				});

				this.router.on('route:stats', function(actions) {        
					var view = new StatsView();
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