from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = '表示したいメッセージ文です'
    message_list = ['メッセージ文　AAA', 'メッセージ文　BBB']
    message_dict = {'name': '山田 一郎', 'message' : 'こんにちは'}
    
    return render_template('main.html', 
                           message=message, 
                           message_list=message_list, 
                           message_dict=message_dict
                          )

if __name__ == '__main__':
    app.run(
        # host="0.0.0.0",
        # port=8888,
        debug=True,        
    )