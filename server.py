from flask import Flask, render_template, request, redirect
from time import localtime, strftime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)

    loctime =  strftime("%Y-%m-%d %H:%M %p", localtime())

    name_form = request.form['first_name']
    lastname_form = request.form['last_name']
    id_form = request.form['student_id']
    apple_form = request.form['apple']
    strawberry_form = request.form['strawberry']
    rasp_form = request.form['raspberry']

    order = int(request.form['apple'])+ int(request.form['strawberry'])+int(request.form['raspberry'])

    return render_template("checkout.html", first_name=name_form, 
    last_name=lastname_form, student_id=id_form, apple=apple_form, 
    strawberry=strawberry_form, raspberry=rasp_form, loctime=loctime, order=order)

    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    