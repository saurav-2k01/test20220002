from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def greet():
    name = request.args.get("name")
    if name==None:
        return "hello user"
    else:
        return f"welcome {name}"

if __name__ == "__main__":
    app.run(debug=True)
