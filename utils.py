import requests
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAKCjH6EtQ4BAP0A96RZAwukqy35eQMGZAKYYpcn2RfMC84abZA0SIwNaD5w5qsH3eQqx3lwfcz5bSJjWkxWv0ZBNBTBVwrRAMJhr0YqZCHuZCxKs2wBu9ScZBgFCJFYuS11fSWuQ6CtR9tdtbGzZCg3u960HaHGhQYrjNs5Ym1HOCd7tOn4rGwS"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


#def send_image_url(id, img_url):
#    pass


def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"歡迎使用協尋寵物服務\n請選擇：",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"通報相關服務",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"目前的通報清單",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message2(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"請選擇服務內容：\n",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"我要提供",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"走失了QQ",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message3(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"您發現的寵物為：\n",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"貓咪",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"狗狗",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message4(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"是否提供照片\n",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"是",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"否",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message5(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"點選並返回\n",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"返回",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message6(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"您走失的寵物為\n",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"貓咪",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"狗狗",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_button_message7(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient":{
            "id":id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"選擇您要查看的清單\n",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"尋獲寵物清單",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        },
                        {
                            "type":"postback",
                            "title":"走失寵物清單",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

