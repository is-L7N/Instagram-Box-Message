
# Instagram Box Message Bot

A Python tool that monitors your Instagram inbox and displays new messages in the terminal. Optionally, it sends message notifications to a Telegram bot.

## Features
- Automatically checks for new messages in your Instagram inbox.
- Displays sender's name, username, and message text.
- Sends message info and profile photo to Telegram (optional).
- Stores already seen messages in `messages.json` to avoid duplicates.
- Supports converting session ID to Bearer Token and vice versa.

## How to Use
1. Run the script.
2. Choose:
   - `[1]` to convert session ID to Bearer Token or the opposite.
   - `[2]` to run the Instagram inbox monitor.
3. If running the bot:
   - Enter your Instagram Bearer token.
   - Optionally, enter your Telegram bot token and chat ID to enable notifications.
4. The tool will monitor for new messages and optionally send them to Telegram.

## Requirements
- Python 3
- Modules: `requests`, `json`, `base64`, `os`, `time`, `random`

## Screenshot
![Terminal Output](screenshot_terminal.jpg)
![Telegram Notification](screenshot_telegram.jpg)

## Author
- **L7N**
- [Telegram](https://t.me/PyL7N)
- [GitHub](https://github.com/is-L7N)
