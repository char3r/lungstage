from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction
import random, os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ["YOUR_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["YOUR_CHANNEL_SECRET"])

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def response_message(event):

    
    col_questions = [CarouselColumn(title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
                                    text = 'a',
                                    actions=[{"type": "message", "label": "IA1", "text": "正解"},
                                            {"type": "message", "label": "IA2", "text": "正解"},
                                            {"type": "message", "label": "IA3", "text": "正解"}]),
                    CarouselColumn(title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
                                    text = 'a',
                                    actions=[{"type": "message", "label": "IB", "text": "正解"},
                                            {"type": "message", "label": "IIA", "text": "正解"},
                                            {"type": "message", "label": "IIB", "text": "正解"}]),
                    CarouselColumn(title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
                                    text = 'a',
                                    actions=[{"type": "message", "label": "IIIA", "text": "正解"},
                                            {"type": "message", "label": "IIIB", "text": "正解"},
                                            {"type": "message", "label": "IIIC", "text": "正解"}]),
                    CarouselColumn(title = "問題：正しいUICC第8版の肺癌ステージを選べ。",
                                    text = 'a',
                                    actions=[{"type": "message", "label": "IVA", "text": "正解"},
                                            {"type": "message", "label": "IVB", "text": "正解"}])]

    messages = TemplateSendMessage(alt_text="問題です。", template=CarouselTemplate(columns=col_questions))
    line_bot_api.reply_message(event.reply_token, messages)

'''
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    linebot_api.reply_message(event.reply_token, TextSendMessage(text="event.message.text"))
'''
  
if __name__ == '__main__':
    app.run()
