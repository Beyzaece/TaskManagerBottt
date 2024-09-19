import discord
from discord.ext import commands
from database import init_db, add_task, delete_task, show_tasks, complete_task

# Intents ayarları
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='add_task')
async def add_task_command(ctx, *, description: str):
    add_task(description)
    await ctx.send(f'Görev eklendi: {description}')

@bot.command(name='delete_task')
async def delete_task_command(ctx, task_id: int):
    delete_task(task_id)
    await ctx.send(f'Görev silindi: {task_id}')

@bot.command(name='show_tasks')
async def show_tasks_command(ctx):
    tasks = show_tasks()
    if tasks:
        task_list = '\n'.join([f'{task[0]}: {task[1]} (Tamamlandı: {"Evet" if task[2] else "Hayır"})' for task in tasks])
        await ctx.send(f'Tüm Görevler:\n{task_list}')
    else:
        await ctx.send('Görev bulunamadı.')

@bot.command(name='complete_task')
async def complete_task_command(ctx, task_id: int):
    complete_task(task_id)
    await ctx.send(f'Görev tamamlandı: {task_id}')

if __name__ == '__main__':
    init_db()  # Veritabanını başlat


# Tokeni buraya ekleyip botu çalıştır
bot.run('MTI4NjQwNTcxNzk2ODAyNzczOQ.GCKwPF.8i4qhjOdqAOuvqYwAMWoefpcc4sjBJGMtctUMo')
