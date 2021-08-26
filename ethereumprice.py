import requests
response = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot')
data = response.json()
currency = data["data"]["currency"]
price = data["data"]["amount"]


@client.command()
async def eth(ctx):
    embed=discord.Embed(title="Sourced from CoinBase", description="Crypto Commands", color=0x716b94)
    embed.set_author(name=f'{price}', url="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjegIWqp83xAhUMa80KHfa5DWsQwqsBMAB6BAgHEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DoHg5SJYRHA0&usg=AOvVaw0mZdY4jTnKHqwk07LTTExU")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/861439360989396993/861793644951371796/toppng.com-ethereum-purple-blue-icon-1600x1600.png")
    embed.add_field(name="Developed By Spy", value="", inline=True)
    embed.add_field(name="Bot Version 2", value="", inline=True)
    embed.set_footer(text="Used [COMMANDNAMEHERE] !")
    await ctx.send(embed=embed)