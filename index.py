import pyowm;
import telebot;

owm=pyowm.OWM('a3effcbc4922e39fb1cd3e6befc9d581', language = 'ru')

bot = telebot.TeleBot('1037710466:AAGqKQgL106Vl5Qn7shHFXEQPFhF7z_Tg9M');
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Душанбе')
keyboard1.row('Худжанд', 'Куляб')
keyboard1.row('Бустон', 'Вахдат', 'Вахш')
keyboard1.row('Гиссар', 'Гулистон', 'Дангара')
keyboard1.row('Ёвон', 'Исфара',  'Истаравшан')
keyboard1.row('Канибадам', 'Муминабад', 'Норак')
keyboard1.row('Пенджикент', 'Турсунзаде', 'Фархор')
keyboard1.row('Файзобод', 'Хорог', 'Чкаловск')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, выберите город', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_echo(message):
  observation = owm.weather_at_place(message.text)
  w = observation.get_weather()
  temp=w.get_temperature('celsius')['temp']

  answer_text = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + '\n' + \
                'Температура в районе ' + str(round(temp)) + '°C'
  if "Душанбе" in message.text or "Худжанд" in message.text  or "Куляб" in message.text \
     or "Бустон" in message.text or "Вахдат" in message.text or "Фархор" in message.text \
     or "Вахш" in message.text or "Гиссар" in message.text or "Гулистон" in message.text\
     or "Дангара" in message.text or "Ёвон" in message.text or "Исфара" in message.text \
     or "Истаравшан" in message.text or "Канибадам" in message.text or "Муминабад" in message.text\
     or "Норак" in message.text or "Пенджикент" in message.text or "Турсунзаде" in message.text\
     or "Файзобод" in message.text or "Хорог" in message.text or "Чкаловск" in message.text:
    answer = answer_text

  else:
      answer = 'Этого города в списке нет' + '\n'
      answer += 'Повторите попытку'


  bot.send_message(message.chat.id, answer)

bot.polling()