RESPONSES = {
    'start_text':[
        'СТАРТ. ПОГНАЛИ ТЕПЕРЬ НАЧИНАЕМ НАШЕ ОБЩЕНИЕ'
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
        'Данные о клиенте:\nИмя: {name}\nКонтакт: {contact}\nУслуга: {service}\nДеньги: {money}$\nОткуда клиент: {client_from}\nСтатус клиента: {client_status}\n\nВсе верно?'
    ],
    'add_client_bt_yes':[
        "Да, подписываем!"
    ],   
    'add_client_bt_no':[
        "Нее, давай изменем"
    ], 
    'add_client_bt_delete':[
        "Неет, удали это"
    ], 
    'add_client_bd_add':[
        "Добавил в бд"
    ], 
    'add_client_del':[
        "Удалил если захочешь нового то просто напиши команду /add_client"
    ], 
    'add_client_no_change':[
        "Что хочешь изменить?"
    ], 
    'lookupquerymain':[
        '{client_id} - {name} - {contact} - {client_status}\n\n'
    ],
    'lookupquerymain(addition)':[
        'Хочешь посмотреть детально введи команду /deal (contact)'
    ],
    'lookupclient(dealclient)':[
        'Карточка клиента:\n\nИмя: {name}\nКонтакт: {contact}\nУслуга: {service}\nДеньги: {money}$\nОткуда клиент: {client_from}\nСтатус клиента: {client_status}'
    ],
    'statisticsmain(statistics)':[
        "Сумма сделок: {sumcl}$\nКол-во клиентов: {clients}\nСредний чек: {average}$\nЗакрытые сделки: {closed}\nВ работе: {inwork}\nОтказы: {canceled}\nКонверсия: {converstion}"
    ]
}

async def _(text,lang):
    if lang == 'ru':
        return RESPONSES[text][0]
    else:
        return RESPONSES[text][1]