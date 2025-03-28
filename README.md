[Author: Neeraj Mishra (nmcnemis@gmail.com) with GPT code assist].

# MUSICAVENGE
#### Musicavenge (Music Scavenger): A Telegram bot which returns YouTube music videos for the searched query using chat.

![tel](https://github.com/user-attachments/assets/6b3c6e68-2b04-4947-8c27-29feacaa24d4)

-----


#### ⚠ The main file to work with is: ```Musicavenge.py```.

#### ⚠ ```Musicavenge-with-encryption.py``` I made as I was just curious about encryption, basically it just takes the query (the message that user type to the bot) and encrypts it.
#### Note: Now, the ```update.message.text``` seems to be read-only, as when I tried overwrite it with the encrypted one, it gave error as: ```caused error Attribute text of class Message can't be set!```
#### So it feels kinda unnecessary to encrypt as it can still be seen by ```update.message.text```.

-----

### INSTRUCTIONS

##### REQUIRED PYTHON LIBRARIES
To install the required libraries for the python code, execute the following commands:
```python
pip install telegram
pip install python-telegram-bot
```
##### You will also need to get the API for YouTube and the bot token from BotFather for Telegram (instructions are given below).

-----

##### GETTING THE YOUTUBE API AND TELEGRAM BOT TOKEN

![icons8-youtube-48](https://github.com/user-attachments/assets/488f6948-141f-4cdd-818e-9a4b62d95323)

Steps to get the API for YouTube.

1. Make sure you are logged in and then go to https://console.developers.google.com/.
2. Go to Credentials as follows:

   ![image](https://github.com/user-attachments/assets/6c684fd2-6fc1-48db-8b46-bdaeccc3ec73)

3. Go to "Create Credentials > API key" and create your key, you can rename it as per your requirements:

   ![cred](https://github.com/user-attachments/assets/414c8961-2c91-4493-8c88-63b7ad2b3e11)

4. Then go to "Enabled APIs & Services":

   ![api](https://github.com/user-attachments/assets/12c3501c-b7d8-4a19-901d-f37581984580)

   And click on the button:
   
   ![enable](https://github.com/user-attachments/assets/699b974f-495b-4231-a3f0-b2de9c715b88)

5. You will see various apps, find YouTube and then click on it:

   ![yt](https://github.com/user-attachments/assets/549ab059-4c53-444e-8722-c33a7001bdcd)

6. Then simply click on "Enable":

   ![image](https://github.com/user-attachments/assets/72bee5e3-c526-40e1-8311-48e38fd67eab)

  ###### And like this you will have your YouTube API. ✔
-----

![icons8-telegram-48](https://github.com/user-attachments/assets/39a06a2d-1894-4496-8a85-db4cdcf61cc3)

Steps to get the bot token for Telegram.

1. https://t.me/BotFather - This is the bot that will help you to create other Telegram bots.
2. Follow the following steps:

   ![bot](https://github.com/user-attachments/assets/68eb16c5-5051-4b4c-bee9-ef5671cf3aae)

###### And like this you will have your Telegram bot token. ✔

-----
###### Icons by https://icons8.com/
-----
Made with ❤
