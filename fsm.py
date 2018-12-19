from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_button_message2, send_button_message3, send_button_message4, send_button_message5, send_button_message6, send_button_message7


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def is_going_to_user(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '開始使用'
        return False

    def is_going_to_offer_find(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == '通報相關服務'
        return False


    def is_going_to_offer(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '我要提供'
        return False

    def is_going_to_search(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == '尋獲寵物清單'
        return False

    def is_going_to_offer_pet(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            if text == '貓咪' or text == '狗狗':
                f = open('offer.txt', 'a+')
                f.write(text)
                f.write('\n')
                return True
        return False

    def is_going_to_offer_address(self, event):
        if event.get("message"):
            text = event['message']['text']
            # text store address
            f = open('offer.txt', 'a+')
            f.write(text)
            f.write('\n')
            return True
        return False

    def is_going_to_offer_phone(self, event):
        if event.get("message"):
            text = event['message']['text']
            # text store phone number
            f = open('offer.txt', 'a+')
            f.write(text)
            f.write('\n')
            return True
        return False

    def is_going_to_offer_photo(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            if text == '是':
                return True
        return False
    
    def no_offer_photo(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            if text == '否':
                return True
        return False

    def photo(self, event):
        if event.get("message"):
            text = event['message']['text']
            f = open('offer.txt', 'a+')
            f.write(text)
            f.write('\n')
            return True
        return False
    
    def is_going_to_find(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            if text == '走失了QQ':
                return True
        return False

    def is_going_to_phone(self, event):
        if event.get("message"):
            text = event['message']['text']
            f = open('lost.txt', 'a+')
            f.write(text)
            f.write('\n')
            return True
        return False

    def is_going_to_state_photo(self, event):
        if event.get("message"):
            text = event['message']['text']
            f = open('lost.txt', 'a+')
            f.write(text)
            f.write('\n')
            return True
        return False
    
    def is_going_to_address(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            if text == '貓咪' or text == '狗狗':
                f = open('lost.txt', 'a+')
                f.write(text)
                f.write('\n')
                return True
        return False

    def is_going_to_find_end(self, event):
        if event.get("message"):
            text = event['message']['text']
            f = open('lost.txt', 'a+')
            f.write(text)
            f.write('\n')
            return True
        return False
    
    def is_going_to_lost_list(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == '走失寵物清單'
        return False
    
    def back_condition(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text.lower() == '返回'
        return False

    def is_going_to_list(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == '目前的通報清單'
        return False


    def on_enter_user(self, event):
        print('user state')
        sender_id = event['sender']['id']
        responese = send_button_message(sender_id, "", "")

    def on_exit_user(self, event):
        print('Leaving user')


    def on_enter_offer(self, event):
        print('您發現的寵物為：(貓咪、狗狗)?')
        sender_id = event['sender']['id']
        response = send_button_message3(sender_id, "", "") 
    def on_exit_offer(self, event):
        print('Leaving offer')

    def on_enter_search(self, event):
        print("I'm entering state search")

        f = open('offer.txt', 'r')
        sender_id = event['sender']['id']
        send_text_message(sender_id, f.read())
        responese = send_button_message5(sender_id, "", "")


    def on_exit_search(self, event):
        print('Leaving state search')

    def on_enter_offer_pet(self, event):
        print('您在哪發現的?(請輸入住址)')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "您在哪發現的?(請輸入住址)")

    def on_exit_offer_pet(self, event):
        print('Leaving state offer per')
        
    def on_enter_offer_address(self, event):
        print('請提供您的電話號碼')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請提供您的電話號碼(09XX-XXX-XXX)")

    def on_exit_offer_address(self, event):
        print('Leaving state offer per')

    def on_enter_offer_phone(self, event):
        print('是否提供照片(是/否)?')

        sender_id = event['sender']['id']
        response = send_button_message4(sender_id, "", "")

    def on_exit_offer_phone(self, event):
        print('Leaving state offer per')

    def on_enter_offer_photo(self, event):
        print('photo')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請提供您的圖片(網址)")

    def on_exit_offer_photo(self, event):
        print('Leaving state offer per')
    
    def on_enter_back_state(self, event):
        print('back')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "已成功提交，謝謝您!!")
        send_button_message5(sender_id, "", "")
        f = open('offer.txt', 'a+')
        f.write('\n')


    def on_exit_back_state(self, event):
        print('Leaving state offer per')

    def on_enter_find(self, event):
        print('find')

        sender_id = event['sender']['id']
        response = send_button_message6(sender_id, "", "")

    def on_exit_find(self, event):
        print('Leaving state find')

    def on_enter_address(self, event):
        print('address')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "您寵物走失的地點為?")

    def on_exit_address(self, event):
        print('Leaving state find')


    def on_enter_phone(self, event):
        print('phone')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請留下您的聯絡方式(09XX-XXX-XXX)")

    def on_exit_phone(self, event):
        print('Leaving state phone')

    def on_enter_state_photo(self, event):
        print('phone')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請提供您寵物的照片(網址)")

    def on_exit_state_photo(self, event):
        print('Leaving state phone')
    
    def on_enter_find_end(self, event):
        print('phone')

        sender_id = event['sender']['id']
        send_text_message(sender_id, "資料已保存，希望您早點找到!!")
        send_button_message5(sender_id, "", "")
        f = open('lost.txt', 'a+')
        f.write('\n')

    def on_exit_find_end(self, event):
        print('Leaving state phone')
   

    def on_enter_lost_list(self, event):
        print("I'm entering state lost_list")

        f = open('lost.txt', 'r')
        sender_id = event['sender']['id']
        send_text_message(sender_id, f.read())
        responese = send_button_message5(sender_id, "", "")

    def on_exit_lost_list(self, event):
        print('Leaving state lost_list')

    def on_enter_offer_find(self, event):
        print("I'm entering state offer_find")
        sender_id = event['sender']['id']
        responese = send_button_message2(sender_id, "", "")

    def on_exit_offer_find(self, event):
        print('Leaving state lost_list')

    def on_enter_list(self, event):
        print("I'm entering state offer_find")
        sender_id = event['sender']['id']
        responese = send_button_message7(sender_id, "", "")

    def on_exit_list(self, event):
        print('Leaving state lost_list')
