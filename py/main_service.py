import discord
from discord.ext import commands
import subprocess
import itertools


def is_admin(user_id):
    admin_ids = {
        176775586704785408,  # Mikal
        178499699064438784,  # Vic
        178496120593317888,  # Ina
        303318339768287232,  # Honey
        178495607105650688,  # Isak
    }

    return admin_ids.__contains__(user_id)


bot = commands.Bot(command_prefix='!', description='description')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def admincheck(ctx):
    if is_admin(ctx.author.id):
        await ctx.send('You are admin')
    else:
        await ctx.send('You are not admin')


@bot.command()
async def server_status(ctx):
    await sudo(ctx, *("bash", "-c", "arkmanager", "status", "@all"))


@bot.command()
async def server_restart(ctx):
    await sudo(ctx, *("bash", "-c", "arkmanager", "restart", "@all"))


@bot.command()
async def server_update(ctx):
    await sudo(ctx, *("bash", "-c", "arkmanager", "update", "--update-mods", "@all"))


@bot.command()
async def sudo(ctx, *arg):
    if is_admin(ctx.author.id):
        await send_command(ctx, *arg)
    else:
        await ctx.send('You are not admin')


async def send_command(ctx, *arg):
    results = subprocess.run(list(itertools.chain(arg)), stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    await ctx.send('```bash\n{}```'.format(results.stdout.decode("utf-8")))


bot.run('NzAyOTkwNTQ4NTI4NzkxNjUz.XqIKeA.C-S8VAlkynQ0YlNahQXy_KocCzk')
