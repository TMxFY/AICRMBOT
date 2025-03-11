RESPONSES = {
    'start_text':[
        'Привет как дела'
    ],
    'add_client_text':[
        'Добавь нового клиента'
    ],
}

async def _(text,lang):
    if lang == 'ru':
        print(RESPONSES[text][0])
        return RESPONSES[text][0]
    else:
        return RESPONSES[text][1]