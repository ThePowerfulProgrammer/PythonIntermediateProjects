from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def bold_decorator(function):
    
    def wrapper():
        
        function_value = function()
        function_value_bold = f"<b>{function_value}</b>"
        return function_value_bold
    
    return wrapper

def italic_deorator(function):
    
    def wrapper():
        function_value = function()
        function_value_italic = f"<em>{function_value}</em>"
        return function_value_italic

    return wrapper

def underline_decorator(function):
    
    def wrapper():
        function_value = function()
        function_value_underline = f"<u>{function_value}</u>"
        return function_value_underline
    
    return wrapper


@app.route('/')
def homePage():
    return "<h1>Hello Flask</h1>"

@app.route('/bye')
@bold_decorator
@italic_deorator
@underline_decorator
def byePage():
    return "Bye"

@app.route('/username/<name>')
def greetUser(name):
    return f"Greetings {name}"

if __name__ == '__main__':
    app.run()
    
    
    