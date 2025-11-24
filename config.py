# MIS Configuration System - Centralized Configuration File
# This file stores all configurable settings for the MIS system
# All features should reference these values to ensure consistency

# Upload Window Configuration
UPLOAD_WINDOW_START_DAY = 1      # Upload window opens on 1st of month
UPLOAD_WINDOW_END_DAY = 25       # Upload window closes on 25th of month

# Notification Scheduler Configuration
UPLOAD_WINDOW_REMINDER_DAY = 25  # Send final reminder on 25th (same as end day)
UPLOAD_LOCK_DAY = 26             # Lock upload window on 26th (day after end date)

# Scheduler Times (IST - Asia/Kolkata timezone)
UPLOAD_WINDOW_OPEN_HOUR = 10
UPLOAD_WINDOW_OPEN_MINUTE = 0
UPLOAD_WINDOW_REMINDER_HOUR = 16
UPLOAD_WINDOW_REMINDER_MINUTE = 0
UPLOAD_WINDOW_LOCK_HOUR = 0
UPLOAD_WINDOW_LOCK_MINUTE = 0
