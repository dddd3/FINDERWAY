import asyncio
import discord

app = discord.Client()

token = "NzE1MTMzMzc2MDQ2MTcwMTEz.Xs46Mg.1Vh0s5ibvnLuz1UUuF_BmzZ0gd0"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("오류시 관리자에게 문의 요망") 
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "작동 확인":
        await message.channel.send("출력 정상 작동중.")
    if message.content.startswith("봇1부터10"):
        for x in range(10):
            await message.channel.send(x+1) 
    if message.content.startswith("계산"):
        global calcResult
        if message.content[7:].startswith("더하기"):
            calcResult = int(message.content[11:12])+int(message.content[13:14])
            await message.channel.send("Result : "+str(calcResult)) 
        if message.content[7:].startswith("빼기"):
            calcResult = int(message.content[10:11])-int(message.content[12:13])
            await message.channel.send("Result : "+str(calcResult)) 
        if message.content[7:].startswith("곱하기"):
            calcResult = int(message.content[11:12])*int(message.content[13:14])
            await message.channel.send("Result : "+str(calcResult)) 
        if message.content[7:].startswith("나누기"):
            try:
                calcResult = int(message.content[11:12])/int(message.content[13:14])
                await message.channel.send("Result : "+str(calcResult)) 
            except ZeroDivisionError:
                await message.channel.send("You can't divide with 0.")
    if message.content.startswith("맵별 랜드마크"):
        embed=discord.Embed(title="랜드마크", description="", color=0x00ff55)
        embed.set_author(name="FINDERWAY", url="https://blog.naver.com/huntingbear21", icon_url="https://cdn.discordapp.com/attachments/714690275867492432/715172812544933938/20200527_185802_3.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/714690275867492432/715172812544933938/20200527_185802_3.png")
        embed.add_field(name="에란겔", value="프리모스크, 강남", inline=False)
        embed.add_field(name="미라마", value="로스 히고스, 페카도", inline=False)
        embed.add_field(name="사녹", value="루인스, 파라다이스", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("스크림 결과"):
        embed=discord.Embed(title="스크림 결과", description="2020. 5. 17 (일) 데일리 스크림 결과", color=0x00ff56)
        embed.set_author(name="FINDERWAY", url="https://blog.naver.com/huntingbear21", icon_url="https://cdn.discordapp.com/attachments/714690275867492432/715172812544933938/20200527_185802_3.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/714690275867492432/715172812544933938/20200527_185802_3.png")
        embed.add_field(name="멤버", value="clev3ry, Human, Hack, Destiny", inline=False)
        embed.add_field(name="평균 팀 등 수", value="5등", inline=False)
        embed.add_field(name="평균 팀 킬 수", value="4.5", inline=False)
        embed.add_field(name="평균 팀 딜량", value="589.25", inline=False)
        embed.add_field(name="종합", value="6등(31점) [ 킬:18, 순위점수:13점 ]", inline=False)
        embed.set_footer(text="고생하셨습니다.")
        await message.channel.send(embed=embed)
            
app.run(token)
