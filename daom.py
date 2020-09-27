import discord
from discord.ext import commands
import asyncio
from youtube_search import YoutubeSearch
from discord.utils import get
import youtube_dl
import os

bot = commands.Bot(command_prefix=',')
volumes = 25
pf = []

@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}!')

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {'options': '-vn'}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
        self.id = data.get('id')
        self.uploader = data.get('uploader')
        self.uploaderid = data.get('uploader_id')
        self.filename = ytdl.prepare_filename(data)
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@bot.command(pass_context=True, aliases=['j', 'join'])
async def 들어와(msg,*,channel:discord.VoiceChannel = None):
    if channel == None:
        channel = msg.author.voice.channel
    if msg.voice_client is not None:
        await msg.voice_client.move_to(channel)
    else:
        await channel.connect()
@bot.command(pass_context=True, aliases=['v', 'vol'])
async def 볼륨(ctx, vol: int):
    try:
        global volumes
        if ctx.voice_client is None:
            return await ctx.send("봇이 음성채널에 있지 않습니다.")
        if vol < 0 and vol > 200:
            await ctx.send(f"{ctx.author.mention}에 의해 불륨이 변경되었습니다.")
        print(vol / 100)
        ctx.voice_client.source.volume = vol / 100
        await ctx.send(f"볼륨: {vol}%")
        volumes = vol
    except Exception as e:
        print(f'error\n{e}')
@bot.command(pass_context=True, aliases=['s', 'sto'])
async def 중지(ctx):
    global volumes
    voice = get(bot.voice_clients, guild=ctx.guild)
    volumes = 15

    if voice and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        os.remove(player.filename)
        await ctx.send("완료!")
    else:
        await ctx.send("음악이 재생돼고있지 않습니다.")
@bot.command(pass_context=True, aliases=['pa', 'pau'])
async def 일시정지(ctx):
    try:
        voice = get(bot.voice_clients, guild=ctx.guild)

        if voice and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("노래가 일시정지 되었습니다.")
        else:
            await ctx.send("일시정지할 노래가 없습니다.")
    except Exception as e:
        print('error')
@bot.command(pass_context=True, aliases=['r', 'res'])
async def 다시재생(ctx):
    try:
        voice = get(bot.voice_clients, guild=ctx.guild)

        if voice and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("재생 시작!")
        else:
            print("ERROR")
            await ctx.send("ERROR")
    except Exception as e:
        print('error')
@bot.command(pass_context=True, aliases=['l', 'lea'])
async def 나가(msg):
    await msg.voice_client.disconnect()

@bot.command(pass_context=True, aliases=['p', 'pla']) #재생
async def 재생(ctx, *, url):
    try:
        await ctx.voice_client.disconnect()
    except:
        pass
    channel = ctx.author.voice.channel
    try:
        ss = await channel.connect()
    except:
        pass
    try:
        os.remove(pf[0])
        pf.remove(pf[0])
    except:
        pass
    async with ctx.typing():
        player = await YTDLSource.from_url(url)
        print(player.id)
        print(player.title)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice_client.source)
        ctx.voice_client.source.volume = volumes / 100
    pf.append(player.filename)
    embedt = discord.Embed(title=f'{player.title}재생중!!',color=0x00c8ff)
    embedt.set_image(url=f'https://i.ytimg.com/vi/{player.id}/hqdefault.jpg')
    embedt.set_footer(text='다른노래가 나올 경우엔 ,s 을 하시고 다시 플래이를 해 주세요. 그래도 안될 경우엔 ,도움 을 입력해 서포트 서버로 가 주시길 바랍니다.')
    await ctx.send(embed=embedt)
bot.run('NzEzMDA3Mjk2NDc2NzQxNjQz.XsZ1yg.w9tjIrqZHYXbcqW8p9en1Y2dJbo')
