import telebot
from telebot import types
import const

bot = telebot.TeleBot(const.API_TOKEN)


@bot.message_handler(commands=['help'])
def send_text(message):
    bot.send_message(message.chat.id, 'Стоимость цветов вы можете посмотреть здесь: https://vetkakvetka.by/')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_winter_collection = types.KeyboardButton("Зимняя коллекция")
    btn_compositions = types.KeyboardButton("Композиции")
    btn_mono_bouquets = types.KeyboardButton("Монобукеты")
    btn_potted = types.KeyboardButton("Горшечные")
    btn_wedding_bouquets = types.KeyboardButton("Свадебные букеты")
    btn_presents = types.KeyboardButton("Подарки")

    markup.add(btn_winter_collection,btn_compositions,btn_mono_bouquets,btn_potted,
               btn_wedding_bouquets,btn_presents)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Зимняя коллекция":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bouquet_569 = types.KeyboardButton("Букет 569")
            bouquet_112 = types.KeyboardButton("Букет 112")
            bouquet_531 = types.KeyboardButton("Букет 531")
            bouquet_109 = types.KeyboardButton("Букет 109")
            bouquet_582 = types.KeyboardButton("Букет 582")
            back = types.KeyboardButton("Назад")
            markup.add(bouquet_569, bouquet_112, bouquet_531, bouquet_109, bouquet_582, back)

            bot.send_message(message.chat.id, "Зимняя коллекция", reply_markup=markup)
        elif message.text == "Букет 569":
            bot.send_message(message.chat.id,
                             "Информация о товаре:\n"
                             "В составе букета: - антуриум, - хризантема, -эрингиум, - эустома.\n")
            img = open("Артикул 75261.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет 569")
            img.close()

        elif message.text == "Букет 112":
            bot.send_message(message.chat.id,
                             "Информация о товаре: \n",
                             "В составе букета: - роза, - хризантема, -эрингиум.\n")
            img = open("Артикул 75266.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет 112")
            img.close()

        elif message.text == "Букет 531":
            bot.send_message(message.chat.id,
                             "Информация о товаре:\n"
                             "В составе букета: - антуриум, - хризантема, -эрингиум, - эустома.\n")
            img = open("Артикул 78324.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет 531")
            img.close()

        elif message.text == "Букет 109":
            bot.send_message(message.chat.id,
                             "Информация о товаре:\n"
                             "В составе букета: - хризантема, -эрингиум, - эустома.\n")
            img = open("Артикул 75224.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет 109")
            img.close()

        elif message.text == "Букет 582":
            bot.send_message(message.chat.id,
                             "Информация о товаре:\n"
                             "В составе букета: - - Ранункулюс, - Роза кустовая, -Хамелациум, - Эрингиум, - Сосна, - Нобилис.\n")
            img = open("Артикул 79343.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет 582")
            img.close()

        elif message.text == "Композиции":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            in_baskets = types.KeyboardButton("В корзинах")
            decorative_planter= types.KeyboardButton("Декоративное кашпо")
            back = types.KeyboardButton("Назад")
            markup.add(in_baskets,decorative_planter , back)
            bot.send_message(message.chat.id, "Композиции", reply_markup=markup)
        elif message.text == "В корзинах":
            bot.send_message(message.chat.id, "Корзинка в бело-розовой гамме: \n")
            img = open("Артикул 00721.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Садовая козинка")
            img.close()

        elif message.text == "Декоративное кашпо":
            bot.send_message(message.chat.id, "Кашпо с сезонным составом: \n")
            img = open("Артикул 00722.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Садовая козинка")
            img.close()


        elif message.text == "Монобукеты":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            roza = types.KeyboardButton("Роза")
            tulips = types.KeyboardButton("Тюльпаны")
            back = types.KeyboardButton("Назад")
            markup.add(roza,tulips, back)
            bot.send_message(message.chat.id,"Монобукеты:",reply_markup=markup)
        elif message.text == "Роза":
            bot.send_message(message.chat.id, "Монобукет с пионовидной розой: \n")
            img = open("Артикул 70041.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Роза")
            img.close()

        elif message.text == "Тюльпаны":
            bot.send_message(message.chat.id, "Монобукет из тюльпанов: \n")
            img = open("Артикул 70042.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Тюльпаны")
            img.close()

        elif message.text == "Свадебные букеты":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            exotic = types.KeyboardButton("Экзотический букет")
            hydrangea = types.KeyboardButton("Букет с гортензией")
            pink = types.KeyboardButton("Букет в розово-малиновых тонах")
            back = types.KeyboardButton("Назад")
            markup.add(exotic, hydrangea, pink, back)

            bot.send_message(message.chat.id, "Свадебные букеты", reply_markup=markup)
        elif message.text == "Экзотический букет":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              "Экзотические в нашем понимании - это цветы, которые растут где-то \n"
                                              "на тропических островах.\n"
                                              "Но не меньшая экхотика - тюльпаны среди зимы или пионы в сентябре.\n "
                                              "Или подснгежники на новый год.\n")

            img = open("Артикул 6999.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Экзотический букет")

            img.close()
        elif message.text == "Букет с гортензией":
            bot.send_message(message.chat.id, "Информация о товаре: \n"
                                               "Гортензии — одни из немногих растений, способных \n"
                                              "накапливать в себе алюминий,\n"
                                               "который выделяется из кислых почв и у некоторых видов\n "
                                              "образует соединения, дающие им синие оттенки.\n")
            img = open("Артикул 6998.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет с гортензией")
            img.close()

        elif message.text == "Букет в розово-малиновых тонах":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              "В зависимости от наличия и сезонности цветов, состав может незначительно отличаться с,\n"
                                              "сохранением общего вида и цветовой гаммы.\n")

            img = open("Артикул 6997.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Букет в розово-малиновых тонах")
            img.close()


        elif message.text == "Горшечные":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            sansevieria = types.KeyboardButton("Сансевиерия")
            ficus = types.KeyboardButton("Фикус")
            cactus = types.KeyboardButton("Кактус")
            back = types.KeyboardButton("Назад")
            markup.add(sansevieria, ficus, cactus , back)

            bot.send_message(message.chat.id, "Горшечные", reply_markup=markup)
        elif message.text == "Сансевиерия":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              " – один из чемпионов по производству кислорода\n "
                                              "среди домашних растений,\n"
                                              " одновременно это растение поглощает из воздуха \n"
                                              "вредные для здоровья вещества\n")

            img = open("Артикул 7002.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Сансевиерия")
            img.close()

        elif message.text == "Фикус":
            bot.send_message(message.chat.id, "Информация о товаре: \n"
                                               "Фикус “Ginseng”-это один из самых колоритных представителей \n"
                                              "семейства Тутовых, который выращивается в домашнем цветоводстве.\n")
            img = open("Артикул 7001.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Фикус")

            img.close()
        elif message.text == "Кактус":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              " Кактусы выделяются среди множества разнообразных комнатных цветов\n"
                                              " своим необычным видом,\n"
                                              " Они обладают мясистым стволом, в котором собирается влага,\n "
                                              "а их листья превратились в колючки\n")
            img = open("Артикул 7003.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Кактус")
            img.close()


        elif message.text == "Подарки":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            aroma_candles = types.KeyboardButton("Арома свечи")
            cakes = types.KeyboardButton("Торты")
            toys = types.KeyboardButton("Игрушки")
            ceramics = types.KeyboardButton("Керамика")
            vase = types.KeyboardButton("Вазы")
            back = types.KeyboardButton("Назад")
            markup.add(aroma_candles, cakes, toys, ceramics, vase, back)

            bot.send_message(message.chat.id, "Вместе с букетом вы можете заказать родарок:", reply_markup=markup)
        elif message.text == "Арома свечи":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              "Шалфей и мирт, топлёное молоко, потертая замша,\n"
                                              " кокосовый остров, древесный дым.\n")
            img = open("Артикул 5999.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Арома свечи")
            img.close()

        elif message.text == "Торты":
            bot.send_message(message.chat.id, "Информация о товаре: \n"
                                               "Уменьшенная копия классического Медовика.\n"
                                               "Те же ароматные медовые коржи, с прослойками из натурального\n"
                                              " сметанно-сливочного крема.\n")
            img = open("Артикул 5998.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Торт 'Медовик'")
            img.close()

        elif message.text == "Игрушки":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              "Высота игрушки 22см.\n")
            img = open("Артикул 6996.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Игрушка ручной работы «Лиса»")
            img.close()

        elif message.text == "Керамика":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              "Керамическая плитка\n")
            img = open("Артикул 6995.png", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Кружка с картинкой «Жираф»")
            img.close()

        elif message.text == "Вазы":
            bot.send_message(message.chat.id, "Информация о товаре:\n "
                                              "Керамика, Tognana Tognana Porcellane S.p.A.Via\n")
            img = open("Артикул 6994.jpg", "rb")
            bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="Ваза Tongass 18 см")
            img.close()


        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_winter_collection = types.KeyboardButton("Зимняя коллекция")
            btn_compositions = types.KeyboardButton("Композиции")
            btn_mono_bouquets = types.KeyboardButton("Монобукеты")
            btn_potted = types.KeyboardButton("Горшечные")
            btn_wedding_bouquets = types.KeyboardButton("Свадебные букеты")
            btn_presents = types.KeyboardButton("Подарки")

            markup.add(btn_winter_collection, btn_compositions, btn_mono_bouquets,
                       btn_potted,
                       btn_wedding_bouquets, btn_presents)

            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

bot.polling(none_stop=True)
