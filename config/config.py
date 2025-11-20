import os

TOKEN = '8237262870:AAGMAFmVHJkLNk7Ls0j0MG--b-SdXvjWKYM'
# Локальная база для разработки
LOCAL_DB = 'sqlite+aiosqlite:///./workhelper.db'
# База для деплоя
DATABASE_URL = os.getenv('DATABASE_URL', LOCAL_DB)