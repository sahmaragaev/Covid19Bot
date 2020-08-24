import telebot
from covid19_data import JHU
import covid19_data

bot = telebot.TeleBot('YOUR_TOKEN_HERE')

@bot.message_handler(commands=['start'])
def start(message):
  send_mess = f"<b>Hello {message.from_user.first_name}!</b>\n"
  bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
  helpMessage = "Type the country you want to get info of. For instance: United Kingdom or US.\nFor getting worldwide info, please, type Total"
  bot.send_message(message.chat.id, helpMessage, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
  final_message = ""
  get_message_bot = message.text
  
  if get_message_bot == "Total":
    total = covid19_data.dataByName("Total")
    final_message = f"Infected: {total.cases}\nDeaths: " + f"{total.deaths}\nRecovered: " + f"{total.recovered}" + f"\nActive Cases: {total.cases - total.deaths - total.recovered}"
    bot.send_message(message.chat.id, final_message, parse_mode='html') 

  else:
    try:
      inf = covid19_data.dataByName(f"{get_message_bot}")
      total = covid19_data.dataByName("Total")
      final_message = f"Infected: {inf.cases}\nDeaths: " + f"{inf.deaths}\nRecovered: " + f"{inf.recovered}" + f"\nActive Cases: {inf.cases - inf.deaths - inf.recovered}"
      bot.send_message(message.chat.id, final_message, parse_mode='html') 

    except Exception as e:
      print('Exception')
      bot.send_message("No Data found", final_message, parse_mode='html') 

bot.polling(none_stop=True)