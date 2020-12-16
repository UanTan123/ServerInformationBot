import discord
import datetime
import asyncio
import os
import sys

client = discord.Client()
token = "token"
p = '!'

@client.event
async def on_ready():
    print('ServerInformationBot has been on!')

@client.event
async def on_message(message):
    try:

        if message.author.bot:
            return
        
        elif message.content == f'{p}SI':
            now = datetime.datetime.now()
            embed = discord.Embed(
                title=f'{message.guild}의 정보',
                description=f"서버 이름 : {message.guild}\n\
                    서버 아이디 : {message.guild.id}\n\
                    서버 생성일 : {message.guild.created_at.year}년 {message.guild.created_at.month}월 {message.guild.created_at.day}일 {message.guild.created_at.hour}시 {message.guild.created_at.minute}분 {message.guild.created_at.second}초\n\
                    지역 : {message.guild.region}\n\
                    잠수 채널 : {message.guild.afk_channel} (타이머: {message.guild.afk_timeout}초)\n\
                    시스템 채널 : <#{message.guild.system_channel.id}>\n\
                    부스트 레벨 : {message.guild.premium_tier}레벨(부스트 횟수 : {message.guild.premium_subscription_count})\n\
                    주인 아이디 : {message.guild.owner_id}\n\
                    서버 설명 : {message.guild.description}\n\
                    2단계 인증 수준 : {message.guild.mfa_level}(1 : true, 0 : false)\n\
                    비디오 채널 최대 사용자 수 : {message.guild.max_video_channel_users}명\n\
                    서버의 최대 회원 수 : {message.guild.max_members}명\n\
                    서버의 인증 레벨 : {message.guild.verification_level}레벨\n\
                    서버의 명시적 콘텐츠 필터 : {message.guild.explicit_content_filter}\n\
                    서버의 알림 설정 : {message.guild.default_notifications}\n\
                    서버에서 선호하는 장소 : {message.guild.preferred_locale}\n\
                    서버가 큰지 여부 : {message.guild.large}\n\
                    서버의 최대 커스텀 이미지 수 : {message.guild.emoji_limit}\n\
                    서버의 최대 전송 바이트 수 : {message.guild.bitrate_limit}byte\n\
                    서버의 최대 파일 전송 바이트 수 : {message.guild.filesize_limit}byte\n\
                    ",
                colour=discord.Colour.blue()
            ).set_footer(icon_url=message.author.avatar_url, text=f"| {message.author.display_name} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초")
            embed.set_image(url=message.guild.icon_url)
            await message.channel.send(embed=embed)

            result = ""
            for emoji in message.guild.emojis:
                result += str(emoji)
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                title=f'서버이모지',
                description=f'커스텀 이모지 : {str(result)}\n갯수 : {str(len(message.guild.emojis))}'
                ).set_image(url=message.guild.banner_url)
            await message.channel.send(embed=embed)
            roles = [role for role in message.guild.roles]
            embed = discord.Embed(
                color=0x00D8FF,
                title='서버역할',
            ).add_field(name='이 서버의 역할 정보', value=" ".join([role.mention for role in roles][1:]), inline=False)
            embed.add_field(name='서버의 역할 갯수', value=f'{len(roles)-1}개', inline=False)
            await message.channel.send(embed=embed)

    except Exception as e:
        await client.get_channel(int(762942002060460036)).send(f"오류 발생 : {e}")
        print(e)

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        act=["!SI", "ServerInformation"]
        for i in act:
            game = discord.Game(str(i))
            await client.change_presence(status=discord.Status.dnd, activity=game)
            await asyncio.sleep(5)
client.loop.create_task(my_background_task())
client.run(token)
os.execv(sys.executable, ['python']+sys.argv)
