import discord
import youtube_dl
from discord.ext import commands
from youtube_search import YoutubeSearch
import asyncio
import time
import subprocess
import imaplib
import urllib.request
from bs4 import BeautifulSoup
from youtubesearchpython import SearchVideos
import re
import base64
import numpy as np
import requests
from PIL import Image
import random
import os
import configparser
from discord import Permissions
import urllib
import simplejson

client = commands.Bot(command_prefix=',',status=discord.Status.online)
current_index = 1
volumes = 15
queues = []
PlayLst = []

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print(client)
    print("ready")
import shutil
from discord.utils import get
import youtube_dl
import urllib
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import os
from os import system
import asyncio
import pafy


def scrape_info(url): 
      
    # getting the request from url 
    r = requests.get(url) 
      
    # converting the text 
    s = BeautifulSoup(r.text, "html.parser") 
      
    # finding meta info for title 
    title = s.find("span", class_="watch-title").text.replace("\n", "") 
      
    # finding meta info for views 
    views = s.find("div", class_="watch-view-count").text 
      
    # finding meta info for likes 
    likes = s.find("span", class_="like-button-renderer").span.button.text 
      
    # saving this data in dictionary 
    data = {'title':title, 'views':views, 'likes':likes} 
      
    # returning the dictionary 
    return data 
@client.command(pass_context=True, aliases=['j', 'joi'])
async def 들어와(ctx):
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
        print(f'error\n{e}')


@client.command(pass_context=True, aliases=['s', 'sto'])
async def 중지(ctx):
    global volumes
    voice = get(client.voice_clients, guild=ctx.guild)
    queues.clear()
    volumes = 15

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send("완료!")
    else:
        await ctx.send("음악이 재생돼고있지 않습니다.")
        
@client.command(pass_context=True, aliases=['p', 'pla'])
async def 재생(ctx, *, url):
    aul= ctx.author.id
    if url.find('https://www.youtu') == 0:
        url_t = url.split('=')
        z = len(url_t) - 1
        url_id = url_t[int(z)]
        v = pafy.new(url_id)
        url_title = v.title
        url = v.title
    else:
        search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
        o = eval(search.result())["search_result"]
        t = o[0]
        url_id = t['id']
        url_title = t['title']
    global volumes
    queues.append(url)
    def check_queue(url_id,aul):
        global current_index
        Queue_infile = len(queues)
        if Queue_infile > 0:
            if current_index >= len(queues):
                current_index = 0
            url = queues[current_index]
            print(queues)
            current_index += 1
            song_there = os.path.isfile(f"{url_id}_{aul}.mp3")
            try:
                if song_there:
                    os.remove(f"{url_id}_{aul}.mp3")
            except PermissionError:
                return
            voice = get(client.voice_clients, guild=ctx.guild)

            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': False,
                'outtmpl': f"./{url_id}_{aul}.mp3",
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
                print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
                c_paths = os.path.dirname(os.path.realpath(__file__))
                system("spotdl -ff song -f " + '"' + c_paths + '"' + " -s " + song_search)

            voice.play(discord.FFmpegPCMAudio(f"{url_id}_{aul}.mp3"), after=lambda e: check_queue())
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = volumes / 100
        else:
            queues.clear()

    song_there = os.path.isfile(f"{url_id}_{aul}.mp3")
    try:
        if song_there:
            os.remove(f"{url_id}_{aul}.mp3")
            queues.clear()
    except PermissionError:
        await ctx.send("오류발생!!")
        return

    a = await ctx.send("불러오는 중...")

    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': False,
        'outtmpl': f"./{url_id}_{aul}.mp3",
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
    voice.play(discord.FFmpegPCMAudio(f"{url_id}_{aul}.mp3"), after=lambda e: check_queue(url_id,aul))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = volumes / 100
    await a.delete()
    embed = discord.Embed(title=f'{url_title}재생준비중!!',color=0x00c8ff)
    embed.set_image(url=f'https://i.ytimg.com/vi/{url_id}/hqdefault.jpg')
    c = await ctx.send(embed=embed)
    await asyncio.sleep(1.5)
    embedt = discord.Embed(title=f'{url_title}재생중!!',color=0x00c8ff)
    embedt.set_image(url=f'https://i.ytimg.com/vi/{url_id}/hqdefault.jpg')
    embedt.set_footer(text='다른노래가 나올 경우엔 ,s 을 하시고 다시 플래이를 해 주세요. 그래도 안될 경우엔 ,도움 을 입력해 서포트 서버로 가 주시길 바랍니다.')
    await c.edit(embed=embedt)
client.run("NzEzMDA3Mjk2NDc2NzQxNjQz.XuWK4w.1D-nap9ca7zYP__JuEwdxiQ4ZEU")
