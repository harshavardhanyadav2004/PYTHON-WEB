from flask import * 
app = Flask(__name__)
app.secret_key="abc"
dictionary = {}
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login")
def home1():
  if "login" in session:
      return redirect(url_for("home3"))
  return render_template("index1.html")
@app.route("/success",methods=["POST","GET"])
def home2():
    uname = request.form["label_name"]
    passwd = request.form["label_password"]
    session["login"] = "Passed"
    dictionary.update(request.form)
    return redirect(url_for("home3"))
@app.route("/view")
def home3():
    if "login" not in session:
        return redirect(url_for("home1"))
    return render_template("index2.html",list1 = dictionary)
@app.route("/LogOut")
def home4():
    if "login" in session:
        session.pop("login",None)
    return redirect(url_for("home"))
if __name__=='__main__':
    app.run(debug=True)
