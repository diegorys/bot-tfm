def startConversationalBOT():
    import os
    from conversational_bot.infrastructure.telegram.telegram_client import TelegramClient

    print(f"STARTING CONVERSATIONAL BOT...")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    telegramClient: TelegramClient = TelegramClient(TELEGRAM_TOKEN)
    print("WAITING FOR USER MESSAGE...")
    telegramClient.pool()
    

startConversationalBOT()