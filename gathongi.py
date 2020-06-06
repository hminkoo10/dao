#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
import time
import openpyxl
from discord.ext import commands
import random
import dbkrpy
import turtle
import turtle as t
import os
import asyncio
import datetime

notice = list()
tkdyd = []
check = []
bot = commands.Bot(command_prefix=('개똥아 '))
PRM = ['657773087571574784', '653106214288228357', '694406375228440606']
token = "NzAyMTI3ODk1MDc3ODQ3MDkx.XtTS_A.ZVg8du0uLo1fOXClC8jQ1Nifdy4"

@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}!')
    print('정상작동중...')
    messages = ["명의 사용자와 함께", "접두어 = 개똥아", "여러 가지 말", "개의 서버와 함께"]
    while True:
        if messages[0] == '명의 사용자와 함께':
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"개똥아 도움 | {str(len(bot.users))}명의 사용자와 함께"))
        elif messages[0] == '개의 서버와 함께':
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"개똥아 도움 | {str(len(bot.guilds))}개의 서버와 함께"))
        else:
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="개똥아 도움 | " + messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(3.5)
        if datetime.timedelta(hours=1):
            check = []
@bot.command()
async def 안녕(ctx):
    await ctx.channel.send((ctx.author.mention) + '님 안녕하세요!:hugging: :hugging_face:')
    await ctx.channel.send(':hugging_face:')
@bot.command()
async def 건의링크(ctx):
    await ctx.channel.send('https://discord.gg/PKGMwSB')
@bot.command()
async def 실룩실룩(ctx):
    await ctx.channel.send('https://cdn.discordapp.com/attachments/705635075005349908/709709012383301643/dummy.gif')
@bot.command()
async def 사랑(ctx):
    await ctx.channel.send('https://cdn.discordapp.com/attachments/709700588438421514/709707910116147211/14cca446acaa8b37.gif')
@bot.command()
async def 흙(ctx):
    await ctx.channel.send('https://cdn.discordapp.com/attachments/705635075005349908/709708134079528970/341fc71ee0340864.gif')
@bot.command()
async def 도움전달(ctx, user:discord.Member):
    await user.send('hminkoo10#3679님한테 건의하고 물어보세요!')
    await user.send('이 봇은 그냥 대화봇이예요!')
    embed = discord.Embed(title="도움말",color=0xe67e22,description="서버 관리봇, 개똥이.접두어:개똥아") #임베드 변수 지정
    embed.add_field(name="건의", value="- ``개똥아 건의``, ``개똥아 건의링크``로 확인", inline=False) #field add
    embed.add_field(name="움직이는 이모티콘", value="- ``개똥아 실룩실룩, 사랑, 흙``으로 확인", inline=False) #field add
    embed.add_field(name="초대링크", value="- ``개똥아 초대링크, 초대코드``로 확인", inline=False) #field add
    embed.add_field(name="보유서버", value="- ``개똥아 보유서버``로 확인", inline=False)#field add
    embed.add_field(name="매시지 2개삭제", value="- ``개똥아 삭제``로 확인", inline=False)
    embed.add_field(name="모두 삭제 (개똥이에게 모든 권한을 줘야함)", value="- ``개똥아 clear``로 확인", inline=False)
    embed.add_field(name="메시지 전달", value="-``개똥아 dm @맨션 내용``으로 확인", inline=False)
    embed.add_field(name="출석체크", value="- ``출석체크, ㅊㅊ``으로 확인 ``출석 리스트``로 확인", inline=False)
    embed.add_field(name="정보", value="- ``개똥아 정보(맨션)``로 확인", inline=False)
    embed.add_field(name="타이머", value="- ``개똥아 타이머 (초) (제목)``로 확인", inline=False)
    embed.add_field(name="개똥이 서포터", value="- ``https://discord.gg/PKGMwSB``", inline=False)
    embed.add_field(name="공지 (only 서버관리자)", value="- ``개똥아 (에브리원)공지 내용``", inline=False)
    embed.set_footer(text=(ctx.author.name), icon_url=ctx.author.avatar_url)
    await user.send(embed=embed)
    embed = discord.Embed(description = "[개똥이 서포터 <----- 클릭!!](https://discord.com/invite/PKGMwSB)",color=0xe67e22)
    await user.send(embed=embed)
    await ctx.send("DM으로 전송했어요!")
@bot.command()
async def 도움(ctx):
    await ctx.author.send('hminkoo10#3679님한테 건의하고 물어보세요!')
    await ctx.author.send('이 봇은 그냥 대화봇이예요!')
    embed = discord.Embed(title="도움말",color=0xe67e22,description="서버 관리봇, 개똥이.접두어:개똥아") #임베드 변수 지정
    embed.add_field(name="건의", value="- ``개똥아 건의``, ``개똥아 건의링크``로 확인", inline=False) #field add
    embed.add_field(name="움직이는 이모티콘", value="- ``개똥아 실룩실룩, 사랑, 흙``으로 확인", inline=False) #field add
    embed.add_field(name="초대링크", value="- ``개똥아 초대링크, 초대코드``로 확인", inline=False) #field add
    embed.add_field(name="보유서버", value="- ``개똥아 보유서버``로 확인", inline=False)#field add
    embed.add_field(name="매시지 2개삭제", value="- ``개똥아 삭제``로 확인", inline=False)
    embed.add_field(name="모두 삭제 (개똥이에게 모든 권한을 줘야함)", value="- ``개똥아 clear``로 확인", inline=False)
    embed.add_field(name="메시지 전달", value="-``개똥아 dm @맨션 내용``으로 확인", inline=False)
    embed.add_field(name="출석체크", value="- ``출석체크, ㅊㅊ``으로 확인 ``출석 리스트``로 확인", inline=False)
    embed.add_field(name="정보", value="- ``개똥아 정보(맨션)``로 확인", inline=False)
    embed.add_field(name="타이머", value="- ``개똥아 타이머 (초) (제목)``로 확인", inline=False)
    embed.add_field(name="개똥이 서포터", value="- ``https://discord.gg/PKGMwSB``", inline=False)
    embed.add_field(name="공지 (only 서버관리자)", value="- ``개똥아 (에브리원)공지 내용``", inline=False)
    embed.set_footer(text=(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.author.send(embed=embed)
    embed = discord.Embed(description = "[개똥이 서포터 <----- 클릭!!](https://discord.com/invite/PKGMwSB)",color=0xe67e22)
    await ctx.author.send(embed=embed)
    await ctx.send("DM으로 전송했어요!")
@bot.command()
async def 갸우뚱(ctx):
    await ctx.channel.send('***(갸우뚱?)*** 난 크시가 아니지만...')
@bot.command()
async def 빛영자(ctx):
    await ctx.channel.send('```빛영자```님은 저를 엔트리 서버로 초대해주신 좋은 분이세요!!')
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
    await ctx.channel.send('근데... 사랑하면 좋아요즘 주세요! https://koreanbots.dev/bots/702127895077847091')
@bot.command()
async def 초대링크(ctx):
    await ctx.channel.send('https://tenor.com/view/cat-loading-error-angry-fuck-gif-8985245')
    time.sleep(7)
    await ctx.channel.send('https://koreanbots.dev/bots/702127895077847091')
@bot.command()
async def 초대코드(ctx):
    await ctx.channel.send('https://tenor.com/view/cat-loading-error-angry-fuck-gif-8985245')
    time.sleep(7)
    await ctx.channel.send('https://bit.ly/35NUgRp')
@bot.command()
async def 배워(ctx, *, text):
    for guild in bot.guild, member:
        await ctx.send(guilds)
@bot.command()
async def 온라인(ctx):
    await ctx.author.send('await bot.change_presence(status=discord.Status.online)')
@bot.command()
async def 자리비움(ctx):
    await ctx.author.send('await bot.change_presence(status=discord.Status.idle)')
@bot.command()
async def 방해금지(ctx):
    await ctx.author.send('await bot.change_presence(status=discord.Status.dnd)')
@bot.command()
async def 오프라인(ctx):
    await ctx.author.send('await bot.change_presence(status=discord.Status.offline)')
@bot.command()
async def 공지(ctx, *, text):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="@here",color=0x9b59b6,description="공지") #임베드 변수 지정
        embed.add_field(name="made by hminkoo10#6898", value=(text), inline=False) #field add
        embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        if str(ctx.author.id) in PRM:
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(title="@here",color=0x9b59b6,description="공지") #임베드 변수 지정
            embed.add_field(name="made by hminkoo10#6898", value=(text), inline=False) #field add
            embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send('관리자권한이 없습니다. (실행 요구 권한 : admin)')
@bot.command()
async def 전체공지(ctx, *, text):
    if ctx.message.author.id == 657773087571574784:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="@here",color=0x9b59b6,description="공지") #임베드 변수 지정
        embed.add_field(name="made by hminkoo10#6898", value=(text), inline=False) #field add
        embed.set_footer(text=ctx.author.name + "-개똥이 관리자", icon_url=ctx.author.avatar_url)
        await ctx.get_channel.send(embed=embed)
    else:
        await ctx.channel.send('봇 관리자가 아닙니다')
@bot.command()
async def 보유서버(ctx):
    for guild in bot.guilds:
        await ctx.channel.send(guild)
@bot.command()
async def 관리자보유서버(ctx):
    await ctx.channel.send(bot.guilds)
@bot.command()
async def 말해(ctx, *, text):
    await ctx.channel.send(text)
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
@bot.command()
async def 건의(ctx, *, msg):
    print(msg)
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
#       user = await client.wait_for('reaction_add', timeout=7, check=check)  # 반응 추가할때까지 기다리는 코드. timeout=7은 7초 기다리면 타임아웃 오류를 발생시키는걸 의미.
#       except asyncio.TimeoutError:
#           await ctx.channel.send("타임 아웃!")
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
async def dm(ctx, user:discord.Member, *, msg):
    await user.send(ctx.author.mention)
    await user.send(ctx.author)
    await user.send('님이 이렇게 전해달라는군요!')
    await user.send(msg)
    await ctx.channel.send('DM을 보냈어요! 메시지 내용')
    await ctx.channel.send(msg)
#@bot.command()
#async def 가위바위보()
#    await ctx.channel.send('가위 바위 보중에 1개를 입력하세요')
#    async def 가위()
#        
@bot.command()
async def 정상작동확인():
    print(f'로그인 성공: {bot.user.name}!')
    t.forward(1)
    t.left(90)
    t.forward(2)
    t.left(90)
    t.forward(3)
    t.left(90)
    t.forward(4)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(6)
    t.left(90)
    t.forward(7)
    t.left(90)
    t.forward(8)
    t.left(90)
    t.forward(9)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(11)
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(13)
    t.left(90)
    t.forward(14)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(16)
    t.left(90)
    t.forward(17)
    t.left(90)
    t.forward(18)
    t.left(90)
    t.forward(19)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(21)
    t.left(90)
    t.forward(22)
    t.left(90)
    t.forward(23)
    t.left(90)
    t.forward(24)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(26)
    t.left(90)
    t.forward(27)
    t.left(90)
    t.forward(28)
    t.left(90)
    t.forward(29)
    t.left(90)
    t.forward(30)
    print('정상작동중...')
@bot.listen()
async def on_message(message):
    if message.content == "개똥아 빗자루":
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
        if channel in notice:
            await ctx.send("이미 등록됨")
        else:
            notice.append(channel)
            await ctx.send("완료")
    else:
        if ctx.author.guild_permissions.administrator:
            if channel in notice:
                await ctx.send("이미 등록됨")
            else:
                notice.append(channel)
                await ctx.send("완료")
        else:
            await ctx.send("관리자권한이 없습니다")
@bot.command()
async def 공지보내기(ctx, *, msg):
    if ctx.message.author.id == 657773087571574784:
        for i in notice:
            embed = discord.Embed(title="@here",color=0x9b59b6,description="공지") #임베드 변수 지정
            embed.add_field(name="made by hminkoo10#6898", value=(msg), inline=False) #field add
            embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
            await i.send(embed=embed)
    else:
        if ctx.author.guild_permissions.administrator:
            for i in notice:
                embed = discord.Embed(title="@here",color=0x9b59b6,description="공지") #임베드 변수 지정
                embed.add_field(name="made by hminkoo10#6898", value=(msg), inline=False) #field add
                embed.set_footer(text=ctx.author.name + "-인증됨(PRM)", icon_url=ctx.author.avatar_url)
                await i.send(embed=embed)
        else:
            await ctx.channel.send("관리자 권한이 없습니다")
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
async def 킥(ctx, user:discord.Member, *, msg):
    await ctx.guild.kick(user)
@bot.listen()
async def on_message(message):
    if message.content.startswith("개똥아 학습"):
        file = openpyxl.load_workbook("read.xlsx")
        sheet = file.active

@bot.listen()
async def on_message(message):
    if message.content.startswith("개똥아 출첵") or message.content.startswith("개똥아 ㅊㅊ") or message.content.startswith("출석체크"):
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
    if message.content.startswith("개똥아 출석 리스트"):
        finalcheck = "개똥이봇"
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
        os.system("python gathongi.py")
        exit()
#        await ctx.send("모든 모듈을 리로드했어요!")
#        imp.reload(discord)
#        self.bot.reload_extension("gathongi.py")
@bot.listen()
async def on_message(message):
    if message.content.startswith("개정보"):
        date = datatime.datatime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xf1c40f)
        embed = embed.add_field(name="이름", value=message.author.name, inline=True)
        embed = embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed = embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed = embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
@bot.command()
async def 정보(ctx, user:discord.Member):
    a = user.avatar_url
    embed = discord.Embed(description = f"[프로필 원본 보기]({a})", color=0xf1c40f)
    embed.add_field(name=user, value=user.id, inline=False)
    embed.add_field(name="사용자 지정 상태", value=user.activity, inline=False)
    embed.add_field(name="상태", value=user.status, inline=False)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
@bot.command()
async def 역할전달(ctx, user:discord.Member, txt):
    if ctx.author.guild_permissions.administrator:
        b = txt
        role = discord.utils.get(ctx.guild.roles, name=f"{b}")
        await user.add_roles(role)
        await ctx.send("전달 완료!")
    else:
        await ctx.send("관리자권한이 없음")
@bot.command()
async def 역할가져가기(ctx, user:discord.Member, txt):
    if ctx.author.guild_permissions.administrator:
        b = txt
        role = discord.utils.get(ctx.guild.roles, name=f"{b}")
        await user.remove_roles(role)
        await ctx.send("역할을 가져왔어요!")
    else:
        await ctx.send("관리자권한이 없음")
@bot.listen()
async def on_message(message):
    if message.content.startswith("개똥아"):
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
bot.run(token)
