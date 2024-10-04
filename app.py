from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('static', 'ads.txt')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/privacy')
def privacy():
    return render_template('Privacy.html')

@app.route('/terms')
def terms():
    return render_template('Terms.html')

if __name__ == '__main__':
    app.run(debug=True)
