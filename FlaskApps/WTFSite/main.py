from flask import Flask, render_template,request
from form import MyForm


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = MyForm()
    if request.method == "GET":
        return render_template(template_name_or_list='login.html', form=form)
    elif request.method == "POST":
        if (form.validate_on_submit()):
            print("suceess") 
            print(request.form.get('email'))
            print(request.form.get('password'))
            if (form.email.data == 'admin@example.com' and form.password.data =="12345678"):
                # render using template inheritance            
                return render_template(template_name_or_list='success.html')
            else:
                return render_template(template_name_or_list="denied.html")            


if __name__ == '__main__':
    SECRET_KEY = 'asecretkey'.encode('utf-8')
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(debug=True)
