define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/collections/rocket',
	'app/models/launch',
	'text!app/templates/modals/launch_edit.html'
	], function(Backbone, Marionette, EventBus, RocketCollection, Launch, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: _.template(viewHtml),
			initialize: function (){
				if(!this.model)
					this.model = new Launch({
						launch_date : moment().format(),
						payload : "",
						payload_purpose : "",
						launch_url : "",
						customer : "",
						customer_url : "",
						launch_date_tbd : false,
						country : ""
					});

				var ref = this;

				this.model.on("invalid", function(model, error) {
					ref.$el.find(".alert-danger").html(error);
					ref.$el.find(".alert-danger").removeClass('hide');
				});	
			},
			events: {
				"click .btn-success" : "save",
				"click .btn-danger" : "delete"
			},
			onRender: function (){
				var collection = new RocketCollection();
				
				var ref = this;

				collection.fetch({
					success: function () {
						ref.$el.find(".combo-rocket").append("<option value=''></option>")

						collection.models.forEach(function (rocket){
							var selectedText = "";

							if(rocket.get("id") == ref.model.get("rocket"))
							{
								selectedText = " selected ";
							}

							ref.$el.find(".combo-rocket").append("<option value='" + rocket.get("id") + "' " + selectedText + ">" + rocket.get("name") + "</option>")
						});
					}
				});

				this.$el.find(".combo-status").find("option").each(function () {
					if($(this).text() == ref.model.get("status"))
						$(this).attr("selected", "selected");
				});

				this.$el.find(".combo-orbit").find("option").each(function () {
					if($(this).text() == ref.model.get("orbit"))
						$(this).attr("selected", "selected");
				});
			},
			save: function () {
				var ref = this;

				var launch_date_time = this.$el.find("#input-launch-date-time").val()
				var launch_date_date = this.$el.find("#input-launch-date-date").val()
				var launch_date_timezone = this.$el.find("#input-launch-date-timezone").val()

				var launch_date = new Date(launch_date_date + " " + launch_date_time + " " + launch_date_timezone);

				var launch_date_tbd =  this.$el.find(".checkbox-tbd").is(':checked');

				this.model.save({
					orbit: this.$el.find(".combo-orbit").val(),
					status: this.$el.find(".combo-status").val(),
					rocket: this.$el.find(".combo-rocket").val(),
					launch_date: launch_date.toISOString(),
					launch_date_tbd : launch_date_tbd,
					payload: this.$el.find("#input-payload").val(),
					country: this.$el.find("#input-country").val(),
					payload_purpose: this.$el.find("#input-purpose").val(),
					launch_url: this.$el.find("#input-launch-url").val(),
					customer: this.$el.find("#input-customer").val(),
					customer_url: this.$el.find("#input-customer-url").val()
				});

				ref.model.refreshCustomProperties();

				ref.$el.hide();

				var editEvent = 'launch:edited:' + this.model.id;
				EventBus.trigger(editEvent, ref.model);
			},
			delete: function (){
				this.model.destroy();
			}
		});

		return View;
	});