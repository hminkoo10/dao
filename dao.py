#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
import time
import openpyxl
from discord.ext import commands
import random
from shellvaluepy.info import shell
import dbkrpy
import turtle
from boto3 import client
import pyfiglet
import turtle as t
import os
import asyncio
import datetime as pydatetime
from captcha.image import ImageCaptcha
import qrcode
import calendar
from gtts import gTTS
import smtplib
from email.mime.text import MIMEText
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import base64
import urllib,requests
import operator
from bs4 import BeautifulSoup
import ast
import uptimes.uptimes
import traceback
import sys
from googletrans import Translator
import subprocess
import aiohttp
import json
from numpyencoder import NumpyEncoder
import giphy_client #cmd에 'pip install giphy_client'
from giphy_client.rest import ApiException
import os
from twilio.rest import Client
import shutil
from discord.utils import get
from os import system
import shutil
import requests

#startup_extensions = ['cogs.Test_file']

#if __name__ == "__main__":
#    for extension in startup_extensions:
#        try:
#            discord.ext.commands.bot.load_extension(extension)
#        except Exception as e:
#            exc = '{}: {}'.format(type(e).__name__, e)
#            print('불러오기에 실패하셨습니다 {}\n{}'.format(extension,exc))
#os.chdir("/Users/hmink.DESKTOP-ANOIGRQ/Downloads/hminkoo/디스코드/봇/다오/dao")
with open('data_server.json', 'r') as f:
    jstring = open("data_server.json", "r", encoding='utf-8-sig').read()
    notice = json.loads(jstring)
channel = list()
with open('data_learn.json', 'r') as f:
    jstring = open("data_learn.json", "r", encoding='utf-8-sig').read()
    dict1 = json.loads(jstring)
with open('data_money.json', 'r') as f:
    jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
    money = json.loads(jstring)
with open('data_money_cool.json', 'r') as f:
    jstring = open("data_money_cool.json", "r", encoding='utf-8-sig').read()
    money_cool = json.loads(jstring)
with open('data_command_1.json', 'r') as f:
    jstring = open("data_command_1.json", "r", encoding='utf-8-sig').read()
    command_1 = json.loads(jstring)


typed = {}
dict2 = {}
tkdyd = []
giphy_token = 'uBpiTkQ9beqY4NayRkx6sz9bMSTkRpDE'
check = []
with open('prefixes.json', 'r') as f:
    jstring = open("prefixes.json", "r", encoding='utf-8-sig').read()
    prefixList = json.loads(jstring)
default_prefix = ","
async def prefix(bot, message):
    return prefixList.get(str(message.author.id), ",")
bot = commands.Bot(command_prefix=prefix,owner_id=657773087571574784)
dao = commands.Bot(command_prefix=';')
PRM = ['657773087571574784']
token = "NzEzMDA3Mjk2NDc2NzQxNjQz.XsZ1yg.w9tjIrqZHYXbcqW8p9en1Y2dJbo"
DBKR_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzAwNzI5NjQ3Njc0MTY0MyIsImlhdCI6MTU5MTEwNDk5MywiZXhwIjoxNjIyNjYyNTkzfQ.DusY04FtN-Gry0H9WP-pnLFqWkTg1TuKAyM9fzklDJedqjKk4VIpgk6SC70p1xZfQ_e08kOE_sGS-Vd5alI0U3JO3a_l2VIGZFAno2f79jU4ZRTbLKKKCEhY8eLGQ__rAawAbV8vgXrS0HWtM3fQEE23ud7DriLJAuRjn9Cgvjg"
progress = "none"
player1 = "none"
player2 = "none"
player1_card1 = 0
player1_card2 = 0
with open('data_money_command_2.json', 'r') as f:
    jstring = open("data_money_command_2.json", "r", encoding='utf-8-sig').read()
    money_command_2 = json.loads(jstring)
player1_card3 = 0
player2_card1 = 0
player2_card2 = 0
player2_card3 = 0
randomnum = "none"
player1_bat = "none"
player2_bat = "none"
player1_result = "none"
player2_result = "none"
item_money = {'증가벽돌': '2500','복구시스템': '4000'}
queues = list()
volume = ''
with open('data_money_command_1.json', 'r') as f:
    jstring = open("data_money_command_1.json", "r", encoding='utf-8-sig').read()
    money_command_1 = json.loads(jstring)
que = {}
playerlist = {}
playlist = list() #재생목록 리스트
admin = ['657773087571574784']
api_instance = giphy_client.DefaultApi()
with open('data_server_invite.json', 'r') as f:
    jstring = open("data_server_invite.json", "r", encoding='utf-8-sig').read()
    server_invite = json.loads(jstring)
with open('data_server_cool.json', 'r') as f:
    jstring = open("data_server_cool.json", "r", encoding='utf-8-sig').read()
    server_cool = json.loads(jstring)


def search_gifs(query):
    try:
        return api_instance.gifs_search_get(giphy_token, query,
                                            limit=5, rating='r',
                                            lang=["en","ru","ua","kr"]
                                               )

    except ApiException:
        pass
def gif_response(emotion):
    try:
        gifs = search_gifs(emotion)
        lst = list(gifs.data)
        gif = random.choices(lst)
        return gif[0].url
    except IndexError:
        pass
def randomcolor():
    return random.randint(0x0,0xffffff)
async def main():
    userid = "713007296476741643"
    info = await dbkrpy.CheckVote.get_response(token,userid)
    print(dbkypy.CheckVote(info).check)

def setup(bot):
    bot.add_cog(Corona(bot))
def write(file, tup):
    with open(f"{file}.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(tup, f, indent=2, ensure_ascii=False)
def read(file):
    with open(f'{file}.json', 'r') as f:
        jstring = open(f"{file}.json", "r", encoding='utf-8-sig').read()
def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)
def PVCY():
    pop = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',';','u','g','b','m','q','f','a','z','c','x','k','l','p','q','w','r','o']
    privacy = ''
    for i in range(20):
        privacy = privacy + random.choice(pop)
    return privacy
privacy = PVCY()
@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}!')
    print('정상작동중...')
    messages = ["명의 사용자와 함께", "접두어 = ,", "ver.4.7.1", "개의 서버와 함께"]
    while True:
        if messages[0] == '명의 사용자와 함께':
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f",도움 | {str(len(bot.users))}명의 사용자와 함께"))
        elif messages[0] == '개의 서버와 함께':
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f",도움 | {str(len(bot.guilds))}개의 서버와 함께"))
        else:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=",도움 | " + messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(3.5)
@bot.command()
async def 안녕(ctx):
    await ctx.channel.send((ctx.author.mention) + '님 안녕하세요!:hugging: :hugging_face:')
    await ctx.channel.send(':hugging_face:')
@bot.command()
async def 건의링크(ctx):
    await ctx.channel.send('https://discord.gg/PKGMwSB')
@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title="도움말",color=randomcolor(),description="서버 관리봇, 뮤직봇, 도박, 음악 모든게 다 있는, 디노.접두어:,") #임베드 변수 지정
    embed.add_field(name="초대링크", value="- ``,초대``로 확인", inline=False) #field add
    embed.add_field(name="매시지 삭제", value="- ``,삭제 (수)``로 확인", inline=False)
    embed.add_field(name="모두 삭제", value="- ``,clear``로 확인", inline=False)
    embed.add_field(name="출석체크(불완전)", value="- ``출석체크, ㅊㅊ``으로 확인 ``출석 리스트``로 확인", inline=False)
    embed.add_field(name="정보", value="- ``,정보(맨션)``로 확인", inline=False)
    embed.add_field(name="타이머", value="- ``,타이머 (초) (제목)``로 확인", inline=False)
    embed.add_field(name="DM보내기", value="- ``,우체국 @맨션 내용``로 확인", inline=False)
    embed.add_field(name="학습기능", value="``,학습 (1) (2)``를 하고 ``,(1)``로 확인",inline=False)
    embed.add_field(name="코로나 현황", value="``,코로나현황``로 확인",inline=False)
    embed.add_field(name="16진수 변환", value="``,color (빨강) (파랑) (노랑)``로 확인",inline=False)
    embed.add_field(name="영화순위(상위 10개)(네이버 api업데이트로 인해 작동하지 않음)", value="``,영화순위``로 확인", inline=False)
    embed.add_field(name="날씨", value="``,날씨 (지역)``로 확인", inline=False)
    embed.add_field(name="번역", value="``,번역 (번역할 언어) (번역될 언어) (번역될 낱말)``로 확인\n^^ 예시 : ,번역 ko en 안녕\n값 : Hello", inline=False)
    embed.add_field(name="슬로우모드(only 서버관리자)", value="``,슬로우모드 (초)``로 확인", inline=False)
    embed.add_field(name="운세", value="``,운세 00자리``로 확인", inline=False)
    embed.add_field(name="홍보", value="``,홍보``(홍보 채널에 보내짐)로 확인", inline=False)
    embed.add_field(name="사진편집", value="``,사진편집 이미지url 색갈(영어) 글``로 확인", inline=False)
    embed.add_field(name="돈 관련", value="``,돈줘\n,랭킹\n,내돈\n,훔쳐보기 @맨션\n,구매 (증가벽돌, 복구시스템)\n,사용 증가벽돌\n,복구 (복구암호)``로 확인", inline=False)
    embed.add_field(name="Text To Speech(음성채널에 대신 말해줌)", value="음성채널에 접속 후 ``,speech text``로 확인", inline=False)
    embed.add_field(name="사용량", value="``,사용량``로 확인", inline=False)
    embed.add_field(name="접두사", value="``,프리픽스``(개인 접두사입니다. 다른 서버에도 동일한 접두사 입니다)로 확인", inline=False)
    embed.add_field(name="디노 서포터", value="- ``https://discord.gg/zwzXuVz``", inline=False)
    embed.set_footer(text=(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.author.send(embed=embed)
    embed = discord.Embed(description = "[디노 서포터 <----- 클릭!!](https://discord.gg/zwzXuVz)",color=0x00ffae)
    await ctx.author.send(embed=embed)
    await ctx.send("DM으로 전송했어요!")
#@bot.command()
#class DBKRinfo(commands.Cog):
#
#    def __init__(self, bot):
#        self.bot = bot
#
#        async def getinfo(self, ctx):
#            info = await dbkrpy.GetById.get_response(538659580855451648)
#            dbkr = dbkrpy.DBKRGetById(info)
#            await ctx.send(dbkr.id)
#
#    def setup(bot):
#        bot.add_cog(DBKRinfo(bot))
@bot.command()
async def 사랑해(ctx):
    await ctx.channel.send('저두요!!')
    await ctx.channel.send('https://tenor.com/view/milk-and-mocha-kiss-love-in-love-gif-11453877')
    await ctx.channel.send('근데... 사랑하면 좋아요즘 주세요!')
@bot.command()
async def 초대(ctx):
    embed = discord.Embed(description = f"[디노봇 초대링크](https://discord.com/api/oauth2/authorize?client_id=713007296476741643&permissions=8&scope=bot)", color=0xf1c40f)
    embed.set_image(url="https://cdn.discordapp.com/attachments/702088239502065704/718732359704248380/3e5bae5149803302.png")
    await ctx.send(embed=embed)
    await ctx.send("QR코드가 포함되어 있습니다!")
@bot.command()
async def 테스트(ctx, *, text):
    for guild in bot.guild, member:
        await ctx.send(guilds)
@bot.command()
async def 온라인(ctx):
    await bot.change_presence(Status.online)
@bot.command()
async def 자리비움(ctx):
    await bot.change_presence(Status.idle)
@bot.command()
async def 방해금지(ctx):
    await bot.change_presence(Status.dnd)
@bot.command()
async def 오프라인(ctx):
    await bot.change_presence(Status.offline)
@bot.command()
async def 공지(ctx, *, text):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="@everyone",color=0x9b59b6,description="공지") #임베드 변수 지정
        embed.add_field(name=ctx.user.name, value=(text), inline=False) #field add
        embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        if str(ctx.author.id) in PRM:
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(title="@everyone",color=0x9b59b6,description="공지") #임베드 변수 지정
            embed.add_field(name=ctx.user.name, value=(text), inline=False) #field add
            embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send('관리자권한이 없습니다. (실행 요구 권한 : admin)')
@bot.command()
async def 보유서버(ctx):
    if str(ctx.author.id) in PRM:
        embed = discord.Embed(title='보유서버')
        for guild in bot.guilds:
            embed.add_field(name=guild,value=None)
        await ctx.channel.send(guild)
@bot.command()
async def 관리자보유서버(ctx):
    await ctx.channel.send(bot.guilds)
@bot.command()
async def 말해(ctx, *, text):
    await ctx.channel.send(f"{text}\n``{ctx.author.name}님이 따라하라고 명령했습니다``")
@bot.command()
async def 삭제(ctx, *, amount=999999999999999999999):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.channel.send('메시지 관리권한이 없습니다(요구권한 : 메시지관리 권한)')
@bot.command()
async def clear(ctx):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=1000000000000000)
    else:
        await ctx.channel.send('메시지 관리권한이 없습니다(요구권한 : 메시지관리 권한)')
@bot.listen()
async def on_message(message):
    if message.content.startswith(",건의"):
        author = bot.get_user(int(657773087571574784))
        choice = message.content.split(" ")
        msg = message.content[4: ]
        msgsender = message.author
        msgguild = message.guild.name
        msgchannel = message.channel.name

        if msg[0:4] == "http" or msg[0:5] == "https" or msg[0:3] == "www":
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="디노봇 건의", value="""
            건의장이 전송되지 않았습니다!
            건의장 미전송 사유: 링크 사용
            """, inline=False)
            embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdhFXEV%2FbtqEOaCVWlv%2FxbKPxv8Mskgsvlf3jwiEIK%2Fimg.png")
            await message.channel.send(embed=embed)
        elif msg == "":
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="디노봇 건의", value="""
            건의장이 전송되지 않았습니다!
            건의장 미전송 사유: 내용 없음
            """, inline=False)
            embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdhFXEV%2FbtqEOaCVWlv%2FxbKPxv8Mskgsvlf3jwiEIK%2Fimg.png")
            await message.channel.send(embed=embed)
        else:
            invites = await message.channel.create_invite(destination = message.channel, xkcd = True, max_uses = 100)
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="디노봇 건의", value="""
            피슝! 건의장이 도착했어요!
            건의장 내용: {}
            건의한 사람: {}
            건의장을 보낸 서버: {}
            건의장을 보낸 채널: {}
            건의장을 보낸 채널 초대링크: {}
            """.format(msg, msgsender, msgguild, msgchannel, invites), inline=False)
            embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdhFXEV%2FbtqEOaCVWlv%2FxbKPxv8Mskgsvlf3jwiEIK%2Fimg.png")
            await author.send(embed=embed)

            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="디노봇 건의", value="""
            건의장이 정상적으로 전송되었습니다!
            건의장 내용: {}
            건의한 사람: {}
            건의장을 보낸 서버: {}
            건의장을 보낸 채널: {}
            """.format(msg, msgsender, msgguild, msgchannel), inline=False)
            embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdhFXEV%2FbtqEOaCVWlv%2FxbKPxv8Mskgsvlf3jwiEIK%2Fimg.png")
            await message.channel.send(embed=embed)
@bot.command()
async def 건의(ctx, *, msg):
    print(msg)
    file = open("건의.txt", "a+")
    file.write(str("\n") + str(ctx.author) + str(":") + str(msg))
    file.close
    #await ctx.send(str(msg) + str("라고 발빠른 디노가 전해줬어요!"))
@bot.command()
async def 건의장초기화(ctx):
    file = open("건의.txt", "w")
    file.write("")
    file.close
    await ctx.send("건의장을 초기화 했어요!")
@bot.command()
async def 건의장읽기(ctx):
    file = open("건의.txt")
    await ctx.send(file.read())
@bot.command()
async def 타이머(ctx, time, *, text):
    c = text
    d = time
    e = ctx.author.mention
    await ctx.send(f"{d}초후에 {c}라고 알려드릴게요!")
    await asyncio.sleep(int(f"{d}"))
    await ctx.channel.send(f"{e}님! 시간이 다 되었어요! 제목:{c}")
@bot.command()
async def 주사위(ctx):
    dice = ['1','2','3','4','5','6']
    await ctx.channel.send(random.choice(dice))
#@bot.command()
#async def 마트(ctx):
#    list_a = [":grinning:",":grin:",":joy:",":rofl:",":smiley:",":smile:"]
#    var_a = random.choice(list_a)
#    await ctx.channel.send(f"{var_a}을 찾아라!")
#    def check(reaction, user):
#        return user == ctx.author and str(reaction.emoji) == var_a  # :grin: 라는 반응을 추가했는지 인식하는코드
#    try:
#        user = await bot.wait_for('reaction_add', timeout=7, check=check)  # 반응 추가할때까지 기다리는 코드. timeout=7은 7초 기다리면 타임아웃 오류를 발생시키는걸 의미.
#        if except asyncio.TimeoutError:
#            await ctx.channel.send("타임 아웃!")
#    else:
#        await ctx.channel.send("오! 잘 찾아왔어요!")
@bot.command()
async def 프리미엄(ctx):
    await ctx.channel.send('https://discord.gg/PKGMwSB 여기서 프리미엄 신청을 하세요')
#@bot.event()
#async def on_ready(ctx):
#    async def on_ready():
#    print(f'{client.user}로 로그인하였습니다.')

#    Data = await Bot.getVote(userid)
#    print(Data)
@bot.command()
async def 로또(ctx):
    로또 = ['꽝','꽝','꽝','당첨!','꽝','꽝','당첨!','당첨!','꽝','꽝','꽝','꽝','꽝',]
    await ctx.channel.send(random.choice(로또))
@bot.command()
async def 우체국(ctx, user:discord.Member, *, msg):
    #first_date = datetime('&y년 %m월 %d일 %p%I (%H시)시 %M분 %S초 보냄')
    first_date = time.asctime()
    embed = discord.Embed(color=0x00EBFF)
    embed.set_author(name="우체국에서 편지왔어요~")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url="http://bitly.kr/mailarrive")
    embed.add_field(name="보낸 유저 이름", value=str(ctx.message.author) + str("\n") + str(ctx.author.mention), inline=False)
    embed.add_field(name="보낸 유저 아이디", value=ctx.message.author.id, inline=False)
    embed.add_field(name="보낸 서버 아이디", value=ctx.message.guild.id, inline=False)
    embed.add_field(name="보낸 채널 아이디", value=ctx.message.channel.id, inline=False)
    embed.add_field(name="보낸 서버 이름", value=ctx.message.guild.name, inline=False)
    embed.add_field(name="보낸 채널 이름", value=ctx.message.channel.name, inline=False)
    embed.add_field(name="전할 내용", value=msg)
    embed.set_author(name=f"작성일:{first_date}", icon_url=bot.user.avatar_url)
    embed.set_footer(text=(f"작성일:{first_date}"), icon_url=ctx.author.avatar_url)
    await user.send(ctx.message.author.mention, embed=embed)
    await ctx.send("우체부가 아주 잘 전해준다고 했어요!")
@bot.command()
async def 택배(ctx, user:discord.Member, *, msg):
    #first_date = datetime('&y년 %m월 %d일 %p%I (%H시)시 %M분 %S초 보냄')
    first_date = time.asctime()
    embed = discord.Embed(color=0x00EBFF)
    embed.set_author(name="똑똑! 택배왔어요!")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="보낸 유저 이름", value=str(ctx.message.author) + str("\n") + str(ctx.author.mention), inline=False)
    embed.add_field(name="보낸 유저 아이디", value=ctx.message.author.id, inline=False)
    embed.add_field(name="택배 내용", value=msg)
    embed.set_author(name=f"작성일:{first_date}", icon_url="https://cdn.discordapp.com/attachments/717305319390445569/718425698292989962/68cf02c49ae96c340e0c7430959a64da.png")
    embed.set_footer(text=(f"작성일:{first_date}"), icon_url=ctx.author.avatar_url)
    await user.send(ctx.message.author.mention, embed=embed)
    await ctx.send("택배아죠씨가 아주 잘 전해준다고 했어요!")
#@bot.command()
#async def 가위바위보()
#    await ctx.channel.send('가위 바위 보중에 1개를 입력하세요')
#    async def 가위()
#
@bot.listen()
async def on_message(message):
    if message.content.startswith(',멜론차트'):
            print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
            msg=await message.channel.send('멜론차트 정보를 가져오는중.......')
            await asyncio.sleep(5)
            await msg.delete()
            if __name__=="__main__":
                RANK=10
                header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
                req = requests.get('https://www.melon.com/chart/index.htm', headers = header)
                html = req.text
                parse = BeautifulSoup(html, 'html.parser')
                titles = parse.find_all("div", {"class": "ellipsis rank01"})
                songs = parse.find_all("div", {"class": "ellipsis rank02"})
                title = []
                song = []
                embed=discord.Embed(
                    title="멜론차트 순위 입니다",
                    colour=0xff00
                )
                for t in titles:
                    title.append(t.find('a').text)
                for s in songs:
                    song.append(s.find('span', {"class": "checkEllipsis"}).text)
                for i in range(RANK):
                    embed.add_field(name='%3d위'%(i+1), value='%s - %s'%(title[i], song[i]), inline=False)
                import datetime
                now=datetime.datetime.now()
                embed.set_footer(icon_url=message.author.avatar_url, text=f'{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 기')
                embed.set_thumbnail(url ="https://yt3.ggpht.com/a/AATXAJw2h2wZcZDBmQspbRxwZpYsWEz67fDx4Gir=s900-c-k-c0xffffffff-no-rj-mo")
                await message.channel.send(embed=embed)
@bot.listen()
async def on_message(message):
    if message.content.startswith(',링크단축'):
        msg=await message.channel.send('링크 단축하는중...')
        await asyncio.sleep(5)
        await msg.delete()
        print(f'{message.author} ('+ f'{message.author.id}) : {message.content}')
        target=message.content[6]
        client_id="DqTSCjayP8uFjYJCWA3r"
        client_secret="KsaviRkocB"
        header = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
        naver = 'https://openapi.naver.com/v1/util/shorturl'
        data = {'url': target}
        maker=requests.post(url=naver,data=data,headers=header)
        maker.close()
        output=maker.json()['result']['url']
        embed = discord.Embed(title="URL 단축기능",color=0xff00, timestamp=message.created_at)
        embed.add_field(name="단축 링크", value=f'{output}', inline = False)
        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
@bot.listen()
async def on_message(message):
    if message.content == ",빗자루":
        broomcount = 0
        time = 3
        broom = await message.channel.send('{0.author.mention}, 빗자루 아이콘(🧹)을 연타하세요! :slight_smile:'.format(message))
        await broom.add_reaction('🧹')
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '🧹'

        while True:
            try:
                user = await bot.wait_for('reaction_add', timeout=time, check=check)
            except asyncio.TimeoutError:
                broomcount = broomcount * 2
                await message.channel.send("{0.author.mention}, 타임 아웃! :clock12:\n".format(message) + str(
                    broomcount) + '번 빗자루질을 했어요! :broom:\n')
                break
            else:
                broomcount += 1
                time = time * 0.825
@bot.command()
async def 공지채널설정(ctx, channel: discord.TextChannel):
    if ctx.message.author.id == 657773087571574784:
        json_string = json.dumps(notice)
        #channels = str(channel)
        #print(type(channels))
        if channel in notice:
            await ctx.send("이미 등록됨")
        else:
            channels = str(channel.id)
            notice.append(channels)
            #json_string = json.dumps(notice, cls=str)
            #print(json_string)
            with open("data_server.json", "w+", encoding='utf-8-sig') as f:
                json_string = json.dump(notice, f, indent=2, ensure_ascii=False)
            #print(json_string)
            #jstring = json.dumps(notice, indent=4)
            #f = open("data_server.json", "w")
            #f.write(jstring)
            #f.close()
            await ctx.send("json data저장")
            await ctx.send("완료")

@bot.command()
async def 공지보내기(ctx, *, msg, pass_context=True):
    if ctx.message.author.id == 657773087571574784:
        with open('data_server.json', 'r') as f:
            jstring = open("data_server.json", "r", encoding='utf-8-sig').read()
            notice = json.loads(jstring)
            getchannel = []
        for i in notice:
            await bot.wait_until_ready()
            getchannel.append(bot.get_channel(int(i)))
        for e in getchannel:
                await ctx.send("전송시도중")
                try:
                    embed = discord.Embed(title="디노봇 공지",color=discord.Color.gold(),description=None) #임베드 변수 지정
                    embed.add_field(name="공지내용\n=================", value=(msg), inline=False) #field add
                    embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
                    await e.send(embed=embed)
                    await ctx.send("성공")
                except:
                    await ctx.send("실패")

#@bot.listen()
#async def on_message(message):
#    if message.content.startswith(""):
#        file = openpyxl.load_workbook("leavels.xlsx")
#        sheet = file.active
#        exp = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#        i = 1
#        while True:
#            if sheet["A" + str(i)].value == str(message.author.id):
#                sheet["B" + str(i)].value = sheet[sheet["B" + str(i)].value] + 5
#                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value:]:
#                     sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
#                     await message.channel.send("레벨이 올랐습니다.\n현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
#                file.save("leavels.xlsx")
#                break


#            if sheet["A" + str(i)].value == None:
#                sheet["A" + str(i)].value = str(message.author.id)
#                sheet["A" + str(i)].value = 0
#                sheet["A" + str(i)].value = 1
#                file.save("leavels.xlsx")
#                break
#                
#            i += 1
@bot.command()
async def 킥(ctx, user:discord.Member, *, text):
    if ctx.author.guild_permissions.administrator:
        await ctx.guild.kick(user, reason=text)
        await ctx.send(f"{user}님을 킥 했어요! \n 킥사유:{text}")
    else:
        await ctx.send("관리자 권한이 없어요!")
@bot.command()
async def 밴(ctx, user:discord.Member, *, text):
    if ctx.author.guild_permissions.administrator:
        await ctx.guild.ban(user, reason=text)
        await ctx.send(f"{user}님을 밴 했어요! \n 밴사유:{text}")
    else:
        await ctx.send("관리자 권한이 없어요!")
@bot.command()
async def 언밴(ctx):
    user = ["4:22"]
    await ctx.guild.unban(user)
    await ctx.send(f"{user}님을 언밴 했어요!")
@bot.listen()
async def on_message(message):
    if message.content.startswith(",학습"):
        file = openpyxl.load_workbook("read.xlsx")
        sheet = file.active

@bot.listen()
async def on_message(message):
    if message.content.startswith(",출첵") or message.content.startswith(",ㅊㅊ") or message.content.startswith(",출석체크"):
        if str(message.author.name) in check:
            await message.channel.send("이미 출석체크를 했습니다")
        else:
            check.append(message.author.name)
            embed = discord.Embed(color=0xf1c40f)
            embed.add_field(name="출석체크 시스템", value="""
            출석체크가 정상적으로 완료되었습니다.
            """, inline=False)
            embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2F9M6qG%2FbtqEdyejxb6%2Fp6cEiCqE8QERwOg5EhDTn1%2Fimg.png")
            await message.channel.send(embed=embed)
@bot.listen()
async def on_message(message):
    if message.content.startswith("출석 리스트"):
        finalcheck = "디노봇"
        for i in check:
            finalcheck = finalcheck + ", " + (i)
        embed = discord.Embed(color=0xf1c40f)
        embed.add_field(name="출석체크한 유저", value="""
        {}
        """.format(finalcheck), inline=False)
        embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2F9M6qG%2FbtqEdyejxb6%2Fp6cEiCqE8QERwOg5EhDTn1%2Fimg.png")
        await message.channel.send(embed=embed)
@bot.command()
async def 리로드(ctx):
    if ctx.message.author.id == 657773087571574784:
        await ctx.send("리로드중입니다! 잠시만 기다려주세요!")
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="재부팅"))
        time.sleep(1)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="재부팅"))
        time.sleep(2)
        await ctx.send("리로드 완료!")
        os.system("python3 dao.py")
        exit()
#        await ctx.send("모든 모듈을 리로드했어요!")
#        imp.reload(discord)
#        self.bot.reload_extension("gathongi.py")
@bot.listen()
async def on_message(message):
    if message.content == ",정보":
        import datetime
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xf1c40f)
        embed = embed.add_field(name="이름", value=f'{message.author}\n\n#{message.author.discriminator}', inline=True)
        embed = embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed = embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed = embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
@bot.command()
async def 정보(ctx, user:discord.Member):
    a = user.avatar_url
    embed = discord.Embed(description = f"[프로필 원본 보기]({a})", color=0xf1c40f)
    embed.add_field(name=user, value=f'{user.id}\n\n#{user.discriminator}', inline=False)
    embed.add_field(name="사용자 지정 상태", value=user.activity, inline=False)
    embed.add_field(name="상태", value=user.status, inline=False)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
@bot.command()
async def 역할전달(ctx, user:discord.Member, *, txt):
    if ctx.author.guild_permissions.administrator:
        b = txt
        role = discord.utils.get(ctx.guild.roles, name=f"{b}")
        await user.add_roles(role)
        await ctx.send("전달 완료!")
    else:
        await ctx.send("관리자권한이 없음")
@bot.command()
async def 역할빼기(ctx, user:discord.Member, *, txt):
    if ctx.author.guild_permissions.administrator:
        b = txt
        role = discord.utils.get(ctx.guild.roles, name=f"{b}")
        await user.remove_roles(role)
        await ctx.send("역할을 가져왔어요!")
    else:
        await ctx.send("관리자권한이 없음")
@bot.listen()
async def on_message(message):
    if message.content.startswith(","):
        tkdyd.append(message.author.name)
@bot.command()
async def 사용횟수(ctx):
    await ctx.send(tkdyd)
@bot.command()
async def 덧셈(ctx, one, two):
    f = float(one) + float(two)
    g = one
    h = two
    await ctx.send(f"{g}+{h}={f} 입니다!")
@bot.command()
async def 뺄셈(ctx, one, two):
    k = float(one) - float(two)
    i = one
    j = two
    await ctx.send(f"{i}-{j}={k} 입니다!")
@bot.command()
async def 곱셈(ctx, one, two):
    l = float(one) * float(two)
    n = one
    m = two
    await ctx.send(f"{n}*{m}={l} 입니다!")
@bot.command()
async def 나눗셈(ctx, one, two):
    o = float(one) / float(two)
    p = one
    q = two
    await ctx.send(f"{p}/{q}={o} 입니다!")
@bot.command()
async def 제곱(ctx, one, two):
    r = float(one) ** float(two)
    s = one
    t = two
    await ctx.send(f"{s}**{t}={r} 입니다!")
@bot.listen()
async def on_message(message):
    if message.content.startswith(",도박도움") or message.content.startswith(",도박방법"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="디노봇 도박 방법!", value="""
        지금부터 도박하는 방법에 대해 말씀드릴게요!
        
        이 게임은 뽑은 카드의 수를 합쳐 나오는 수의 일의 자리가 큰 사람이 이기는 게임입니다!
        J, Q, K 카드는 각각 숫자 11, 12, 13으로 간주합니다.

        1. '랜지 코인 받기'로 코인을 획득해 주세요!
        2. '도박 신청 <아이디>'로 도박을 신청하세요!
        3. 상대방이 '예'라고 대답하면 도박이 시작됩니다.
        4. '카드 뽑기'를 입력하시면 DM으로 뽑힌 카드 2장이 전송됩니다!
        5. 카드가 좋지 않다면 1장까지만 더 뽑을 수 있습니다.
        6. 베팅할 랜지 코인의 개수를 입력하세요!
        7. 이긴 사람이 랜지 코인을 모두 가져갑니다!

        즐거운 게임 되세요!
        """, inline=False)
        await message.author.send(embed=embed)
@bot.listen()
async def on_message(message):
    if message.content.startswith(",도박신청"):
        global progress
        global player2
        global player1
        global player1_card1
        global player1_card2
        global player1_card3
        global player2_card1
        global player2_card2
        global player2_card3
        global randomnum
        global player1_bat
        global player2_bat
        global player1_result
        global player2_result

        if (progress) == "none":
            choice = message.content.split(" ")
            player1 = (message.author.display_name)
            player2 = choice[1]
            print(player2)
            
            progress = "invite"
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="디노봇 도박", value="""
            {}님께서 {}님께 도박을 신청하였습니다.
            도박 신청을 수락하시려면 '**예**'를 입력해 주시고 거절하시려면 '**아니요**'를 입력해 주세요.

            **주의: 닉네임에 공백 혹은 대괄호가 포함되어 있으면 인식할 수 없습니다.**
            """.format(player1, player2), inline=False)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="디노봇 도박", value="""
            현재 다른 플레이어들의 초대 및 게임이 진행중입니다.
            """, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("아니요"):
        if progress == "invite":
            if message.author.display_name == player2:
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                도박 신청이 거부되었습니다.
                """, inline=False)
                await message.channel.send(embed=embed)
                progress = "none"
                player1 = "none"
                player2 = "none"
                player1_card1 = 0
                player1_card2 = 0
                player1_card3 = 0
                player2_card1 = 0
                player2_card2 = 0
                player2_card3 = 0
                randomnum = "none"
                player1_bat = "none"
                player2_bat = "none"
                player1_result = "none"
                player2_result = "none"
        if progress == "one_more_card":
            if message.author.display_name == player1 or message.author.display_name == player2:
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                **서버**에서 **'배팅 <배팅할 랜지 코인(숫자만 입력)>'**을 입력하여 배팅을 해주세요.
                """, inline=False)
                await message.author.send(embed=embed)

    if message.content.startswith("예"):
        if progress == "invite":
            if message.author.display_name == player2:
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                도박 신청이 수락되었습니다.
                """, inline=False)
                await message.channel.send(embed=embed)
                progress = "card"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                ',카드 뽑기'를 입력하여 카드를 뽑으세요!
                """, inline=False)
                await message.channel.send(embed=embed)
        if progress == "one_more_card" or progress == "one_more_card_1":
            if message.author.display_name == player1:
                randomnum = random.randrange(1,14)
                player1_card3 = randomnum
                if progress == "one_more_card_1":
                    progress = "bat"
                else:
                    progress = "one_more_card_1"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                한번 더 뽑은 당신의 카드는 {} 입니다!
                """.format(player1_card3), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                **서버**에서 **'배팅 <배팅할 랜지 코인(숫자만 입력)>'**을 입력하여 배팅을 해주세요.
                """, inline=False)
                await message.author.send(embed=embed)
            if message.author.display_name == player2:
                randomnum = random.randrange(1,14)
                player2_card3 = randomnum
                if progress == "one_more_card_1":
                    progress = "bat"
                else:
                    progress = "one_more_card_1"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                한번 더 뽑은 당신의 카드는 {} 입니다!
                """.format(player2_card3), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                **서버**에서 **'배팅 <배팅할 랜지 코인(숫자만 입력)>'**을 입력하여 배팅을 해주세요.
                """, inline=False)
                await message.author.send(embed=embed)
                

    if message.content.startswith(",카드 뽑기"):
        if progress == "card" or progress == "card_1":
            if message.author.display_name == player1:
                randomnum = random.randrange(1,14)
                player1_card1 = randomnum
                randomnum = random.randrange(1,14)
                player1_card2 = randomnum
                if progress == "card_1":
                    progress = "one_more_card"
                else:
                    progress = "card_1"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                당신의 카드는 {}, {} 입니다!
                """.format(player1_card1, player1_card2), inline=False)
                await message.author.send(embed=embed)
            if message.author.display_name == player2:
                randomnum = random.randrange(1,14)
                player2_card1 = randomnum
                randomnum = random.randrange(1,14)
                player2_card2 = randomnum
                if progress == "card_1":
                    progress = "one_more_card"
                else:
                    progress = "card_1"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                당신의 카드는 {}, {} 입니다!
                """.format(player2_card1, player2_card2), inline=False)
                await message.author.send(embed=embed)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="디노봇 도박", value="""
        한 장 더 뽑으시려면 '**예**'를 입력해 주시고 바로 베팅을 하시려면 '**아니요**'를 입력해 주세요.
        """, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(",배팅"):
        if progress == "bat" or progress == "bat_1":
            if message.author.display_name == player1:
                choice = message.content.split(" ")
                player1_bat = choice[1]
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                {}님께서 랜지 코인 {}개를 배팅하셨습니다.
                """.format(player1, player1_bat), inline=False)
                await message.channel.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                랜지 코인 {}개가 정상적으로 배팅되었습니다.
                """.format(player1_bat), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="도박 결과를 입력해 누가 승리했는지 확인하세요!", inline=False)
                await message.author.send(embed=embed)
                if progress == "bat_1":
                    progress = "result"
                else:
                    progress = "bat_1"
            if message.author.display_name == player2:
                choice = message.content.split(" ")
                player2_bat = choice[1]
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                {}님께서 랜지 코인 {}개를 배팅하셨습니다.
                """.format(player2, player2_bat), inline=False)
                await message.channel.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                랜지 코인 {}개가 정상적으로 배팅되었습니다.
                """.format(player2_bat), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="도박 결과를 입력해 누가 승리했는지 확인하세요!", inline=False)
                await message.author.send(embed=embed)
                if progress == "bat_1":
                    progress = "result"
                else:
                    progress = "bat_1"
        
    if message.content.startswith(",도박 결과"): 
        if progress == "result":
            if player1_bat != 0 and player2_bat != 0:
                progress = "none"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                3초 뒤 결과가 공개됩니다.
                """, inline=False)
                await message.channel.send(embed=embed)
                time.sleep(3)
                player1_result = player1_card1 + player1_card2 + player1_card3
                player1_result = player1_result % 10
                player2_result = player2_card1 + player2_card2 + player2_card3
                player2_result = player2_result % 10
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                {}님의 카드는 {}, {}, {} 입니다.
                """.format(player1, player1_card1, player1_card2, player1_card3), inline=False)
                await message.channel.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="디노봇 도박", value="""
                {}님의 카드는 {}, {}, {} 입니다.
                """.format(player2, player2_card1, player2_card2, player2_card3), inline=False)
                await message.channel.send(embed=embed)
                if player1_result > player2_result:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="디노봇 도박", value="{}님의 승리입니다! 축하드립니다 {}님!".format(player1, player1), inline=False)
                    await message.channel.send(embed=embed)
                if player1_result < player2_result:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="디노봇 도박", value="{}님의 승리입니다! 축하드립니다 {}님!".format(player2, player2), inline=False)
                    await message.channel.send(embed=embed)
                if player1_result == player2_result:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="디노봇 도박", value="무승부입니다 ㅠ.ㅠ 배팅한 코인의 반을 서로 가져갑니다.", inline=False)
                    await message.channel.send(embed=embed)
                progress = "none"
                player1 = "none"
                player2 = "none"
                player1_card1 = 0
                player1_card2 = 0
                player1_card3 = 0
                player2_card1 = 0
                player2_card2 = 0
                player2_card3 = 0
                randomnum = "none"
                player1_bat = "none"
                player2_bat = "none"
                player1_result = "none"
                player2_result = "none"
@bot.listen()
async def on_message(message):
    if message.content.startswith("도박 종료"):
        if message.author.id == 657773087571574784 or message.author.display_name == player1 or message.author.display_name == player2:
            await message.channel.send(embed=discord.Embed(description="도박이 강제 종료되었습니다.", color=0xffa500))
            progress = "none"
            player1 = "none"
            player2 = "none"
            player1_card1 = 0
            player1_card2 = 0
            player1_card3 = 0
            player2_card1 = 0
            player2_card2 = 0
            player2_card3 = 0
            randomnum = "none"
            player1_bat = "none"
            player2_bat = "none"
            player1_result = "none"
            player2_result = "none"
        else:
            await message.channel.send(embed=discord.Embed(description="개발자나 현재 도박 플레이어만 할 수 있는 기능이에요.", color=0xff0000))
@bot.command()
async def hellothisisverification(ctx):
    await ctx.send("디스코드봇 합작계정#3927 \n hminkoo10#3679 \n jhcplace#4760")
@bot.command()
async def 초대링크생성(ctx, user:discord.Member):
    cheofldzm = user.id
    embed = discord.Embed(description = f"[이거 입니다! 그런데 사람은 아니겠죠? :zany_face:](https://discord.com/api/oauth2/authorize?client_id={cheofldzm}&permissions=8&scope=bot)",color=0xe67e22)
    await ctx.send(embed=embed)
@bot.command()
async def 확인(ctx):
    info = await dbkrpy.CheckVote.get_response("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzAwNzI5NjQ3Njc0MTY0MyIsImlhdCI6MTU5MTEwNDk5MywiZXhwIjoxNjIyNjYyNTkzfQ.DusY04FtN-Gry0H9WP-pnLFqWkTg1TuKAyM9fzklDJedqjKk4VIpgk6SC70p1xZfQ_e08kOE_sGS-Vd5alI0U3JO3a_l2VIGZFAno2f79jU4ZRTbLKKKCEhY8eLGQ__rAawAbV8vgXrS0HWtM3fQEE23ud7DriLJAuRjn9Cgvjg", ctx.author.id)
    dbkr = dbkrpy.CheckVote(info)
    await ctx.channel.send(dbkr.check)
    #await ctx.channel.send(info)
    captcha = ImageCaptcha()
    msg = ""
    a = ""
    for i in range(6):
        a += str(random.randint(0, 9))

    name = str(ctx.author) + str(".png")
    captcha.write(a, name)

    await ctx.channel.send(file=discord.File(name))

    if msg.content.startswith == (a):
        await ctx.channel.send("인증을 완료했어요!")
        info = await dbkrpy.CheckVote.get_response("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzAwNzI5NjQ3Njc0MTY0MyIsImlhdCI6MTU5MTEwNDk5MywiZXhwIjoxNjIyNjYyNTkzfQ.DusY04FtN-Gry0H9WP-pnLFqWkTg1TuKAyM9fzklDJedqjKk4VIpgk6SC70p1xZfQ_e08kOE_sGS-Vd5alI0U3JO3a_l2VIGZFAno2f79jU4ZRTbLKKKCEhY8eLGQ__rAawAbV8vgXrS0HWtM3fQEE23ud7DriLJAuRjn9Cgvjg", ctx.author.id)
        dbkr = dbkrpy.CheckVote(info)
        await ctx.channel.send(dbkr.check)
        await ctx.channel.send(info)
    else:
        await ctx.chennel.send("오답이예요! 다시 시도해 보세요~")
        return
#@bot.listen()
#async def on_message(message):
#    if message.content.startswith(","):
#        dice = ["y","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n","n"]
#        yesorno = random.choice(dice)
#        if yesorno == "y":
#            info = await dbkrpy.CheckVote.get_response("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzAwNzI5NjQ3Njc0MTY0MyIsImlhdCI6MTU5MTEwNDk5MywiZXhwIjoxNjIyNjYyNTkzfQ.DusY04FtN-Gry0H9WP-pnLFqWkTg1TuKAyM9fzklDJedqjKk4VIpgk6SC70p1xZfQ_e08kOE_sGS-Vd5alI0U3JO3a_l2VIGZFAno2f79jU4ZRTbLKKKCEhY8eLGQ__rAawAbV8vgXrS0HWtM3fQEE23ud7DriLJAuRjn9Cgvjg", message.author.id)
#            dbkr = dbkrpy.CheckVote(info)
#            yee = dbkr.check
#            embed = discord.Embed(description = "[[광고]디노를 초대해주세요!](https://discord.com/oauth2/authorize?client_id=713007296476741643&scope=bot&permissions=8)", color=0xff0000)
#            await message.channel.send(embed=embed)
#            embed = discord.Embed(description = "[[광고]디노한테 좋아요를 눌러주세요!](https://koreanbots.dev/bots/713007296476741643)", color=0xff0000)
#            await message.channel.send(embed=embed)
@bot.command()
async def 핑(ctx):
    time1 = time.time()
    if (round(bot.latency*1000)) > 230:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 매우 나쁨:no_entry:""".format(round(bot.latency*1000)), color=0xff0000)
    if (round(bot.latency*1000)) < 230:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 양호:white_check_mark:""".format(round(bot.latency*1000)), color=0x00ff00)
    if (round(bot.latency*1000)) < 185:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 매우 좋음:green_heart:""".format(round(bot.latency*1000)), color=0x0000ff)
    edit = await ctx.send(embed=discord.Embed(title='핑!', color=0x0ff00))
    time2 = time.time()
    time4 = float(time2) - float(time1)
    time5 = str(time4)
    time6 = time5[2:5]
    time7 = f'{time6}ms'
    embed.add_field(name="디스코드 메시지 핑", value=f'{time7}')
    await edit.edit(embed=embed)
@bot.command()
async def ping(ctx):
    tso = ger_get_now_timestamp()
    await ctx.send('pong!')
    tst = get_now_timestamp()
    ll = float(tso) - float(tst)
    await ctx.send(ll)
@bot.command()
async def 역할생성(ctx, *, text):
    if ctx.author.guild_permissions.administrator:
        await ctx.guild.create_role(name=text)
        await ctx.send(f"{text}역할을 생성했어요! \n 역할을 전달하시려면 ,역할전달 @맨션 {text} 입니다!")
    else:
        await ctx.send("관리자권한이 없어요!")
@bot.command()
async def 역할삭제(ctx, *, text):
    if ctx.author.guild_permissions.administrator:
        await ctx.guild.delete_role(name=text)
        await ctx.send(f"{text}역할을 삭제했어요!")
    else:
        await ctx.send("관리자권한이 없어요!")
@bot.command(name="eval")
async def eval_(ctx, *, code):
    if str(ctx.author.id) in admin:
        try:
            await ctx.send(eval(code))
        except Exception as ex:
            await ctx.send(f'오류발생!\n에러코드:{str(ex)}')
@bot.command()
async def 유저수동기화(ctx, *, text):
    await text.edit(name="유저")
@bot.command()
async def qr코드(ctx, *, link):
    img = qrcode.make(link)
    img.save(str(ctx.author) + str('.png'))
    name = str(ctx.author) + str('.png')
    await ctx.author.send(file=discord.File(name))
    await ctx.send("DM으로 QR코드를 전송했어요!")
@bot.command()
async def qr코드전달(ctx, user:discord.Member, *, link):
    img = qrcode.make(link)
    img.save(str(ctx.author) + str('.png'))
    name = str(ctx.author) + str('.png')
    await user.send(file=discord.File(name))
    await ctx.send("DM으로 QR코드를 전송했어요!")
@bot.command()
async def 제작자(ctx):
    await ctx.send(admin)
@bot.command()
async def 암호생성(ctx, *, text):
    captcha = ImageCaptcha()
    msg = ""
    a = text
    name = str(ctx.author) + str(".png")
    captcha.write(a, name)

    await ctx.channel.send(file=discord.File(name))
#@bot.listen()
#async def on_message(message):
#    if message.content.startswith(","):
#        async with message.typing():
#            print("타이핑중")
@bot.command()
async def 타이핑(message):
    async with message.typing():
        import typing
        em = "<:dummy:709371261024862278>"
        await ctx.send(em)

@bot.listen()
async def on_error(event, args, **kwargs):
    if event == "on_message": #on_message에서 발생했을때 작동합니다.
        message = args[0] #args값에는 여러개가 들어올수도 있으니, 첫번째껏만 잡아줍니다.
        exc = sys.exc_info() #sys를 활용해서 에러를 확인합니다.
        message.channel.send(str(exc[0].__name__) + "" + str(exc[1])) #그 에러를 출력합니다.
        return
@bot.listen()
async def on_message_delete(message):
    if message.guild.id == int('753048689399824384'):
        await bot.get_channel(int(753048689399824384)).send(f"<#{message.channel.id}>\n메세지 삭제 감지(" + str(message.author) + "): " + message.content)
        return
#@bot.command()
async def on_member_leaves(member):
    if member.message.guild.id == 701974089421553806:
        await bot.get_channel(712933494489088041).send(f"{member.author.mention}님이 오셨어요! 환영 해 주세요!")
        return
#@bot.listen()
async def on_guild_join(guild):
	await guild.message.channel.send("새로운 서버에 접속!" + str(guild))
	return
#@bot.listen()
async def on_member_ban(guild, user):
	await guild.channel.send(f"{user}님이 밴 되었습니다")
	return
#@bot.listen()
async def on_member_unban(guild, user):
	await guild.channel.send(f"{user}님이 언밴 되었습니다")
	return
@bot.listen()
async def on_message(message):
	if message.content.startswith(',가위바위보'):
		rsp = ["가위","바위","보"]
		embed = discord.Embed(title="가위바위보",description="가위바위보를 합니다 3초내로 (가위/바위/보)를 써주세요!", color=0x00aaaa)
		channel = message.channel
		msg1 = await message.channel.send(embed=embed)
		def check(m):
			return m.author == message.author and m.channel == channel
		try:
			msg2 = await bot.wait_for('message', timeout=7.5, check=check)
		except asyncio.TimeoutError:
			await msg1.delete()
			embed = discord.Embed(title="가위바위보",description="앗 7초가 지났네요...!", color=0x00aaaa)
			await message.channel.send(embed=embed)
			return
		else:
			await msg1.delete()
			bot_rsp = str(random.choice(rsp))
			user_rsp  = str(msg2.content)
			answer = ""
			if bot_rsp == user_rsp:
				answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "아쉽지만 비겼습니다."
			elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (bot_rsp == "바위" and user_rsp == "보"):
				answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "아쉽지만 제가 졌습니다."
			elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (bot_rsp == "보" and user_rsp == "바위"):
				answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "제가 이겼습니다!"
			else:
				embed = discord.Embed(title="가위바위보",description="앗, 가위, 바위, 보 중에서만 내셔야죠...", color=0x00aaaa)
				await message.channel.send(embed=embed)
				return
			embed = discord.Embed(title="가위바위보",description=answer, color=0x00aaaa)
			await message.channel.send(embed=embed)
			return
@bot.command()
async def tts(ctx, *, bom):
    await ctx.channel.send(f"{bom}\n{ctx.author.name}님이 커맨드를 사용했습니다",tts=True)
@bot.listen()
async def on_message(message):
    if message.content.startswith(",서버나가"):
        if str(ctx.author.id) in admin:
            imd = massage.content[5:]
            to_leave = bot.get_guild(int(imd))
            await bot.leave_server(to_leave)
            await message.channel.send("OK")
@bot.command()
async def 초대목록(ctx):
    await ctx.guild.id.invites()
#@bot.command()
#async def 언밴(ctx, user):
#    await (ctx.guild.id).unban(user, reason=None)
@bot.listen()
async def on_message(message):
    if message.content.startswith(",서버초대링크생성"):
        await message.channel.id.invites()
@bot.command()
async def id확인(ctx, il: int):
    imm = bot.get_user(il)
    await ctx.send(str(imm))
@bot.command()
async def 학습(ctx, one, *, two):
    dict1[one] = two + '\n' f'``{ctx.author}님이 알려주셨어요!``'
    file = open("학습기록.txt", "a+")
    file.write(str("\n") + str(ctx.author) + str(":") + str(one) + str(":") + str(two))
    file.close
    with open("data_learn.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(dict1, f, indent=2, ensure_ascii=False)
    await ctx.send("json데이터 저장중")
    await ctx.send("OK")
@bot.listen()
async def on_message(message):
    if message.content.startswith(","):
        with open('data_server.json', 'r') as f:
            jstring = open("data_learn.json", "r", encoding='utf-8-sig').read()
        dict1 = json.loads(jstring)
        hi = message.content[1:]
        try:
            send = dict1[hi]
            await message.channel.send(send)
        except:
            pass
@bot.command()
async def 지워(ctx, text):
    if str(ctx.author.id) in admin:
        del dict1[text]
        with open("data_learn.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(dict1, f, indent=2, ensure_ascii=False)
        await ctx.send("json DB저장중")
        await ctx.send("OK")
@bot.command()
async def 학습확인(ctx):
    await ctx.send(dict1)
@bot.command()
async def 달력(ctx, num):
    cale = (calendar.calendar(num))
    print(f"{cale}")
@bot.command()
async def 비속어추가(ctx, *, one):
    if str(ctx.author.id) in admin:
        dict2[one] = '비속어를 사용했어요 :angry: ! \n사용한 비속어 : ' + one
        file = open("비속어.txt", "a+")
        file.write(str("\n") + str(ctx.author) + str(":") + str(one))
        file.close

        file = open("비속어디셔너리.txt", "a+")
        file.write(dict2)
        file.close
        await ctx.send("OK")
#@bot.listen()
#async def on_message(message):
#    if message.content.startswith(""):
#        hi = message.content[0:]
#        send = dict2[hi]
#        await message.channel.purge(limit=1)
#        await message.channel.send(str(send) + str("\n비속어 사용자 : ") + str(message.author))
#        file = open("비속어사용.txt", "a+")
#        file.write(str("\n") + str(message.author) + str(":") + str(send))
#        file.close
@bot.command()
async def 비속어삭제(ctx, text):
    if str(ctx.author.id) in admin:
        del dict2[text]
        await ctx.send("OK")
@bot.command()
async def 비속어확인(ctx):
    file = open("비속어사용.txt")
    await ctx.send(file.read())
@bot.command()
async def 크레딧(ctx):
    await ctx.send("랭킹 도움: 파이어리자드")
@bot.command()
async def 밴처리(ctx, user:discord.Member, *, text):
    if str(ctx.author.id) in admin:
        await ctx.guild.ban(user, reason=text)
        await ctx.send(f"{user}님을 밴 했어요! \n 밴사유:{text}")
@bot.command()
async def 뮤트(ctx, user:discord.Member):
    try:
        if ctx.author.guild_permissions.manage_roles:
            member = user.name
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await user.add_roles(role)
            await ctx.send(f"{member}님이 뮤트당했습니다\n본 기능은 시험중이며 역할설정은 관리자가 해야됩니다")
        else:
            await ctx.send("역할관리권한이 없어요")
    except:
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await ctx.guild.create_role(name="Muted")
        await user.add_roles("Muted")
        member = user.name
        await ctx.send(f"{member}님이 뮤트당하였습니다\n본 기능은 시험중이며 역할설정은 관리자가 해야됩니다")
@bot.command()
async def 메일(ctx, mail, *, text):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('discord.dao.bot.0564.hminkoo10@gmail.com', 'orqikrcirwvzrwgv')
    msg = MIMEText(f'{ctx.author} : {text}')
    msg['Subject'] = f'안녕하세요 디스코드 디노봇입니다 {ctx.author}님이 메일을 전해달라고 하네요'
    s.sendmail("discord.dao.bot.0564.hminkoo10@gmail.com", f"{mail}\n위 메시지는 디스코드에서 디노가 보낸 메시지 입니다", msg.as_string())
    s.quit()
    await ctx.send(f"{mail}님 한테 {text}라고 {ctx.author.mention}님이 메일을 전달했어요!")
@bot.command()
async def color(ctx, red, green, blue):
    nextmode = 0
    colorfind = red.isdecimal()
    if colorfind == True:
        if int(red) > -1 and int(red) < 256:
            nextmode = 1
        else: await ctx.send("값이 너무 크거나 작습니다. 0부터 255 사이의 수를 입력하세요.")
    else: await ctx.send("올바르지 않은 값입니다. 0부터 255 사이의 수를 입력하세요.")
    if nextmode == 1:
        colorfind = green.isdecimal()
        if colorfind == True:
            if int(green) > -1 and int(green) < 256:
                nextmode = 2
            else: await ctx.send("값이 너무 크거나 작습니다. 0부터 255 사이의 수를 입력하세요.")
        else: await ctx.send("올바르지 않은 값입니다. 0부터 255 사이의 수를 입력하세요.")
    if nextmode == 2:
        colorfind = blue.isdecimal()
        if colorfind == True:
            if int(blue) > -1 and int(blue) < 256:
                nextmode = 3
                await ctx.send("출력중...")
            else: await ctx.send("값이 너무 크거나 작습니다. 0부터 255 사이의 수를 입력하세요.")
        else: await ctx.send("올바르지 않은 값입니다. 0부터 255 사이의 수를 입력하세요.")
    hexred = hex(int(red))
    hexgreen = hex(int(green))
    hexblue = hex(int(blue))
    if len(hexred) == 3: hexred = (str("0x0") + str(hexred[2]))
    if len(hexgreen) == 3: hexgreen = (str("0x0") + str(hexgreen[2]))
    if len(hexblue) == 3: hexred = (str("0x0") + str(hexblue[2]))
    if nextmode == 3:
        hexcolor = (str("#")+ str(hexred[2:].upper()) + str(hexgreen[2:].upper()) + str(hexblue[2:].upper()))
        hexcolor2 = (str("0x")+ str(hexred[2:].upper()) + str(hexgreen[2:].upper()) + str(hexblue[2:].upper()))
    embed = discord.Embed(color=int(hexcolor2, base=16), title=hexcolor, description = None)    
    await ctx.send(embed=embed)
@bot.command()
async def 구글링(ctx, *, text):
    url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={text}'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all(class_='sh_blog_title')

    for i in title:
        await ctx.send(i.attrs['title'])
        await ctx.send(i.attrs['href'])
@bot.command()
async def eval_(ctx, *, cmd):
    if str(ctx.author.id) in admin:
        try:
            fn_name = "_eval_expr"

            cmd = cmd.strip("` ")

    # add a layer of indentation
            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    # wrap in async def body
            body = f"async def {fn_name}():\n{cmd}"

            parsed = ast.parse(body)
            body = parsed.body[0].body

            insert_returns(body)

            env = {
                'bot': ctx.bot,
                'discord': discord,
                'commands': commands,
                'ctx': ctx,
                '__import__': __import__
            }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)

            result = (await eval(f"{fn_name}()", env))
            await ctx.send(result)
        except Exception as ex:
            await ctx.send(f'오류발생!\n에러내용:{str(ex)}')
@bot.command()
async def 수정(ctx, one, two, *, three):
    edit = await ctx.send(one)
    await asyncio.sleep(int(f"{two}"))
    await edit.edit(content=three)
@bot.command()
async def on_command_error(ctx, error):
    with Exception as exi:
        ex = exi
        await ctx.send(f'에러내용: {str(ex)}')
@bot.command(name="exec")
async def exec_(ctx, *, code):
    if str(ctx.author.id) in admin:
        embed = discord.Embed(title="execing... <a:loadding:726965248762052708>", color=0xff0000)
        zzzzz = await ctx.send(embed=embed)
        b = os.system(code)
        if b == 0:
            a = subprocess.check_output(code, shell=True)
            bbb = a.decode('EUC-KR', 'backslashreplace')
            embed = discord.Embed(title=f'정상동작 <a:okay:726967334861799514>', color = 0x0000ff, description = f'실행코드\n```cmd\n{code}\n```\n\n실행값\n```cmd\n{bbb}\n```')
            await zzzzz.edit(embed = embed)
        else:
            await ctx.send(f'```diff\n-ERROR!!-\n```')
            sss = subprocess.check_output(code, shell=True)
            await ctx.send(f"오류코드:\n```cmd\n{sss}\n```")
@bot.command()
async def 번역(ctx, lano, lant, *, text):
    translator = Translator()
    result = translator.translate(text=text, src=lano, dest=lant)
    await ctx.send(embed=discord.Embed(title=f'{text} ---> {result.text}', color = 0x3498db))
@bot.command()
async def 업타임text(self, ctx):
    import base64, datetime
    from bs4 import BeautifulSoup
    from urllib import parse
    import time, random, json
    from run import START
    from tools.requests import reqjson
    import psutil, cpuinfo
    uptime = round(time.time() - START)
    if uptime >= 86400:
        ut1 = uptime // 86400
        ut2 = uptime % 86400
        ut3 = ut2 // 3600
        ut4 = ut2 % 3600
        ut5 = ut4 // 60
        ut6 = ut4 % 60
        await ctx.send(f'{ut1}일 {ut3}시간 {ut5}분 {ut6}초 동안 작동됨')
    elif uptime >= 3600:
        ut1 = uptime // 3600
        ut2 = uptime % 3600
        ut3 = ut2 // 60
        ut4 = ut2 % 60
        await ctx.send(f'{ut1}시간 {ut3}분 {ut4}초 동안 작동됨')
    elif uptime >= 60:
        ut1 = uptime // 60
        ut2 = uptime % 60
        await ctx.send(f'{ut1}분 {ut2}초 동안 작동됨')
    elif uptime < 60:
        await ctx.send(f'{uptime}초 동안 작동됨')
@bot.command()
async def 업타임즈(ctx):
    if str(ctx.author.id) in admin:
        embed = discord.Embed(title="checking... <a:loadding:726965248762052708>", color=0xff0000)
        zzzzz = await ctx.send(embed=embed)
        b = os.system('uptime')
        if b == 0:
            a = subprocess.check_output(code, shell=True)
            bbb = a.decode('EUC-KR', 'backslashreplace')
            embed = discord.Embed(title=f'정상동작 <a:okay:726967334861799514>', color = 0x0000ff, description = f'실행명령어\n```cmd\nuptime\n```\n\n실행값\n```cmd\n{bbb}\n```')
            await zzzzz.edit(embed = embed)
        else:
            await ctx.send(f'```diff\n-ERROR!!-\n```')
            sss = subprocess.check_output(code, shell=True)
            await ctx.send(f"오류코드:\n```cmd\n{sss}\n```")
class reaction():
    @bot.listen()        
    async def on_reaction_add(reaction, user):
        global aa
        aaa = reaction.emoji
        aa = aaa
        print(aa)
    @bot.command()
    async def 이모지(ctx):
        try:
            await ctx.send(aa)
        except:
            pass
@bot.command()
async def 하트(ctx, user:discord.Member):
    info = await dbkrpy.CheckVote.get_response("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzAwNzI5NjQ3Njc0MTY0MyIsImlhdCI6MTU5MTEwNDk5MywiZXhwIjoxNjIyNjYyNTkzfQ.DusY04FtN-Gry0H9WP-pnLFqWkTg1TuKAyM9fzklDJedqjKk4VIpgk6SC70p1xZfQ_e08kOE_sGS-Vd5alI0U3JO3a_l2VIGZFAno2f79jU4ZRTbLKKKCEhY8eLGQ__rAawAbV8vgXrS0HWtM3fQEE23ud7DriLJAuRjn9Cgvjg", user.id)
    dbkr = dbkrpy.CheckVote(info)
    await ctx.channel.send(dbkr.check)
@bot.listen()
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 입장',
            description=f'{member.mention}님이 {member.guild}에 들어오셨습니다.\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00f000
        )
        embed.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(syschannel).send(embed=embed)
    except:
        return None

@bot.listen
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 퇴장',
            description=f'{member.mention}님이{member.guild}에 퇴장 했습니다.\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(syschannel).send(embed=embed)
    except:
        return None
@bot.listen()
async def on_guild_join(guild):
    await guild.owner.send(f'`{bot.user.name}`를 {guild.name}에 초대해주셔서 감사드립니다!\n앞으로 {bot.user.name}는 더 발전하겠습니다 \n https://koreanbots.dev/bots/713007296476741643 여기서 하트추가를 눌러주세요!')
@bot.command()
async def 전체공지(ctx, *, msg):
    for guild in bot.guilds:
      try:
        await guild.channels[0].send(msg)
        print("성공")
      except:
        print("실패..")
@bot.listen()
async def on_message(message):
    if message.content.startswith("디노야 "):
                pingpongurl = "https://builder.pingpong.us/api/builder/5ea0f0cbe4b0e921afb16f6d/integration/v0.2/custom"
                pingpongauth = "Basic a2V5OjFhMzJlOGQxM2U3MWM2YTMyYWUwNjkyZDZkOTczNjhj" 
                msg = message.content[4:]
                header = {
                     'Authorization': pingpongauth,
                    'Content-Type': 'application/json'
                }
                param = {
                    'request': {
                        'query': msg
                    }
                }
                async with aiohttp.ClientSession(headers=header) as session:
                    async with session.post(pingpongurl+f'/{message.author.id}', json=param) as res:
                        data = await res.json()
                        assert 'response' in data
                        assert 'replies' in data['response']
                        for reply in data['response']['replies']:
                            if 'text' in reply:
                                await message.channel.send(reply['text'])
@bot.listen()
async def on_message(message):
    if message.content.startswith(',전체 임베드 공지'):
                if str(message.author.id) != '657773087571574784':
                    await message.channel.send('나 해킹해봐', '관리자 기능')
                    return None
                import datetime
                msg=message.content[11:]
                now=datetime.datetime.now()
                embed=discord.Embed(
                    title=msg.split('/')[0],
                    description=msg.split('/')[1],
                    colour=0xff00
                ).set_footer(icon_url=message.author.avatar_url, text=f' {str(message.author.display_name)} - 인증됨 | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                for i in bot.guilds:
                    arr=[0]
                    alla=False
                    flag=True
                    z=0
                    for j in i.channels:
                        arr.append(j.id)
                        z+=1
                        if '📢봇_공지' in j.name or '봇-공지' in j.name or '봇-공지사항' in j.name or '공지-봇' in j.name or '봇_공지' in j.name or '봇공지' in j.name:
                            if str(j.type)=='text':
                                try:
                                    await j.send(embed=embed)
                                    alla=True
                                except:
                                    pass
                                break
                    if alla==False:
                        try:
                            chan=i.channels[1]
                        except:
                            pass
                        if str(chan.type)=='text':
                            try:
                                await chan.send(embed=embed)
                            except:
                                pass
                await message.channel.send('공지 전송을 완료했습니다')
@bot.command()
async def 슬로우모드(ctx, edittime):
    if ctx.author.guild_permissions.manage_channels:
        await ctx.channel.edit(slowmode_delay=int(edittime))
        await ctx.send(f"슬로우모드를 {edittime}으로 지정했어요!")
    else:
        await ctx.send("관리자권한이 없어요!")
#@bot.command()
@dao.command()
async def 테스팅(ctx):
    await ctx.send('테스팅')
@bot.command()
async def 내보내기(ctx, *, file):
    if str(ctx.author.id) in admin:
        await ctx.send(f"{file}을 내보내는 중입니다!")
        try:
            await ctx.send(file=discord.File(f'{file}'))
        except:
            await ctx.send("파일이 없는거 같은데여...")
@bot.command()
async def 파일생성(ctx, filee, *, text):
    if str(ctx.author.id) in admin:
        await ctx.send(f"{filee}을 생성하는 중입니다!")
        try:
            file = open(f"{filee}", "w+", encoding='utf-8-sig')
            file.write(f'{text}')
            file.close
        except:
            await ctx.send("알수없는 오류로 파일을 생성하지 못했어요...")
        try:
            await ctx.send(file=discord.File(f'{filee}'))
        except:
            await ctx.send("알수없는 오류로 파일을 못 내보냈어요...")
@bot.listen()
async def on_message(message):
    if message.content.startswith(',gif'): #명령어
        if gif_response(message.content[5:]) != None:
            await message.channel.send('이 기능이 삭제되었습니다(이유:19금)')
        else:
            await message.channel.send('관련 gif를 찾지 못하였습니다.')
@bot.listen()
async def on_message(message):
    if message.content.startswith(",캡챠"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author) + ".png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await bot.wait_for("message", timeout=12.5, check=check)
        except:
            if msg.content == a:
                await message.channel.send("인증이 완료되었어요!")
            elif msg.content != a:
                await message.channel.send("어... 혹시 봇이세여?")
            else:
                await message.channel.send("시관초과입니다!\n||혹시 봇이신가여||")
            return

        if msg.content == a:
            await message.channel.send("인증이 완료되었어요!")
        else:
            await message.channel.send("어... 혹시 봇이세여?\n||오답||")
@bot.command()
async def 돈줘(ctx):
    try:
        with open('data_money_cool.json', 'r') as f:
            jstring = open("data_money_cool.json", "r", encoding='utf-8-sig').read()
            money_cool = json.loads(jstring)
        abcd = int(time.time()) - int(money_cool[str(ctx.author.id)])
        if int(abcd) >= int('1800'):
            money_test = int(random.randint(1000, 2000))
            with open('data_money.json', 'r') as f:
                jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
                money = json.loads(jstring)
            money_money = int(money[str(ctx.author.id)])
            money_money += money_test
            money[str(ctx.author.id)] = money_money
            money_cool[str(ctx.author.id)] = time.time()
            with open("data_money.json", "w+", encoding='utf-8-sig') as f:
                json_string = json.dump(money, f, indent=2, ensure_ascii=False)
            await ctx.send(f"{money_test}원을 지급했습니다!")
            with open("data_money_cool.json", "w+", encoding='utf-8-sig') as f:
                json_string = json.dump(money_cool, f, indent=2, ensure_ascii=False)
        else:
            if str(ctx.author.id) in admin:
                await ctx.send(f"쿨타임이 안지났어요!\n쿨타임 : 30분\n||{abcd}||\n||hint : -1800||")
            else:
                await ctx.send("쿨타임이 안지났어요!\n쿨타임 : 30분")
    except:
        money_test = int(random.randint(1000, 2000))
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        money[str(ctx.author.id)] = money_test
        money_cool[str(ctx.author.id)] = time.time()
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        with open("data_money_cool.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money_cool, f, indent=2, ensure_ascii=False)
        await ctx.send(f"{money_test}원을 지급했습니다!")
@bot.command()
async def 관리자_돈추가(ctx, user: discord.Member, money1):
    if str(ctx.author.id) in admin:
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        money[str(user.id)] += int(money1)
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        await ctx.send(f"{user}님의 돈에서 {money1}원을 추가했어요!")
@bot.command()
async def 관리자_돈설정(ctx, user: discord.Member, money1):
    if str(ctx.author.id) in admin:
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        money[str(user.id)] = int(money1)
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        await ctx.send(f"{user}님의 돈에서 {money1}원으로 설정했어요!")
@bot.command()
async def 관리자_돈빼기(ctx, user: discord.Member, money1):
    if str(ctx.author.id) in admin:
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        money[str(user.id)] -= int(money1)
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        await ctx.send(f"{user}님의 돈에서 {money1}원을 뺏어요!")
@bot.command()
async def 내돈(ctx):
    with open('data_money.json', 'r') as f:
        jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
        money = json.loads(jstring)
    user_money = money[str(ctx.author.id)]
    await ctx.send(f'지금 내 돈은 {user_money}원이예요!')
@bot.command()
async def 훔쳐보기(ctx, user: discord.Member):
    with open('data_money.json', 'r') as f:
        jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
        money = json.loads(jstring)
    user_money = money[str(user.id)]
    await ctx.send(f'지금 {user}님 돈은 {user_money}원이예요!')
@bot.command()
async def 돈전달(ctx, user: discord.Member, money2):
    with open('data_money.json', 'r') as f:
        jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
        money = json.loads(jstring)
    ababb = money[str(ctx.author.id)] - int(money2)
    if ababb <= int('-1'):
        await ctx.send("자기 돈보다 더 큰데요?")
    else:
        if money2 <= 0:
            await ctx.send('1이상의 정수를 입력 해 주세요!')
            return
        money[str(ctx.author.id)] -= int(money2)
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        money[str(user.id)] += int(money2)
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        user_money = money[str(ctx.author.id)]
        await ctx.send(f'{user}님한테 {money2}원을 전달했어요! \n지금 내 돈은 {user_money}원이예요!')
@bot.command()
async def 탈퇴(ctx):
    with open('data_money.json', 'r') as f:
        jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
        money = json.loads(jstring)
    try:
        del money[str(ctx.author.id)]
    except:
        pass
    with open("data_money.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(money, f, indent=2, ensure_ascii=False)
    with open('data_money_cool.json', 'r') as f:
        jstring = open("data_money_cool.json", "r", encoding='utf-8-sig').read()
        money_cool = json.loads(jstring)
    try:
        del money_cool[str(ctx.author.id)]
    except:
        pass
    with open("data_money_cool.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(money_cool, f, indent=2, ensure_ascii=False)
    with open('data_money_command_1.json', 'r') as f:
        jstring = open("data_money_command_1.json", "r", encoding='utf-8-sig').read()
        money_command_1 = json.loads(jstring)
    try:
        del money_command_1[str(ctx.author.id)]
    except:
        pass
    write('data_money_command_1', money_command_1)
    with open('data_money_command_2', 'r') as f:
        jstring = open("data_money_command_2.json", "r", encoding='utf-8-sig').read()
        money_command_2 = json.loads(jstring)
    try:
        del money_command_2[str(ctx.author.id)]
    except:
        pass
    write('data_money_command_2', money_command_2)
    await ctx.send("탈퇴가 완료되었어요!")
@bot.command()
async def 구매(ctx, item_name):
    with open('data_money.json', 'r') as f:
        jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
        money = json.loads(jstring)
    with open('data_money_command_1.json', 'r') as f:
        jstring = open("data_money_command_1.json", "r", encoding='utf-8-sig').read()
        money_command_1 = json.loads(jstring)
    with open('data_money_command_2.json', 'r') as f:
        jstring = open("data_money_command_2.json", "r", encoding='utf-8-sig').read()
        money_command_2 = json.loads(jstring)
    try:
        ababb = money[str(ctx.author.id)] - int(item_money[str(item_name)])
    except:
        await ctx.send(f'{item_name}이란 아이템이 없거나 디노의 돈 기능을 1번도 사용하지 않았어요!\n,돈줘 를 입력 해 보세요!')
    if ababb <= int('-1'):
        await ctx.send("이런... 돈을 더 벌고 와보세요!")
    else:
        print(money[str(ctx.author.id)])
        money_test_2 = int(money[str(ctx.author.id)]) - int(item_money[item_name])
        print(money_test_2)
        money[str(ctx.author.id)] = money_test_2
        try:
            if item_name == '증가벽돌':
                money_command_1[str(ctx.author.id)] += int('1')
            elif item_name == '복구시스템':
                money_command_2[str(ctx.author.id)] += int('1')
        except:
            if item_name == '증가벽돌':
                money_command_1[str(ctx.author.id)] = int('1')
            elif item_name == '복구시스템':
                money_command_2[str(ctx.author.id)] = int('1')
        with open("data_money_command_1.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money_command_1, f, indent=2, ensure_ascii=False)
        with open("data_money_command_2.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money_command_2, f, indent=2, ensure_ascii=False)
        with open("data_money.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(money, f, indent=2, ensure_ascii=False)
        print(money[str(ctx.author.id)])
        await ctx.send("아이템이 추가됬어요!")
@bot.command()
async def 짤추가(ctx, name1, url):
    with open('data_command_1.json', 'r') as f:
        jstring = open("data_command_1.json", "r", encoding='utf-8-sig').read()
        command_1 = json.loads(jstring)
    command_1[name1] = f'{url}'
    with open("data_command_1.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(command_1, f, indent=2, ensure_ascii=False)
    await ctx.send("완료")
@bot.command()
async def 짤(ctx, name):
    with open('data_command_1.json', 'r') as f:
        jstring = open("data_command_1.json", "r", encoding='utf-8-sig').read()
        command_1 = json.loads(jstring)
    embed = discord.Embed(title='짤', color=0x2ecc71)
    try:
        urle = command_1[name]
    except:
        await ctx.send(f"{name}이란 짤을 찾을 수 없어요!")
    embed.set_image(url=urle)
    await ctx.send(embed=embed)
@bot.command()
async def 사용(ctx, item_name):
    if item_name == '증가벽돌':
        with open('data_money_command_1.json', 'r') as f:
            jstring = open("data_money_command_1.json", "r", encoding='utf-8-sig').read()
            money_command_1 = json.loads(jstring)
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        if money_command_1[str(ctx.author.id)] >= int('1'):
            random_money_1 = [1,2,3,4,5,6]
            random_money = random.choice(random_money_1)
            if random_money == 2 or random_money == 4 or random_money == 6:
                money_command_1[str(ctx.author.id)] -= int('1')
                money[str(ctx.author.id)] += money[str(ctx.author.id)]
                await ctx.send(embed=discord.Embed(title=f'와! 강화에 성공했어요!\n돈이 2배로 늘어났습니다!\n현재 내 돈은 {money[str(ctx.author.id)]}원 이예요!', color=0x2ecc71))
                with open("data_money_command_1.json", "w+", encoding='utf-8-sig') as f:
                    json_string = json.dump(money_command_1, f, indent=2, ensure_ascii=False)
                with open("data_money.json", "w+", encoding='utf-8-sig') as f:
                    json_string = json.dump(money, f, indent=2, ensure_ascii=False)
            else:
                money_command_1[str(ctx.author.id)] -= int('1')
                asdf = money[str(ctx.author.id)] / 2
                money[str(ctx.author.id)] -= int(asdf)
                with open("data_money_command_1.json", "w+", encoding='utf-8-sig') as f:
                    json_string = json.dump(money_command_1, f, indent=2, ensure_ascii=False)
                with open("data_money.json", "w+", encoding='utf-8-sig') as f:
                    json_string = json.dump(money, f, indent=2, ensure_ascii=False)
                await ctx.send(embed=discord.Embed(title=f'이런... 강화에 실패했어요ㅜㅜ\n내 돈에서 반이 줄어들었어요...\n현재 내 돈은 {money[str(ctx.author.id)]}원 이예요', color=0xff0000))
        else:
            await ctx.send("증가벽돌이 없는데 찾아오면 안돼죠!")
    elif item_name == '복구시스템':
        with open('data_money_command_2.json', 'r') as f:
            jstring = open("data_money_command_2.json", "r", encoding='utf-8-sig').read()
            money_command_2 = json.loads(jstring)
        with open('data_money.json', 'r') as f:
            jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
            money = json.loads(jstring)
        if money_command_2[str(ctx.author.id)] <= int('1'):
            d = money_command_2[str(ctx.author.id)] - int('1')
            if d <= int('-1'):
                await ctx.send("아이템이 없는데여ㅡㅡ;")
            else:
                money_command_2[str(ctx.author.id)] -= int('1')
                with open('data_money_command_1.json', 'r') as f:
                    jstring = open("data_money_command_1.json", "r", encoding='utf-8-sig').read()
                    money_command_1 = json.loads(jstring)
                try:
                    print(money_command_1[str(ctx.author.id)])
                except:
                    money_command_1[str(ctx.author.id)] = 0.0
                ss = {'id': ctx.author.id, 'money': money[str(ctx.author.id)], 'money_command_1': money_command_1[str(ctx.author.id)]}
                s = json.dumps(ss)
                b = s.encode("UTF-8")
                e = base64.b64encode(b)
                s1 = e.decode("UTF-8")
                with open("data_money_command_2.json", "w+", encoding='utf-8-sig') as f:
                    json_string = json.dump(money_command_2, f, indent=2, ensure_ascii=False)
                await ctx.channel.send(embed=discord.Embed(title=f'복구 암호가 생성되었어요!\n복구 암호는 {s1}이예요!\n정보를 잃었을때 ,복구 {s1}이라고 해 보세요!', color=0x2ecc71))
    else:
        await ctx.send(f'{item_name}이란 아이템이 없는데요?')
@bot.command()
async def sms(ctx, number, message2):
    touser = number[1:]
    account_sid = 'ACcb3b7fe7ece7b9706366583008deb73c'
    auth_token = '58420af649801bf7b1d55fc428df9f1b'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=f'{ctx.author}:{message2}',
                     from_='+13867533935',
                     to=f'+82{touser}'
                 )
    await ctx.send("메시지가 성공적으로 보내졌어요!")
@bot.command()
async def 테스트1(ctx):
    ss = {'money_command_1': money_command_1[str(ctx.author.id)], 'money': money[str(ctx.author.id)]}
    s = str(ss)
    print(s)
    b = s.encode("UTF-8")
    e = base64.b64encode(b)
    s1 = e.decode("UTF-8")
    await ctx.send(s1)
@bot.command()
async def 테스트2(ctx, *, s):
    #if int(ctx.author.id) in admin:
        b1 = s.encode("UTF-8")
        d = base64.b64decode(b1)
        s2 = d.decode("UTF-8")
        await ctx.channel.send(s2)
@bot.command()
async def 랭킹(ctx):
    with open('data_money.json', 'r') as f:
        jstring = open("data_money.json", "r", encoding='utf-8-sig').read()
    money = json.loads(jstring)
    embed = discord.Embed(title="랭킹\n\n\n", color=0xff0000)
    rank = dict(sorted(money.items(),key=operator.itemgetter(1), reverse=True))
    print(rank)
    rankkey = list(rank.keys())
    print(rankkey)
    rankvalue = list(rank.values())
    print(rankvalue)
    rankoutput = ""
    for d in range(min(len(rankkey), 10)):
        rankoutput = f'돈 : {rankvalue[d]}'
        embed.add_field(name=f"{d + 1}등 : {bot.get_user(int(rankkey[d]))}\n", value=f"{rankoutput}", inline=False)
    for d in range(len(rankkey)):
        print(type(rankkey[d]))
        print(type(ctx.author.id))
        if ctx.author.id == int(rankkey[d]):
            rankoutput = f'돈 : {rankvalue[d]}'
            embed.add_field(name=f"==============", value=f"\n\n\n{d + 1}등 : {bot.get_user(int(rankkey[d]))}\n돈 : {rankvalue[d]}", inline=False)        
    await ctx.channel.send(embed=embed)
@bot.command()
async def 복구(ctx, *, s):
    try:
        b1 = s.encode("UTF-8")
        d = base64.b64decode(b1)
        s2 = d.decode("UTF-8")
        print(s2, type(s2))
        information = eval(s2)
        if information['id'] == int(ctx.author.id):
            money[str(ctx.author.id)] = information['money']
            money_command_1[str(ctx.author.id)] = information['money_command_1']
            write('data_money', money)
            write('data_money_command_1', money_command_1)
            await ctx.send("복구가 완료되었어요!")
        else:
            await ctx.send("코드 발급자가 아닙니다")
    except:
        await ctx.send("올바르지 않는 코드입니다")
@bot.command()
async def 운세(ctx,*,star):
    response = requests.get('https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=운세 '+star)
    readerhtml = response.text
    soup = BeautifulSoup(readerhtml, 'lxml')
    luck = soup.find("p",{"class": "text _cs_fortune_text"}).get_text()
    luembed = discord.Embed(color=0x192131, title=ctx.author.name+"님의 운세" , description=luck)
    await ctx.channel.send(embed = luembed)
@bot.command(pass_context=True)
async def invite(ctx):
    invitelinknew = await ctx.message.channel.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color=0xf41af4)
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Discord server invited link.")
    await ctx.send(embed=embedMsg)
@bot.command()
async def 도박(ctx, a, b):
    random = random.randint(1, 100)

@bot.command()
async def 사진편집(ctx, urla, pill, *, text):
    url = urla
    response = requests.get(url, stream=True)
    with open(f'{ctx.author.id}.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file) 
    img = Image.open(f"{ctx.author.id}.jpg")
    print(type(img.size))
    draw = ImageDraw.Draw(img)
    #font = ImageFont.load("arial.pil")
    font_size = int(22)
    font = ImageFont.truetype('H2GTRM.TTF', font_size)
    w,h = font.getsize(text)
    W = img.size[0]
    draw.text((int((W-w)/2), img.size[1]-h*2),text,fill=pill,font=font)
    img.save(f'{ctx.author.id}.png')
    await ctx.send(file=discord.File(f'{ctx.author.id}.png'))
@bot.listen()
async def on_message(message):
    if message.content == '<@!713007296476741643>':
        await message.channel.send('''
안녕하세요! 전 디봇이예요!
개발자는 hminkoo10#2879 님이시고, 프리픽스는 , 도움 명령어는 ,help 와 ,도움 이예요!
명령어가 서로 다르니 조심하세요!!
''')
@bot.command()
async def 다운로드(ctx, url, pjm):
    response = requests.get(url, stream=True)
    with open(f'{ctx.author.id}.{pjm}', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    await ctx.send(file=discord.File(f'{ctx.author.id}.{pjm}'))
@bot.command()
async def 디엠공지(ctx,msg,pass_context=True):
    getuser = []
    for i in bot.users:
        await bot.wait_until_ready()
        getuser.append(bot.get_channel(int(i)))
    for e in getuser:
        print(e)
        await ctx.send("전송시도중")
        try:
            embed = discord.Embed(title="디노봇 공지",color=0x9b59b6,description=None) #임베드 변수 지정
            embed.add_field(name="공지내용\n=================", value=(msg), inline=False) #field add
            embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)                    
            await e.send(embed=embed)
            await ctx.send("성공")
        except:
            await ctx.send("실패")
@bot.command()
async def 디엠공지테스트(ctx, pass_context=True):
    for i in bot.users:
        a = i.id
        print(a)
        print(type(a))
        await bot.get_user(a).send('. 마지막 테스트 .')
@bot.command()
async def 개발자등록(ctx, *, pvcy):
    global privacy
    if pvcy == privacy:
        msg = await ctx.send('<@657773087571574784>님의 동의가 필요합니다.')
        await msg.add_reaction('✅')
        await msg.add_reaction('🚫')
        def check(reaction, user):
            return reaction.emoji == '✅' and user.id == 657773087571574784
        try:
            await bot.wait_for('reaction_add',timeout=300,check=check)
        except asyncio.TimeoutError:
            await ctx.send('개발자가 동의를 안해주셨어요')
        else:
            admin.append(f'{ctx.author.id}')
            PRM.append(f'{ctx.author.id}')
            privacy = PVCY()
            await ctx.send('암호가 일치합니다. 개발자로 등록되셨습니다.')
    else:
        await ctx.send('암호가 일치하지 않습니다')
@bot.command()
async def 개발자암호(ctx):
    global privacy
    if ctx.author.id == 657773087571574784:
        await ctx.author.send(f'인증 암호는 {privacy} 입니다.')
@bot.command()
async def 암호초기화(ctx):
    global privacy
    if ctx.author.id == 657773087571574784:
        privacy = PVCY()
        await ctx.send('완료')
@bot.command()
async def 개발자초기화(ctx):
    if ctx.author.id == 657773087571574784:
        admin.clear()
        PRM.clear()
        await ctx.send('완료')

@bot.command()
async def speech(ctx, *, msg):
    import re
    pkor = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    peng = re.compile('[a-z|A-Z]')
    mkor = pkor.search(msg)
    meng = peng.search(msg)
    if mkor and meng:
        tts = gTTS(text=msg, slow=False, lang='en')
    elif mkor and not meng:
        tts = gTTS(text=msg, slow=False, lang='ko')
    else:
        tts = gTTS(text=msg, slow=False, lang='en')
    tts.save(f'{ctx.author.id}.mp3')
    await ctx.send(file=discord.File(f'{ctx.author.id}.mp3'))
    if ctx.author.voice.channel == None:
        channel = ctx.author.voice.channel
    if ctx.voice_client is not None:
        vc = await ctx.voice_client.move_to(channel)
    else:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(f'{ctx.author.id}.mp3'), after=lambda e: print('done', e))
    while (vc.is_playing()==1):
        pass
    await ctx.voice_client.disconnect()
    os.remove(f'{ctx.author.id}.mp3')
@bot.command()
async def 쿨타임(ctx):
    with open('data_money_cool.json', 'r') as f:
        jstring = open("data_money_cool.json", "r", encoding='utf-8-sig').read()
        money_cool = json.loads(jstring)
    a = int(time.time()) - int(money_cool[str(ctx.author.id)])
    b = int(a) // 60
    await ctx.send(f'지금 내 쿨타임이 {30 - int(b)}분 남았어요!')
@bot.command()
async def 홍보(ctx):
    with open('data_server_cool.json', 'r') as f:
        jstring = open("data_server_cool.json", "r", encoding='utf-8-sig').read()
        server_cool = json.loads(jstring)
    with open('data_server_invite.json', 'r') as f:
        jstring = open("data_server_invite.json", "r", encoding='utf-8-sig').read()
        server_invite = json.loads(jstring)
    if ctx.guild.owner.id != ctx.author.id:
        await ctx.send(f'{ctx.guild.owner}님이 아닙니다')
        return
    try:
        e = server_cool[str(ctx.guild.id)]
        print(e)
    except:
        server_cool[str(ctx.guild.id)] = 0
    a = int(time.time()) - int(server_cool[str(ctx.guild.id)])
    print(a)
    if int(a) >= int(86400):
        server_cool[str(ctx.guild.id)] = int(time.time())
        invitelinknew = await ctx.message.channel.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 10)
        embed = discord.Embed(title=f'{ctx.guild.name}서버에 초대합니다!',color=discord.Color.blue())
        embed.add_field(name=f"{ctx.guild.name}서버 초대링크", value=invitelinknew)
        embed.set_footer(text='홍보를 비허용하실땐 ,홍보거부 를 하시고, 허용하실땐 ,홍보허용 을 입력 해 주세요', icon_url=ctx.guild.icon_url)
        for i in bot.guilds:
            for j in i.channels:
                if j.name == '홍보':
                    if str(j.type) == 'text':
                        try:
                            print(server_invite[str(i.id)])
                            print(i.id)
                            e = server_invite[str(i.id)]
                            print(e)
                        except:
                            server_invite[str(i.id)] = 0
                        if server_invite[str(i.id)] == 0:
                            await j.send(embed=embed)
                        else:
                            pass
                else:
                    pass
    else:
        await ctx.send('앗! 쿨타임이 안지났어요! 내일 다시 시도 해 보세요!')
    with open("data_server_cool.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(server_cool, f, indent=2, ensure_ascii=False)
    with open("data_server_invite.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(server_invite, f, indent=2, ensure_ascii=False)
@bot.command()
async def 홍보허용(ctx):
    if ctx.guild.owner.id == ctx.author.id:
        with open('data_server_invite.json', 'r') as f:
            jstring = open("data_server_invite.json", "r", encoding='utf-8-sig').read()
            server_invite = json.loads(jstring)
        server_invite[str(ctx.guild.id)] = 0
        write('data_server_invite',server_invite)
        await ctx.send('완료!')
    else:
        await ctx.send('서버소유자가 아닙니다')
@bot.command()
async def 홍보거부(ctx):
    if ctx.guild.owner.id == ctx.author.id:
        with open('data_server_invite.json', 'r') as f:
            jstring = open("data_server_invite.json", "r", encoding='utf-8-sig').read()
            server_invite = json.loads(jstring)
        server_invite[str(ctx.guild.id)] = 1
        write('data_server_invite',server_invite)
        await ctx.send('완료!')
    else:
        await ctx.send('서버소유자가 아닙니다')
@bot.command()
async def 업타임(ctx):
    nowtime = uptimes.uptimes.uptimes()
    odays = nowtime.split(' ')[0]
    ohours = nowtime.split(' ')[2]
    omin = nowtime.split(' ')[4]
    osec = nowtime.split(' ')[6]

    days = odays[2:len(odays)-2]
    hours = ohours[2:len(ohours)-2]
    minutes = omin[2:len(omin)-2]
    seconds = osec[2:len(osec)-2]
    await ctx.send(f'저는 {days}일, {hours}시간 {minutes}분 {seconds}초 동안 작동됐어요!')
@bot.command()
async def 프리픽스(ctx):
    await ctx.send(',접두사확인 으로 이 서버에 접두사를 확인 가능하고, ,접두사변경(프리픽스 ,확정)(개인 접두사이니 다른 사람의 기본 접두사는 , 입니다)')
@bot.command(name="접두사변경")
async def _prefix(ctx, new_prefix):
    prefixList[str(ctx.author.id)] = new_prefix
    write('prefixes',prefixList)
    await ctx.send('완료!\n일부 명령어는 적용돼지 않습니다')
@bot.listen()
async def on_message(message):
    if not message.content.startswith(',접두사확인'):
        return
    with open('prefixes.json', 'r') as f:
        jstring = open("prefixes.json", "r", encoding='utf-8-sig').read()
        prefixList = json.loads(jstring)
    await message.channel.send(f'프리픽스는 {prefixList[str(message.author.id)]}')
@bot.listen()
async def on_command_error(ctx,error):
    await ctx.message.add_reaction('<a:pass:760474783606505503>')
    for i in admin:
        if isinstance(error, commands.CommandNotFound):
            return
        invites = await ctx.channel.create_invite(destination = ctx.channel, xkcd = True, max_uses = 100)
        embed = discord.Embed(title='<a:pass:760474783606505503> Command Error', colour=discord.Color.red())
        embed.add_field(name='에러', value=error)
        embed.add_field(name='서버', value=ctx.guild)
        embed.add_field(name='채널', value=ctx.channel)
        embed.add_field(name='초대링크', value=invites)
        embed.add_field(name='유저', value=ctx.author)
        embed.add_field(name='사용한 메시지', value=ctx.message.clean_content)
        embed.timestamp = datetime.datetime.utcnow()
        await bot.get_user(int(i)).send(embed=embed)
@bot.command()
async def ascii(ctx, *, text):
    ascii_banner = pyfiglet.figlet_format(text)
    await ctx.send(f'```\n{ascii_banner}\n```')
@bot.command()
async def 사용량(ctx):
    
    import matplotlib.pyplot as plt
    jstring = open("typinged.json", "r", encoding='utf-8-sig').read()
    typed = json.loads(jstring)
    a = list(typed.keys())
    b = list(typed.values())
    if len(a) >= 6:
        c = True
        e = a.copy()
        while c:
            d = str(e[0])
            del typed[str(d)]
            if len(e) == 6:
                c = False
                break
            else:
                del e[0]
        write('typinged',typed)
    a = list(typed.keys())
    b = list(typed.values())
    plt.plot(a,b)
    plt.savefig(f'{ctx.author.id}.png', dpi=300)
    plt.clf()
    await ctx.send(file=discord.File(f'{ctx.author.id}.png'))
@bot.listen()
async def on_message(message):
    import datetime
    jstring = open("typinged.json", "r", encoding='utf-8-sig').read()
    typed = json.loads(jstring)
    if message.content.startswith(prefixList.get(str(message.author.id), ",")):
        jstring = open("typinged.json", "r", encoding='utf-8-sig').read()
        typed = json.loads(jstring)
        try:
            typed[str(datetime.date.today())] += 1
        except:
            await message.author.send('오늘의 첫 사용자 입니다!')
            typed[str(datetime.date.today())] = 1
        write('typinged',typed)
@bot.command()
async def 고정(ctx,message):
    await bot.get_message(message).pin()
bot.run(token)

