from flask import Flask, render_template
from post import Post

app = Flask(__name__)


# A path for home , the general layout + post index
@app.route("/Home")
def homePage():
    post = Post()

    titles = post.getBlogTitles()
    subtitles = post.getBlogSubtitles()
    ids = post.getBlogIds()
    print(ids)
    
    return render_template(template_name_or_list='home.html',titles=titles,subtitles=subtitles, ids=ids)    


# A path for indiviual post details
@app.route("/Blog/<int:id>")
def getBlogPost(id):
    post = Post()

    body = post.getBlogPost(id)
    title = post.getBlogTitle(id)
    subtitle = post.getBlogSubtitle(id)

    return render_template('postDetail.html', body=body,title=title, subtitle=subtitle)
    

# Paths for details from navbar


# path 


if __name__ == "__main__":
    
    app.run(debug=True)