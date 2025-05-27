from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route("/")

def home():
    return "Flask is working just fine"

@app.route("/signup" , methods=["POST"])
def signup():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    print(f"Data recieved {name , email , password}")

    return jsonify({"message": "signup data recived successfully"})


if __name__ == "__main__" :
    app.run(debug=True)
