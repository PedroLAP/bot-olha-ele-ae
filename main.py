import asyncio

import discord
from mutagen.mp3 import MP3

from constants import BOT_ID, FFMPEG_EXE, TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")


@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel
    if channel is None or member.id == BOT_ID:
        return
    else:
        voice_client = await channel.connect()
        audio_path = "olha_ele_ae.mp3"
        audio = MP3(audio_path)
        voice_client.play(
            discord.FFmpegPCMAudio(
                source=audio_path,
                executable=FFMPEG_EXE,
            )
        )
        await asyncio.sleep(audio.info.length)
        await discord.VoiceClient.disconnect(voice_client)


client.run(TOKEN)
