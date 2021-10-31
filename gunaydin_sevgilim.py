from instabot import Bot
from datetime import datetime
import time

bot = Bot()

username = ""  # Kullanıcı adınız.
password = ""  # Şifreniz.
sevgilim = ""  # Mesaj gidecek kişinin kullanıcı adı.

# Giriş yapma
bot.login(username=username, password=password)


# Günaydın mesajı atma fonksiyonu
def gunaydin():
    message = "Günaydın sevgilim <3"
    girlfriend = [sevgilim]

    bot.send_message(message, girlfriend)


while True:
    t = datetime.now()
    if t.hour == 08 and t.minute == 10:
        gunaydin()
        continue
    time.sleep(50)
