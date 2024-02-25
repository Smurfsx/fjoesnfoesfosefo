from colorama import Back, Fore, Style
import os
import json
from discord.interactions import Interaction
from requests import post, Session, get
from re import search
from random import choice
from string import ascii_uppercase, digits
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
import requests as ru
import discord
from discord import ui
import time
import platform
from datetime import datetime
import pytz
import asyncio
from discord import app_commands
from discord_webhooks import DiscordWebhooks
from discord.ext.commands import Bot
import aiohttp
import uuid
from typing import Any, Coroutine, Literal
import json
from bs4 import BeautifulSoup as bs
from pystyle import Colors, Colorate
import itertools
from discord import SyncWebhook
import requests
from re import match
import sys
import subprocess
from promptpay import qrcode
import itertools
from discord import Activity, ActivityType, Status
import interactions
import os 
import platform
import random
import requests
from interactions import *

from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://axocoder.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Axo")

now_utc = datetime.utcnow()
desired_timezone = 'Asia/Bangkok'  # เปลี่ยนตามที่ต้องการ
OWNERS = (1168831563086172212)
token = "MTIxMTI1NzIyOTM3ODg1NDkyMg.G4C3IT.YkgH55MdHywYf17hf7-Otr_hizD4nflvDo1jik"
# แปลงเวลาปัจจุบันเป็น time zone ที่ต้องการ
now_desired_timezone = now_utc.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(desired_timezone))
formatted_time = now_desired_timezone.strftime("%Y-%m-%d %H:%M:%S")  
alert1 = "ได้สร้าง Embed แล้วที่ ช่อง"
Alert = "> <:awoo:1187994363855380592>  คุณไม่มีสิทธิ์ หรือ การอนุณาติที่สามารถใช้คำสั่งนี้ได้คะ "
avatarbot = "https://media.discordapp.net/attachments/1205061777235378236/1205067657393737728/7fff4581bf927300ee17cd02ef57b235.jpg?ex=65d705b6&is=65c490b6&hm=727ea22517b250f83f2465081cedd31d3ee91be2f103b10fc640b32b5fc6bfde&=&format=webp&width=554&height=684"
code_file = 'gencode_data.json'
items_file = 'items_data.json'
phone = "0627489222"
topup_id = 1211258618167558145
buy_id = 1211258531249000468
saveroles_id = 1205056554785574922



with open('Download.json') as config_file:
    data = json.load(config_file)

V1 = data['Download_v1']
V2 = data['Download_v2']
V3 = data['Download_v3']
V4 = data['Download_v4']
V5 = data['Download_v5']
V6 = data['Download_v6']



# ชื่อสินค้า

SHOP1 = "AOB FIVEM"
SHOP1_Description = "โปรแกรม AOB FIVM"

SHOP2 = "POINTER FIVEM [รออัพเดท]"
SHOP2_Description = "Pointer"

SHOP3 = "[รออัพเดท]"
SHOP3_Description = "Wait update..."










# ไฟล์ KEY เปลี่ยน V ด้วย
KEY_V1 = "Stock/Rockstar.txt"
# KEY_V1 = "KEY.txt"
# KEY_V1 = "KEY.txt"
# KEY_V1 = "KEY.txt"
# KEY_V1 = "KEY.txt"













# โหลดข้อมูลจากไฟล์ JSON
try:
    with open('money_data.json', 'r') as f:
        money_data = json.load(f)
except json.decoder.JSONDecodeError:
    # กรณีที่เกิด JSONDecodeError ให้สร้างไฟล์ JSON ใหม่
    money_data = {}
    with open('money_data.json', 'w') as f:
        json.dump(money_data, f)


class PromptPayModal(ui.Modal, title="ระบบเติมเงินแบบ PromptPay"):

    amount = ui.TextInput(label="จำนวนเงินที่ต้องการเติม", placeholder="ตัวเลขจำนวนเงิน เช่นอยากเติม 10 บาท เขียน (10)", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        phone = '0658503179'  # Default value
        amount = float(self.amount.value)  # Convert to float
        payload_with_amount = qrcode.generate_payload(phone, amount)

        # Specify the directory named "PromptPay" where you want to save the image
        save_directory = "PromptPay"

        # Ensure the directory exists, if not, create it
        os.makedirs(save_directory, exist_ok=True)

        filename = os.path.join(save_directory, f"qrcode-{phone}-amount-{amount}.png")
        qrcode.to_file(payload_with_amount, filename)

        # Send the image in the Discord channel
        with open(filename, "rb") as file:
            qr_file = discord.File(file, filename=filename)
            embed = discord.Embed(
                title="ระบบ PromptPay สแกนจ่ายเงิน",
                description="`สแกน QRCODE ด่านบนนี้ได้เลย`",
                color=0x4188ff
            )
            embed.set_image(url="attachment://" + filename)
            await interaction.response.send_message(embed=embed, file=qr_file, ephemeral=True)

class Topup(ui.Modal, title="ระบบเติมเงินโดยอังเป๋า"):
    topup = ui.TextInput(label="โดเนทผ่าน TrueMoney", placeholder="กรอกลิงค์ซองอั่งเปา", style=discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        topup_value = self.topup.value

        if not match(r"https:\/\/gift\.truemoney\.com\/campaign\/\?v=+[a-zA-Z0-9]{18}", topup_value):
            await interaction.response.send_message("> เติมเงินไม่สำเร็จรหัสผิดพลาด", ephemeral=True)
            return

        voucher_code = topup_value.split("?v=")[1]
        response = requests.post(
            f"https://gift.truemoney.com/campaign/vouchers/{voucher_code}/redeem",
            json={"mobile": phone, "voucher_hash": voucher_code},
            headers={
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                "Content-Type": "application/json",
                "Origin": "https://gift.truemoney.com",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
            },
        )
        redeemdata = response.json()

        if response.status_code == 200 and redeemdata["status"]["code"] == "SUCCESS":
            amount = float(redeemdata["data"]["my_ticket"]["amount_baht"])

            # เพิ่มเงินให้สมาชิก
            if str(interaction.user.id) not in money_data:
                money_data[str(interaction.user.id)] = 0
            money_data[str(interaction.user.id)] += amount

            # บันทึกข้อมูลลงในไฟล์ JSON
            with open('money_data.json', 'w') as f:
                json.dump(money_data, f)
            
            done = discord.Embed(
                description=f'`✅ : เติมเงินสำเร็จ` `|` จำนวน `{amount}` บาท', color=0x32CD32
            )
            await interaction.response.send_message(embed=done, ephemeral=True)

            channel = client.get_channel(topup_id)  # แก้ไข ID ของช่องที่ต้องการแจ้งเตือน
            user = interaction.user
            embed = discord.Embed(
                title="🏦 ระบบแจ้งเตือนการเติมเงิน",
                description=f"\n`✅` `:` เติมเงินสำเร็จ ทางเราได้ Add Money ให้คุณเรียบร้อยแล้วคะ \n\n คุณ : {interaction.user.mention} \n\n เติมเงินเข้ามาเป็นจำนวนเงิน : {amount} บาท\nระบบอังเป๋า :\n ```{topup_value}```",
                color=0xff0000,
            )
            embed.set_author(name="ระบบขายยศอัติโนมัติ", url="", icon_url=avatarbot)          
            embed.set_thumbnail(url=user.avatar.url)
            
    
            await channel.send(embed=embed)

        if response.status_code == 400 or response.status_code == 410:
            await interaction.response.send_message(
                "ซองอั่งเปานี้ถูกใช้ไปแล้ว หรือ ใส่ลิงค์ให้ถูก ", ephemeral=True)
##################################################### เมนู


class market(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.value = None
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 6000, commands.BucketType.user)
    @discord.ui.button(label="Rockstar ID",emoji="<:Rockstar_Games_Logo:1211207575316467712>", style=discord.ButtonStyle.red, custom_id="rockstar_id")
    async def rockstarsell(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed=discord.Embed(title="",description="",color=0xff2c2c)
        embed.set_author(name="Seller Rockstar FiveM", url="", icon_url=avatarbot)  
        embed.add_field(name="> กรุณาอ่านก่อนซื้อ", value="**หากคุณทำการซื้อไปแล้ว จะไม่คืนเงินทั้งสิน ยกเว้น จะมีข้อผิดพลาดของทางร้านเช่น Rockstar เข้าไม่ได้ , Rockstar ไม่มีเกมส์ มีปัญหาอื่นๆ กด Ticket > <#1210518444655644702>**", inline=False)
        # embed.add_field(name="วิดีโอตัวอย่าง", value="[คลิ๊กที่นี่เพื่อดูวิดีโอ](https://www.youtube.com/)", inline=False)
        embed.set_image(url="https://media-rockstargames-com.akamaized.net/tina-uploads/posts/8971o8789584a4/f6d5b66356959d032c06b15f8e0a3d3da269b1c8.jpg")
        message = await interaction.response.send_message(content="", embed=embed, view=shopv1(), ephemeral=True)
        
    @discord.ui.button(label="🧧「อั่งเปา」", style=discord.ButtonStyle.primary, custom_id="market_id1")
    async def market1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Topup())

    @discord.ui.button(label="🏦「ธนาคาร」", style=discord.ButtonStyle.red, custom_id="market_id2")
    async def market2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(content="เติมเงินด้วยธนาคาร กรุณากด Ticket > <#1210518444655644702>", ephemeral=True) #view=market1()

    @discord.ui.button(label="💰「เช็คยอดเงิน」", style=discord.ButtonStyle.green, custom_id="market_id3")
    async def market3(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user      
        user_id = str(interaction.user.id)  # เปลี่ยน interaction.author เป็น interaction.user
        money = money_data.get(user_id, 0)
        if money == 0:
                    embed = discord.Embed(title="ระบบเช็คยอดเงิน", description=f"`❌` `:` กรุณาเติมเงินเพื่อเปิดเข้าใช้งานเปิดบัญชี หรือ เงินในบัญชีหมด", color=0x15ff00)
                    embed.set_author(name="ระบบขายยศอัติโนมัติ", url="", icon_url=avatarbot)
                    embed.set_thumbnail(url=user.avatar.url)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
                    embed = discord.Embed(title="ระบบเช็คยอดเงิน", description=f"`💸` `:` คุณมีเงินจำนวนในระบบอยู่ : {money} บาท", color=0x15ff00)
                    embed.set_author(name="ระบบขายยศอัติโนมัติ", url="", icon_url=avatarbot)
                    embed.set_thumbnail(url=user.avatar.url)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
    @discord.ui.button(label="Check Rockstar",emoji="<:Rockstar_Games_Logo:1211207575316467712>", style=discord.ButtonStyle.gray, custom_id="check_rockstar")
    async def checkrockstar(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open("Stock/Rockstar.txt", "r") as file:
            checkrockstar = sum(1 for line in file)
        embed=discord.Embed(title="",description="",color=0xff2c2c)
        embed.set_author(name="Check Rockstar FiveM", url="", icon_url=avatarbot)  
        embed.add_field(name="Rockstar คงเหลือ", value=f"**> {checkrockstar}**", inline=False)
        message = await interaction.response.send_message(content="", embed=embed, ephemeral=True)
        
        
        
        
        
class shopv1(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="ยืนยืนการสั่งซื้อ",emoji="<:checkmark:1187994587650850886> ", style=discord.ButtonStyle.green, custom_id="shopv1_id1")
    async def shopv1(self, interaction: discord.Interaction, button: discord.ui.Button):
        item_name = "item1"

        # ซื้อของโดยใช้เงิน
        user_id = str(interaction.user.id)  # Using interaction.user instead of ctx.author

        try:
            with open(items_file, 'r') as f:
                items_data = json.load(f)
        except json.decoder.JSONDecodeError:
            items_data = {}

        if item_name in items_data:
            item_price = items_data[item_name]['price']
            if user_id in money_data and money_data[user_id] >= item_price:
                money_data[user_id] -= item_price
                update_money_data()
                money = money_data.get(user_id, 0)
                user = interaction.user
                channel = client.get_channel(buy_id)
                embed = discord.Embed(
                title="Logs Buy",
                description=f"> User : {interaction.user} \n > Buy : Rockstar \n > Money  : {money}",
                )
                await channel.send(embed=embed)
                embed=discord.Embed(title="",description="",color=0xff2c2c)
                embed.set_author(name="Notifications", url="", icon_url=avatarbot)  
                embed.add_field(name="", value="**> กรุณาเช็ค ข้อความส่วนตัวของคุณ**", inline=False)
                message = await interaction.response.send_message(content="", embed=embed, ephemeral=True)
                with open(f"{KEY_V1}", "r") as file:
                        first_line = file.readline().strip()

                with open(f"{KEY_V1}", "r") as file:
                    lines = file.readlines()

                with open(f"{KEY_V1}", "w") as file:
                    file.writelines(lines[1:]) 
                embed=discord.Embed(title="Rockstar ID PASS",description=f"**Rockstar : ```{first_line}```**")
                embed.set_author(name="", url="")  
                await interaction.user.send(content="", embed=embed)
            else:
                await interaction.response.edit_message(content=f'`❌` `:` เงินของคุณไม่พอสำหรับการสั่งซื้อ จำนวนเงิน {item_price} บาท', embed=None ,view=None)
        else:
            await interaction.response.send_message(f'{item_name} is not available for purchase.')


    @discord.ui.button(label="ยกเลิก",emoji="<:Yes:1187994016269205604> ", style=discord.ButtonStyle.red, custom_id="botdonate_id2")
    async def botdonate2(self, interaction: discord.Interaction, button: discord.ui.Button):
         message = await interaction.response.edit_message(content="ยกเลิกการสั่งซื้อสำเร็จ", embed=None, view=None)



##################################  Front1
        
        
# class market1(discord.ui.View):
#     def __init__(self) -> None:
#         super().__init__(timeout=None)      
#     @discord.ui.button(label="สร้าง QR PROMTPAY",emoji="<:PPbbx:1193528947468673057> ", style=discord.ButtonStyle.primary, custom_id="market1_id1")
#     async def market1(self, interaction: discord.Interaction, button: discord.ui.Button):
#         await interaction.response.send_modal(PromptPayModal())
        


##################################  on_ready
class aclient(commands.Bot):
    def __init__(self): 
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())
        self.role = None

    async def on_ready(self):
        os.system('cls')
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        activity = discord.Streaming(name="Combat - Shop", url="https://www.twitch.tv/Dekbangtlez")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) + " Commands")
        self.add_view(market())





client = aclient()


@client.tree.command(name='setupmarket', description='ใส่ ID CHANNEL (ADMINONLY)')
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(channel_id='ตัวอย่าง 1193256543974592574')
async def modal(interaction: commands.Context, channel_id: str): 
      embed=discord.Embed(title="",description="",color=0xff0000)
      embed.set_author(name="Combat Shop - Rockstar FiveM", url="")
      embed.add_field(name="> Rockstar?", value="**เข้าได้แค่Fivem หรือเอาไปปลดแบน เซิฟเวอร์ที่โดนแบนจากกันโปร\nรับประกันหลังการซื้อ 1 วัน\nอัดคลิปตั้งแต่ซื้อจนถึงใส่รหัสเข้าFivem**", inline=False)
      embed.add_field(name="> Claim Rockstar", value="**รหัสไม่มีเกมส์\nรหัสผิด\n*สำคัญ ก่อนเคลมต้องอัดคริปตอนซื้อ - ตอนเข้ารหัส**", inline=False)
      embed.add_field(name="> Price", value="**ราคา 30 บาท**", inline=False)
      embed.set_image(url="https://www.the-sun.com/wp-content/uploads/sites/6/2023/12/PGONCHAR_W9279jpg-JS730571119.jpg")
      channel = client.get_channel(int(channel_id))
      await interaction.response.send_message(f'ได้สร้างคำสั่งบนห้อง <#{channel_id}>', ephemeral=True)
      await channel.send(embed=embed, view=market())
@modal.error
async def modal_error(interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingPermissions):
            await interaction.response.send_message(f"{Alert}", ephemeral=True)

@client.tree.command(name='checkpoint', description='คำสั่งเช็คเงิน (ADMINONLY)')
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(member='ผู้ใช้งาน')
async def check_money(interaction: discord.Interaction, member: discord.Member):
    money = money_data.get(str(member.id), 0)
    embed = discord.Embed(
    title="เช็คยอดเงิน",
    description=f"```👤 คุณ``` {member.name} \n🧧 ```มียอดเงินคงเหลือ``` : {money} บาท",
    color=0x15ff00
    )
    embed.set_author(name="ระบบขายยศอัติโนมัติ", url="", icon_url=avatarbot, ephemeral=True)
    await interaction.response.send_message(embed=embed)
    # await interaction.response.send_message(f'ผู้ใช้ {member.name} มียอดเงิน {money} บาท', ephemeral=True)
@check_money.error
async def check_money(interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingPermissions):
            await interaction.response.send_message(f"{Alert}", ephemeral=True)













def update_money_data():
    # บันทึกข้อมูลเงินลงในไฟล์ JSON
    with open('money_data.json', 'w') as f:
        json.dump(money_data, f)

def get_leaderboard(limit):
    # ดึงข้อมูลอันดับเงินเยอะที่สุดจากไฟล์ JSON
    sorted_leaderboard = sorted(money_data.items(), key=lambda x: x[1], reverse=True)
    return sorted_leaderboard[:limit]

def remove_code(code):
    # ลบรหัสออกจากรายการและบันทึกข้อมูลลงในไฟล์ JSON
    try:
        with open(code_file, 'r') as f:
            code_data = json.load(f)
    except json.decoder.JSONDecodeError:
        code_data = {}

    if code in code_data:
        del code_data[code]
        save_code_data_after_removal(code_data)
        return True
    return False

def save_code_data_after_removal(code_data):
    # บันทึกข้อมูลรหัสลงในไฟล์ JSON หลังจากการลบ
    with open(code_file, 'w') as f:
        json.dump(code_data, f)

def set_money_amount(member, amount):
    # ตั้งค่าจำนวนเงินของสมาชิกและบันทึกข้อมูลลงในไฟล์ JSON
    user_id = str(member.id)
    money_data[user_id] = amount

    update_money_data()

client.run(token)
