RocketApp = new Backbone.Marionette.Application();

RocketApp.addRegions({
  appRegion: "#app"
});

RocketApp.addInitializer(function(options){
  var appView = new AppView();
  RocketApp.appRegion.show(appView);

  Backbone.history.start(); 
});

Helpers = {
  convert_to_human: function (date)
  {
    return moment(date, "YYYY-MM-DD h:mm:ss a").fromNow();
  }
}

/* Layouts */

AppView = Backbone.Marionette.LayoutView.extend({
  template: "#view-app",
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

      this.router.on('route:about', function(actions) {        
        var view = new AboutView();
        ref.contentRegion.show(view);
      });
  }
});

/* Views */

LaunchRowView = Backbone.Marionette.ItemView.extend({
  template: "#view-launch-row",
  tagName: 'tr'
});

HomeView = Backbone.Marionette.LayoutView.extend({
  template: "#view-home",
  tagName: 'div',
  regions: {
    gridRegion: "#grid-launches"
  },
  onRender: function () {
    var gridView = new GridView();
    this.gridRegion.show(gridView);
  }
});

AboutView = Backbone.Marionette.ItemView.extend({
  template: "#view-about",
  tagName: 'div'
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

            model.launch_date_human = Helpers.convert_to_human(model.launch_date);

		        var rowView = new LaunchRowView({
              model: model
            });

            ref.$el.find("table.launches").append(rowView.render().el);
		      });

          ref.$el.find(".video-link").each(function () {
            var hostname = new URL($(this).attr("href")).hostname;

            var provider = "";

            switch(hostname)
            {
              case "www.youtube.com":
                provider = "youtube";
                break;
            }

            $(this).html("<img src='static/images/video_providers/" + provider + ".png' style='width: 30px' title='Click to watch this launch!' />");
          });

          $(".fancybox").fancybox({
              helpers : {
                media: true
            },
            youtube : {
                autoplay: 1
            }
          }
            );
        },
        error: function (collection, response, options) {

        }
  	});

  }
});

/* Models */

Launch = Backbone.Model.extend({
  initialize: function(){
    var launch_date = this.get("launch_date");

    if(launch_date)
      this.set("launch_date_human", Helpers.convert_to_human(launch_date));
  }
});

LaunchCollection = Backbone.Collection.extend({
	model: Launch,
	url: function () {
		return "api/launches"
	}
});


AppRouter = Backbone.Router.extend (
  { 
    routes: { 
      '' : 'home', 
      'about': 'about' 
    } 
  }); 

/* Run */

$(document).ready(function(){
  RocketApp.start();
});

