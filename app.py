from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "yibajiu189"
machine = TocMachine(
    states=[
        'start',
        'user',
        'offer',
        'offer_pet',
        'offer_address',
        'offer_phone',
        'offer_photo',
        'back_state',
        'search',
        'find',
        'address',
        'phone',
        'state_photo',
        'find_end',
        'lost_list',
        'offer_find',
        'list'
    ],
    transitions=[
        {   'trigger': 'advance',
            'source': 'start',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'offer_find',
            'conditions': 'is_going_to_offer_find'
        },
        {
            'trigger': 'advance',
            'source': 'offer_find',
            'dest': 'find',
            'conditions': 'is_going_to_find'
        },
        {
            'trigger': 'advance',
            'source': 'offer_find',
            'dest': 'offer',
            'conditions': 'is_going_to_offer'
        },
        {
            'trigger': 'advance',
            'source': 'offer',
            'dest': 'offer_pet',
            'conditions': 'is_going_to_offer_pet'
        },
        {
            'trigger': 'advance',
            'source': 'offer_pet',
            'dest': 'offer_address',
            'conditions': 'is_going_to_offer_address'
        },
        {
            'trigger': 'advance',
            'source': 'offer_address',
            'dest': 'offer_phone',
            'conditions': 'is_going_to_offer_phone'
        },
        {
            'trigger': 'advance',
            'source': 'offer_phone',
            'dest': 'offer_photo',
            'conditions': 'is_going_to_offer_photo'
        },
        {
            'trigger': 'advance',
            'source': 'offer_phone',
            'dest': 'back_state',
            'conditions': 'no_offer_photo'
        },
        {
            'trigger': 'advance',
            'source': 'offer_photo',
            'dest': 'back_state',
            'conditions': 'photo'
        },
        {
            'trigger': 'advance',
            'source': 'find',
            'dest': 'address',
            'conditions': 'is_going_to_address'
        },
        {
            'trigger': 'advance',
            'source': 'address',
            'dest': 'phone',
            'conditions': 'is_going_to_phone'
        },

        {
            'trigger': 'advance',
            'source': 'phone',
            'dest': 'state_photo',
            'conditions': 'is_going_to_state_photo'
        },
        {
            'trigger': 'advance',
            'source': 'state_photo',
            'dest': 'find_end',
            'conditions': 'is_going_to_find_end'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'list',
            'conditions': 'is_going_to_list'
        },
        {
            'trigger': 'advance',
            'source': 'list',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'list',
            'dest': 'lost_list',
            'conditions': 'is_going_to_lost_list'
        },

        {
            'trigger': 'advance',
            'source': [
                'back_state',
                'search',
                'find_end',
                'lost_list'
            ],
            'dest': 'user',
            'conditions': 'back_condition'
        }
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
