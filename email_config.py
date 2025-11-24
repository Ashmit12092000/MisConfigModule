"""
Email Configuration File
Store your SMTP credentials here for the email notification system.

IMPORTANT SECURITY NOTES:
1. DO NOT commit this file to version control if it contains real credentials
2. This file is already added to .gitignore for your security
3. For production, consider using Replit Secrets instead
"""

# SMTP Server Configuration
SMTP_CONFIG = {
    # Your email provider's SMTP server (e.g., smtp.gmail.com, smtp.office365.com)
    'SMTP_HOST': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'SMTP_USERNAME': 'ashmitliyuu@gmail.com',  # Replace with your email
    'SMTP_PASSWORD': 'ecvw zqfs mfmx qdvr',      # Replace with app password
    'SMTP_FROM_EMAIL': 'ashmitliyuu@gmail.com', # Replace with your email
    'SMTP_FROM_NAME': 'MIS System'
}

"""
Example Configuration for Gmail:

SMTP_CONFIG = {
    'SMTP_HOST': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'SMTP_USERNAME': 'your-email@gmail.com',
    'SMTP_PASSWORD': 'your-app-specific-password',
    'SMTP_FROM_EMAIL': 'your-email@gmail.com',
    'SMTP_FROM_NAME': 'MIS Upload System'
}

Gmail Users: Generate an App Password:
1. Go to Google Account → Security → 2-Step Verification
2. Scroll to "App passwords"
3. Generate password for "Mail"
4. Use that password in SMTP_PASSWORD
"""

"""
Example Configuration for Outlook/Office365:

SMTP_CONFIG = {
    'SMTP_HOST': 'smtp.office365.com',
    'SMTP_PORT': 587,
    'SMTP_USERNAME': 'your-email@outlook.com',
    'SMTP_PASSWORD': 'your-password',
    'SMTP_FROM_EMAIL': 'your-email@outlook.com',
    'SMTP_FROM_NAME': 'MIS Upload System'
}
"""
# Email SMTP Configuration
# DO NOT commit this file to git (already in .gitignore)

SMTP_CONFIG = {
    # Gmail example - use App Password, not regular password
    'SMTP_HOST': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'SMTP_USERNAME': 'ashmitliyuu@gmail.com',  # Replace with your email
    'SMTP_PASSWORD': 'ecvw zqfs mfmx qdvr',      # Replace with app password
    'SMTP_FROM_EMAIL': 'ashmitliyuu@gmail.com', # Replace with your email
    'SMTP_FROM_NAME': 'MIS System'
}

# For Gmail:
# 1. Enable 2-factor authentication
# 2. Generate App Password: https://myaccount.google.com/apppasswords
# 3. Use the app password above (not your regular password)

# For other providers (Outlook, Yahoo, etc.):
# - Outlook: smtp.office365.com, port 587
# - Yahoo: smtp.mail.yahoo.com, port 587
# - Replace SMTP_HOST accordingly
