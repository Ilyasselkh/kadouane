/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { CalendarCommonRenderer } from "@web/views/calendar/calendar_common/calendar_common_renderer";

patch(CalendarCommonRenderer.prototype, {
    get options() {
        const options = super.options;

        if (this.props.model.scale !== "month") {
            return options;
        }

        return {
            ...options,
            fixedWeekCount: true,
            showNonCurrentDates: true,
        };
    },
});
