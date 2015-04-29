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
				"click .listing" : "openClick"
			},
			initialize: function () {
				EventBus.on('launch:edited:' + this.model.id, this.render, this);
			},
			editLaunchClick: function()
			{
				EventBus.trigger('launch:edit', this.model);
			},
			openClick: function () {
				location.href = "#/launches/" + this.model.get("id");
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