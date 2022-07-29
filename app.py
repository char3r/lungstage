from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction
import random, os

app = Flask(__name__)

linebot_api = LineBotApi(os.environ["YOUR_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["YOUR_CHANNEL_SECRET"])

ques_list = [['T1aN0M0', 'IA1'],
             ['T1bN0M0', 'IA2'],
             ['T1cN0M0', 'IA3'],
             ['T2aN0M0', 'IB'],
             ['T2bN0M0', 'IIA'],
             ['T3N0M0', 'IIB'],
             ['T4N0M0', 'IIIA'],
             ['T1aN1M0', 'IIB'],
             ['T1bN1M0', 'IIB'],
             ['T1cN1M0', 'IIB'],
             ['T2aN1M0', 'IIB'],
             ['T2bN1M0', 'IIB'],
             ['T3N1M0', 'IIIA'],
             ['T4N1M0', 'IIIA'],
             ['T1aN2M0', 'IIIA'],
             ['T1bN2M0', 'IIIA'],
             ['T1cN2M0', 'IIIA'],
             ['T2aN2M0', 'IIIA'],
             ['T2bN2M0', 'IIIA'],
             ['T3N2M0', 'IIIB'],
             ['T4N2M0', 'IIIB'],
             ['T1aN3M0', 'IIIB'],
             ['T1bN3M0', 'IIIB'],
             ['T1cN3M0', 'IIIB'],
             ['T2aN3M0', 'IIIB'],
             ['T2bN3M0', 'IIIB'],
             ['T3N3M0', 'IIIC'],
             ['T4N3M0', 'IIIC'],
             ['TanyNanyM1a', 'IVA'],
             ['TanyNanyM1b', 'IVA'],
             ['TanyNanyM1c', 'IVB']]

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    
'''
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    linebot_api.reply_message(event.reply_token, \
                             TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    #ques_num = random.randrange(len(ques_list))
    #question = ques_list[ques_num][0]
    
    carousel_template = CarouselTemplate(
        columns = [
        CarouselColumn(
            title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
            text = "a",
            actions=[MessageAction(type = "message", label = "IA1", text="****"),
                    MessageAction(type = "message", label = "IA2", text="****"),
                    MessageAction(type = "message", label = "IA3", text="****")]),
        CarouselColumn(
            title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
            text = "a",
            actions=[MessageAction(type = "message", label = "IB", text="****"),
                    MessageAction(type = "message", label = "IIA", text="****"),
                    MessageAction(type = "message", label = "IIB", text="****")]),
        CarouselColumn(
            title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
            text = "a",
            actions=[MessageAction(type = "message", label = "IIIA", text="****"),
                    MessageAction(type = "message", label = "IIIB", text="****"),
                    MessageAction(type = "message", label = "IIIC", text="****")]),
        CarouselColumn(
            title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
            text = "a",
            actions=[MessageAction(type = "message", label = "IVA", text="****"),
                    MessageAction(type = "message", label = "IVB", text="****")])
        ])

    messages = TemplateSendMessage(alt_text="問題です。", template=carousel_template)
    line_bot_api.reply_message(event.reply_token, messages)
'''

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    #ques_num = random.randrange(len(ques_list))
    #question = ques_list[ques_num][0]
    '''
    carousel_template = CarouselTemplate(
        columns = [CarouselColumn(
            title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
            text = "a",
            actions=[MessageAction(type = "message", label = "IVB", text="****")])
        ])
    '''
    #messages = TemplateSendMessage(alt_text="問題です。", template=carousel_template)
    line_bot_api.reply_message(event.reply_token, messages=TextSendMessage(text='a'))
  
if __name__ == '__main__':
    app.run()
