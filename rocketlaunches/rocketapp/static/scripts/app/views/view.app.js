define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/models/rocket',
	'app/regions/modal',
	'app/views/view.home',
	'app/views/view.rockets',
	'app/views/view.rocket',
	'app/views/view.about',
	'app/views/view.stats',
	'app/views/view.launch.modal',
	'text!app/templates/app.html'
	], function(
		Backbone, 
		Marionette,
		// Misc. 
		events, 
		// Models
		Rocket, 
		// Regions
		ModalRegion, 
		// Views
		HomeView, 
		RocketsView, 
		RocketView, 
		AboutView, 
		StatsView, 
		LaunchModal,
		// Html
		appHtml){

		AppRouter = Backbone.Router.extend({
			routes: { 
				'' : 'home',
				'rockets' : 'rockets', 
				'rockets/:id' : 'rockets_view', 
				'stats' : 'stats', 
				'about': 'about' 
			} 
		}); 

		function Log(msg)
		{
			console.log(msg);
		}

		var contentRegion = Backbone.Marionette.Region.extend({
			el: "#content"
		});

		AppView = Backbone.Marionette.LayoutView.extend({
			template: function () {
				return appHtml;
			},
			tagName: 'div',
			regions: {    
				contentRegion: contentRegion,
				modalRegion: ModalRegion
			},
			initialize: function () {
				this.router = new AppRouter();

				events.on('launch:edit', this.renderLaunchEdit, this);

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
			},
			renderLaunchEdit: function(args)
			{
				console.log('edit')
				var view = new LaunchModal();
				this.modalRegion.show(view);
			}
		});

		return AppView;
	});