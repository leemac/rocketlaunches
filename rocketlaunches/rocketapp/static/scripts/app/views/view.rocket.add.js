define([
	'backbone',
	'marionette',
	'app/common/events',
	'app/models/rocket',
	'text!app/templates/rocket.add.html'
	], function(Backbone, Marionette, EventBus, Rocket, viewHtml){

		View = Backbone.Marionette.LayoutView.extend({
			template: _.template(viewHtml),
			initialize: function (){
				if(!this.model)
					this.model = new Rocket({
						name : "aa",
						height: "33",
						diameter: "333",
						mass: "2",
						stages: "2",
						payload_to_leo: "33",
						payload_to_sso: "33",
						status: "ddd",
						wiki_url: "dfsdf",
						country: "us",
						rocket_function: "ddd",
						cost: 3333,
						cost_year: 233,
						first_flight_date: "2010-03-01",
						manufacturer: "ddd",
						manufacturer_url: "dddd"
					});

				var ref = this;

				this.model.on("invalid", function(model, error) {
					ref.$el.find(".alert-danger").html(error);
					ref.$el.find(".alert-danger").removeClass('hide');
				});	
			},
			events: {
				"click .btn-success" : "save"
			},
			save: function () {
				var ref = this;
			
				var launch_date_date = this.$el.find("#input-launch-date-date").val()
		
				this.model.save({
					name : this.$el.find("#input-name").val(),
					height: this.$el.find("#input-height").val(),
					diameter: this.$el.find("#input-diameter").val(),
					mass: this.$el.find("#input-mass").val(),
					stages: this.$el.find("#input-stages").val(),
					payload_to_leo: this.$el.find("#input-payload-leo").val(),
					payload_to_sso: this.$el.find("#input-payload_sso").val(),
					status: this.$el.find("#input-status").val(),
					wiki_url: this.$el.find("#input-wiki-url").val(),
					country: this.$el.find("#input-country").val(),
					rocket_function: this.$el.find("#input-function").val(),
					cost:this.$el.find("#input-cost").val(),
					cost_year: this.$el.find("#input-cost-year").val(),
					first_flight_date: new Date(this.$el.find("#input-first-flight").val()).toISOString(),
					manufacturer: this.$el.find("#input-manufacturer").val(),
					manufacturer_url: this.$el.find("#input-manufacturer-url").val(),				
				});

				var editEvent = 'rocket:edited:' + this.model.id;
				EventBus.trigger(editEvent, ref.model);
			},
			delete: function (){
				this.model.destroy();
			}
		});

		return View;
	});