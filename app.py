from flask import Flask, render_template, request

app = Flask(__name__)

# 初始书签列表
bookmarks = [
    {'id': 1, 'title': 'Google', 'url': 'https://www.google.com'},
    {'id': 2, 'title': 'Bing', 'url': 'https://www.bing.com'},
    {'id': 3, 'title': 'Yahoo', 'url': 'https://www.yahoo.com'},
]

users = [
    {"username": "admin", "password": "admin"},
    {"username": "user", "password": "user"},
]


@app.route('/')
def index():
    return render_template('index.html', bookmarks=bookmarks)


@app.route('/add_bookmark', methods=['GET', 'POST'])
def add_bookmark():
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']
        id = bookmarks[-1]['id'] + 1
        if not url.startswith('http'):
            url = 'https://' + url
        bookmarks.append({'id': id, 'title': title, 'url': url})
        return render_template('index.html', bookmarks=bookmarks)
    else:
        return render_template('add_bookmark.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    pass


@app.route('/register')
def register():
    pass


if __name__ == '__main__':
    app.run(debug=True)
