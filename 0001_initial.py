import telebot 
import json 
import subprocess

TOKEN = "................."
bot = telebot.TeleBot(TOKEN)

def collect_posts(channel):
    with open(f"{channel}.txt") as file:
        file = file.readlines()
    posts = []
    for n, line in enumerate(file):
        file[n] = json.loads(file[n])
        links = [link for link in file[n]['outlinks'] if channel not in link]
        p = str(file[n]['content']) + "\n\n" + str("\n".join(links))
        posts.append(p)
    return posts 


def upload_posts(num_posts, channel):
    command = f'snscrape --max-result {num_posts} --jsonl telegram-channel {channel} > {channel}.txt'
    subprocess.run(command, shell=True)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Напиши:\n1. название канала, откуда выгрузить\n2. сколько последних постов выгрузить\n3. куда выгрузить\n\nПример ввода:\n `other_channel 10 my_channel` ")     


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    try:
        channel, num_posts, target_channel = str(message.text).split()
        target_channel = "@"+target_channel
        
        upload_posts(num_posts, channel)
        posts = collect_posts(channel)
        while posts:
            bot.send_message(target_channel, posts.pop())
        
        bot.reply_to(message, "Отлично, пересылка завершена")

    except:
        bot.reply_to(message, "Неправильный формат. Нажми /start, чтобы увидеть правильный формат ввода")


if __name__ == "__main__":
    bot.polling()    
