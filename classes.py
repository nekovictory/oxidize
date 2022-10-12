# pkgs
import dotenv 
import importlib
import discord
import asyncio
import os

# bot class
class Bot(discord.Client):
    # our init func
    def __init__(self):
        # load environment
        dotenv.load_dotenv()

        # prepare caches
        self.events = []
        self.cmds = {}
        self.aliases = {}

        intents = discord.Intents.all()

        super().__init__(intents = intents)

    # our startup func
    def go(self):
        # get all cogs
        cogs = os.listdir('cogs')

        # iterate through them
        for cog in cogs:
            # get all of this cog's files
            files = os.listdir(f'cogs/{cog}')

            # iterate through them
            for file in files:
                # trim file name
                name = file.replace('.py', '')

                # import cmd
                cmd = importlib.import_module(f'cogs.{cog}.{name}')

                # cache cmd
                self.cmds[name] = cmd

                # iterate through aliases
                for alias in cmd.aliases:
                    self.aliases[alias] = cmd
        
        # get all events
        events = os.listdir('events')

        # iterate through them
        for file in events:
            # trim event name
            name = file.replace('.py', '')
    
            # cache event
            self.events.append(name)

            # register event
            code = open(f'events/{name}.py').read()

            exec(code, {'bot': self})
        
        # login
        self.run(os.getenv('token'))