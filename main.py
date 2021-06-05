import telebot
from telebot.apihelper import send_message
from telebot.types import Chat
import requests
import json
API_KEY = "1885106886:AAFBE8K_lo8-9YXifJjXPSKlXpWfqR_VDMg"

BSC_API_KEY = 'HG1TZJPJHNAMFR61UAF94QWA5KABX6YSD2'

BNC_KEY = "qAY5a041gEgMiodImKqOVbrMoVzaiKL9KisqfQcFIn7ANgX6nsMwdM7SRR39qJbU"
BNC_SEC = "XXvNVVTGJLntmDb5UpnLADOwXgZXL3OjUoV0pawQDDwadICmsAy8SXuPu6XkutQf"


WBNB_CONTRACT = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
WBNB_ADDRESS = '0xcaa6991DE146D316B15d92C33D8D07aEF972ABE2'
WBNB_DECIMA = 18


LITC_CONTRACT = '0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb'
LICT_ADDRESS = '0xcaa6991DE146D316B15d92C33D8D07aEF972ABE2'
LITC_DECIMA  = 9

def getPrice():
    data = open("pricupdate.json")
    price = json.load(data)
    x = price['price']
    return x
    
bot = telebot.TeleBot(API_KEY)

try:
    @bot.message_handler(content_types=["new_chat_members"])
    def newMember(message):
        bot.send_message(message.chat.id, text='''
    🥳 Hey there , Welcome to the LITC !🥳

    🔥🔥🔥 <a href="https://twitter.com/libitcat/status/1400074739100512263">AMA Event @12th of July 2021</a>

    Type <a href="#">command /start</a> to start help command list.

    🔥 About <a href="https://libitcat.finance">LITC</a>

    🔥 About <a href="#">Current /price of LITC</a>

    🔥 Buy LITC 💰 <a href="https://www.dextools.io/app/pancakeswap/pair-explorer/0xcaa6991de146d316b15d92c33d8d07aef972abe2">BNB/LITC on DEXT (updating)</a> | 💰 <a href="https://poocoin.app/tokens/0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb">BNB/LITC on Poocoin</a>

    Thanks you, 
    LITC Team.''',disable_web_page_preview = True,reply_markup=None,parse_mode='HTML')

    @bot.message_handler(commands=["price"])
    def love(message):
        bot.send_message(message.chat.id, text='''
    <strong> Current price  🔥🔥🔥</strong>
    1 LICT
    🔥🔥🔥{0}  
    '''.format(getPrice()),reply_markup=None,parse_mode='HTML')

    @bot.message_handler(commands=["shill"])
    def love(message):
        bot.send_message(message.chat.id, text='''
    <strong>I Love My LITC 🥰🥰🥰  😍😍😍</strong>

    <strong> SHARE THE LIBITCAT.FINANCE WITH YOUR FRIENDS  🥳🥳🥳</strong>

    <strong>Buy 🚀 Buy 🚀 Buy 🚀</strong>

    <strong>GET 🚀 MORE 🚀 RICH 🚀 TOGETHER 🚀</strong>

    🚀🚀🚀🚀🚀''',reply_markup=None,parse_mode='HTML')


    @bot.message_handler(commands="[start]")
    def start(message):
        bot.send_message(message.chat.id, text='''
    Type <a href="#start">command start</a> to start help command list.

    🔥 About <a href="https://libitcat.finance">LITC</a>

    🔥 Current Price <a href="#">/price</a>

    🔥 Buy LITC 💰 <a href="https://www.dextools.io/app/pancakeswap/pair-explorer/0xcaa6991de146d316b15d92c33d8d07aef972abe2">BNB/LITC on DEXT (updating)</a> | 💰 <a href="https://poocoin.app/tokens/0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb">BNB/LITC on Poocoin</a>

    🔥 SHILL Content to Viral <a href="#">/shill</a>

    🔥 OUR PROGRAMS <a href="#">/program</a>

    🔥 <a href="https://docs.google.com/forms/d/e/1FAIpQLScqSn5sqgpebIaafpNvHq2QtYIUMp3J7EJpWZzLHo4RLSy-jg/viewform">SWAPPED FOR OLD TOKENS</a>

    Thanks you, 
    LITC Team.''',disable_web_page_preview = True,reply_markup=None,parse_mode='HTML')

    @bot.message_handler(commands=["LITC"])
    def dingu(message):
        bot.send_message(message.chat.id, text='''

    <strong>Welcome to LITC</strong>

    Token Name: <strong>LITC</strong>

    🔥 <a href="https://docs.google.com/forms/d/e/1FAIpQLScqSn5sqgpebIaafpNvHq2QtYIUMp3J7EJpWZzLHo4RLSy-jg/viewform">SWAPPED FOR OLD TOKENS</a>

    🔥🔥🔥 <a href="https://twitter.com/libitcat/status/1400074739100512263">AMA Event @12 July 2021</a>

    <strong>Contract Address: 0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb</strong>

    📈 <a href="https://poocoin.app/tokens/0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb">Chart</a> | 📈 <a href="https://www.dextools.io/app/pancakeswap/pair-explorer/0xcaa6991de146d316b15d92c33d8d07aef972abe2">Chart</a>

    💰 <a href="https://www.dextools.io/app/pancakeswap/pair-explorer/0xcaa6991de146d316b15d92c33d8d07aef972abe2">BNB/LITC on DEXT</a> | 💰 <a href="https://poocoin.app/tokens/0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb"> BNB/LITC on Poocoin</a>

    📝 <a href="https://bscscan.com/token/0x395678a4bab1cfe77bed9ddadca47b89a2b85dbb">BSCSCAN</a> | 🌍 <a href="https://libitcat.finance">WEBSITE</a>

    🐦 <a href="https://twitter.com/libitcat">TWITTER</a> | 💬 <a href="https://t.me/LibitcatFinance">TELEGRAM</a>

    🔈  <a href="https://vt.tiktok.com/ZSJHkkDKy">Tiktok </a>''',disable_web_page_preview = True,reply_markup=None,parse_mode='HTML') 

    @bot.message_handler(commands="[/program]")
    def program(message):
        bot.send_message(message.chat.id, text='''

    🤩🤩🤩 TIKTOK | YOUTUBE LIBITCAT AIRDROP  🤩🤩🤩

    🔥 4000 views = $30 🥇

    🔥 100k views = $400 🏆

    😉 Terms and Conditions: Inside your video content must include Libitcat token name and a link to libitcat.finance

    ✨ HOW TO GET THE BOUNTY  ✨

    ✨ POST THE LINK OF VIDEO ON YOUTUBE OR TIKTOK INCLUDING YOUR CHANNEL ID WITH A SCREENSHOT ✨

    ✨ ✨ ✨

    Thanks you, 
    LITC Team.''',disable_web_page_preview = True,reply_markup=None,parse_mode='HTML')

except:
    pass

bot.polling(none_stop=False, interval=1)
