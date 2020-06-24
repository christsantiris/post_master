from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
  {
    'title': 'Post 1',
    'content': 'This is post 1',
    'author': 'Chris'
  },
    {
    'title': 'Post 2',
    'content': 'This is post 2'
  },
    {
    'title': 'Post 3',
    'content': 'This is post 3'
  }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)