from flask import Flask, render_template, request
from detect_fake_news import detectFake

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the news article text from the form
        news_text = request.form['news_text']

        # Call your fake news detection program with the news_text input
        result = detectFake(news_text)

        # Render a template with the result
        return render_template('index.html', result=result)
    else:
        # Render the form template
        return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)