import os
import telegram
from telegram.ext import Updater, CommandHandler
import logging

# Setting up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables
scores = {}


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome to Game Score Bot! Use /addscore to add a score, /descore to delete a score, '
                              '/scoreboard to view the scores.')


def addscore(update, context):
    """Add a score to the scoreboard."""
    if len(context.args) != 2:
        update.message.reply_text('Usage: /addscore <player_name> <score>')
        return
    player_name = context.args[0]
    score = int(context.args[1])
    scores[player_name] = score
    update.message.reply_text(f'Score added for {player_name}: {score}')


def descore(update, context):
    """Delete a score from the scoreboard."""
    if len(context.args) != 1:
        update.message.reply_text('Usage: /descore <player_name>')
        return
    player_name = context.args[0]
    if player_name in scores:
        del scores[player_name]
        update.message.reply_text(f'Score deleted for {player_name}')
    else:
        update.message.reply_text(f'No score found for {player_name}')


def scoreboard(update, context):
    """Display the scoreboard."""
    if not scores:
        update.message.reply_text('Scoreboard is empty.')
    else:
        scoreboard_text = 'Scoreboard:\n'
        for player, score in scores.items():
            scoreboard_text += f'{player}: {score}\n'
        update.message.reply_text(scoreboard_text)


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Available commands:\n'
                              '/start - Start the bot\n'
                              '/addscore <player_name> <score> - Add a score\n'
                              '/descore <player_name> - Delete a score\n'
                              '/scoreboard - View the scoreboard\n'
                              '/help - Show this help message')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater("6377816124:AAHFPqLH2FlVUjNhIqGG8jGxnYC1qL9-Ems", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("addscore", addscore))
    dp.add_handler(CommandHandler("descore", descore))
    dp.add_handler(CommandHandler("scoreboard", scoreboard))
    dp.add_handler(CommandHandler("help", help_command))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
  
