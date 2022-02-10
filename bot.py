from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent, Message

# from gitbot import get_repos
import gitbot
from config import bot_token, api_hash, api_id

print("asdg")


def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])


print("starting")
# api_id = 859123
# api_hash = 'de7f36205f4ff5b0190ef2b3c3646486'
# bot_token = '5295491783:AAFHwfQE8AmIK8cU5lJFI2LyDmh204G2r0I'

client = Client(session_name='Git Repo Bot', bot_token=bot_token, api_hash=api_hash, api_id=api_id)


def make_repos(data):
    ls = gitbot.get_repos(data)

    r = [InlineQueryResultArticle(i["name"], InputTextMessageContent(i["url"]), description=i["desc"]) for i in ls]
    print(len(r))
    return r


@client.on_message()
def handle_message(bot: Client, message: Message):
    user_id = message.from_user.id
    if message.text:
        bot.send_message(user_id, "This is a simple bot"
                                  " to search "
                                  "and find a github repository of a user.\nuse it inline like:\n"
                                  "```@gitrepbot username```")


# @client.on_callback_query()
# def handle_callback_query(bot: Client, query: CallbackQuery):
#     print("asd")
#     if query.data == 'start':
#         bot.edit_inline_text(query.inline_message_id, 'توضیحات بازی', reply_markup=IKM([('پایان', 'end')]))
#     elif query.data == 'end':
#         bot.edit_inline_text(query.inline_message_id, 'بازی تمام شد!!')


@client.on_inline_query()
def handle_inline_query(bot: Client, query: InlineQuery):
    q = query.query
    print(q)
    # print(req(parse_input(query.query)))
    # results = [InlineQueryResultArticle('شروع بازی جدید', InputTextMessageContent('متن بلند'),
    #                                     description="hello this is fde")]
    results = make_repos(q)
    bot.answer_inline_query(query.id, results, cache_time=3000)


client.run()
