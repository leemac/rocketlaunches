RocketApp = new Backbone.Marionette.Application();

RocketApp.addRegions({
  mainRegion: "#app",
  gridRegion: "#grid-launches"
});

RocketApp.addInitializer(function(options){
  var appView = new AppView();
  RocketApp.mainRegion.show(appView);

  var gridView = new GridView();
  RocketApp.gridRegion.show(gridView);
});

/* Views */

AppView = Backbone.Marionette.CompositeView.extend({
  template: "#view-app",
  tagName: 'div'
});

LaunchRowView = Backbone.Marionette.ItemView.extend({
  template: "#view-launch-row",
  tagName: 'tr'
});

GridView = Backbone.Marionette.CompositeView.extend({
  template: "#view-launches",
  tagName: 'div',
  onRender: function () {
    var ref = this;

  	var collection = new LaunchCollection();
  	collection.fetch({
  		success: function (collection, response, options) {
  			 _.each(collection.models, function(model) {

		        var rowView = new LaunchRowView({
              model: model
            });

            ref.$el.find(".grid").append(rowView.render().el);
		      });
        },
        error: function (collection, response, options) {

        }
  	});
  }
});

/* Models */

Launch = Backbone.Model.extend({

});

LaunchCollection = Backbone.Collection.extend({
	model: Launch,
	url: function () {
		return "api/launches"
	}
});

/* Run */

$(document).ready(function(){
  RocketApp.start();
});
