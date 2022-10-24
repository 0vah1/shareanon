from telegram.ext import Application
from linker.handler import handlers
from utils import envs


bot = Application.builder().token(envs.token).concurrent_updates(True).build()
bot.add_handlers(handlers)
bot.run_polling()
