from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [{"image": "/static/images/blackjack.png", 
                 "title": "Blackjack", 
                 "description": "A command line blackjack game made with Python", 
                 "github": "https://github.com/N-Smith-00/CPS109-Blackjack"},
                {"image": "/static/images/yahtzee.png",
                 "title": "Yahtzee",
                 "description": "A command line Yahtzee game made with Python",
                 "github": "https://github.com/N-Smith-00/Yahtzee"},
                {"image": "/static/images/placeholder_image.jpg",
                 "title": "This website",
                 "description": "A website made with HTML, CSS, Python, and Flask",
                 "github": "https://github.com/N-Smith-00/Portfolio-Website"}]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)