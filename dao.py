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
import datetime as pydatetime

notice = list()
tkdyd = []
check = []
bot = commands.Bot(command_prefix=(','))
PRM = ['657773087571574784','564250827959566359','694406375228440606']
token = "NzEzMDA3Mjk2NDc2NzQxNjQz.Xs5beA.pDkDd1FmNVNjlEc7eAyO8HJS3IQ"
DBKR_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcxMzAwNzI5NjQ3Njc0MTY0MyIsImlhdCI6MTU5MTEwNDk5MywiZXhwIjoxNjIyNjYyNTkzfQ.DusY04FtN-Gry0H9WP-pnLFqWkTg1TuKAyM9fzklDJedqjKk4VIpgk6SC70p1xZfQ_e08kOE_sGS-Vd5alI0U3JO3a_l2VIGZFAno2f79jU4ZRTbLKKKCEhY8eLGQ__rAawAbV8vgXrS0HWtM3fQEE23ud7DriLJAuRjn9Cgvjg"
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

async def main():
    userid = "713007296476741643"
    info = await dbkrpy.CheckVote.get_response(token,userid)
    print(dbkypy.CheckVote(info).check)
@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}!')
    print('정상작동중...')
    os.system("python gathongi.py")
    print('개똥이 실행 완료!')
    messages = ["명의 사용자와 함께", "접두어 = ,", "ver.2.3.7", "개의 서버와 함께"]
    while True:
        if messages[0] == '명의 사용자와 함께':
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f",도움 | {str(len(bot.users))}명의 사용자와 함께"))
        elif messages[0] == '개의 서버와 함께':
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f",도움 | {str(len(bot.guilds))}개의 서버와 함께"))
        else:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=",도움 | " + messages[0]))
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
async def 도움전달(ctx, user:discord.Member):
    embed = discord.Embed(title="도움말",color=0xe67e22,description="서버 관리봇, 개똥이.접두어:개똥아") #임베드 변수 지정
    embed.add_field(name="초대링크", value="- ``,초대링크, 초대코드``로 확인", inline=False) #field add
    embed.add_field(name="~~보유서버~~ 본 기능은 koreanbots에 의하여 막힌 기능입니다.", value="- ``,보유서버``로 확인", inline=False)#field add
    embed.add_field(name="매시지 삭제", value="- ``,삭제 (수)``로 확인", inline=False)
    embed.add_field(name="모두 삭제", value="- ``,clear``로 확인", inline=False)
    embed.add_field(name="메시지 전달", value="-``,dm @맨션 내용``으로 확인", inline=False)
    embed.add_field(name="출석체크", value="- ``출석체크, ㅊㅊ``으로 확인 ``출석 리스트``로 확인", inline=False)
    embed.add_field(name="정보", value="- ``,정보(맨션)``로 확인", inline=False)
    embed.add_field(name="타이머", value="- ``,타이머 (초) (제목)``로 확인", inline=False)
    embed.add_field(name="DM보내기", value="- ``,우체국 @맨션 내용``로 확인", inline=False)
    embed.add_field(name="다오 서포터", value="- ``https://discord.gg/PKGMwSB``", inline=False)
    embed.add_field(name="공지 (only 서버관리자)", value="- ``,공지 내용``", inline=False)
    embed.set_footer(text=(ctx.author.name), icon_url=ctx.author.avatar_url)
    await user.send(embed=embed)
    embed = discord.Embed(description = "[다오 서포터 <----- 클릭!!](https://discord.com/invite/PKGMwSB)",color=0xe67e22)
    await user.send(embed=embed)
    await ctx.send("DM으로 전송했어요!")
@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title="도움말",color=0xe67e22,description="서버 관리봇, 개똥이.접두어:개똥아") #임베드 변수 지정
    embed.add_field(name="초대링크", value="- ``,초대링크, 초대코드``로 확인", inline=False) #field add
    embed.add_field(name="보유서버", value="- ``,보유서버``로 확인", inline=False)#field add
    embed.add_field(name="매시지 삭제", value="- ``,삭제 (수)``로 확인", inline=False)
    embed.add_field(name="모두 삭제", value="- ``,clear``로 확인", inline=False)
    embed.add_field(name="메시지 전달", value="-``,dm @맨션 내용``으로 확인", inline=False)
    embed.add_field(name="출석체크", value="- ``출석체크, ㅊㅊ``으로 확인 ``출석 리스트``로 확인", inline=False)
    embed.add_field(name="정보", value="- ``,정보(맨션)``로 확인", inline=False)
    embed.add_field(name="타이머", value="- ``,타이머 (초) (제목)``로 확인", inline=False)
    embed.add_field(name="DM보내기", value="- ``,우체국 @맨션 내용``로 확인", inline=False)
    embed.add_field(name="다오 서포터", value="- ``https://discord.gg/PKGMwSB``", inline=False)
    embed.add_field(name="공지 (only 서버관리자)", value="- ``,공지 내용``", inline=False)
    embed.set_footer(text=(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.author.send(embed=embed)
    embed = discord.Embed(description = "[다오 서포터 <----- 클릭!!](https://discord.com/invite/PKGMwSB)",color=0xe67e22)
    await ctx.author.send(embed=embed)
    await ctx.send("DM으로 전송했어요!")
@bot.command()
async def 갸우뚱(ctx):
    await ctx.channel.send('***(갸우뚱?)*** 난 크시가 아니지만...')
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
async def 초대링크(ctx):
    await ctx.channel.send('https://tenor.com/view/cat-loading-error-angry-fuck-gif-8985245')
    time.sleep(5)
    await ctx.channel.send('https://discord.com/api/oauth2/authorize?client_id=713007296476741643&permissions=8&scope=bot')
@bot.command()
async def 초대코드(ctx):
    await ctx.channel.send('https://tenor.com/view/cat-loading-error-angry-fuck-gif-8985245')
    time.sleep(5)
    await ctx.channel.send('https://discord.com/api/oauth2/authorize?client_id=713007296476741643&permissions=8&scope=bot')
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
async def 우체국(ctx, user:discord.Member, *, msg):
    #first_date = datetime('&y년 %m월 %d일 %p%I (%H시)시 %M분 %S초 보냄')
    first_date = time.asctime()
    embed = discord.Embed(color=0x00EBFF)
    embed.set_author(name="우체국에서 편지왔어요~")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url="http://bitly.kr/mailarrive")
    embed.add_field(name="보낸 유저 이름", value=ctx.message.author.name, inline=False)
    embed.add_field(name="보낸 유저 아이디", value=ctx.message.author.id, inline=False)
    embed.add_field(name="보낸 서버 아이디", value=ctx.message.guild.id, inline=False)
    embed.add_field(name="보낸 채널 아이디", value=ctx.message.channel.id, inline=False)
    embed.add_field(name="보낸 서버 이름", value=ctx.message.guild.name, inline=False)
    embed.add_field(name="보낸 채널 이름", value=ctx.message.channel.name, inline=False)
    embed.add_field(name="전할 내용", value=msg)
    embed.set_author(name=f"작성일:{first_date}", icon_url="https://cdn.discordapp.com/attachments/717305319390445569/718425698292989962/68cf02c49ae96c340e0c7430959a64da.png")
    embed.set_footer(text=(f"작성일:{first_date}"), icon_url=ctx.author.avatar_url)
    await user.send(ctx.message.author.mention, embed=embed)
    await ctx.send("우체부가 아주 잘 전해준다고 했어요!")
#@bot.command()
#async def 가위바위보()
#    await ctx.channel.send('가위 바위 보중에 1개를 입력하세요')
#    async def 가위()
#        
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
    if message.content.startswith("출첵") or message.content.startswith("ㅊㅊ") or message.content.startswith("출석체크"):
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
        finalcheck = "다오봇"
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
        os.system("python dao.py")
        exit()
#        await ctx.send("모든 모듈을 리로드했어요!")
#        imp.reload(discord)
#        self.bot.reload_extension("gathongi.py")
@bot.listen()
async def on_message(message):
    if message.content.startswith(",,정보"):
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
async def 역할빼기(ctx, user:discord.Member, txt):
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
@bot.listen()
async def on_message(message):
    if message.content.startswith("도박 도움") or message.content.startswith("도박 방법"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="다오봇 도박 방법!", value="""
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
    if message.content.startswith("도박신청"):
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
            embed.add_field(name="다요봇 도박", value="""
            {}님께서 {}님께 도박을 신청하였습니다.
            도박 신청을 수락하시려면 '**예**'를 입력해 주시고 거절하시려면 '**아니요**'를 입력해 주세요.

            **주의: 닉네임에 공백 혹은 대괄호가 포함되어 있으면 인식할 수 없습니다.**
            """.format(player1, player2), inline=False)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="다오봇 도박", value="""
            현재 다른 플레이어들의 초대 및 게임이 진행중입니다.
            """, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("아니요"):
        if progress == "invite":
            if message.author.display_name == player2:
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
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
                embed.add_field(name="다오봇 도박", value="""
                **서버**에서 **'배팅 <배팅할 랜지 코인(숫자만 입력)>'**을 입력하여 배팅을 해주세요.
                """, inline=False)
                await message.author.send(embed=embed)

    if message.content.startswith("예"):
        if progress == "invite":
            if message.author.display_name == player2:
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                도박 신청이 수락되었습니다.
                """, inline=False)
                await message.channel.send(embed=embed)
                progress = "card"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                '카드 뽑기'를 입력하여 카드를 뽑으세요!
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
                embed.add_field(name="다오봇 도박", value="""
                한번 더 뽑은 당신의 카드는 {} 입니다!
                """.format(player1_card3), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
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
                embed.add_field(name="다오봇 도박", value="""
                한번 더 뽑은 당신의 카드는 {} 입니다!
                """.format(player2_card3), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                **서버**에서 **'배팅 <배팅할 랜지 코인(숫자만 입력)>'**을 입력하여 배팅을 해주세요.
                """, inline=False)
                await message.author.send(embed=embed)
                

    if message.content.startswith("카드 뽑기"):
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
                embed.add_field(name="다오봇 도박", value="""
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
                embed.add_field(name="다오봇 도박", value="""
                당신의 카드는 {}, {} 입니다!
                """.format(player2_card1, player2_card2), inline=False)
                await message.author.send(embed=embed)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="다오봇 도박", value="""
        한 장 더 뽑으시려면 '**예**'를 입력해 주시고 바로 베팅을 하시려면 '**아니요**'를 입력해 주세요.
        """, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("배팅"):
        if progress == "bat" or progress == "bat_1":
            if message.author.display_name == player1:
                choice = message.content.split(" ")
                player1_bat = choice[1]
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                {}님께서 랜지 코인 {}개를 배팅하셨습니다.
                """.format(player1, player1_bat), inline=False)
                await message.channel.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                랜지 코인 {}개가 정상적으로 배팅되었습니다.
                """.format(player1_bat), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="도박 결과를 입력해 누가 승리했는지 확인하세요!", inline=False)
                await message.author.send(embed=embed)
                if progress == "bat_1":
                    progress = "result"
                else:
                    progress = "bat_1"
            if message.author.display_name == player2:
                choice = message.content.split(" ")
                player2_bat = choice[1]
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                {}님께서 랜지 코인 {}개를 배팅하셨습니다.
                """.format(player2, player2_bat), inline=False)
                await message.channel.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                랜지 코인 {}개가 정상적으로 배팅되었습니다.
                """.format(player2_bat), inline=False)
                await message.author.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="도박 결과를 입력해 누가 승리했는지 확인하세요!", inline=False)
                await message.author.send(embed=embed)
                if progress == "bat_1":
                    progress = "result"
                else:
                    progress = "bat_1"
        
    if message.content.startswith("도박 결과"): 
        if progress == "result":
            if player1_bat != 0 and player2_bat != 0:
                progress = "none"
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                3초 뒤 결과가 공개됩니다.
                """, inline=False)
                await message.channel.send(embed=embed)
                time.sleep(3)
                player1_result = player1_card1 + player1_card2 + player1_card3
                player1_result = player1_result % 10
                player2_result = player2_card1 + player2_card2 + player2_card3
                player2_result = player2_result % 10
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                {}님의 카드는 {}, {}, {} 입니다.
                """.format(player1, player1_card1, player1_card2, player1_card3), inline=False)
                await message.channel.send(embed=embed)
                embed = discord.Embed(color=0x00ff00)
                embed.add_field(name="다오봇 도박", value="""
                {}님의 카드는 {}, {}, {} 입니다.
                """.format(player2, player2_card1, player2_card2, player2_card3), inline=False)
                await message.channel.send(embed=embed)
                if player1_result > player2_result:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="다오봇 도박", value="{}님의 승리입니다! 축하드립니다 {}님!".format(player1, player1), inline=False)
                    await message.channel.send(embed=embed)
                if player1_result < player2_result:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="다오봇 도박", value="{}님의 승리입니다! 축하드립니다 {}님!".format(player2, player2), inline=False)
                    await message.channel.send(embed=embed)
                if player1_result == player2_result:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="다오봇 도박", value="무승부입니다 ㅠ.ㅠ 배팅한 코인의 반을 서로 가져갑니다.", inline=False)
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
    await ctx.send(dbkr.check)
    await ctx.sned(info)
@bot.listen()
async def on_message(message):
    if message.content.startswith(","):
        dice = ["y","n","n","n","n","n","n","n","n","n","n","n","n","n"]
        yesorno = random.choice(dice)
        if yesorno == "y":
            embed = discord.Embed(description = "[[광고]다오를 초대해주세요!](https://discord.com/oauth2/authorize?client_id=713007296476741643&scope=bot&permissions=8)", color=0xff0000)
            await message.channel.send(embed=embed)
            embed = discord.Embed(description = "[[광고]다오한테 좋아요를 눌러주세요!](https://koreanbots.dev/bots/713007296476741643)", color=0xff0000)
            await message.channel.send(embed=embed)
@bot.command()
async def 핑(ctx):
    if (round(bot.latency*1000)) > 230:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 매우 나쁨:no_entry:""".format(round(bot.latency*1000)), color=0xff0000)
            await ctx.channel.send(embed=embed)
    if (round(bot.latency*1000)) < 230:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 양호:white_check_mark:""".format(round(bot.latency*1000)), color=0x00ff00)
            await ctx.channel.send(embed=embed)
    if (round(bot.latency*1000)) < 185:
            embed = discord.Embed(color=0x00ff00)
            embed = discord.Embed(title=":ping_pong:퐁!", description="""
            현재 디스코드 api핑: {0}ms
            상태: 매우 좋음:green_heart:""".format(round(bot.latency*1000)), color=0x0000ff)
            await ctx.channel.send(embed=embed)
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
bot.run(token)
