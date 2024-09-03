from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():    
    return render_template(template_name_or_list='home.html')

@app.route("/login", methods=["POST", "GET"])
def processData():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)
        return f"<h1>Name: {name} Password {password}</h1>"        
    else:
        return "<h1>Error</h1>"

    
    
    

if __name__ == "__main__":
    
    app.run(debug=True)