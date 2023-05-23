from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route("/")
def home():
    role = request.cookies.get("role")

    if role == "admin":
        flag = "This is not flag"
    else:
        flag = ""

    resp = make_response(render_template("index.html", flag=flag))
    if not role:
        resp.set_cookie("role", "user")
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
