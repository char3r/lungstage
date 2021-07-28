# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random

app = Flask(__name__)

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

print(len(ques_list))


@app.route('/', methods=["GET"])
def get():
    ques_num = random.randrange(len(ques_list))
    question = ques_list[ques_num][0]

    return render_template('index.html',
                           title='問題',
                           message1=question,
                           ques_num=ques_num)


@app.route('/answer', methods=["POST"])
def post():
    ans_post = request.form.get('radio')
    ques_num = int(request.form.get('ques_num'))
    question = ques_list[ques_num][0]
    answer = ques_list[ques_num][1]

    if ans_post == answer:
        result = '○ 正解'
    else:
        if ans_post is None:
            ans_post = '未解答'
        result = '× 不正解（あなたの解答：{}）'.format(ans_post)

    return render_template('answer.html',
                           title='解答',
                           message1=result,
                           message2=question,
                           message3=answer)


if __name__ == '__main__':
    app.run()
