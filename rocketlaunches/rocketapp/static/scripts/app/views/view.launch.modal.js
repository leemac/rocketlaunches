define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/collections/rocket',
	'text!app/templates/modals/launch_edit.html'
	], function(Backbone, Marionette, EventBus, RocketCollection, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: _.template(viewHtml),
			initialize: function (){
				
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
						collection.models.forEach(function (rocket){
							var selectedText = "";

							if(rocket.get("id") == ref.model.get("rocket_id"))
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
				this.model.set("orbit", this.$el.find(".combo-orbit").val());
				this.model.set("status", this.$el.find(".combo-status").val());
				this.model.set("rocket", this.$el.find(".combo-rocket").val());

				this.model.set("launch_date", this.$el.find("#input-launch-date").val());
				this.model.set("payload", this.$el.find("#input-payload").val());
				this.model.set("purpose", this.$el.find("#input-purpose").val());
				this.model.set("launch_url", this.$el.find("#input-launch-url").val());
				this.model.set("customer", this.$el.find("#input-customer").val());
				this.model.set("customer_url", this.$el.find("#input-customer-url").val());

				this.model.save();
				this.model.refreshCustomProperties();

				EventBus.trigger('launch:edited:' + this.model.id, this.model);

				this.$el.hide();
			},
			delete: function (){
				this.model.destroy();
			}
		});

		return View;
	});