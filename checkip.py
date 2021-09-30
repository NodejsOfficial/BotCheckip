import discord,requests,sys,os
from ping3 import ping, verbose_ping
from discord.ext import commands

token = "Token" #Token บอท
client =  commands.Bot(command_prefix="n!")

@client.event
async def on_ready():
    print("Bot is online.")


@client.event
async def on_message(message):
    msg = message.content.split()
    try:
        url = msg[1].replace("-", "_")
    except:
        url = ""

    if int(message.channel.id) == 66666666666666: #ใส่idห้องที่จะให้บอทพิมพ์


                if message.content.startswith("n!check"):
                    embed = discord.Embed(title="Check/Ip/https/ping BY | Node.js", description="All Commands", color=0xf8fc03)
                    embed.add_field(name="n!httpcheck (Url)", value="> httpcheck", inline=False)
                    embed.add_field(name="n!ipcheck (Ip)", value="> checkip", inline=False)
                    embed.add_field(name="n!ping(Ip)", value="> pingip", inline=False)
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/869212527446335518/869228880827928606/5.jpg')
                    embed.set_footer(text='BOT BY | Node.js', icon_url='https://cdn.discordapp.com/attachments/866644902628818954/868750639751114752/216800335_547086389761904_6021980829694075076_n.png')
                    await message.channel.send(embed=embed)
        
                if message.content.startswith("n!help"):
                    embed = discord.Embed(title="Check/Ip/https/ping BY : Node.js", description="All Commands", color=0xe303fc)
                    embed.add_field(name="n!check", value="> Use this Command to watch more", inline=False)
                    embed.add_field(name="n!invite", value="> Use this Command to invite Bot", inline=False)
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/869212527446335518/869228880827928606/5.jpg')
                    embed.set_footer(text='BOT BY | Node.js', icon_url='https://cdn.discordapp.com/attachments/866644902628818954/868750639751114752/216800335_547086389761904_6021980829694075076_n.png')
                    await message.channel.send(embed=embed)

                if message.content.startswith("n!invite"):
                    embed = discord.Embed(title="Invite Bot CheckIp", description="Invite Bot", color=0xe303fc)
                    embed.description = "[Invite!](https://discord.com/oauth2/authorize?client_id=869241084377706556&permissions=2148005952&scope=bot)"
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/869212527446335518/869228880827928606/5.jpg')
                    embed.set_footer(text='BOT BY | Node.js', icon_url='https://cdn.discordapp.com/attachments/866644902628818954/868750639751114752/216800335_547086389761904_6021980829694075076_n.png')
                    await message.channel.send(embed=embed)
                            
                if message.content.startswith("n!httpcheck"):
                    req = requests.get(msg[1])
                    embed = discord.Embed(title="htppscheck-Requests", color=0x9875EF)
                    embed.add_field(name="HttpCheck - Successfully",value="```Status : "+str(req.status_code)+"```")
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/869212527446335518/869228880827928606/5.jpg')
                    embed.set_footer(text='BOT BY | Node.js', icon_url='https://cdn.discordapp.com/attachments/866644902628818954/868750639751114752/216800335_547086389761904_6021980829694075076_n.png')
                    await message.channel.send(embed=embed)

                if message.content.startswith("n!ipcheck"):
                    api = "http://ip-api.com/json/"+str(msg[1])
                    req = requests.get(api)
                    data = req.json()
                    embed = discord.Embed(title="Check-Location",description=f'Country: {data["country"]}\nCountry Code: {data["countryCode"]}\nRegion: {data["region"]}\nRegion Name: {data["regionName"]}\nCity: {data["city"]}\nZip Code: {data["zip"]}\nละติจูด: {data["lat"]}\nลองติจูด: {data["lon"]}\nTime Zone: {data["timezone"]}\nISP: {data["isp"]}\nOrganization: {data["org"]}',color=0x03fc03)
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/869212527446335518/869228880827928606/5.jpg')
                    embed.set_footer(text='BOT BY | Node.js', icon_url='https://cdn.discordapp.com/attachments/866644902628818954/868750639751114752/216800335_547086389761904_6021980829694075076_n.png')
                    await message.channel.send(embed=embed)
                if message.content.startswith("n!ping"):
                    try:
                        r = "%.2f" % int(ping(str(msg[1]))*1000)
                        embed = discord.Embed(title="Host : "+str(msg[1])+" Ping : " + str(r) + " ms", color=0x1296f9)
                    except:
                        embed = discord.Embed(title="Host : "+str(msg[1])+" Ping : " + "Request timed out", color=0x1296f9)




client.run(token)