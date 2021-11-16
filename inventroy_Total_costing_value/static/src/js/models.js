odoo.define('product_arabic_name.models', function (require) {
    "use strict";
    var core = require('web.core');
    var ajax = require('web.ajax');
    var qweb = core.qweb;
    var models = require('point_of_sale.models');
    var _super_posmodel = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({initialize:function(session, attributes) {
    var self =this;
    models.load_fields('product.product',['arabic_name','standard_price']);
    _super_posmodel.initialize.apply(this, arguments);
    },
    });
});
