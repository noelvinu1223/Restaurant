from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)
from query import allbranch, allchefs, allmenu, allservers, ci, fi, oi, pi, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, \
    q11, trigger


@app.route('/test')
def hello_world():
    return 'Working Success'


@app.route("/")
def indexPage():
    branches = allbranch()
    chefsss = allchefs()
    menuuu = allmenu()
    serve = allservers()
    return render_template("index.html", branchInfo=branches, chefinfo=chefsss, menuinfo=menuuu, serverinfo=serve)


@app.route("/query1")
def query1():
    cursor, cursor1 = q1()
    return render_template("demo1.html", cursor=cursor, cursor1=cursor1)


@app.route("/query2")
def query2():
    cursor = q2()
    return render_template("demo2.html", cursor=cursor)


@app.route("/query3")
def query3():
    cursor = q3()
    return render_template("demo3.html", cursor=cursor)


@app.route("/query4")
def query4():
    cursor = q4()
    return render_template("demo4.html", cursor=cursor)


@app.route("/query5")
def query5():
    cursor = q5()
    return render_template("demo5.html", cursor=cursor)


@app.route("/query6")
def query6():
    cursor = q6()
    return render_template("demo6.html", cursor=cursor)


@app.route("/query7")
def query7():
    cursor = q7()
    return render_template("demo7.html", cursor=cursor)


@app.route("/query8")
def query8():
    cursor = q8()
    return render_template("demo8.html", cursor=cursor)


@app.route("/query9")
def query9():
    cursor = q9()
    return render_template("demo9.html", cursor=cursor)


@app.route("/query10")
def query10():
    cursor = q10()
    return render_template("demo10.html", cursor=cursor)


@app.route("/query11")
def query11():
    cursor = q11()
    return render_template("demo11.html", cursor=cursor)


@app.route("/customerInfo")
def customerinfo():
    list1ofcustomer = ci()
    return render_template("customerinfo.html", info=list1ofcustomer)


@app.route("/costmer", methods=["GET", "POST"])
def customerinput():
    if request.method == "POST":
        customerName = request.form.get("customerName", None)
        customerId = request.form.get("customerId", None)
        duration = request.form.get("duration", None)
        tableno = request.form.get("tableNo", None)
        branchId = request.form.get("branchId", None)
        nos = request.form.get("Nos", None)
        Phone = request.form.get("Phone", None)

        conn = sqlite3.connect('../PycharmProjects/Restaurant/restaurant.db')
        conn.execute('''INSERT INTO customer (cust_id,
             c_name,
             phone,
              table_no,
               no_of_seats,
               b_id,
                 duration) VALUES (?,?,?,?,?,?,?) ''',
                     (customerId
                      , customerName
                      , Phone
                      , tableno
                      , nos
                      , branchId,
                      duration))
        conn.commit()
        conn.close()
        trigger()
        return redirect(url_for("indexPage"))
    elif request.method == "GET":
        return render_template("customer.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedbackinfo():
    if request.method == "POST":
        name = request.form.get("name", None)
        comment = request.form.get("comments", None)
        foodoption = request.form.get("food", None)
        serviceoption = request.form.get("services", None)

        conn = sqlite3.connect('../PycharmProjects/Restaurant/restaurant.db')
        conn.execute('''INSERT INTO feedback (name,
             comments,
             food,
              service
            ) VALUES (?,?,?,?) ''',
                     (name
                      , comment
                      , foodoption
                      , serviceoption
                      ))
        conn.commit()
        conn.close()
        return redirect(url_for("indexPage"))
    elif request.method == "GET":
        return render_template("feedback.html")


@app.route("/orders", methods=["GET", "POST"])
def orderinfo():
    if request.method == "POST":
        mid = request.form.get("menu_id", None)
        cid = request.form.get("customer_id", None)

        conn = sqlite3.connect('../PycharmProjects/Restaurant/restaurant.db')
        conn.execute('INSERT INTO orders (menu_id,cust_id) VALUES (?,?) ',
                     (mid, cid))
        conn.commit()
        conn.close()
        return redirect(url_for("indexPage"))
    elif request.method == "GET":
        return render_template("orders.html")


@app.route("/parkinga", methods=["GET", "POST"])
def parkinginput():
    if request.method == "POST":
        vehno = request.form.get("vn", None)
        vtype = request.form.get("type1", None)
        brid = request.form.get("branchid", None)
        cuid = request.form.get("customerid", None)
        ti = request.form.get("timein", None)
        to = request.form.get("timeout", None)

        conn = sqlite3.connect('../PycharmProjects/Restaurant/restaurant.db')
        conn.execute('''INSERT INTO parking (vehicle_no,
             type,
             b_id,
              cust_id,
               time_in,
               time_out
                 ) VALUES (?,?,?,?,?,?) ''',
                     (vehno
                      , vtype
                      , brid
                      , cuid
                      , ti
                      , to
                      ))
        conn.commit()
        conn.close()
        return redirect(url_for("indexPage"))
    elif request.method == "GET":
        return render_template("parking.html")


@app.route("/feedbackInfor")
def feedbackinfor():
    list2ofcustomer = fi()
    return render_template("feedbackinfo.html", info=list2ofcustomer)


@app.route("/orders")
def orderinput():
    return render_template("orders.html")


@app.route("/ordersinfo")
def ordersinfo():
    list3ofcustomer = oi()
    return render_template("ordersinfo.html", info=list3ofcustomer)


@app.route("/parkinginfo")
def parkinginfo():
    list4ofcustomer = pi()
    return render_template("parkinginfo.html", info=list4ofcustomer)


@app.route("/feedback")
def feedbackinput():
    return render_template("feedback.html")


@app.route("/queries")
def queries():
    return render_template("queries.html")


if __name__ == '__main__':
    app.run(debug=True)
