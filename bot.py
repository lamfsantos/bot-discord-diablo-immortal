import nextcord
import datetime
from nextcord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import pytz
from datetime import datetime, timedelta
from db import repository

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Create a .env file on the project root with this two variables below
GUILD_ID = int(os.environ.get("GUILD_ID"))
TOKEN = os.environ.get("TOKEN")

TIMEZONE = "America/Sao_Paulo"

bot = commands.Bot()

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

	channel = bot.get_channel(GUILD_ID)

	await check_upcoming_event()

async def check_upcoming_event():
	channel = bot.get_channel(GUILD_ID)	
	current_time = get_current_time_by_timezone();
	event_time = parse_time_to_string(add_ten_minutes_to_datetime(current_time))

	events = repository.find_events_by_time_and_day_of_the_week(event_time, get_current_day_of_the_week());

	if events != []:
		print(current_time)
		print(get_current_day_of_the_week())
		await send_messages(channel, events)

async def send_messages(channel, events):
	for event in events:
		message = "Atenção! O evento \'" + event[0] + "\' começa em 10 minutos."
		print(message)
		print()
		await channel.send(message)

def parse_time_to_string(time):
	return time.strftime("%H:%M:%S")

def get_current_time_by_timezone():
	timezone = pytz.timezone(TIMEZONE)
	current_time = datetime.now(timezone)
	current_time = current_time.replace(second = 0)

	return current_time

def add_ten_minutes_to_datetime(time):
	return time + timedelta(minutes=10)

def get_current_day_of_the_week():
	today = get_current_time_by_timezone()
	day_of_week = today.strftime("%A")

	return day_of_week

scheduler = AsyncIOScheduler()
scheduler.add_job(check_upcoming_event, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
	bot.run(TOKEN)

	asyncio.get_event_loop().run_forever()
