import discord
from discord.ext import commands
from config import settings
import json
import requests


bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def meme(ctx):
    response = requests.get('https://some-random-api.ml/meme') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Meme') # Создание Embed'a
    embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed


@bot.command()
async def mute(ctx, member: discord.Member):
     await member.edit(mute = True)

@bot.command()
async def unmute(ctx, member: discord.Member):
     await member.edit(mute = False)\

def add_role(self, ctx, role:discord.Role=None):
        """Add a role allowed to add messages to the starboard defaults to @everyone"""
        server = ctx.message.server
        if server.id not in self.settings:
            await self.bot.send_message(ctx.message.channel, 
                                        "I am not setup for the starboard on this server!\
                                         \nuse starboard set to set it up.")
            return
        everyone_role = await self.get_everyone_role(server)
        if role is None:
            role = everyone_role
        if role.id in self.settings[server.id]["role"]:
            await self.bot.send_message(ctx.message.channel, "{} can already add to the starboard!".format(role.name))
            return
        if everyone_role.id in self.settings[server.id]["role"] and role != everyone_role:
            self.settings[server.id]["role"].remove(everyone_role.id)
        self.settings[server.id]["role"].append(role.id)
        dataIO.save_json("data/star/settings.json", self.settings)
        await self.bot.send_message(ctx.message.channel, "Starboard role set to {}.".format(role.name)) 
    

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена