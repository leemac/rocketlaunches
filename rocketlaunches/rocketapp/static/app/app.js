RocketApp = new Backbone.Marionette.Application();

RocketApp.addRegions({
  mainRegion: "#app"
});

RocketApp.addInitializer(function(options){
  var appView = new AppView();
  RocketApp.mainRegion.show(appView);
});

AppView = Backbone.Marionette.CompositeView.extend({
  template: "#view-app",
  tagName: 'div'
});

$(document).ready(function(){
  RocketApp.start();
});