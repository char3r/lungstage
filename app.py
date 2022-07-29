from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn
import random, os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ["YOUR_CHANNEL_ACCESS_TOKEN"])
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
             
stage_list = ["IA1", "IA2", "IA3", "IB", "IIA", "IIB", "IIIA", "IIIB", "IIIC", "IVA", "IVB"]

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def response_message(event):
    ques_num = random.randrange(len(ques_list))
    question, answer = ques_list[ques_num]
    
    def discriminant_state(answer_index: int):
        if answer==stage_list[answer_index]:
            return f"◯ 正解\n{question}→Stage {answer}"
        else:
            return f"× 不正解\nあなたの答えは Stage {stage_list[answer_index]}\n正解は {question}→Stage {answer}"
                                            
    col_questions = [CarouselColumn(title = question,
                                    text = "正しいUICC第8版の肺癌ステージを選べ。",
                                    actions=[{"type": "message", "label": stage_list[0], "text": discriminant_state(0)},
                                        {"type": "message", "label": stage_list[1], "text": discriminant_state(1)},
                                        {"type": "message", "label": stage_list[2], "text": discriminant_state(2)}]),
                     CarouselColumn(title = question,
                                    text = "正しいUICC第8版の肺癌ステージを選べ。",
                                    actions=[{"type": "message", "label": stage_list[3], "text": discriminant_state(3)},
                                        {"type": "message", "label": stage_list[4], "text": discriminant_state(4)},
                                        {"type": "message", "label": stage_list[5], "text": discriminant_state(5)}]),
                     CarouselColumn(title = question,
                                    text = "正しいUICC第8版の肺癌ステージを選べ。",
                                    actions=[{"type": "message", "label": stage_list[6], "text": discriminant_state(6)},
                                        {"type": "message", "label": stage_list[7], "text": discriminant_state(7)},
                                        {"type": "message", "label": stage_list[8], "text": discriminant_state(8)}]),
                     CarouselColumn(title = question,
                                    text = "正しいUICC第8版の肺癌ステージを選べ。",
                                    actions=[{"type": "message", "label": stage_list[9], "text": discriminant_state(9)},
                                        {"type": "message", "label": stage_list[10], "text": discriminant_state(10)},
                                        {"type": "uri", "label": "TNMまとめ（肺癌学会）", "uri": "https://www.haigan.gr.jp/guideline/2021/1/0/210100000000.html"}])]

    messages = TemplateSendMessage(alt_text=f"問題 {question}", template=CarouselTemplate(columns=col_questions))
    line_bot_api.reply_message(event.reply_token, messages)

'''
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    linebot_api.reply_message(event.reply_token, TextSendMessage(text="event.message.text"))
'''
  
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT",5000)))
