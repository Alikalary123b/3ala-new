# ⌯ Hey, Bro This File Code By : HASSIEN
# ⌯ Syntx : Python3
# ⌯ This File Is Free !!
# ⌯ Devlloper Channel : @Z_L_N
# ⌯ Thanks You Bro Enjoy
#====================================#
import telebot
import requests
from telebot import types
#-----------[ Colors ]-----------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
r = "1234567890"
#------------------------------[Start CoDe]------------------------------
token = input(f'{B} [{C}⌯{X}] {C}ENTER TOKEN{X} » ' + C)
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- Check ❤️‍🔥",callback_data = 'check')

#----#

@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Welcome to Paid Proxy Check Bot 
- - - - - - - - - - 
Developer: @N_P_X 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	log(call.message)
    if call.data == 'gen':
        gen(call.message)
        
def log(message):
 k = 0
 f = 0
 bot.send_message(message.chat.id,f"Now Started!")
@bot.message_handler(func=lambda m: True)
def proxy(message):
    if ("check") in message.text:
        prox = ""
        urlsd = ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes"
        ]
        for url in urlsd:
            prox += requests.get(url).text
            proxys = prox.split('\r\n')
            bot.send_message(message.chat.id,proxys)

bot.polling()