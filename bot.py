import nextcord
from nextcord.ext import commands

TESTING_GUILD_ID = 123456789  # Replace with your guild ID

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    channel = bot.get_channel(TESTING_GUILD_ID)

    await channel.send("Mensagem")

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Teste")

bot.run('token here')