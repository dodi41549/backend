from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cats = [
        {
            'name': 'Kitty',
            'image': 'kitty.jpg',
            'description': 'A cute and playful kitty.'
        },
        {
            'name': 'Simba',
            'image': 'simba.jpg',
            'description': 'A majestic and friendly cat.'
        },
        {
            'name': 'Whiskers',
            'image': 'whiskers.jpg',
            'description': 'A mischievous and adventurous cat.'
        }
    ]
    return render_template('index.html', cats=cats)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
