from secret import TOKEN
from secret import apikey
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = TOKEN

bot = telebot.TeleBot(yourkey,parse_mode=None)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    send = (message.text)[7:]
    print(send)
    # TODO: 1.2 Get movie information from the API
    resp = requests.get("http://www.omdbapi.com/?t={0}&apikey={1}".format(send,apikey))
    print(resp.json())
    # TODO: 1.3 Show the movie information in the chat window 
    if (resp.json()['Response'] == 'True'):
        bot.reply_to(message, 'movie found')
        base_url = "https://api.telegram.org/bot5790993091:AAH-GZEtzUwqCR2liGsNB3W5Zj1sub6QpN8/sendPhoto"
        photo_website = str(resp.json()['Poster'])
        name = resp.json()['Title']
        Year = resp.json()['Year']
        Released = resp.json()['Released']
        Rating = resp.json()['imdbRating']
        param = {
            "chat_id" : "644523214",
            "photo" : photo_website,
            "caption" : "Movie Name : {0}\nYear : {1}\nReleased Date : {2}\nImdb Rating : {3}".format(name,Year,Released,Rating)
        }
        resp_img = requests.get(base_url, data = param)
        print(resp_img)
    elif  (resp.json()['Response'] == 'False'):
        bot.reply_to(message, 'movie not found')
        
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    with open('Movie.csv','w') as csvfile:
        fieldnames = ['Movie','Year','Released','imdbRating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
        writer.writeheader()
        writer.writerow({'Movie':name,'Year':Year,'Released':Released,'imdbRating':Rating})
        
     
    
  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    base_url1 = "https://api.telegram.org/bot5790993091:AAH-GZEtzUwqCR2liGsNB3W5Zj1sub6QpN8/sendDocument"
    my_file = open("./Movie.csv","rb")
    parameters1 = {
        "chat_id" : "644523214",
    }
    file = {
        "document" : my_file
    }
    resp1 = requests.get(base_url1,data = parameters1,files = file)
    print(resp1.text)

@bot.message_handler(func=lambda message: botRuning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
