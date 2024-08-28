from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    post = Post()

    titles = post.getBlogTitles()
    subtitles = post.getBlogSubtitles()
    ids = post.getBlogIds()
    
    
    return render_template("index.html", titles=titles,subtitles=subtitles, ids=ids)
    
@app.route('/blog/<int:id>')
def getBlogPost(id):
    post = Post()

    body = post.getBlogPost(id)
    title = post.getBlogTitle(id)
    subtitle = post.getBlogSubtitle(id)

    return render_template('post.html', body=body,title=title, subtitle=subtitle)

if __name__ == "__main__":
    app.run(debug=True)
