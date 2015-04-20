define([
	'backbone',
	'marionette',
	'app/models/launch',
	'app/models/subscriber',
	'app/common/events',
	'app/views/view.launch.grid',
	'app/collections/launch',
	'text!app/templates/home.html'
	], function(Backbone, Marionette, Launch, Subscriber, EventBus, GridView, LaunchCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: function() {
				return _.template(viewHtml);
			},
			tagName: 'div',
			regions: {
				upcomingRegion: "#grid-upcoming"
			},
			events: {
				"click .btn-add-launch" : "addLaunchClick",
				"click .button-subscribe" : "addSubscriber"
			},
			addSubscriber: function ()
			{
				var enteredEmail = this.$el.find(".textbox-email").val();

				if(!this.validateEmail(enteredEmail)) {
					alert("Please enter a valid email!");
					return;
				}
					
				var subscriber = new Subscriber();
				subscriber.set("email", enteredEmail);

				subscriber.save();
			},
			addLaunchClick: function()
			{
				EventBus.trigger('launch:add');
			},
			onRender: function () {		
				this.refreshGrids();
				EventBus.on('launch:edited', this.refreshGrids, this);			
			},
			refreshGrids: function (){
				this.renderUpcomingLaunches();
			},
			renderUpcomingLaunches: function () {
				var launchCollection = new LaunchCollection();
				
				var ref = this;

				launchCollection.fetch({
					data: $.param({ type: 'upcoming'}),
					success: function () {
						ref.$el.find(".loader").hide();
						var gridView = new GridView({
							collection: launchCollection
						});

						ref.upcomingRegion.show(gridView);
					}
				});
			},
			validateEmail: function (email) {
			    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
			    return re.test(email);
			}
		});

		return View;
	});