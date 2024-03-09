from flask import Flask, render_template
import dao

app = Flask(__name__)

@app.route('/')
def index():
    categories= dao.load_catergory()
    products=dao.load_product()
    return render_template('index.html', categories=categories, products=products)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
