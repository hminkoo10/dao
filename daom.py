import discord
from discord.ext import commands
import shutil
from discord.utils import get
import youtube_dl
import os
from os import system
import asyncio
client = commands.Bot(command_prefix='!')
volumes = 15
queues = []
PlayLst = []
@client.command(pass_context=True, aliases=['j', 'joi'])
async def 들어와(ctx):
    """Подключиться к текущему голосовому каналу"""
    try:
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            return await voice.move_to(channel)

        await channel.connect()
        await ctx.send(f"봇이 {channel}로 접속하였습니다!")
    except Exception as e:
        await ctx.send(f"음성채널 접속 후 시도하세요!")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def 나가(ctx):
    """Отключиться от текущего голосового канала"""
    try:
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"봇이 {channel}에서 나갔습니다.")
        else:
            await ctx.send("봇이 음성채널에 접속 한 적이 없습니다.")
    except Exception as e:
        await ctx.send("봇이 음성채널에 없습니다.")


@client.command(pass_context=True, aliases=['pa', 'pau'])
async def 일시정지(ctx):
    """Приостановить воспроизведение"""
    try:
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            await ctx.send("노래가 일시정지 되었습니다.")
        else:
            await ctx.send("일시정지할 노래가 없습니다.")
    except Exception as e:
        print('error')


@client.command(pass_context=True, aliases=['r', 'res'])
async def 다시재생(ctx):
    """Продолжить воспроизведение"""
    try:
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            print("продолжение")
            voice.resume()
            await ctx.send("재생 시작!")
        else:
            print("ERROR")
            await ctx.send("ERROR")
    except Exception as e:
        print('error')


@client.command(pass_context=True, aliases=['v', 'vol'])
async def 볼륨(ctx, vol: int):
    """Изменение громкости (.volume 50)"""
    try:
        global volumes
        if ctx.voice_client is None:
            return await ctx.send("봇이 음성채널에 있지 않습니다.")
        if vol < 0 or vol > 200:
            await ctx.send(f"{ctx.author.mention}에 의해 불륨이 변경되었습니다.")
            return
        print(vol / 100)
        ctx.voice_client.source.volume = vol / 100
        await ctx.send(f"볼륨: {vol}%")
        volumes = vol
    except Exception as e:
        print('error')


@client.command(pass_context=True, aliases=['c', 'clr'])
async def 초기화(ctx):
    """Очистить очередь воспроизведения"""
    global volumes
    voice = get(client.voice_clients, guild=ctx.guild)
    queues.clear()
    volumes = 15

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send("초기화 완료!")
    else:
        await ctx.send("초기화 상태입니다.")
@client.command(pass_context=True, aliases=['p', 'pla'])
async def 재생(ctx, *url: str):
    """Воспроизвести трек (URL или название)"""
    global volumes
    queues.append(url)

    def check_queue():
        global current_index
        Queue_infile = len(queues)
        if Queue_infile > 0:
            if current_index >= len(queues):
                current_index = 0
            url = queues[current_index]
            print(queues)
            current_index += 1
            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
            except PermissionError:
                return
            voice = get(client.voice_clients, guild=ctx.guild)

            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': False,
                'outtmpl': "./song.mp3",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            song_search = " ".join(url)

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    print("загрузка\n")
                    ydl.download([f"ytsearch1:{song_search}"])
            except:
                print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
                c_paths = os.path.dirname(os.path.realpath(__file__))
                system("spotdl -ff song -f " + '"' + c_paths + '"' + " -s " + song_search)

            voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = volumes / 100
        else:
            queues.clear()

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
    except PermissionError:
        await ctx.send("오류발생!!")
        return

    await ctx.send("불러오는 중...")

    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': False,
        'outtmpl': "./song.mp3",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    song_search = " ".join(url)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{song_search}"])
    except:
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -ff song -f " + '"' + c_path + '"' + " -s " + song_search)
    queues.append(url)
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = volumes / 100

client.run("NzEzMDA3Mjk2NDc2NzQxNjQz.XuWK4w.1D-nap9ca7zYP__JuEwdxiQ4ZEU")
