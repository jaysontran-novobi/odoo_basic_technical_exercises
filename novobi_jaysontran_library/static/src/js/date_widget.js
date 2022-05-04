odoo.define('book_borrower.widget', function (require) {
    "use strict";

    var basic_fields = require('web.basic_fields');
    var field_registry = require('web.field_registry');

    var TodayAboveTime = basic_fields.FieldDate.extend({
        init: function () {
            this.nodeOptions.datepicker.minDate = 0;
            this._super.apply(this, arguments);
        }
    });

    field_registry.add('todayabove_time', TodayAboveTime);

    return TodayAboveTime;
});