define([
  'backbone',
  'marionette',
  ], function(Backbone, Marionette){

    var ModalRegion = Backbone.Marionette.Region.extend({
      el: "#modal",

      constructor: function(){
        _.bindAll(this);
        Backbone.Marionette.Region.prototype.constructor.apply(this, arguments);
        this.on("view:show", this.showModal, this);
      },

      getEl: function(selector){
        var $el = $(selector);
        $el.on("hidden", this.close);
        return $el;
      },

      showModal: function(view){
        console.log('showing!')
        view.on("close", this.hideModal, this);
        this.$el.modal('show');
      },

      hideModal: function(){
        this.$el.modal('hide');
      }
    });

    return ModalRegion;
  });