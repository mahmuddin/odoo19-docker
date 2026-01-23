# Simple Timeline View for Odoo 19 Community (Calendar-based)

A lightweight module that adds timeline visualization to Odoo 19 Community Edition using the Calendar view.

## ⚠️ **CRITICAL: Gantt View is Enterprise-Only**

**The Reality:**
- The native `<gantt>` view tag is **ONLY available in Odoo Enterprise**
- It does NOT exist in Odoo 19 Community Edition at all
- Attempting to use `<gantt>` in Community causes JavaScript errors

**This Module's Solution:**
- Uses **Calendar View** (which IS in Community)
- Provides timeline-like visualization
- Shows task schedules with start/end dates
- Color-coded by project

## What This Module Does

✅ Enhanced **Calendar View** for Project Tasks  
✅ Timeline visualization of task schedules  
✅ Color-coded by project  
✅ Shows task duration (start to end date)  
✅ **Graph View** for task analysis  
✅ Integration with existing Project module  

❌ NOT a true Gantt chart (Enterprise only)  
❌ No task dependencies  
❌ No critical path analysis  

## Installation

1. Copy this module to your Odoo addons directory ✓ (Already done)
2. Restart Odoo server
3. Activate Developer Mode
4. Go to Apps → Update Apps List
5. Search for "Simple Timeline"
6. Click Install

## Usage

1. Go to **Project → Tasks**
2. Click on the **Calendar** view icon (📅)
3. You'll see your tasks displayed in a calendar/timeline format
4. Switch to **Graph** view for analysis charts

### Setting Task Dates

- Open any task
- Set the **Deadline** field
- Add **Start Date** and **End Date**
- The task will appear in the Calendar view

## Features Overview

- **Calendar Timeline**: Monthly/weekly/daily views of tasks
- **Color Coding**: Tasks are colored by project
- **Duration Display**: Shows task span from start to end
- **Team Visibility**: See assigned users with avatars

## Why No True Gantt?

| Feature | Available in Community? |
|---------|------------------------|
| `<gantt>` XML tag | ❌ Enterprise Only |
| `@web/views/gantt/gantt_view` JS | ❌ Enterprise Only |
| Calendar view | ✅ Yes |
| Graph view | ✅ Yes |
| Timeline module (OCA) | ⏳ Not yet for v19 |

## Comparison: What's Missing vs Enterprise

| Feature | This Module (Community) | Enterprise |
|---------|------------------------|------------|
| Visual Timeline | ✅ (Calendar) | ✅ (Gantt) |
| Task Dependencies | ❌ | ✅ |
| Drag & Drop | ⚠️ Limited | ✅ |
| Critical Path | ❌ | ✅ |
| Resource Planning | ❌ | ✅ |
| Gantt-specific features | ❌ | ✅ |

## Alternative Solutions

If you need REAL Gantt functionality:

### 1. **OCA Modules** (Free, when available)
- **Status**: ⏳ Not yet ported to Odoo 19.0
- **Modules to watch**:
  - `web_timeline` - Timeline view widget
  - `project_timeline` - Project-specific timeline
- **Where**: https://github.com/OCA/web (branch 19.0)
- **When**: Typically 3-6 months after Odoo release

### 2. **Odoo Enterprise** (Paid)
- **Pros**: Full Gantt, official support, all features
- **Cons**: Costs money (~$30-50/user/month)
- **Info**: https://www.odoo.com/pricing

### 3. **Third-Party Paid Modules**
- Check Odoo Apps Store
- Search: "gantt community"
- **Note**: Few available for v19 yet (too new)

### 4. **Custom Development**
- Hire an Odoo developer
- Build custom gantt using JavaScript libraries (D3.js, vis.js, etc.)
- Integrate with Odoo backend

## Technical Details

This module:
- Extends `project.task` model
- Adds `date_start` and `date_end` datetime fields
- Provides enhanced calendar view
- Adds graph view for analysis
- Uses only Community-available features

**Does NOT:**
- Use `<gantt>` tag (causes errors)
- Import `@web/views/gantt/gantt_view` (doesn't exist)
- Require Enterprise license

## Compatibility

- **Odoo Version**: 19.0
- **Edition**: Community Edition ONLY
- **Dependencies**: project, web (both in Community)

## Known Limitations

1. **Calendar view ≠ Gantt view**
   - Different user experience
   - Less specialized for project planning

2. **No task dependencies**
   - Can't show predecessor/successor relationships

3. **No resource allocation**
   - Can't plan team capacity

4. **Limited timeline features**
   - Basic visualization only

## Troubleshooting

### JavaScript errors about gantt_view?
- ✓ Fixed in current version
- Module no longer tries to load Enterprise modules

### Tasks not showing in Calendar?
- Ensure tasks have `date_start` and `date_end` set
- Check that task dates are within the viewed calendar range

### Want real Gantt?
- Wait for OCA `web_timeline` to be ported to 19.0
- Or upgrade to Odoo Enterprise
- Or use paid modules from Apps Store

## What Happened to Gantt?

The original version of this module tried to use `<gantt>` tags, but:

1. ❌ `<gantt>` is Enterprise-only
2. ❌ Causes JS errors in Community
3. ❌ `@web/views/gantt/gantt_view` doesn't exist in Community
4. ✅ Switched to Calendar view (works in Community)

## Support & Contribution

This is a workaround solution for Community Edition. 

**For production use:**
- Consider Enterprise (if budget allows)
- Wait for OCA timeline modules (free, better functionality)
- This module is a temporary solution

## License

LGPL-3

## Author

Mahmuddin

---

**Last Updated**: January 2026  
**Module Version**: 19.0.1.0.0  
**Reality Check**: Gantt = Enterprise only, Calendar = Community workaround
