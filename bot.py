import random
import sqlite3
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, KeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from filters import IsAdminFilter
from asyncio import sleep

TOKEN = "1851633847:AAEeM50BU2StVFqBSgWdY0mCWZR9dfqmkes"
ADMIN_ID = 1004250581

bot = Bot(token=TOKEN, parse_mode="html")
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)

@dp.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    startbtn = InlineKeyboardMarkup()
    btn1 = KeyboardButton(text="💈Игры", callback_data="game_cmd")
    btn2 = KeyboardButton(text="Основные🚀", callback_data="all_cmd")
    btn3 = KeyboardButton(text="⭐Поддержка⭐", url="https://t.me/CocAhell")
    startbtn.add(btn1,btn2)
    startbtn.add(btn3)
    await msg.answer(f'<b>Приветствую {msg.from_user.first_name}!</b>', reply_markup=startbtn)
    conn = sqlite3.connect('limite.db')
    bd = conn.cursor()
    bd.execute(f'SELECT * FROM limits WHERE id = (?)', (msg.from_user.id, ))
    #вытаскиваем строку
    data1 = bd.fetchone()
    
    connection = sqlite3.connect('useridb.db')
    db = connection.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS useri (
    id BIGINT,
    money BIGINT,
    ban INT,
    max_give BIGINT,
    bon BIGINT,
    glob INT,
    nick TEXT,
    dick TEXT,
    status TEXT
    )""")
    connection.commit()
    # делаем запрос в таблицу users и ищем пользователя где
    # chat_id = message.from_user.id
    db.execute("SELECT * FROM useri WHERE id = (?)", (msg.from_user.id, ))
    #вытаскиваем строку
    data = db.fetchone()
    # если нету такого
    if data1 is None:
            await dp.bot.send_message(1004250581, text=f"+лимитс - <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.first_name}</a>")
            bd.execute(f"INSERT INTO limits VALUES (?, ?, ?, ?)", ("0", "0", "0", msg.from_user.id))
            conn.commit()
            
    if data is None:
        await dp.bot.send_message(msg.chat.id, text="Бонусом вам выданно <b>5.000</b>💰")
        await dp.bot.send_message(1004250581, text=f"#новый_пользователь\nНик: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.first_name}</a>\nИд: <code>{msg.from_user.id}</code>")
        # добавим в базу
        db.execute(f"INSERT INTO useri VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (msg.from_user.id, 5000, 0, 10000, 0, 0, f"{msg.from_user.first_name}", "0", "0"))
        connection.commit()
            
@dp.message_handler(commands=['date'])
async def start_message(msg: types.Message):
    current_datetime = datetime.now().date()
    print(current_datetime)

@dp.message_handler(commands=['crt'])
async def start_message(msg: types.Message):
    connection = sqlite3.connect('limite.db')
    db = connection.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS limits (
    bonus TEXT,
    ledenec TEXT,
    click TEXT,
    id BIGINT
    )""")
    connection.commit()
    await msg.answer("Всё, больше не надо!")
        
@dp.callback_query_handler(text="game_cmd")
async def send_random_value(call: types.CallbackQuery):
    exitbtn = InlineKeyboardMarkup()
    exit1 = KeyboardButton(text="↩️Назад", callback_data="exit")
    exitbtn.add(exit1)
    await call.message.delete()
    await call.message.answer("<b>Игровые команды:</b>\n\n<code>Слот (число)</code> - <b>игра слот</b>\n<code>Бас (число)</code> - <b>игра бас</b>\n<code>Боул (число)</code> - <b>игра боул</b>\n<code>Фут (число)</code> - <b>игра фут</b>\n<code>Дротик (число)</code> - <b>игра дротик</b>\n<code>/dice (ставка) (число)</code> - <b>игра кубик</b>\n<code>Б или Баланс</code> - <b>ваш баланс</b>\n<code>Бонус</code> - <b>взять бонус</b>\n<code>Кока инфо</code> - <b>ваш профиль</b>", reply_markup=exitbtn)
    
@dp.callback_query_handler(text="all_cmd")
async def send_random_value(call: types.CallbackQuery):
    exitbtn = InlineKeyboardMarkup()
    exit1 = KeyboardButton(text="↩️Назад", callback_data="exit")
    exitbtn.add(exit1)
    await call.message.delete()
    await call.message.answer("<b>Я нахожусь в разработке.</b>\n\n<b>Команды:</b>\n\n<code>!ban</code>, <code>!бан</code> - <b>заблокировать пользователя группы!</b>\n<code>!unban</code>, <code>!разбан</code> - <b>разблокировать пользователя группы!</b>\n<code>!kick</code>, <code>!кик</code> - <b>кикнуть/выгнать пользователя группы!</b>\n<code>!mute</code>, <code>!мут</code> - <b>выдать мут пользователю группы!</b>\n<code>!unmute</code>, <code>!размут</code> - <b>снять мут с пользователя группы!</b>\n<code>!dm</code>, <code>!удалить</code> - <b>удалить сообщение!</b>\n<code>!promote</code> - <b>выдать админку!</b>\n<code>!unpromote</code> - <b>забрать админку!</b>\n<code>!pin</code> - <b>закрепить сообщение!</b>\n<code>!unpin</code> - <b>открепить сообщение!</b>\n<code>!unpin_all</code> - <b>открепить все сообщения!</b>", reply_markup=exitbtn)

@dp.callback_query_handler(text="exit")
async def send_random_value(call: types.CallbackQuery):
    startbtn = InlineKeyboardMarkup()
    btn1 = KeyboardButton(text="💈Игры", callback_data="game_cmd")
    btn2 = KeyboardButton(text="Основные🚀", callback_data="all_cmd")
    btn3 = KeyboardButton(text="⭐Поддержка⭐", url="https://t.me/CocAhell")
    startbtn.add(btn1,btn2)
    startbtn.add(btn3)
    await call.message.delete()
    await call.message.answer("<b>Главное меню</b>", reply_markup=startbtn)
    
@dp.message_handler(commands=['ras'])
async def bot_message(msg: types.Message):
    if msg.chat.id == ADMIN_ID:
        s = msg.text
        word = s.replace('/ras', '').split(" ", 1)
        try:
            connection = sqlite3.connect('useridb.db')
            db = connection.cursor()
            db.execute(f'SELECT * FROM useri')
        # вытащим всех
            row = db.fetchall()
        
        # если пользовати есть 
            if len(row) > 0:
                print(f"{word[1]}")
                await msg.answer("Запускаю рассылку...")
               # начинаем перебор
                num = 0
                good = 0
                nogood = 0
                allg = 0
                for iu in row:
                    num += 1
                    chat_id = str(iu[0])
                    try:
                        await dp.bot.send_message(chat_id, text=f"{word[1]}")
                        allg += 1
                        good += 1
                        
                    except Exception:
                        nogood += 1
                    if num % 25:
                        await sleep(1)
                else:
                    await msg.answer(f"Всего: {allg}\nУдачно: {good}\nНеудачно: {nogood}")
        except IndexError:
            await msg.answer("Введите текст рассылки")
        else:
            return
            
@dp.message_handler(commands=['addglob'])
async def addglob(msg: types.Message):
     await msg.answer("Потом сдлаю")
     
@dp.message_handler(commands=['dice'])
async def bot_message(msg: types.Message):
    connection = sqlite3.connect('useridb.db')
    db = connection.cursor()
    db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.from_user.id, ))
    #вытаскиваем строку
    data = db.fetchone()
    s = msg.text
    word = s.replace('/dice', '').split(" ", 2)
    try:
        print(word[1])
        if int(word[1]) < 1:
            await msg.answer("Ведите число от 1 до 6")
        elif int(word[1]) > 6:
        	await msg.answer("Ведите число от 1 до 6")
        else:
            bot_data = await dp.bot.send_dice(msg.chat.id)
            bot_data = bot_data['dice']['value']
            if int(word[1]) == bot_data:
                result = f"Выигрыш +{int(word[2])*1.5}"
                rest = int(word[2])*1.5
            else:
                result = f"Проигрыш -{int(word[2])}" 
                rest = -int(word[2])
            await dp.bot.send_message(msg.chat.id, text=f"Выпало: {bot_data}\nВаше число: {word[1]}\n\n{result}")
            db.execute(f"Update useri set money={data[1]} + {rest} WHERE id = (?)", (msg.from_user.id, ))
            connection.commit()
    except IndexError:
        await msg.answer("Введите <code>/dice «число» «ставка»</code>")
    else:
        return

@dp.message_handler(commands=['money'])
async def agive_message(msg: types.Message):
    if msg.chat.id == ADMIN_ID:
        connection = sqlite3.connect('useridb.db')
        db = connection.cursor()
        db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.from_user.id, ))
        #вытаскиваем строку
        data = db.fetchone()
        s = msg.text
        word = s.replace('/money', '').split(" ", 2)
        try:
            await msg.answer(f"Баланс <code>{word[1]}</code> изменён, и составляет <b>{round(data[1]+int(word[2]))}</b>")
            db.execute(f"Update useri set money={data[1]} + {int(word[2])} WHERE id = (?)", (int(word[1]), ))
            connection.commit()
        except IndexError:
            await msg.answer("Введите ид пользователя")
        else:
            return

@dp.message_handler(commands=['help']) 
async def help_message(message: types.Message): 
    await message.reply("<b>Я нахожусь в разработке.</b>\n\n<b>Команды:</b>\n\n<code>!ban</code>, <code>!бан</code> - <b>заблокировать пользователя группы!</b>\n<code>!unban</code>, <code>!разбан</code> - <b>разблокировать пользователя группы!</b>\n<code>!kick</code>, <code>!кик</code> - <b>кикнуть/выгнать пользователя группы!</b>\n<code>!mute</code>, <code>!мут</code> - <b>выдать мут пользователю группы!</b>\n<code>!unmute</code>, <code>!размут</code> - <b>снять мут с пользователя группы!</b>\n<code>!dm</code>, <code>!удалить</code> - <b>удалить сообщение!</b>\n<code>!promote</code> - <b>выдать админку!</b>\n<code>!unpromote</code> - <b>забрать админку!</b>\n<code>!pin</code> - <b>закрепить сообщение!</b>\n<code>!unpin</code> - <b>открепить сообщение!</b>\n<code>!unpin_all</code> - <b>открепить все сообщения!</b>")
    
@dp.message_handler(commands=['gay'])
async def help_message(message: types.Message):
    await message.reply("🌈Ты гей на " + str(random.randint(1, 100)) + "%")
    

@dp.message_handler(commands=['bot'])
async def bot_message(message:types.Message):
    await message.reply("ЧЕГО ТЕБЕ ЧЕЛОВЕК👿")
    
@dp.message_handler(commands=["rules"])
async def rules(message: types.Message):
    await message.reply("""<a href="https://telegra.ph/Pravila-06-25-8">ПРАВИЛА</a>""")

@dp.message_handler(Text("@CocAhell", ignore_case=True))
async def kras(message: types.Message):
    await message.reply("Прошу не тэгать его без причины!")

@dp.message_handler(Text(["Бот!", "/bot", "!бот"],ignore_case=True))
async def bot(message: types.Message):
    bot_tag = ["ЧТООООО?!","Нету его.","@CocABlog:)","Слушаю","Сам ты бот👿","Хээээй!","Говори","И че? И че?"]
    await message.reply(f"{random.choice(bot_tag)}\nЗадержка 1 сек. ⌚")

@dp.message_handler(content_types=["new_chat_members"])
async def new(message: types.Message):
    await message.answer(f"""Привествую тебя <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, в нашем уютном чате, но прошу тебя прочитать правила /rules""")

@dp.message_handler(content_types=["left_chat_member"])
async def left(message: types.Message):
    left = ["ну и вали...","Ты куда?!","Бл@тб.","Тебе и так тут были не рады...","Ну наконецто!","Печаль,беда:("]
    await message.reply(f"{random.choice(left)}")

@dp.message_handler(Text("!gay",ignore_case=True))
async def gay(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return
    
    await message.answer(f"""<a href="tg://user?id={message.reply_to_message.from_user.id}>{message.reply_to_message.from_user.first_name}</a> гей на {random.randint(0,100)}%""")

@dp.message_handler(is_admin=True, commands=["mute","мут"], commands_prefix="!")
async def mute(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("Не бро, я не буду глушить админа.")
        return
    
    await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions())
    
    await message.answer(f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.id}<a> замутил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")

@dp.message_handler(is_admin=True, commands=["unmute","размут"], commands_prefix="!")
async def unmute(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return
    
    await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True))
    
    await message.answer(f"""ОК. <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a> может спокойно говорить, но пусть придержит язык за зубами.""")

@dp.message_handler(is_admin=True, commands=["ban","бан","банан"], commands_prefix="!")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("Не бро, я не буду банить админа.")
        return

    await message.bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    
    await message.answer(f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.id}<a> забанил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")

@dp.message_handler(is_admin=True, commands=["unban","разбан"], commands_prefix="!")
async def unban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return
    
    await message.bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    
    await message.answer(f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.id}<a> разбанил(а) <a href="tg://user?id={message.reply_to_message.id}">{message.reply_to_message.first_name}</a>""")

@dp.message_handler(is_admin=True, commands=['dm',"удалить"], commands_prefix="!")
async def delete_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("Не бро, я не буду удалять сообщение админа.")
        return

    await message.reply_to_message.delete()
    await message.reply("Сообщение удалено !")

@dp.message_handler(content_types=["text"])
async def chat_comand(msg: types.Message):
    connection = sqlite3.connect('useridb.db')
    db = connection.cursor()
    db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.from_user.id, ))
    #вытаскиваем строку
    data = db.fetchone()
    txt = msg.text.lower()
    if txt.startswith('бас') == True:
        param = txt[4:]
        if param != '':
            word = int(param)
            try:
                if int(word) < 1:
                    await msg. answer("<b>Ставка должна быть больше 1!</b>")
                elif int(word) > int(data[1]):
                    await msg.answer(f"<b>Недостаточно монет!</b>\nВаш баланс: <b>{data[1]}</b>")
                else:
                    print(word)
                    bot_data = await dp.bot.send_dice(msg.chat.id, emoji="🏀")
                    bot_data = bot_data['dice']['value']
                    await sleep(5)
                    if bot_data == 1:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 2:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 3:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 4:
                        result = f"Попадание! <b>+{int(word)*1.5}</b>"
                        rest = int(word)*1.5
                    elif bot_data == 5:
                        result = f"В точку! <b>+{int(word)*2}</b>"
                        rest = int(word)*2
                    await msg.answer(f"{result}")
                    db.execute(f"Update useri set money={data[1]} + {rest} WHERE id = (?)", (msg.from_user.id, ))
                    connection.commit()
            except IndexError:
                await msg.answer("Введите <code>Бас «ставка»</code>")
            else:
                return
    elif msg.text.lower().startswith('фут') == True:
        txt = msg.text.lower()
        param = txt[4:]
        if param != '':
            word = int(param)
            try:
                if int(word) < 1:
                    await msg. answer("<b>Ставка должна быть больше 1!</b>")
                elif int(word) > int(data[1]):
                    await msg.answer(f"<b>Недостаточно монет!</b>\nВаш баланс: <b>{data[1]}</b>")
                else:
                    print(word)
                    bot_data = await dp.bot.send_dice(msg.chat.id, emoji="⚽")
                    bot_data = bot_data['dice']['value']
                    await sleep(5)
                    if bot_data == 1:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 2:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 3:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 4:
                        result = f"Попадание! <b>+{int(word)*1.5}</b>"
                        rest = int(word)*1.5
                    elif bot_data == 5:
                        result = f"В точку! <b>+{int(word)*2}</b>"
                        rest = int(word)*2
                    await msg.answer(f"{result}")
                    db.execute(f"Update useri set money={data[1]} + {rest} WHERE id = (?)", (msg.from_user.id, ))
                    connection.commit()
            except IndexError:
                await msg.answer("Введите <code>Фут «ставка»</code>")
            else:
                return
    elif msg.text.lower().startswith('боул') == True:
        txt = msg.text.lower()
        param = txt[5:]
        if param != '':
            word = int(param)
            try:
                if int(word) < 1:
                    await msg. answer("<b>Ставка должна быть больше 1!</b>")
                elif int(word) > int(data[1]):
                    await msg.answer(f"<b>Недостаточно монет!</b>\nВаш баланс: <b>{data[1]}</b>")
                else:
                    print(word)
                    bot_data = await dp.bot.send_dice(msg.chat.id, emoji="🎳")
                    bot_data = bot_data['dice']['value']
                    await sleep(5)
                    if bot_data == 1:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 2:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 3:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 4:
                        result = f"Попадание! <b>+{int(word)*1.5}</b>"
                        rest = int(word)*1.5
                    elif bot_data == 5:
                        result = f"В точку! <b>+{int(word)*2}</b>"
                        rest = int(word)*2
                    elif bot_data == 6:
                        result = f"В точку! <b>+{int(word)*2}</b>"
                        rest = int(word)*2
                    await msg.answer(f"{result}")
                    db.execute(f"Update useri set money={data[1]} + {rest} WHERE id = (?)", (msg.from_user.id, ))
                    connection.commit()
            except IndexError:
                await msg.answer("Введите <code>Боул «ставка»</code>")
            else:
                return
    elif msg.text.lower().startswith('дротик') == True:
        txt = msg.text.lower()
        param = txt[7:]
        if param != '':
            word = int(param)
            try:
                if int(word) < 1:
                    await msg. answer("<b>Ставка должна быть больше 1!</b>")
                elif int(word) > int(data[1]):
                    await msg.answer(f"<b>Недостаточно монет!</b>\nВаш баланс: <b>{data[1]}</b>")
                else:
                    print(word)
                    bot_data = await dp.bot.send_dice(msg.chat.id, emoji="🎯")
                    bot_data = bot_data['dice']['value']
                    await sleep(5)
                    if bot_data == 1:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 2:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 3:
                        result = f"Промах! <b>-{word}</b>"
                        rest = -int(word)
                    elif bot_data == 4:
                        result = f"Попадание! <b>+{int(word)*1.5}</b>"
                        rest = int(word)*1.5
                    elif bot_data == 5:
                        result = f"В точку! <b>+{int(word)*2}</b>"
                        rest = int(word)*2
                    await msg.answer(f"{result}")
                    db.execute(f"Update useri set money={data[1]} + {rest} WHERE id = (?)", (msg.from_user.id, ))
                    connection.commit()
            except IndexError:
                await msg.answer("Введите <code>Дротик «ставка»</code>")
            else:
                return
    elif msg.text.lower() == 'кока инфо':
            if data[2] == 1:
                cs = "Да"
            else:
                cs = "Нет"
            if data[5] == 1:
                glob = "Да"
            else:
                glob = "Нет"
            await msg.answer(f"Имя: <b>{msg.from_user.first_name}</b>ℹ️\n〰️〰️〰️〰️〰️〰️\nИд: <code>{msg.from_user.id}</code>🆔\n〰️〰️〰️〰️〰️〰️\nМонеты: <b>{round(data[1])}</b>💰\n〰️〰️〰️〰️〰️〰️\nСердец: <b>{data[4]}</b>❤️\n〰️〰️〰️〰️〰️〰️\nАдмин бота: <b>{glob}</b>👮‍♂️\n〰️〰️〰️〰️〰️〰️\nВ чс: <b>{cs}</b>🚫\n〰️〰️〰️〰️〰️〰️\nЛимит: <b>{data[3]}</b>⏳")
    elif msg.text.lower() == 'баланс':
        await msg.answer(f"Баланс: {str(round(data[1]))}")
    elif msg.text.lower() == 'б':
        await msg.answer(f"Баланс: {str(round(data[1]))}")
    elif msg.text.lower() == 'бонус':
        bon = random.randint(1000, 5000)
        if data[1] > 50:
            await msg.answer(f"Бонус можно получить если баланс меньше 50 монет!\nУ вас: <b>{round(data[1])}</b>")
        else:
            await msg.answer(f"Вы получили <b>{bon} монет</b>!\nБаланс: <b>{int(round(data[1])+bon)}</b>")
            db.execute(f"Update useri set money={data[1]} + {int(bon)} WHERE id = (?)", (msg.from_user.id, ))
            connection.commit()
                
    elif msg.text.lower().startswith('слот') == True:
        txt = msg.text.lower()
        param = txt[5:]
        if param != '':
            word = int(param)
            try:
                if data[1] < int(word):
                    await msg.answer("<b>Недостаточно монет!</b>")
                elif word < 1:
                    await msg.answer("<b>Ставка должна быть больше 1!</b>")
                else:
                    arr = ["⭐","👍","❤️","👿","⚔️"]
                    a = random.choice(arr)
                    b = random.choice(arr)
                    c = random.choice(arr)
                    print(f"{word}")
                    await msg.reply("|"+a+"|"+b+"|"+c+"|")
                    if a == b == c:
                        await msg.answer(f"Джэкпот! +{word*3}")
                        db.execute(f"Update useri set money={data[1]} + {word*3} WHERE id = (?)", (int(data[0]), ))
                        connection.commit()
                    elif a == b:
                        await msg.answer(f"Пара! +{word*2}")
                        db.execute(f"Update useri set money={data[1]} + {word*2} WHERE id = (?)", (int(data[0]), ))
                        connection.commit()
                    elif b == c:
                        await msg.answer(f"Пара! +{word*2}")
                        db.execute(f"Update useri set money={data[1]} + {word*2} WHERE id = (?)", (int(data[0]), ))
                        connection.commit()
                    elif a == c:
                        await msg.answer(f"Пара! +{word*2}")
                        db.execute(f"Update useri set money={data[1]} + {word*2} WHERE id = (?)", (int(data[0]), ))
                        connection.commit()
                    else:
                        await msg.answer(f"Проигрыш! -{word}")
                        db.execute(f"Update useri set money={data[1]} - {word} WHERE id = (?)", (int(data[0]), ))
                        connection.commit()
            except IndexError:
                await msg.answer("Введите ставку")
            else:
                return
            
    elif msg.text.lower() in ["+","спс","спасибо"]:
        if not msg.reply_to_message:
            pass
        elif msg.reply_to_message.from_user.id == msg.from_user.id:
            pass
        else:
            connection = sqlite3.connect('useridb.db')
            db = connection.cursor()
            db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.reply_to_message.from_user.id, ))
            data1 = db.fetchone()
            try:
                await dp.bot.send_message(msg.chat.id, f"""<a href='tg://user?id={msg.from_user.id}'>{msg.from_user.first_name}</a>
дал(а) сердечко:
<a href='tg://user?id={msg.reply_to_message.from_user.id}'>{msg.reply_to_message.from_user.first_name}</a>
Теперь его карма: <b>{str(data1[4]+1)}❤️</b>""")
                db.execute(f"Update useri set bon={data1[4]} + 1 WHERE id = (?)", (msg.reply_to_message.from_user.id, ))
                connection.commit()
            except TypeError:
            	pass
    elif msg.text.lower().startswith('!дать') == True:
        txt = msg.text.lower()
        param = txt[6:]
        if param != '':
            word = int(param)
            try:
                if not msg.reply_to_message:
                    await msg.answer("<b>Пиши в ответ на сообщение!</b>")
                else:
                    connection = sqlite3.connect('useridb.db')
                    db = connection.cursor()
                    db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.reply_to_message.from_user.id, ))
                    data1 = db.fetchone()
                    if data[1] < int(word):
                        await msg.answer("<b>Недостаточно монет!</b>")
                    else:
                        await msg.answer(f"<a href='tg://user?id={msg.from_user.id}'>{msg.from_user.first_name}</a> передал {word} <a href='tg://user?id={msg.reply_to_message.from_user.id}'>{msg.reply_to_message.from_user.first_name}</a>")
                        db.execute(f"Update useri set money={data[1]} - {int(word)} WHERE id = (?)", (msg.from_user.id, ))
                        db.execute(f"Update useri set money={data1[1]} + {int(word)} WHERE id = (?)", (msg.reply_to_message.from_user.id, ))
                        connection.commit()
            except IndexError:
                await msg.answer("Введите число!")
            else:
                return
            
    elif msg.text.lower() == "кока глоб!":
        if msg.from_user.id == ADMIN_ID:
            if not msg.reply_to_message:
                await msg.answer(f"<a href='tg://user?id={msg.from_user.id}'>Хозяин</a>, ответьте на сообщение человека которому хотите дать админку!")
            else:
                connection = sqlite3.connect('useridb.db')
                db = connection.cursor()
                db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.reply_to_message.from_user.id, ))
                data1 = db.fetchone()
                if data1[5] == 1:
                    await msg.answer(f"<a href='tg://user?id={msg.reply_to_message.from_user.id}'>{msg.reply_to_message.from_user.first_name}</a>, и так админ!")
                else:
                    await msg.answer(f"<a href='tg://user?id={msg.from_user.id}'>Хозяин</a>, выдал админку на бота:\n<a href='tg://user?id={msg.reply_to_message.from_user.id}'>{msg.reply_to_message.from_user.first_name}</a>")
                    db.execute(f"Update useri set glob={data1[5]} + 1 WHERE id = (?)", (msg.reply_to_message.from_user.id, ))
                    connection.commit()

    elif msg.text.lower() == "кока не глоб!":
        if msg.from_user.id == ADMIN_ID:
            if not msg.reply_to_message:
                await msg.answer(f"<a href='tg://user?id={msg.from_user.id}'>Хозяин</a>, ответьте на сообщение человека у которого хотите забрать админку!")
            else:
                connection = sqlite3.connect('useridb.db')
                db = connection.cursor()
                db.execute(f'SELECT * FROM useri WHERE id = (?)', (msg.reply_to_message.from_user.id, ))
                data1 = db.fetchone()
                if data1[5] == 0:
                    await msg.answer(f"<a href='tg://user?id={msg.reply_to_message.from_user.id}'>{msg.reply_to_message.from_user.first_name}</a>, и так не админ!")
                else:
                    await msg.answer(f"<a href='tg://user?id={msg.from_user.id}'>Хозяин</a>, забрал админку на бота у:\n<a href='tg://user?id={msg.reply_to_message.from_user.id}'>{msg.reply_to_message.from_user.first_name}</a>")
                    db.execute(f"Update useri set glob={data1[5]} - 1 WHERE id = (?)", (msg.reply_to_message.from_user.id, ))
                    connection.commit()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
