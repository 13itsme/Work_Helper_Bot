Work Helper Bot
A Telegram bot for managing video records

Work Helper Bot is a clean and fast Telegram assistant built with Aiogram 3 and SQLAlchemy.
It helps you keep track of videos by allowing you to easily:

✨ Add new records
📝 Edit existing ones
📋 List all saved videos
🗑️ Delete single entries or wipe everything at once

All data is stored in a PostgreSQL database using fully asynchronous ORM operations.

Perfect for small personal workflows, team utilities, and automation tasks.

🚀 Features

Telegram Bot built with Aiogram 3

Asynchronous database management via SQLAlchemy

Full CRUD support (Create, Read, Update, Delete)

Clean command handling

FSM support for confirmations (e.g. delete all)

Easy deployment (Render, Railway, Fly.io)

📦 Installation
1. Clone the repository
git clone https://github.com/your/repo.git
cd repo

2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux & Mac
.venv\Scripts\activate      # Windows

3. Install all dependencies
pip install -r requirements.txt

⚙️ Configuration

Create in folder config your config.py file:

BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname


Make sure your PostgreSQL database exists.

▶️ Running the Bot
python app.py
OR
Press shift + f10 in app.py


If everything is set correctly, the bot will start and connect to Telegram + your database.

☁️ Deployment (Render)

Push your code to GitHub

Go to Render → New Web Service

Choose your GitHub repo

Set build command:

pip install -r requirements.txt


Set start command:

python app.py


Add environment variables in the Render dashboard


In my If you want to use the bot only on your local computer:
• simply keep the development database configuration from core.py
• make sure PostgreSQL is running locally
• create the database manually
• and run the bot using:
python app.py

