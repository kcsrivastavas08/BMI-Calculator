from flask import Flask, request, render_template  #py elliot.py #render template for rendering a template
app = Flask(__name__)


 #it helps to designate a url...we can define as many time as we want
@app.route('/', methods=['GET', 'POST']) #it helps to designate a url
def root():
    bmi= ''
    if request.method == 'POST' and 'username' in request.form:
        name=float(request.form.get('username'))
        food=float(request.form.get('userfood'))
        bmi = bodymassindex(name, food)
    
    return render_template("index.html",
                            bmi=bmi)

def bodymassindex(name, food):
    return round ((name / (food/100) ** 2), 2)
                           


app.run()
#css in static
#html in templates
