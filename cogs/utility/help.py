# pkgs
import asyncio

# properties
aliases = ['cmds']
info = 'sends this'

# run func
async def run(bot, ctx, args):
    cmds = [f'{name} `?` {cmd.info}' for name, cmd in bot.cmds.items()]

    await ctx.channel.send('\n'.join(cmds))