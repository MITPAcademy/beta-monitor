import discord
from discord.ext import tasks, commands
from discord import ButtonStyle, Interaction
from discord.ui import View, Button
import subprocess
from translator import translate
from config import *
from monitor import check_discord_api, check_bot_discloud
import sys
import os
from datetime import datetime, timedelta, timezone

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def start_local_bot():
    subprocess.Popen(["start", "start-bot.bat"], shell=True)

class LanguageSwitcher(View):
    def __init__(self, message, current_lang):
        super().__init__(timeout=None)
        self.message = message
        self.current_lang = current_lang

        languages = ["en", "pt", "es", "de", "fr", "it", "ru", "ja", "ar"]
        for lang in languages:
            if lang != current_lang:
                button = Button(label=lang.upper(), style=ButtonStyle.primary, custom_id=f"lang_{lang}")
                button.callback = self.make_lang_callback(lang)
                self.add_item(button)

    def make_lang_callback(self, lang):
        async def callback(interaction: Interaction):
            translated_title = translate("Beta Bot Status", lang)
            translated_message = translate(self.message, lang)
            embed = discord.Embed(
                title=translated_title,
                description=translated_message,
                color=discord.Color.red()
            )
            await add_footer(interaction.client, embed)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except discord.errors.NotFound:
                # Interaction expired or is unknown, ignore or optionally log this event
                pass
        return callback

    async def interaction_check(self, interaction: Interaction) -> bool:
        return True

async def add_footer(bot, embed):
    # Get bot latency (ping)
    ping_ms = round(bot.latency * 1000)
    # Get current time in GMT-3 (Brasilia) using timezone-aware objects
    now_utc = datetime.now(timezone.utc)
    now_gmt3 = now_utc.astimezone(timezone(timedelta(hours=-3)))
    time_str = now_gmt3.strftime("%Y-%m-%d %H:%M:%S")
    footer_text = f"Ping: {ping_ms}ms | {time_str} GMT-3 🇧🇷"
    embed.set_footer(text=footer_text)

async def send_status_message(channel, lang=DEFAULT_LANG):
    api_online = check_discord_api()
    bot_online = check_bot_discloud()

    if api_online and not bot_online:
        message = translate("The bot is offline. Restarting it locally...", lang)
        start_local_bot()
    elif not api_online:
        message = translate("Discord API is down. Bot is offline due to Discord issues.", lang)
    else:
        message = translate("Everything is online. Bot is running normally.", lang)

    embed = discord.Embed(title=translate("Beta Bot Status", lang), description=message, color=discord.Color.red())
    await add_footer(bot, embed)
    view = LanguageSwitcher(message=message, current_lang=lang)
    await channel.send(embed=embed, view=view)

@bot.event
async def on_ready():
    print(f"online: {bot.user}")
    monitor_bot.start()

@tasks.loop(minutes=5)
async def monitor_bot():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await send_status_message(channel, lang=DEFAULT_LANG)
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")

bot.run(BOT_TOKEN)