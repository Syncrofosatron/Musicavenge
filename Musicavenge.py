import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Set up logging of messages.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# YouTube API endpoint
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

# Replace the text within quotes with your YouTube Data API key.
YOUTUBE_API_KEY = "YOUR YOUTUBE API"

# Function to start the Telegram bot.
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Type a song or video name and we will send you its link here...')

# Function to search for the music that user queries in chat on YouTube.
async def search_and_play(update: Update, context: CallbackContext) -> None:
    # Get the user's input query.
    query = update.message.text.strip()

    # If no text is provided, ask for input
    if not query:
        await update.message.reply_text('Please provide a song name or artist to search for!')
        return

    # Log the query to debug in case of issues or just for status on things.
    logger.info(f"Searching for: {query}")

    # Make a request to the YouTube Data API
    response = requests.get(
        YOUTUBE_API_URL,
        params={
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            # 10 is used to loosely filter results to Music, can be removed if there's a need for broader results.
            'videoCategoryId': '10',
            # Change below as per your neeeds of getting results.
            'maxResults': 1
        }
    )

    if response.status_code == 200:
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            # Get the first result.
            video = data['items'][0]
            video_title = video['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"  # Link to the video

            # Send song info to the user.
            await update.message.reply_text(f"Found: {video_title}\nWatch here: {video_url}")
        else:
            await update.message.reply_text('No results found for your query.')
    else:
        await update.message.reply_text("An error occurred while searching for the song.")

# Function to handle errors.
async def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    # Set up the application.
    application = Application.builder().token("YOUR TELEGRAM BOT TOKEN KEY").build()

    # Add command handlers.
    application.add_handler(CommandHandler("start", start))

    # Handle normal messages (search query), the ~filters.COMMAND will be negated/ignored if there is a command mentioned in the user query.
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_and_play))

    # Add error handler.
    application.add_error_handler(error)

    # Start the bot.
    application.run_polling()

if __name__ == '__main__':
    main()
