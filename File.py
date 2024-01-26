from flask import *
import mysql.connector
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("print.html")
@app.route("/success",methods=["POST","GET"])
def user():
    uname = request.form["name"]
    passwd = request.form["pass"]
    if passwd == "":
        return redirect(url_for("home"))
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="bro")
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO vardhan (name,password) VALUES (%s,%s)",(uname,passwd))
    mydb.commit()
    return "SuccessFull"
if __name__=="__main__":
    app.run(debug=True)

    