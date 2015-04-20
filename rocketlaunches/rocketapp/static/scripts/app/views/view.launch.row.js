define([
	'marionette',
	'countdown',
	'app/common/events',
	'text!app/templates/launch.row.html',
	'app/views/view.launch.row.details'
	], function(Marionette, countdown, EventBus, ViewHtml, RowDetailsView){

		LaunchRowView = Backbone.Marionette.ItemView.extend({
			template: _.template(ViewHtml),
			tagName: function () {
				return "div";
			},
			events: {
				"click .btn-edit" : "editLaunchClick",
				//"click .listing" : "expandClick"
			},
			initialize: function () {
				EventBus.on('launch:edited:' + this.model.id, this.render, this);
			},
			editLaunchClick: function()
			{
				EventBus.trigger('launch:edit', this.model);
			},
			expandClick: function () {
				var ref = this;
				var speed = 300;
				var listing = this.$el.find(".listing");

				listing.stop();

				if(!this.isExpanded)
				{						
					this.isExpanded = true;
					this.originalHeight = this.$el.height();

					listing.animate({
		                height : '400px'	
	            	}, speed, 'swing', function () {
						// TODO: Make this more marionette-like
	            		ref.$el.find(".details").html(new RowDetailsView({ model : ref.model }).$el.html());
	            	});
				}
				else
				{
					this.isExpanded = false;
					
					// TODO: Make this more marionette-like
					ref.$el.find(".details").html("");

					listing.animate({
		                height : this.originalHeight + 'px'
	            	}, speed, 'swing');
				}
			},
			render: function () {
				this.$el.html(this.template(this.model.toJSON()));

				var countdownElement = this.$el.find(".countdown");

				var date = countdownElement.attr("js-launch-date");

				countdown(new Date(date),
						    function(ts) {
						      countdownElement.html(ts.toHTML());
						    },
						    countdown.DAYS|countdown.HOURS|countdown.MINUTES|countdown.SECONDS);
			}
		});

		return LaunchRowView;
	});