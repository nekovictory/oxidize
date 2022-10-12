# pkgs
import asyncio

# register event
@bot.event
async def on_message(ctx):
    str = ctx.content
    
    if ctx.guild and str.startswith('py.'):
        args = str.split(' ')
        name = args.pop(0)[3:]
        cmd = bot.cmds.get(name) or bot.aliases.get(name)

        if cmd:
            await cmd.run(bot, ctx, args)