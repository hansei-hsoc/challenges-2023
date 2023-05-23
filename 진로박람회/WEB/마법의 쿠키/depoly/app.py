from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route("/")
def home():
    role = request.cookies.get("role")

    if role == "admin":
        flag = "hsoc{C00ki3s_4r3_M4g1c}"
    else:
        flag = ""

    resp = make_response(render_template("index.html", flag=flag))
    if not role:
        resp.set_cookie("role", "user")
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
