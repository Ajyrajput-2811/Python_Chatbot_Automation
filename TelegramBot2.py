import telegram

import requests

import datetime


from telegram.bot import Bot

bot = telegram.Bot(token="5953779084:AAH7X7KJ-ZNQ8c4oeEia2JfLSGLzdiJxKKI")

from telegram.ext import Updater , CommandHandler , MessageHandler

updater = Updater(token="5953779084:AAH7X7KJ-ZNQ8c4oeEia2JfLSGLzdiJxKKI" , use_context = True)

dispatcher = updater.dispatcher

#response send by Bot

def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id , text='Hii, How i can help you😊.')


def start (update,context):
   context.bot.send_message( chat_id=update.effective_chat.id  ,text='Hello,start your journey with us.')

def youtube_url(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Here your youtubeurl ==> www.youtube.com')    

def google_url(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Here your googleurl ==> www.google.com')    

def facebook_url(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Here your facebook_url ==> www.facebook.com')  

def help(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id , text=
    """
    There are few command that can you use:
     /start --> start your bot
    /youtube --> Give it  to you youtube url
    /google -->  Give it  to you google url
    /facebook --> Give it  to you facebook url
    /Linkedin_url --> your linkedin_url
    /quote --> for generate quote
    /by 
    
    """
    )   

def linkedin(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id , text='Here your linkedin_url ==> www.linkedin.com/in/Ajay-Rajput2811') 

def getQuote(update,context):
    response =requests.get('https://dummyjson.com/quotes/random')
    if(response.status_code==200):
        data = response.json()
        print(data['quote'])
        context.bot.send_message(chat_id=update.effective_chat.id,text = data['quote'])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id , text ='Error,something went wrong!')   

def sendBy(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Nice talking to you.👍' )        



### Handler

hello_handler = CommandHandler('hello',hello)
dispatcher.add_handler(hello_handler)

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)


youtube_handler = CommandHandler('youtube',youtube_url)
dispatcher.add_handler(youtube_handler)


google_handler = CommandHandler('google',google_url)
dispatcher.add_handler(google_handler)


facebook_handler = CommandHandler('facebook',facebook_url)
dispatcher.add_handler(facebook_handler)


help_handler = CommandHandler('help',help)
dispatcher.add_handler(help_handler)

linkedin_handler = CommandHandler('Mylinkedin_url',linkedin)
dispatcher.add_handler(linkedin_handler)

quote_handler = CommandHandler('quote',getQuote)
dispatcher.add_handler(quote_handler)

sendingBy_handler = CommandHandler('by',sendBy)
dispatcher.add_handler(sendingBy_handler)


updater.start_polling()
updater.idle()