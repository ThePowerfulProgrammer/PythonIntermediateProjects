from flask import Flask, render_template
import requests
import random



app = Flask(__name__)

@app.route("/")
def homePage():
    numbers = [random.randint(0,10) for _ in range(10)]
    return render_template(template_name_or_list='home.html', numbers=numbers)

@app.route("/guess/<name>")
def guess(name):
    genderAPIEndpoint = f'https://api.genderize.io?name={name}'

    response = requests.get(genderAPIEndpoint)
    response.raise_for_status()
    print(response.text)
    print(response.json)
    
    name = response.json()['name']
    gender = response.json()['gender']
    prob = float(response.json()['probability']) * 100
    
    ageAPIEndpoint = f"https://api.agify.io?name={name}"
    response = requests.get(ageAPIEndpoint)
    response.raise_for_status()
    age = response.json()['age']
    
    return render_template(template_name_or_list='guess.html', name=name, gender=gender, prob=prob, age=age)
    

if __name__ == "__main__":
    app.run(debug=True)
    