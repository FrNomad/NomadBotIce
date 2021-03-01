import discord
import random
import os

hochul="얼음아"
client = discord.Client()
embedcolor = 0x2121E5

mode=0

#-------명령-----------
randomGreet = ["마크하고싶당","왜?","왜불러?","ㅖ?","살아있음 걱정 ㄴㄴ","호출했니?","나 불렀니?","호출했냐?","살아있다고!!!",
            "뭐?","왜 시비임?","내 이름만 부르지마","호출하셨습니까? **(정중 +10)**","부르셨습니까? **(정중 +10)**", "호출하셨사옵니까? **(정중 +20)**",
            "부르셨사옵니까? **(정중 +20)**", "생존신고 합니다", "작동중지 상태입니다......는 헛소리","얼음봇 없다~~","ㄷ졌습니ㄷ","**볼드체 ㅎㅇ**","*기울임체 ㅎㅇ*","~~널 숙청할테다~~ 죄송함돠"]
greet = ["ㅎㅇ", "안녕"]
developer = ["개발자", "제작자"]
mincho=["민초", "민트초코"]
nomad=["노매드","FrNomad"]
teasenomad=["얼어붙은유목민","얼어뒤진유목민","얼어뒤진노매드","얼어뒤진","정신나간","멍청한"]
modeop=["모드변경","모드"]
kimdro=["김드로","드로","kimdro"]
drogen=["드로젠","김민석"]
dg=["디지메트로","디지","디지행님","디지형님","디지형"]
flint=["플린트","파브릭","flintt","fabric"]
mc=["마크","마인크래프트"]
teasebot=["바보","멍청이","모자란애","멍청한애","바보멍청이"]
juew=["juew","쥬","배준혁"]
drobot=["김드로봇","드로봇"]
#----------------------
#-------임베드----------
helpem = discord.Embed(title="얼음이와 노는 법",description="얼음이와 노는법을 정리해봤어요~~!", color=embedcolor)
helpem.add_field(name="얼음아", value="-얼음이의 생존 여부를 확인합니다.", inline=False)
helpem.add_field(name="얼음아 안녕", value="-얼음이와 인사합니다.", inline=False)
helpem.add_field(name="얼음아 개발자", value="-얼음이의 개발자를 말합니다.", inline=False)
helpem.add_field(name="얼음아 민초", value="-얼음이의 민초파 여부를 확인합니다.", inline=False)
helpem.add_field(name="이외에도 많은 기능들이 숨어있으니 잘 찾아보세요~~!",value="얼음봇 드림", inline=False)
#----------------------


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("얼음아 도움말"))
  print("봇 실행완료")
  print(client.user.name)
  print(client.user.id)

@client.event
async def on_message(message):
    args = message.content.split(" ")
    rd = random.randint(0, len(randomGreet))
    if message.content == hochul:
        await message.channel.send(f"{message.author.mention}, {randomGreet[rd-1]}")
    if args[0] == hochul:
        global mode
        msg = args[1]
        mt = message.author.mention
        if mode == 0:
            if msg == "도움말":
                await message.channel.send(f"{mt}, DM에 나랑 노는법 보내놨다")
                await message.author.send(embed=helpem)
            elif msg in modeop:
                mode += 1
                await message.channel.send("모드가 변경되었습니다. 현재 모드는 **존댓말** 모드입니다.")
            elif msg in greet:
                await message.channel.send(f"{mt}, ㅎㅇㅎㅇ")
            elif msg in developer:
                await message.channel.send(f"{mt}, 내 개발자는 노매드님이심")
            elif msg in mincho:
                await message.channel.send(f"{mt}, 내 개발자분이 민초파라서 나도 민초파임 민초가 을마나 맛있는데 ㅎㅎ")
            elif msg in nomad:
                await message.channel.send(f"{mt}, 내 개발자임 그러니까 나 만드신 분")
            elif msg in teasenomad:
                await message.channel.send(f"{mt}, 누구라도 놀렸다가는 가만 안둘거임....")
            elif msg in kimdro:
                await message.channel.send(f"{mt}, RTM 잘하시는 그분? 어우 그분은 머리 좋죠 ㅎㅎ ~~대신 저분은 민초를 극혐해서 별로 안좋아함~~")
            elif msg in drogen:
                await message.channel.send(f"{mt}, ~~수소~~ 이분은 평범하지만 성품이 참 바르신 분임")
            elif msg in dg:
                await message.channel.send(f"{mt}, ~~맨날 RTX 타령하는 분~~ 마도제 최고의 도시맵인 디지월드를 개발하는 분임. 디지월드 퀄리티는 키야~")
            elif msg in flint:
                await message.channel.send(f"{mt}, BE 건축 장인이심~ 가보는 아무도 못따라잡음~~ 개인적으로 존경하는 인간임!")
            elif msg in mc:
                await message.channel.send(f"{mt}, 내 개발자분이 좋아하는 게임임. 그래서 나도 좋아함")
            elif msg in teasebot:
                await message.channel.send(f"{mt}, 나 놀리지 말라고~ ㅠㅠ")
            elif msg in juew:
                await message.channel.send(f"{mt}, 그분은 불운의 인물이자 되게 빡빡하심")
            elif msg in drobot:
                await message.channel.send(f"{mt}, 드로봇 멍청이!\n드로봇 세상에서 제일 멍청이!\n드로봇 다중우주에서 제일 멍청이!\n드로봇 뒤로 돌아섰더니 이우현이 단두대 준비하고있던 멍청이!\n드로봇한테 누가 뭐 물어봤는데 기억도 못해서 멍청이 대우받는 멍청이!")
            else:
                if msg in message.author.name:
                    await message.channel.send(f"{mt}, 너")
                #else:
                   #if msg in message.guild.get_member(int(message.author.id))
        elif mode == 1:
            if msg == "도움말":
                await message.channel.send(f"{mt}, DM에 저랑 노는 방법을 정리해서 보내놨습니다.")
                await message.author.send(embed=helpem)
            elif msg in modeop:
                mode = 0
                await message.channel.send("모드가 변경되었습니다. 현재 모드는 **반말(보통)** 모드입니다")
            elif msg in greet:
                await message.channel.send(f"{mt}, 안녕하세요~!")
            elif msg in developer:
                await message.channel.send(f"{mt}, 제 개발자는 노매드님이라고 계십니다 ㅎㅎ")
            elif msg in mincho:
                await message.channel.send(f"{mt}, 제 개발자분이 민초파라서 저도 민초파입니다")
            elif msg in nomad:
                await message.channel.send(f"{mt}, 제 개발자 분이십니다 다시 설명하자면 저를 만드신 분이시죠")
            elif msg in teasenomad:
                await message.channel.send(f"{mt}, 누구라도 놀렸다가는 가만히 두지 않겠습니다....")
            elif msg in kimdro:
                await message.channel.send(f"{mt}, 그분은 RTM 잘하시는 분이죠~! 머리 좋은 분입니다 ~~대신 민초를 별로 안좋아하셔서 별로 안좋아합니다~~")
            elif msg in drogen:
                await message.channel.send(f"{mt}, ~~수소~~ 이분은 평범하지만 성품이 정말 바르신 분이죠")
            elif msg in dg:
                await message.channel.send(f"{mt}, ~~맨날 RTX 타령하시는 분~~ 마도제 최고의 도시맵인 디지월드를 개발하시는 분입니다. 디지월드의 퀄리티는 기가 막히죠~")
            elif msg in flint:
                await message.channel.send(f"{mt}, BE 건축 장인이시죠~ 가보는 아무도 못따라잡아요~~ 개인적으로 존경합니다!")
            elif msg in mc:
                await message.channel.send(f"{mt}, 제 개발자분이 좋아하시는 게임입니다. 그래서 저도 좋아하는 게임이죠")
            elif msg in teasebot:
                await message.channel.send(f"{mt}, 얼음봇 놀리지 마세요 ㅠㅠ")
            elif msg in juew:
                await message.channel.send(f"{mt}, 그분은 불운의 인물이자 되게 빡빡하신 분입니다.")
            elif msg in drobot:
                await message.channel.send(f"{mt}, 드로봇 멍청이!\n드로봇 세상에서 제일 멍청이!\n드로봇 다중우주에서 제일 멍청이!\n드로봇 뒤로 돌아섰더니 이우현이 단두대 준비하고있던 멍청이!\n드로봇한테 누가 뭐 물어봤는데 기억도 못해서 멍청이 대우받는 멍청이!")
            else:
                if msg in message.author.name:
                    await message.channel.send(f"{mt}, 당신입니다")
        

client.run(os.environ['token'])
