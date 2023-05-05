## hello.py
from flask import Flask
app = Flask(__name__)

@app.route('/uer/<name>')
def user(name):
    return '<h1>hello, {}!</h1>'.format(name)

@app.route('/')
def index():
    return '<h1>hello world!</h1>'



from flask import Flask, jsonify
import threading

app = Flask(__name__)

def task():
    # 在这里编写需要进行并发处理的任务逻辑
    # while True:
    for i in range(10):
        print("zhouxinyu is my son")
    return "Task completed successfully!"

@app.route('/process')
def process():
    thread = threading.Thread(target=task)
    thread.start()
    for i in range(10):
        print(i)
    return jsonify({"message": "Task started successfully!"})




if __name__ == '__main__':
    app.run(debug=True)