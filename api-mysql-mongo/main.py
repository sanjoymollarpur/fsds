from flask import Flask ,request,jsonify
import mysql.connector as connection
app = Flask(__name__)
conn = connection.connect(host="localhost",user="root", use_pure=True)
my_cursor=conn.cursor()
my_cursor.execute("create database if not exists taskdb")
my_cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


@app.route('/insert',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        my_cursor.execute("insert into taskdb.tasktable  values(%s , %s)",(name ,number))
        conn.commit()
        return jsonify(str('succesfully inserted'))



@app.route("/update" , methods= ['POST'])
def update():
    if request.method=='POST':
         get_name = request.json['name']
         my_cursor.execute("update taskdb.tasktable set number = number + 500 where name = %s ",(get_name,))
         conn.commit()
         return jsonify(str("updated successfully"))


@app.route("/delete" , methods= ['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        my_cursor.execute("delete from taskdb.tasktable where name = %s",(name_del,))
        conn.commit()
        return jsonify(str("deleted successfully"))

@app.route("/fetch",methods = ['POST','GET'])
def fetch_data():
    my_cursor.execute("select * from taskdb.tasktable")
    l = []
    for i in my_cursor.fetchall():
        l.append(i)
    return jsonify(str(l))


if __name__ == '__main__':
    app.run()
    

