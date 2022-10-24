from telegram import Update
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters, ContextTypes
from utils import hash_ids


async def start_share_anon(u: Update, _):
    await u.message.reply_markdown('send the message or /cancel')
    return 1


async def get_link(u: Update, _):
    m = await u.message.reply_markdown(u.message.text_markdown)
    cid, mid = m.chat_id, m.id
    await u.message.reply_markdown(f'message code: `{hash_ids.encode(cid, mid)}`')
    return ConversationHandler.END


async def cancel(u: Update, _):
    return ConversationHandler.END


async def see_message(u: Update, _: ContextTypes.DEFAULT_TYPE):
    try:
        c, m = hash_ids.decode(u.message.text)
        await _.bot.forward_message(
            u.effective_chat.id, c, m, protect_content=True
        )
    except:
        pass


handlers = [
    ConversationHandler(
        per_chat=False,
        entry_points=[CommandHandler('share', start_share_anon)],
        states={1: [MessageHandler(filters.TEXT & ~ filters.COMMAND, get_link)]},
        fallbacks=[CommandHandler('cancel', cancel)],
    ),
    MessageHandler(filters.TEXT & ~filters.COMMAND, see_message)
]
