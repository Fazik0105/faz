from multiprocessing.reduction import send_handle
import telebot 
from telebot import types


TOKEN = '5210173851:AAFfJtFrsjZDLe9sYsNpq9lvPit2n9DOksM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','START'])
def start(message):
    bot.send_message(message.chat.id,' PAROLNI TERING!!!πππ')

@bot.message_handler(commands=['assalam','ASSALAM','Assalam'])
def mrfoosh(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Arab tili grammatikasiπ')
    item2 = types.KeyboardButton('Arab tili fonetikasi π£π')
    markup.add(item1,item2)
    
    bot.send_message(message.chat.id,'Assalomu alaykum,{0.first_name}!'.format(message.from_user),reply_markup=markup)
   
#####################################"""""birinchi_bolim""""""######################################################

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Arab tili grammatikasiπ':
             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
             item1 = types.KeyboardButton('πΉ video-darslik πΉ')
             item2 = types.KeyboardButton('π§ ovozli-darslar π§')
             back = types.KeyboardButton('π')
             markup.add(item1, item2,back)
             
             bot.send_message(message.chat.id,'π',reply_markup=markup)
             
        elif message.text == 'πΉ video-darslik πΉ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1π')
            item2 = types.KeyboardButton('2π')
            item3 = types.KeyboardButton('3π')
            item4 = types.KeyboardButton('4π')
            item5 = types.KeyboardButton('5π')
            item6 = types.KeyboardButton('6π')
            item7 = types.KeyboardButton('7π')
            item8 = types.KeyboardButton('8π')
            item9 = types.KeyboardButton('9π')
            item10 = types.KeyboardButton('10π')
            item11 = types.KeyboardButton('11π')
            item12 = types.KeyboardButton('12π')
            item13 = types.KeyboardButton('13π')
            item14 = types.KeyboardButton('14π')
            item15 = types.KeyboardButton('15π')
            item16 = types.KeyboardButton('16π')
            item17 = types.KeyboardButton('17π')
            item18 = types.KeyboardButton('18π')
            item19 = types.KeyboardButton('19π')
            back = types.KeyboardButton('π.')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,item11,item12,item13,item14,item15,item16,item17,item18,item19, back)
            
            bot.send_message(message.chat.id,'π',reply_markup=markup)
            
        elif message.text == 'π§ ovozli-darslar π§':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('π§ 1-audio π§')
            item2 = types.KeyboardButton('π§ 2-audio π§')
            item3 = types.KeyboardButton('π§ 3-audio π§')
            item4 = types.KeyboardButton('π§ 4-audio π§')
            item5 = types.KeyboardButton('π§ 5-audio π§')
            item6 = types.KeyboardButton('π§ 6-audio π§')
            item7 = types.KeyboardButton('π§ 7-audio π§')
            item8 = types.KeyboardButton('π§ 8-audio π§')
            item9 = types.KeyboardButton('π§ 9-audio π§')
            item10 = types.KeyboardButton('π§ 10-audio π§')
            item11 = types.KeyboardButton('π§ 11-audio π§')
            item12 = types.KeyboardButton('π§ 12-audio π§')
            item13 = types.KeyboardButton('π§ 13-audio π§')
            item14 = types.KeyboardButton('π§ 14-audio π§')
            item15 = types.KeyboardButton('π§ 15-audio π§')
            item16 = types.KeyboardButton('π§ 16-audio π§')
            item17 = types.KeyboardButton('π§ 17-audio π§')
            item18 = types.KeyboardButton('π§ 18-audio π§')
            item19 = types.KeyboardButton('π§ 19-audio π§')
            back = types.KeyboardButton('π.')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,item11,item12,item13,item14,item15,item16,item17,item18,item19, back)
            
            bot.send_message(message.chat.id,'π§',reply_markup=markup)
            
            
        elif message.text == 'π.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('πΉ video-darslik πΉ')
            item2 = types.KeyboardButton('π§ ovozli-darslar π§')
            back = types.KeyboardButton('π')
            markup.add(item1, item2,back)
            
            bot.send_message(message.chat.id,'π.',reply_markup=markup)
            
#######################################""""ARAB FONETIKASI""""##################################################################


        
        elif message.text == 'Arab tili fonetikasi π£π':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1-darsπ£')
            item2 = types.KeyboardButton('2-darsπ£')
            item3 = types.KeyboardButton('3-darsπ£')
            item4 = types.KeyboardButton('4-darsπ£')
            item5 = types.KeyboardButton('5-darsπ£')
            item6 = types.KeyboardButton('6-darsπ£')
            item7 = types.KeyboardButton('7-darsπ£')
            item8 = types.KeyboardButton('8-darsπ£')
            item9 = types.KeyboardButton('9-darsπ£')
            item10 = types.KeyboardButton('10-darsπ£')
            item11 = types.KeyboardButton('11-darsπ£')
            item12 = types.KeyboardButton('12-darsπ£')
            item13 = types.KeyboardButton('13-darsπ£')
            item14 = types.KeyboardButton('14-darsπ£')
            item15 = types.KeyboardButton('15-darsπ£')
            item16 = types.KeyboardButton('16-darsπ£')
            item17 = types.KeyboardButton('17-darsπ£')
            item18 = types.KeyboardButton('18-darsπ£')
            item19 = types.KeyboardButton('19-darsπ£')
            back = types.KeyboardButton('π')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,item11,item12,item13,item14,item15,item16,item17,item18,item19, back)
            
            bot.send_message(message.chat.id,'π£',reply_markup=markup)
        
       
############################""""""""""BACK"""""###############################################################

        elif message.text == 'π':
             markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
             item1 = types.KeyboardButton('Arab tili grammatikasiπ')
             item2 = types.KeyboardButton('Arab tili fonetikasi π£π')
             markup.add(item1,item2)
    
             bot.send_message(message.chat.id,'π',reply_markup=markup)


###########################"""""'Grammatika""""###################################################################
        
        
        elif message.text == '1π':
            bot.send_message(message.chat.id,'Madina1')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/2?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/3?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/4?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/5?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/6?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/7?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/8?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/9?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/10?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/11?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/12?single')    
        elif message.text == '2π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/30?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/31?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/32?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/33?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/34?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/35?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/36?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/37?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/38?single')    
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/39?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/40?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/41?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/42?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/50?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/51?single')
        elif message.text == '3π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/59?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/60?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/61?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/62?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/63?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/64?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/65?single')
            
        elif message.text == '4π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/74?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/75?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/76?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/77?single')
        elif message.text == '5π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/83?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/84?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/85?single')
        elif message.text == '6π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/91?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/92?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/93?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/94?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/95?single')
        elif message.text == '7π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/102?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/103?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/104?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/105?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/106?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/107?single')
        elif message.text == '8π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/115?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/116?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/117?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/118?single')
        elif message.text == '9π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/142?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/143?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/148?single')
        elif message.text == '10π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/151?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/152?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/153?single')
        elif message.text == '11π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/155?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/156?single')
        elif message.text == '12π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/158?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/159?single')
        elif message.text == '13π':
            bot.send_message(message.chat.id,'Madina2')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/161?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/162?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/163?single')
        elif message.text == '14π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/169?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/170?single')
        elif message.text == '15π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/178?single')
        elif message.text == '16π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/180?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/181?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/182?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/183?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/184?single')
        elif message.text == '17π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/187?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/188?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/189?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/190?single')
        elif message.text == '18π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/192?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/193?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/194?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/195?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/196?single')
        elif message.text == '19π':
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/198?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/199?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/200?single')
            bot.send_video(message.chat.id,r'https://t.me/araboqgramma/201?single')

            
            
# ########################################## Audio ####################################################
        elif message.text == 'π§ 1-audio π§':
            # bot.send_document(message.chat.id,r'?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/13?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/14?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/15?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/16?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/17?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/18?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/19?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/20?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/21?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/22?single')
        elif message.text == 'π§ 2-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/123?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/43?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/44?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/45?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/46?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/47?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/48?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/49?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/52?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/53?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/54?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/55?single')
        elif message.text == 'π§ 3-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/124?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/66?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/67?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/68?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/69?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/70?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/71?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/72?single')
        elif message.text == 'π§ 4-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/125?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/78?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/79?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/80?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/81?single')
        elif message.text == 'π§ 5-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/126?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/86?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/87?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/88?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/89?single')
        elif message.text == 'π§ 6-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/127?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/96?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/97?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/98?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/99?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/100?single')
        elif message.text == 'π§ 7-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/128?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/108?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/109?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/110?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/111?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/112?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/113?single')
        elif message.text == 'π§ 8-audio π§':
            bot.send_document(message.chat.id,r'https://t.me/araboqgramma/129?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/119?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/120?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/121?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/122?single')
        elif message.text == 'π§ 9-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 10-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 11-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 12-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 13-audio π§':
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/165?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/166?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/167?single')
        elif message.text == 'π§ 14-audio π§':
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/172?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/173?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/174?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/175?single')
            bot.send_audio(message.chat.id,r'https://t.me/araboqgramma/176?single')
        elif message.text == 'π§ 15-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 16-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 17-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 18-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')
        elif message.text == 'π§ 19-audio π§':
            bot.send_message(message.chat.id,'Audio mavjud emas')

# ###################################### fonetika ##################################################

        elif message.text == '1-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/2?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/4?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/5?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/6?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/7?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/8?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/9?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/10?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/11?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/12?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/13?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/14?single')
        elif message.text == '2-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/16?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/17?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/18?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/19?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/20?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/21?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/22?single')
        elif message.text == '3-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/25?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/26?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/27?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/28?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/29?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/30?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/31?single')
        elif message.text == '4-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/33?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/34?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/35?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/36?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/37?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/38?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/39?single')
        elif message.text == '5-darsπ£':  
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/41?single')
        elif message.text == '6-darsπ£':  
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/43?single')
        elif message.text == '7-darsπ£':  
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/46?single')
        elif message.text == '8-darsπ£':  
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/48?single')
        elif message.text == '9-darsπ£':  
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/50?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/51?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/52?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/53?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/54?single')
        elif message.text == '10-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/56?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/57?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/58?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/59?single')
        elif message.text == '11-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/61?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/62?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/63?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/64?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/65?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/66?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/67?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/68?single')
        elif message.text == '12-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/70?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/71?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/72?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/73?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/74?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/75?single')
        elif message.text == '13-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/77?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/78?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/79?single')
        elif message.text == '14-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/81?single')
        elif message.text == '15-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/83?single')
        elif message.text == '16-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/87?single')
        elif message.text == '17-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/89?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/90?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/91?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/92?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/93?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/94?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/95?single')
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/96?single')
        elif message.text == '18-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/98?single')        
        elif message.text == '19-darsπ£':
            bot.send_video(message.chat.id,r'https://t.me/learnarabian/100?single')
        else:
            bot.send_message(message.chat.id,'Wrong message!')
    
bot.polling(none_stop=True)

