from flask import Flask
import os


app=Flask(__name__)

@app.route("/") #路徑
def home():
    return "我愛廖子柔"

@app.route("/test")   #第二網站路徑
def test():
    return "This is the test"

if __name__=="__main__":
    port = 90
    app.run(host='0.0.0.0', port=port)


