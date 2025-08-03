# Telegram Session & API Credential Auto-Creator

This script automatically:
- Logs in to `my.telegram.org` with your phone number and OTP.
- Creates a new Telegram application (generates `api_id` and `api_hash`).
- Saves a Telethon session for later use.
- Telethon session saved on session folder

> ⚠️ **Important:** Use this script in compliance with [Telegram’s Terms of Service]. Do not use it for spamming, excessive scraping, or any activity that violates Telegram’s rules.

## Features
- Login via Telegram web form using OTP.
- Random app creation (title, shortname, etc.).
- Fetching `api_id` and `api_hash` from `my.telegram.org/apps`.
- Initializing and saving a Telethon session.
- Logging credentials to `telesession.txt`.

## Requirements

- Python 3.10+ (virtualenv recommended)
- Proxy (recommended)
- A valid phone number that can receive Telegram OTP codes.

## Dependencies

Install the dependencies with pip:

```bash
pip install -r requirements.txt
```

The script will prompt for:

Number: Your phone number in Telegram format (e.g., +6281234567890)

OTP: The one-time password sent by Telegram during authentication

how to run the script 

```bash
python telesessionauto.py
```
