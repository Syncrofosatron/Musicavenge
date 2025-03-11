import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from cryptography.fernet import Fernet

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# YouTube API endpoint
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

# Replace with your YouTube Data API key
YOUTUBE_API_KEY = "YOUR YOUTUBE API"  # Replace with your actual API key

# Put the key generation and instantiation code here so that you only generate the key once.

# Function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Type a song or video name and we will send you its link here...')

# Function to search for music on YouTube
async def search_and_play(update: Update, context: CallbackContext) -> None:
    # Generate a key and instantiate a Fernet instance. Keeping this within this function so that each time a user search for something, a new key is generated.
    # This is just to ensure more safety.
    # You can also put this code below for generating and instantiating key on top (line 18) to only generate the key once for all user queries.
    key = Fernet.generate_key()
    f = Fernet(key)

    # Encrypt the user's input text and store the decrypted one in a variable.
    query = f.encrypt(update.message.text.strip().encode())
    queryDecrypted = f.decrypt(query).decode()

    # If no text is provided, ask for input
    if not queryDecrypted:
        await update.message.reply_text('Please provide a song name or artist to search for!')
        return

    # Log the query to debug
    # logger.info(f"Searching for: {queryDecrypted}")
    print(key);
    print(f);

    # Make a request to the YouTube Data API
    response = requests.get(
        YOUTUBE_API_URL,
        params={
            'part': 'snippet',
            'q': queryDecrypted,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'videoCategoryId': '10',  # Music category (optional, can be removed if you want broader results)
            'maxResults': 1  # Limit to one result for simplicity
        }
    )

    if response.status_code == 200:
        data = response.json()
        
        if 'items' in data and len(data['items']) > 0:
            # Get the first result
            video = data['items'][0]
            video_title = video['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"  # Link to the video

            # Send song info to the user
            await update.message.reply_text(f"Found: {video_title}\nWatch here: {video_url}")
        else:
            await update.message.reply_text('No results found for your query.')
    else:
        await update.message.reply_text("An error occurred while searching for the song.")

    # This will delete the key and fernet instance, but it is not necessary as when the function will end
    #  and the memory will be freed by the Python garbage collector.
    # Also there is almost negligible performacne difference between deleting and not deleting the key and fernet instance
    # as this is a very small program.
    del key
    del f

# Function to handle errors
async def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    # Set up the application
    application = Application.builder().token("YOUR TELEGRAM BOT TOKEN").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Handle normal messages (search query)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_and_play))

    # Add error handler
    application.add_error_handler(error)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
