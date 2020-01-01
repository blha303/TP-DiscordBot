#!/usr/bin/env python3
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_connect():
    pass

if __name__ == "__main__":
    from sys import environ
    client.run(environ.get("DISCORD_TOKEN"))
