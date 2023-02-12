import discord
from discord.ext import commands
from discord.utils import get

# Botのアクセストークン書け！
TOKEN = ''
#アクティビティーのとこが許されるのかは不明
bot = commands.Bot(command_prefix="/" intents=intents, activity=discord.Game("ゴミみてえな人生"))

#インテントの設定（ディベロッパーポータルの方でも変えないと動かんぞ！！）
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#bot起動時のイベント
@bot.event
async def on_ready():
 print('We have logged in as {0.user}'.format(bot))

#コマンドのヤツ difだっけasyncいるっけ
def is_creator(ctx):
    async def predicate(ctx):
        return ctx.role.roleID > role.roleID
    return commands.check(predicate)


@bot.command()
@commands.check(is_creator)
async def promotion(ctx, *, arg):
  target_channel = get(message.guild.channels, name='転送先のチャンネル名')
  await target_channel.send(ctx.content)

 
#こっから先を最適化target_channel = get(message.guild.channels, name='転送先のチャンネル名')
 #await target_channel.send(message.content)
# if message.author.guild_permissions.manage_messages:
        # 特定のロールを持つユーザーである場合の処理を記述する
   #    
   #     await target_channel.send(message.content)


#これを参考にしろ！https://zenn.dev/yuzmidori/articles/7a60b24f1ace4f
#これ使え！！　https://discordpy.readthedocs.io/ja/latest/ext/commands/index.html
# https://discordpy.readthedocs.io/ja/latest/api.html#discord.Intents.message_content

#cliantを全部botに書き換えていけ


