from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)
glucose = [ 
    {
        "glucose_id" : "Little Women",
        "date": ["Lee Wonyoung", "Kim Joychu", "Park Wonso"],
        "glucose" : ["Drama", "Thriller"]
    },

    {
        "glucose_id" : "Squid Game",
        "date": ["Jinja Wong", "Lee Minsuk", "Park Wonso"],
        "glucose" : ["suspence", "Thriller"]
    }
]

@app.route('/glucose', methods=['GET'])
def displayglucose():
    return jsonify(glucose)

@app.route('/glucose', methods=['POST'])
def addglucose():
    glucose = request.get_json()
    glucose.append(glucose)
    return {'id': len(glucose)}, 200
    
@app.route('/glucose/<int:index>', methods=['DELETE'])
def deleteglucose(index):
    glucose.pop(index)
    return 'glucose was successfully deleted', 200

if __name__ == '__main__':
    
    app.run()
