import discord,random
from bs4 import BeautifulSoup
import requests
import urllib

token = "NzEzMDA3Mjk2NDc2NzQxNjQz.XuWK4w.1D-nap9ca7zYP__JuEwdxiQ4ZEU"

client = discord.Client()

@client.event
async def on_ready():
    print('------------------------------------')
@client.event
async def on_message(message):
    if message.content == ",코로나현황":
        yesorno = ['y','n']
        response = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=코로나')
        readerhtml = response.text
        soup = BeautifulSoup(readerhtml, 'lxml')
        data1 = soup.find('div', class_='graph_view')
        data2 = data1.findAll('div', class_='box')
        data3 = data1.findAll('div', class_='box bottom')
        checked = data2[0].find('p', class_='txt').find('strong', class_='num').text
        checking = data2[2].find('p', class_='txt').find('strong', class_='num').text
        free = data3[0].find('p', class_='txt').find('strong', class_='num').text        
        die = data3[1].find('p', class_='txt').find('strong', class_='num').text
        wasup = soup.find('div', class_='csp_notice_info').find('p').find_all(text=True, recursive=True)
        #===============================
        coembed = discord.Embed(color=0x70D4DE, title='코로나현황', description =f'{wasup[1]}' )
        coembed.add_field(name="확진자", value=f'{checked}명', inline=True)
        coembed.add_field(name="격리해제", value=f'{free}명', inline=True)
        coembed.add_field(name="검사중", value=f'{checking}명', inline=True)
        coembed.add_field(name="사망자", value=f'{die}명', inline=True)
        yesorno2 = random.choice(yesorno)
        if yesorno2 == 'y':
            coembed.set_image(url='https://cdn.discordapp.com/attachments/715886051776004097/724133198140932136/200225__1.png')
        else:
            coembed.set_image(url='https://cdn.discordapp.com/attachments/715886051776004097/724176186426785822/19__.jpg')
        await message.channel.send(yesorno2)
        await message.channel.send(embed = coembed)
    if message.content.startswith(",구글링"):
        text = message.content[5:]
        await message.channel.send(f"{text}검색중!")
        url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={text}'
        #url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%85%B8%EB%9E%98+%EB%AA%A8%EC%9D%8C%EC%A7%91&oquery=%EB%B8%94%EB%A1%9C%EA%B7%B8&tqi=UYu2hwp0JXossmkVJudssssst6Z-346222'
        #url = text
        await message.channel.send(f'검색주소 : {url}')
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find_all(class_='sh_blog_title')

        for i in title:
            await message.channel.send(i.attrs['title'])
            await message.channel.send(i.attrs['href'])
client.run(token)
