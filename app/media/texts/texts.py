RESPONSES = {
    'start_text':[
        'Привет как дела'
    ],
    'add_client_text':[
        'Добавь нового клиента'
    ],
    'add_client_contact':[
        'Напиши теперь его контакт в телеграмме через @ или телефон +'
    ],
    'add_client_service':[
        'Какую он услугу хочет?'
    ],
    'add_client_money':[
        'Сколько можно взять денег?'
    ],
    'add_client_from':[
        'Откуда клиент?'
    ],
    'add_client_status':[
        'Какой сейчас этап сделки?'
    ],
    'add_client_finish':[
        'Данные о клиенте:\n{name}\n{contact}\n{service}\n{money}\n{client_from}\n{client_status}\n\nВсе верно?'
    ],
    'add_client_bt_yes':[
        "Да, подписываем!"
    ],   
    'add_client_bt_no':[
        "Нее, давай изменем"
    ], 
    'add_client_bt_delete':[
        "Неет, удали эту хуйню"
    ], 
}

async def _(text,lang):
    if lang == 'ru':
        return RESPONSES[text][0]
    else:
        return RESPONSES[text][1]