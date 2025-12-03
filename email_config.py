"""
Email Configuration File
Store your SMTP credentials here for the email notification system.

"""

# SMTP Server Configuration
SMTP_CONFIG = {
    
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

