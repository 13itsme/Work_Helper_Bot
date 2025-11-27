# Work Helper Bot 🤖

A Telegram bot for tracking video earnings and currency conversion. Built with Python, aiogram, and SQLAlchemy.

## Features ✨

- **Video Management**: Add, edit, delete, and list videos with their costs
- **Financial Tracking**: Calculate total earnings from all videos
- **Currency Conversion**: Convert earnings to different currencies using real-time exchange rates
- **Database Storage**: Persistent storage using SQLAlchemy with SQLite/PostgreSQL support
- **Interactive Commands**: User-friendly command menu with autocomplete

## Commands 📋

| Command | Description |
|---------|-------------|
| `/start` | Start the bot |
| `/help` | Get help information |
| `/add [title] [cost]` | Add a new video with title and cost in USD |
| `/list` | Show all videos with their costs |
| `/sum` | Display total earnings |
| `/edit [old_title] [old_cost] [new_title] [new_cost]` | Edit an existing video |
| `/delete [title]` | Delete a video by title |
| `/delete_all` | Delete all videos (requires confirmation) |
| `/exchange [amount] [currency]` | Convert USD to another currency |
| `/exchange_all [currency]` | Convert total earnings to another currency |

## Tech Stack 🛠️

- **Python 3.12**
- **aiogram** - Telegram Bot API framework
- **SQLAlchemy** - ORM for database operations
- **asyncio** - Asynchronous programming
- **httpx** - HTTP client for API requests
- **SQLite/PostgreSQL** - Database storage

## Installation 🚀

### Prerequisites

- Python 3.12 or higher
- Telegram Bot Token (get from [@BotFather](https://t.me/BotFather))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/13itsme/Work_Helper_Bot.git
cd Work_Helper_Bot
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `config/config.py` file:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
DATABASE_URL = "sqlite+aiosqlite:///./database/bot.db"  # SQLite
# or for PostgreSQL:
# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"
```

5. **Run the bot**
```bash
python app.py
```

## Project Structure 📁
```
WorkHelperBot/
├── api/
│   ├── __init__.py
│   └── exchange_api.py      # Currency conversion API
├── config/
│   ├── __init__.py
│   └── config.py            # Configuration (TOKEN, DATABASE_URL)
├── database/
│   └── bot.db               # SQLite database (auto-created)
├── handlers/
│   ├── __init__.py
│   └── handlers.py          # Command handlers
├── lexicon/
│   ├── __init__.py
│   └── lexicon_en.py        # Bot messages/responses
├── app.py                   # Main entry point
├── core.py                  # Core setup (router, session, engine)
├── models.py                # SQLAlchemy models
├── requirements.txt         # Dependencies
└── README.md
```

## Database Schema 💾

### Records Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key |
| `title` | String(20) | Video title |
| `cost` | Integer | Video cost in USD |

## Usage Examples 📝

### Adding a video
```
/add MyVideo 100
→ Video successfully added!
→ Current total sum of all videos: 100$
```

### Converting currency
```
/exchange 100 EUR
→ 💱 100 USD = 92.50 EUR

/exchange_all PLN
→ 💰 Total conversion:
→ 500 USD = 2000.00 PLN
```

### Listing all videos
```
/list
→ MyVideo - 100$
→ Tutorial - 200$
→ Review - 150$
```

## API Integration 🌐

The bot uses [ExchangeRate-API](https://exchangerate-api.com/) for real-time currency conversion. Supports 160+ currencies including:
- EUR (Euro)
- GBP (British Pound)
- PLN (Polish Zloty)
- JPY (Japanese Yen)
- And many more...

## Configuration ⚙️

### Change Database
Edit `config/config.py`:
```python
# SQLite (default)
DATABASE_URL = "sqlite+aiosqlite:///./database/bot.db"

# PostgreSQL
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"
```

### Bot Commands Menu
Commands are automatically set on bot startup via `set_bot_commands()` in `app.py`.

## Development 🔧

### Requirements
```txt
aiogram==3.x
sqlalchemy==2.x
aiosqlite
httpx
asyncpg  # for PostgreSQL
```

### Running in Development
```bash
python app.py
```

## Troubleshooting 🔍

**Bot doesn't respond:**
- Check if TOKEN is correct in `config/config.py`
- Verify bot is running without errors
- Ensure firewall isn't blocking connections

**Database errors:**
- Delete `database/bot.db` and restart bot to recreate
- Check DATABASE_URL format

**Currency conversion fails:**
- Check internet connection
- Verify currency code is valid (3 letters: USD, EUR, PLN)

## Contributing 🤝

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Author ✍️

**13itsme**
- GitHub: [@13itsme](https://github.com/13itsme)
