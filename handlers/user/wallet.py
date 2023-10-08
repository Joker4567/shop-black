
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import balance

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=balance)
async def process_balance(message: Message, state: FSMContext):
    await message.answer('Ваш кошелек пуст! Пополните баланс\n\n'
                         '✅Заявка на оплату № 29223419. Переведите на банковскую  '
                         'карту удобным для вас способом. \nВажно пополнить '
                         'точную сумму заказа. 2200700878893964 ‼️ у вас есть 30 мин на оплату, '
                         'после чего платёж не будет зачислен. \nПо истечению времени создайте запрос повторно номер заявки идентичный.')

