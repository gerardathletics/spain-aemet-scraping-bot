# Aemet Web Scraping Telegram Bot
## Get the spanish highest and lowest temperature, strongest wind gust and most precipitation from yesterday.

The script scrapes [AEMET](http://www.aemet.es/es/eltiempo/observacion/ultimosdatos?k=esp&datos=img&w=2) website and sends the extreme weather from the previous day via a Telegram (your) Bot. AEMET is the Spanish Meteorological Agency. 

More information about telegram bots can be found [here](https://core.telegram.org/bots). Basically you will have to create a new bot, get the bot id and a token. You can make the bot send the message periodically with some libraries or application like [Wayscript](https://wayscript.com/) (which I'm currently using for running the script everyday at 9:00h).

The bot I created is @EWSpainBot
![Bot screenshot](images/bot_screenshot.jpg)
