import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard
from loader import dp, bot


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='У нас есть груши и яблоки\n'
                              'Если это вам не нужно - нажмите отмена', reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы купили грушу. Груш {quantity}', reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_apple(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы купили яблоки. Яблок {quantity}', reply_markup=pear_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Вы отменили покупку', show_alert=True)
    await call.message.edit_reply_markup()