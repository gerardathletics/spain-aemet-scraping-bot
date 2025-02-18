# Aemet Weather Bot for Telegram
A Telegram bot that delivers daily extreme weather updates from Spain 🌡️🌪️☔

## Overview
This bot scrapes data from [AEMET](http://www.aemet.es/es/eltiempo/observacion/ultimosdatos?k=esp&datos=img&w=2) (Spanish Meteorological Agency) and sends you daily reports including:
- Highest and lowest temperatures
- Strongest wind gusts
- Maximum precipitation
All data is collected from the previous day's measurements across Spain.

![Bot screenshot](images/bot_screenshot.jpg)

## Features
- Daily automated weather updates
- Easy-to-read format
- Official data from AEMET
- Completely free to use

## Getting Started

### Prerequisites
- Python 3.x
- A Telegram account
- Bot token from [@BotFather](https://t.me/botfather)

### Installation
1. Clone this repository
```bash
git clone https://github.com/gerardathletics/spain-aemet-scraping-bot.git
cd spain-aemet-scraping-bot
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your bot token in the configuration file

### Usage
You can run this bot in several ways:
1. **Manual execution**: Run the script directly
```bash
python aemet_scraper.py
```
2. **Automated scheduling**: Set up using:
   - [Wayscript](https://wayscript.com/)
   - Cron jobs
   - Cloud services (AWS, Google Cloud, etc.)

## Try It Out
You can test the bot by messaging [@EWSpainBot](https://t.me/EWSpainBot) on Telegram.

## Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests


## Acknowledgments
- [AEMET](http://www.aemet.es/) for providing the weather data
- [Telegram Bot API](https://core.telegram.org/bots) for the bot infrastructure
