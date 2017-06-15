from flask import Flask, request, render_template

import news

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')

@app.route('/news', methods=['POST'])
def submit_data():
    vals = request.form['news-source']
    id = vals.split('_')[0]
    name = vals.split('_')[1]
    articles = news.main(id)
    print(articles)
    return render_template('news.html', articles=articles, name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0")