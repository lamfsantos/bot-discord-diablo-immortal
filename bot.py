import nextcord
import datetime
from nextcord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

GUILD_ID = 123456789  # Replace with your guild ID
TOKEN = "token here" # Put your bot token here

bot = commands.Bot()

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

	channel = bot.get_channel(GUILD_ID)

	#await channel.send("Mensagem")
	#await notify_event(channel);
	await teste()

async def teste():
	channel = bot.get_channel(GUILD_ID)
	await channel.send("Mensagem")

async def notify_event(channel):
	time_now = datetime.datetime.now()
	
	print(str(time_now.hour + 4 == 18))

	if time_now.hour + 3 == 18:
		await channel.send("Evento")

# @bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
# async def hello(interaction: nextcord.Interaction):
#     await interaction.send("Teste")

scheduler = AsyncIOScheduler()
scheduler.add_job(teste, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
    bot.run(TOKEN)

    asyncio.get_event_loop().run_forever()
