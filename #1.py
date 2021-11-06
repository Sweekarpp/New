from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/")
def wasd():
    return "Dogecoin is up!"
tasks=[
    {
    'id':1,
    'title':u'doge',
    'description':u'data to be executed by doge',
    'done':False
    },
    {
    'id':2,
    'title':u'dogecoin',
    'description':u'data to be executed by dogecoin',
    'done':False
    }
]
@app.route("/data",methods=["POST"])
def AddData():
    if notrequest.json:
        return jsonify({
        "status":"error",
        "message":"Provide data to doge"
        },400)
    task={
    'id':tasks[-1]['id']+1,
    'title':request.json['title'],
    'description':request.json.get('description',""),
    'done':False
    }
    tasks.append(task)
    return jsonify({
    "status":"success",
    "message":"doge got your data"
    })
@app.route("/getdata")
def GetData():
    return jsonify({
    "data":tasks
    })
if(__name__=="__main__"):
    app.run(debug=True)
