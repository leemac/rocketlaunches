define([
  'backbone',
  'marionette',
  ], function(Backbone, Marionette){

    var ModalRegion = Backbone.Marionette.Region.extend({
      el: "#modal",

      constructor: function(){
        _.bindAll(this, 'show', 'showModal');
        Backbone.Marionette.Region.prototype.constructor.apply(this, arguments);
        this.on("show", this.showModal, this);
      },

      getEl: function(selector){
        var $el = $(selector);
        $el.on("hidden", this.close);
        return $el;
      },

      showModal: function(view){
        view.on("close", this.hideModal, this);
        this.$el.find(".modal").modal('show');
      },

      hideModal: function(){
        this.$el.find(".modal").modal('hide');
      }
    });

    return ModalRegion;
  });