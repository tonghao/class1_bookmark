from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "sc-py=ps"

# 初始书签列表
bookmarks = [
    {'id': 1, 'title': 'Google', 'url': 'https://www.google.com', 'user': 'admin'},
    {'id': 2, 'title': 'Bing', 'url': 'https://www.bing.com', 'user': 'user'},
    {'id': 3, 'title': 'Yahoo', 'url': 'https://www.yahoo.com', 'user': 'user'},
]

users = [
    {"username": "admin", "password": "admin"},
    {"username": "user", "password": "user"},
]


@app.route('/')
def index():
    if 'username' in session:
        user_bookmarks = [
            bookmark
            for bookmark in bookmarks
            if bookmark['user'] == session['username']
        ]
        return render_template('index.html', bookmarks=user_bookmarks)
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
    if request.method == 'POST':
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        print(username, password)
        for user in users:
            if user["username"] == username and user["password"] == password:
                session['username'] = username
                return redirect(url_for("index"))
        flash("用户名或密码不正确")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop("username")
    return redirect(url_for('index'))


@app.route('/register')
def register():
    return "register"


if __name__ == '__main__':
    app.run(debug=True)
