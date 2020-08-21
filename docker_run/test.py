from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html',name="heldlo")


import pymongo
@app.route('/mongo')
def connect_mongo():

    client = pymongo.MongoClient("mongodb://root:example@localhost:27017")
    db = client.test
    collection_test = db.test
    # 插入資料
    simple_data={"123":"456"}
    data_id = collection_test.insert_one(simple_data).inserted_id

    return str(data_id)





app.run(host='0.0.0.0')