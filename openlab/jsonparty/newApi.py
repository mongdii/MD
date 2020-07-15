import os, sqlite3, json
from flask import Flask, render_template, jsonify #
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

con = sqlite3.connect('./test.db', check_same_thread=False)

with open('./test.json', encoding = 'utf-8-sig') as f:
    imp_json = json.load(f)


class test1(Resource):
    def get(self, imp_id): #get : server에서 가져옴, post : server에 보냄
        return imp_json[int(imp_id)-11] #index 0번의 page를 11로 설정

class test2(Resource):
    def get(self):
        return imp_json

api.add_resource(test1, '/imp/<imp_id>')
api.add_resource(test2, '/imp')

@app.route('/api/json')
def serviceJson():
    return jsonify(imp_json)

@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <t1>'넉살 탈출'</t1>
    
</body>
</html>'''

if __name__ == '__main__' :
    app.run(debug=True, host='127.0.0.1')
