import discord
import random
import os
import time

hochul="얼음아"
client = discord.Client()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
embedcolor = 0x2121E5
subdly = 0.3

mode=0
stop=0
stopsender=None
stlist=None
nblist=None

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
helpem.add_field(name="얼음아 외워 <노선명>", value="-얼음이가 지하철 노선을 외웁니다.", inline=False)
helpem.add_field(name="이외에도 많은 기능들이 숨어있으니 잘 찾아보세요~~!",value="얼음봇 드림", inline=False)
#----------------------
#-------노선도암기------
lines=["1호선","2호선","3호선","4호선","5호선","6호선","7호선","8호선","9호선"]
l1=["소요산","동두천","보산","동두천중앙","지행","덕정","덕계","양주","녹양","가능","의정부","회룡","망월사","도봉산","도봉","방학","창동","녹천","월계","광운대","석계","신이문","외대앞","회기","청량리","제기동","신설동","동묘앞","동대문","종로5가","종로3가","종각","시청","서울역","남영","용산","노량진","대방","신길","영등포","신도림","구로","구일","개봉","오류동","온수","역곡","소사","부천","중동","송내","부개","부평","백운","동암","간석","주안","도화","제물포","도원","동인천","인천",
    "**----------장항선----------**","가산디지털단지","독산","금천구청","광명**(분기선)**","`금천구청` `>` 석수","관악","안양","명학","금정","군포","당정","의왕","성균관대","화서","수원","세류","병점","서동탄**(분기선)**","`병점` `>` 세마`","오산대","오산","진위","송탄","서정리","지제","평택","성환","직산","두정","천안","봉명","쌍용","아산","탕정(미개통)","배방","온양온천","신창"]
l1n=["100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157","158","159","160","161","",
    "P142","P143","P144", "P144-1", "P145","P146","P147","P148","P149","P150","P151","P152","P153","P154","P155","P156","P157","P157-1","P158","P159","P160","P161","P162","P163","P164","P165","P166","P167","P168","P169","P170","P171","P172","P173","P174","P176","P177"]
l2=["시청","을지로입구","을지로3가","을지로4가","동대문역사문화공원","신당","상왕십리","왕십리","한양대","뚝섬","성수","건대입구","구의","강변","잠실나루","잠실","잠실새내","종합운동장","삼성","선릉","역삼","강남","교대","서초","방배","사당","낙성대","서울대입구","봉천","신림","신대방","구로디지털단지","대림","신도림","문래","영등포구청","당산","합정","홍대입구","신촌","이대","아현","충정로","시청"]
l2n=["201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","239","240","241","242","243","201"]
l3=["대화","주엽","정발산","마두","백석","대곡","화정","원당","원흥","삼송","지축","구파발","연신내","불광","녹번","홍제","무악재","독립문","경복궁","안국","종로3가","을지로3가","충무로","동대입구","약수","금호","옥수","압구정","신사","잠원","고속터미널","교대","남부터미널","양재","매봉","도곡","대치","학여울","대청","일원","수서","가락시장","경찰병원","오금"]
l3n=["309","310","311","312","313","314","315","316","317","318","319","320","321","322","323","324","325","326","327","328","329","330","331","332","333","334","335","336","337","338","339","340","341","342","343","344","345","346","347","348","349","350","351","352"]
l4=["당고개","상계","노원","창동","쌍문","수유","미아","미아사거리","길음","성신여대입구","한성대입구","혜화","동대문","동 대문역사문화공원","충무로","명동","회현","서울역","숙대입구","삼각지","신용산","이촌","동작","총신대입구(이수)","사당","남태령","선바위","경마공원","대공원","과천","정부과천청사","인덕원","평촌","범계","금정","산본","수리산","대야미","반월","상록수","한대앞","중앙","고잔","초지","안산","능길(구.신길온천)","정왕","오이도"]
l4n=["409","410","411","412","413","414","415","416","417","418","419","420","421","422","423","424","425","426","427","428","429","430","431","432","433","434","435","436","437","438","439","440","441","442","443","444","445","446","447","448","449","450","451","452","453","454","455","456"]
l5=["방화","개화산","김포공항","송정","마곡","발산","우장산","화곡","까치산","신정","목동","오목교","양평","영등포구청","영등포시장","신길","여의도","여의나루","마포","공덕","애오개","충정로","서대문","광화문","종로3가","을지로4가","동대문역사문화공원","청구","신금호","행당","왕십리","마장","답십리","장한평","군자","아차산","광나루","천호","강동","길동","굽은다리","명일","고덕","상일동","강일(미개통)","미사","하남풍산","`강동` `>` 둔촌동","올림픽공원","방이","오금","개롱","거여","마천"]
l5n=["510","511","512","513","514","515","516","517","518","519","520","521","522","523","524","525","526","527","528","529","530","531","532","533","534","535","536","537","538","539","540","541","542","543","544","545","546","547","548","549","550","551","552","553","554","555","556","P549","P550","P551","P552","P553","P554","P555"]
l6=["응암 `>` `역촌 (응암순환 방면)`","역촌 `>` `불광 (일방통행)`","불광 `>` `독바위 (일방통행)`","독바위 `>` `연신내 (일방통행)`","연신내 `>` `구산 (일방통행)`","구산 `>` `응암 (일방통행)`","응암 `>` `새절(봉화산 방면)`","새절","증산","디지털미디어시티","월드컵경기장","마포구청","망원","합정","상수","광흥창","대흥","공덕","효창공원","삼각지","녹사평","이태원","한강진","버티고개","약수","청구","신당","동 묘앞","창신","보문","안암","고려대","월곡","상월곡","돌곶이","석계","태릉입구","화랑대","봉화산","신내"]
l6n=["610","611","612","613","614","615","610","616","617","618","619","620","621","622","623","624","625","626","627","628","629","630","631","632","633","634","635","636","637","638","639","640","641","642","643","644","645","646","647","648"]
l7=["장암","도봉산","수락산","마들","노원","중계","하계","공릉","태릉입구","먹골","중화","상봉","면목","사가정","용마산","중곡","군자","어린이대공원","건대입구","뚝섬유원지","청담","강남구청","학동","논현","반포","고속터미널","내방","이수(총신대입구)","남성","숭실대입구","상도","장승배기","신대방삼거리","보라매","신풍","대림","남구로","가산디지털단지","철산","광명사거리","천왕","온수","까치울","부천종합운동장","춘의","신중동","부천시청","상동","삼산체육관","굴포천","부평구청"]
l7n=["709","710","711","712","713","714","715","716","717","718","719","720","721","722","723","724","725","726","727","728","729","730","731","732","733","734","735","736","737","738","739","740","741","742","743","744","745","746","747","748","749","750","751","752","753","754","755","756","757","758","759"]
l8=["암사","천호","강동구청","몽촌토성","잠실","석촌","송파","가락시장","문정","장지","복정","산성","남한산성입구","단대오 거리","신흥","수진","모란"]
l8n=["810","811","812","813","814","815","816","817","818","819","820","821","822","823","824","825","826"]
l9=["개화","김포공항","공항시장","신방화","마곡나루","양천향교","가양","증미","등촌","염창","신목동","선유도","당산","국회 의사당","여의도","샛강","노량진","노들","흑석","동작","구반포","신반포","고속터미널","사평","신논현","언주","선정릉","삼성중앙","봉은사","종합운동장","삼전","석촌고분","석촌","송파나루","한성백제","올림픽공원","둔촌오륜","중앙보훈병원"]
l9n=["901","902","903","904","905","906","907","908","909","910","911","912","913","914","915","916","917","918","919","920","921","922","923","924","925","926","927","928","929","930","931","932","933","934","935","936","937","938"]
#----------------------
#-------함수-----------

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
        global stop
        global stopsender
        global stlist
        global nblist
        global setline
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
        if msg == "외워":
            line = args[2]
            stlist=None
            nblist=None
            if(line in lines):
                if line == "1호선":
                    stlist=l1
                    nblist=l1n
                elif line == "2호선":
                    stlist=l2
                    nblist=l2n
                elif line == "3호선":
                    stlist=l3
                    nblist=l3n
                elif line == "4호선":
                    stlist=l4
                    nblist=l4n
                elif line == "5호선":
                    stlist=l5
                    nblist=l5n
                elif line == "6호선":
                    stlist=l6
                    nblist=l6n
                elif line == "7호선":
                    stlist=l7
                    nblist=l7n
                elif line == "8호선":
                    stlist=l8
                    nblist=l8n
                elif line == "9호선":
                    stlist=l9
                    nblist=l9n
                if stlist != None:    
                    await message.channel.send(f"**{line}을(를) 외워볼까~요?**")
                    if(stop == 1):
                        stop = 0
                    for i in range(0, len(stlist)):
                        if(stop == 1):
                            stop = 0
                            if(stopsender == None):
                                await message.channel.send(f"{mt}, 알겠슈, 그만 외울게요")
                            else:
                                await message.channel.send(f"{stopsender.mention}, 알겠슈, 그만 외울게요")
                                stopsender=None
                            break
                        time.sleep(subdly)
                        if(len(nblist[i]) == 0):
                            await message.channel.send(f"{stlist[i]}")
                        else:
                            await message.channel.send(f"**[{nblist[i]}]** {stlist[i]}")
                    await message.channel.send("**여.기.까.지!**")
                else:
                    await message.channel.send("노선명에 오류가 있거나 입력되지 않은 노선이거나 존재하지 않는 노선입니다.")
            else:
                if len(args) == 2:
                    await message.channel.send("노선명을 기입하여 주십시오.")
                else:
                    await message.channel.send("노선명에 오류가 있거나 입력되지 않은 노선이거나 존재하지 않는 노선입니다.")
        if msg == "그만":
            stop = 1
            stopsender = message.author
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

client.run(os.environ['token'])
