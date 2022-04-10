from aiogram.types import ContentType, Message, InputFile, MediaGroup

from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes)


@dp.message_handler(text='/album')
async def send_album(message: Message):
    album = MediaGroup()

    photo_file_id = 'AgACAgIAAxkBAAIBJmJRpn9KBJwRWMhkIB91GKFiiUJkAAKxuzEbCjaQSipGr5ahb57rAQADAgADeQADIwQ'
    photo1_bytes = InputFile(path_or_bytesio='media/photo1.jpg')
    photo2_bytes = InputFile(path_or_bytesio='media/photo2.jpg')
    album.attach_photo(photo=photo1_bytes)
    album.attach_photo(photo=photo_file_id)
    album.attach_photo(photo=photo2_bytes, caption='Клевые картинки')

    await message.answer_media_group(media=album)