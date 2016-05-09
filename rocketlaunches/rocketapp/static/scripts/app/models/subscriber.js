define(['backbone', 'moment'], function(Backbone){

	Subscriber = Backbone.Model.extend({
		url: function () {
			if(this.id)
				return "api/subscribers/?id=" + this.id;

			return "api/subscribers/";
		}
	});

	return Subscriber;
});