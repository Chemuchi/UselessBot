import json
import os

import discord
from discord.ext import commands

# 현재 스크립트 파일의 경로를 얻습니다.
script_dir = os.path.dirname(os.path.abspath(__file__))
# 상위 폴더의 경로를 얻습니다.
parent_dir = os.path.dirname(script_dir)
# config.json 파일의 경로를 생성합니다.
config_path = os.path.join(parent_dir, 'config.json')

# 파일을 읽어올 때 config_path를 사용합니다.
with open(config_path, 'r') as f:
    config = json.load(f)
guild_id = config['guild_id']['id']

class qr_gen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='qr',description='입력한 링크로 연결되는 QR코드를 만들어줍니다.')
    async def cat(self, ctx: commands.Context, url: str):
        await ctx.reply(f"https://chart.apis.google.com/chart?cht=qr&chs=250x250&chl={url}")



async def setup(client):
    await client.add_cog(qr_gen(client),guilds=[discord.Object(id=guild_id)])