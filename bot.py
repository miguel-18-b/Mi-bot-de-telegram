import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ¡Bienvenido a Gana por Anuncios!\n\n"
        "Usa /menu para ver las opciones disponibles."
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 MENÚ PRINCIPAL\n\n"
        "👤 /start - Iniciar\n"
        "📢 /anuncios - Ver anuncios\n"
        "💰 /saldo - Consultar saldo\n"
        "💳 /retiro - Solicitar retiro\n"
        "📊 /historial - Ver historial\n"
        "ℹ️ /ayuda - Ayuda"
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))

    print("Bot iniciado...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
