import nextcord
import datetime
from nextcord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from db import repository 

GUILD_ID = 123456789  # Replace with your guild ID
TOKEN = "TOKEN" # Put your bot token here

bot = commands.Bot()

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

	channel = bot.get_channel(GUILD_ID)

	print(repository.find_events_by_time_and_day_of_the_week('19:00:00', 'Tuesday'))

	await teste()

async def teste():
	channel = bot.get_channel(GUILD_ID)
	await channel.send("Mensagem")

async def notify_event(channel):
	time_now = datetime.datetime.now()
	
	print(str(time_now.hour + 4 == 18))

	if time_now.hour + 3 == 18:
		await channel.send("Evento")

scheduler = AsyncIOScheduler()
scheduler.add_job(teste, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
	bot.run(TOKEN)

	asyncio.get_event_loop().run_forever()
