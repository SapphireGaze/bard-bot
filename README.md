# Discord Chatbot with BardAPI
### A simple discord chat bot created using [discord.py](https://github.com/Rapptz/discord.py) and [bardapi](https://github.com/dsdanielpark/Bard-API).

## Setup:
Clone this github repository using the command
~~~
git clone https://github.com/SapphireGaze/bard-bot
~~~
Then, change directory into the repository, and download all the required modules from **requirements.txt**
~~~
cd ./bard-bot
pip install -r requirements.txt
~~~
After successfully installing the required modules,
create a **.env** file 
~~~
touch .env
~~~
Open the .env file and store your discord bot token and bard API key ([API key obtain method](https://github.com/dsdanielpark/Bard-API/blob/main/README.md)) in the following format
~~~
BARD_API_KEY=YOUR_KEY_HERE
DISCORD_TOKEN=YOUR_TOKEN_HERE
~~~
Finally, save the **.env** file and close the file, and run the following commands to start the bot
~~~
cd ./src
python3 main.py
~~~
Enjoy!