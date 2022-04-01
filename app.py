from flask import Flask
app=Flask(__name__)

@app.route("/") #路徑
def home():
    return "hello Flask"

@app.route("/test")   #第二網站路徑
def test():
    return "This is the test"

if __name__=="__main__":
    app.run()


