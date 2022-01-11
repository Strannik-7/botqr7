from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token="5020587579:AAHoCbDrk3YTDC4439nWD97SPTEddrmlZXs")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.answer('Привет!\nЯ Бот - Генератор \"Qr\" кодов\nНапиши текст, который ты хочешь преобразовать')

@dp.message_handler()
async def text_massage(message: types.Message):
    await message.answer('Создание QR - Кода...')

    url = 'https://api.qrserver.com/v1/create-qr-code/?data=' + (message.text) +'&size=[100]x[100]'
    await bot.send_photo(message.chat.id, url)
    await bot.send_message(message.chat.id, 'QR - Код готов!\nМожешь прислать еще текст для обработки!')
    #qrc = pq.create(message.text)
    #qrc.png('code.png', scale=10)
    #with open('code.png', 'rb') as photo:
        #await bot.send_photo(message.chat.id, photo)

executor.start_polling(dp)