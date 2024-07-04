import discord
from discord.ext import commands
from TOKEN import TOKEN

# Define os intents que seu bot vai usar
intents = discord.Intents.default()
intents.messages = True  # Permitir leitura de mensagens

# Cria o objeto do bot com os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento que dispara quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando de exemplo
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Comando para exibir informações sobre linguagens de programação
@bot.command()
async def linguagens(ctx):
    linguagens_info = """
    Lista de comandos sobre linguagens de programação:
    
    !python - Informações sobre Python
    !javascript - Informações sobre JavaScript
    !java - Informações sobre Java
    !cpp - Informações sobre C++
    !ruby - Informações sobre Ruby
    !php - Informações sobre PHP
    """
    await ctx.send(linguagens_info)

# Comandos específicos para cada linguagem de programação
@bot.command()
async def python(ctx):
    info_python = "Python é uma linguagem de programação poderosa e fácil de aprender."
    await ctx.send(info_python)

@bot.command()
async def javascript(ctx):
    info_js = "JavaScript é a linguagem de programação padrão da web."
    await ctx.send(info_js)

@bot.command()
async def java(ctx):
    info_java = "Java é uma linguagem de programação popular para desenvolvimento de aplicativos."
    await ctx.send(info_java)

@bot.command()
async def cpp(ctx):
    info_cpp = "C++ é uma linguagem de programação poderosa usada em sistemas e jogos."
    await ctx.send(info_cpp)

@bot.command()
async def ruby(ctx):
    info_ruby = "Ruby é conhecida pela sua simplicidade e produtividade."
    await ctx.send(info_ruby)

@bot.command()
async def php(ctx):
    info_php = "PHP é uma linguagem de programação amplamente usada em desenvolvimento web."
    await ctx.send(info_php)

# Inicia o bot
bot.run(TOKEN)
