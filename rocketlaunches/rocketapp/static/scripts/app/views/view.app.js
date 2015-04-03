define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/models/rocket',
	'app/regions/modal',
	'app/views/view.home',
	'app/views/view.about',
	'app/views/view.stats',
	'app/views/view.launch.modal',
	'app/views/view.launches',
	'app/views/view.rockets',
	'app/views/view.rocket.view',
	'app/views/view.rocket.add',
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
		AboutView, 
		StatsView, 
		LaunchModal,
		LaunchesView, 
		RocketsView, 
		RocketView, 
		RocketAddView,
		// Html
		appHtml){

		AppRouter = Backbone.Router.extend({
			routes: { 
				'' : 'home',
				'rockets' : 'rockets', 
				'rockets/add' : 'rockets_add', 
				'rockets/:id' : 'rockets_view', 				
				'launches' : 'launches', 
				'stats' : 'stats', 
				'about': 'about' 
			} 
		}); 

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

				events.on('launch:add', this.renderLaunchAdd, this);
				events.on('launch:edit', this.renderLaunchEdit, this);
				events.on('rocket:add', this.renderRocketAdd, this);

				var ref = this;

				this.router.on('route:home', function(actions) {        
					var view = new HomeView();
					ref.contentRegion.show(view);
				});

				this.router.on('route:rockets', function(actions) {      
					var view = new RocketsView();
					ref.contentRegion.show(view);
				});

				this.router.on('route:launches', function(actions) {      
					var view = new LaunchesView();
					ref.contentRegion.show(view);
				});

				this.router.on('route:rockets_add', function(actions) {      
					var view = new RocketAddView();
					ref.contentRegion.show(view);
				});

				this.router.on('route:rockets_view', function(id) {      
					
					var rocket = new Rocket({id : id});
					
					rocket.fetch({
						success: function () {
							var view = new RocketView({ model : rocket });
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
			renderLaunchAdd: function()
			{
				var view = new LaunchModal();
				this.modalRegion.show(view);
			},
			renderLaunchEdit: function(launch_model)
			{
				var view = new LaunchModal({ model : launch_model});
				this.modalRegion.show(view);
			},
			renderRocketAdd: function()
			{
				var view = new RocketModal();
				this.modalRegion.show(view);
			},
		});

		return AppView;
	});