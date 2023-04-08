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
	event_time = get_current_time_str()

	events = repository.find_events_by_time_and_day_of_the_week(event_time, get_current_day_of_the_week());

	if events != []:
		print(event_time)
		print(get_current_day_of_the_week())
		await send_messages(channel, events)
	if get_current_time_by_timezone().strftime("%M") == '00':
		print(get_current_time_by_timezone())
		await send_hades_message(channel)

async def send_messages(channel, events):
	for event in events:
		message = "Atenção! O evento \'" + event[0] + "\' começa em 10 minutos."
		print(message)
		print()
		await channel.send(message)

async def send_hades_message(channel):
	hades_event = repository.find_event_by_id(13)[0][0]
	print(hades_event)
	print()
	await channel.send(hades_event)

def get_current_time_str():
	current_time = get_current_time_by_timezone()
	current_time = add_ten_minutes_to_datetime(current_time)
	return current_time.strftime("%H:%M:%S")

def get_current_time_by_timezone():
	timezone = pytz.timezone(TIMEZONE)
	current_time = datetime.now(timezone)
	current_time = current_time.replace(second = 0)

	return current_time
	
def add_ten_minutes_to_datetime(time):
	return time + timedelta(minutes=10)

def get_current_day_of_the_week():
	today = datetime.today()
	day_of_week = today.strftime("%A")

	return day_of_week

scheduler = AsyncIOScheduler()
scheduler.add_job(check_upcoming_event, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
	bot.run(TOKEN)

	asyncio.get_event_loop().run_forever()
