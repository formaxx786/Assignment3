from flask import Flask,jsonify
import json
import os

app=Flask(__name__)

@app.route('/api', methods=['GET'])

def getData():
    filePath=os.path.join(os.path.dirname(__file__),"Data.json")

    try:
        with open(filePath,'r') as file:
            data=json.load(file)
            return jsonify(data),200
    
    except Exception as exc:
        return jsonify({"error": str(exc)})

if '__main__' ==__name__:
    app.run(debug=True)
