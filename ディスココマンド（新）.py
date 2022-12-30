import discord
from discord.ext import commands
import asyncio
#asynicoがいるのかは知らん！！　多分使うやろ！

# Botのアクセストークン書け！
TOKEN = ''
#プレフィックス指定　アクティビティーのとこが許されるのかは不明
bot = commands.Bot(activity=discord.Game("人生"))

#インテントの設定（ディベロッパーポータルの方でも変えないと動かんぞ！！）
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#コマンド書いてくよ～
@bot.command()
async def promotion(ctx,prm,…):


#これを参考にしろ！https://zenn.dev/yuzmidori/articles/7a60b24f1ace4f
#エクステンションの方を使って書いてくれ　確実に楽だから　pyのdocsとごっちゃになりやすいので注意　https://discordpy.readthedocs.io/ja/latest/ext/commands/index.html
