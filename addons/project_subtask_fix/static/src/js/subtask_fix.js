/** @odoo-module **/

/**
 * Temporary JS patch for the Project sub-tasks inline editor.
 *
 * In some situations, pressing keys while editing a sub-task inline
 * crashes with:
 *
 *   TypeError: Cannot read properties of null (reading 'dirty')
 *     at SubtaskListRenderer.onCellKeydownEditMode(...)
 *
 * We wrap the original handler and swallow only this very specific error,
 * so users do not see the Odoo Client Error popup anymore. Other errors
 * are still raised normally.
 */

import { SubtaskListRenderer } from "@project/views/subtask_list/subtask_list_renderer";
import { patch } from "@web/core/utils/patch";

const originalOnCellKeydownEditMode = SubtaskListRenderer.prototype.onCellKeydownEditMode;

if (originalOnCellKeydownEditMode) {
    patch(SubtaskListRenderer.prototype, "project_subtask_fix.onCellKeydownEditMode", {
        onCellKeydownEditMode(ev, ...args) {
            try {
                return originalOnCellKeydownEditMode.call(this, ev, ...args);
            } catch (error) {
                // Only swallow the specific 'reading "dirty"' TypeError we observed.
                const msg = error && error.message ? String(error.message) : "";
                if (msg.includes("reading 'dirty'")) {
                    console.warn(
                        "[project_subtask_fix] Ignored SubtaskListRenderer 'dirty' error:",
                        error
                    );
                    return;
                }
                // Anything else should behave as usual.
                throw error;
            }
        },
    });
}

