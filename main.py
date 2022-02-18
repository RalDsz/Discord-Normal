#Code info:
#Made by Ralston Dsouza
#Secret Token used:OTE3MzI0NjQzNTAzODQxMzEz.Ya3DJg.B8c-SxNE_w371Z1QkaG2oO7ft7g
#Webserver by @adityagarwal121
#latest update 05/01/22

from webserver import keep_alive
import random
from discord.ext import commands
import discord
import time
import string

filtered_words = ["suck"]


def main():
    client = commands.Bot(command_prefix="O! ")
    client.remove_command("help")

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    @client.command(aliases=["h",'H'])
    async def help(ctx):
        em = discord.Embed(title="COMMAND HELP:",
                           description="",
                           color=16777215)
        em.add_field(name="★O! heybot",
                     value="This is a basic command that greets you back.")
        em.add_field(name="★O! info", value="Shows info about ORBT")
        em.add_field(name="★ randnum",
                     value="Generates a Random munber upto 10000")
        em.add_field(name="★O! genpass",
                     value="Generates a unique 10 digit password")
        em.add_field(name="★O! mentionme", value="mentions you")
        em.add_field(name="★O! credits",
                     value="Gives credit to all the developers of the bot")
        em.add_field(name="★O! ping",
                     value="Get the bot's current websocket latency.")
        em.add_field(name="★O! shop",
                     value="Get the bot's current websocket latency.")
        em.add_field(name="★O! buy",
                     value="Get the bot's current websocket latency.")
        em.add_field(name="★O! sell",
                     value="Get the bot's current websocket latency.")
        em.set_footer(text=f"Requested By: {ctx.author.name}",
                      icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=em)

    @client.command(aliases=["filter",'g'])
    async def heelp(ctx):
        em = discord.Embed(title="COMMAND HELP:",
                           description="",
                           color=16777215)
        em.add_field(name="★O! heybot",
                     value="This is a basic command that greets you back.", inline = False)
        em.add_field(name="★O! info", value="Shows info about ORBT")
        em.add_field(name="★ randnum",
                     value="Generates a Random munber upto 10000")
        em.add_field(name="★O! genpass",
                     value="Generates a unique 10 digit password")
        em.add_field(name="★O! mentionme", value="mentions you")
        em.add_field(name="★O! credits",
                     value="Gives credit to all the developers of the bot")
        em.add_field(name="★O! ping",
                     value="Get the bot's current websocket latency.")
        em.add_field(name="★O! shop",
                     value="Get the bot's current websocket latency.")
        em.add_field(name="★O! buy",
                     value="Get the bot's current websocket latency.")
        em.add_field(name="★O! sell",
                     value="Get the bot's current websocket latency.")
        em.set_footer(text=f"Requested By: {ctx.author.name}",
                      icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=em)

    @client.command(aliases=['hi', 'Hi'])
    async def heybot(ctx):
        """Replies back to ypu saying Hi"""
        await ctx.send(f"{ctx.author.mention} Hello to you! 👋 ")

    @client.command(aliases=["i",'I'])
    async def info(ctx):
        """Shows info about RalBot"""
        await ctx.send(
            f" {ctx.author.mention} This is RalBot, a Super Cool Multi Talented and Multi functional bot \n Made my RalDsz "
        )

    @client.command(aliases=['rn','Rn'])
    async def randnum(ctx):
        """ Generates a Random munber upto 10000"""
        await ctx.send(
            f"{ctx.author.mention}Your randomly generated munber is :{random.randrange(10000)}"
        )

    @client.command(aliases=["gp",'Gp'])
    async def genpass(ctx):
        """Generates a 10 digit password"""
        await ctx.send(''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(10)))

    @client.command(aliases=["MM",'Mm'])
    async def mentionme(ctx):
        """Mentions you"""
        await ctx.send(f" {ctx.author.mention}  ")

    @client.command(aliases=["Cr",'CR'])
    async def credits(ctx):
        """ Gives credit to all the developers of the bot """
        await ctx.send(
            f" {ctx.author.mention} Credits: \n This bot was developed my Ralston Dsouza using the Discord.py library \n To get the source code please click here: https://github.com/RalDsz/ORBT \nPLEASE CLICK HERE FOR SPONSORS https://www.paypal.com/paypalme/RalDsz Huge thanks to everyone who has tested  my bot \nSpecial thanks to Yash Bhatia\n Signing off,\n Ralston Dsouza"
        )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel()

        await channel.send(f"Welcome, {member}!Thank you for joining this server and helping ORBT grow :)")

    @client.command(name="ping")
    async def ping(ctx):
        """Get the bot's current websocket and API latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(
            content=
            f"Your latency is{round(ctx.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms \n Requested by:  {ctx.author.name}"
        )

    @client.event
    async def on_message(msg):
        for word in filtered_words:
            if word in msg.content:
                await msg.delete()

        await client.process_commands(msg)

    @client.command(aliases=['Dn', 'dn', 'dN',])
    async def donate(ctx):
        """Replies back to you saying Hi"""
        await ctx.send(f" ***Thank you so much for considering donating!!!*** \n You are helping the employees at RalDsz follow their vision, *building better tech, everyday!* \n You can donate here :smiley:\n https://paypal.me/RalDsz")

    client.run('OTE3MzI0NjQzNTAzODQxMzEz.Ya3DJg.fyi7Pb-fIEGbycI2qiL1p0Wa2bE')


keep_alive()

if __name__ == '__main__':
    main()

# END OF CODE BY RALSTON Dsouza
# FOR ANY HELP PLS CONTACT "megagravity.dsz@gmail.com"
# Wishing you a Wonderful day!
#Thank you all for making this project wonderful
