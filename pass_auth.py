from flask import Flask, jsonify , request
app = Flask(__name__)

users = {
    "alex" : "alimon",
    "giga" : "gumiya",
    "hudin" : "gijayi"
}

@app.route("/pass_auth" , methods = ['GET'])

def pass_auth():
    return jsonify({"message" : "The end point is working just fine"})

@app.route("/login", methods = ['POST'])

def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username]==password:
        return jsonify({"message" : "Valid input"}) , 201
    else:
        return jsonify({"message" : "not valid username or password"}) , 401

if __name__ == '__main__':
    app.run(debug = True)
