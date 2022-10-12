# pkgs
import asyncio

# properties
aliases = ['latency']
info = 'sends my ping'

# run func
async def run(bot, ctx, args):
    await ctx.channel.send(f'{bot.ws.latency}ms')