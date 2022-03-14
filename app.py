from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_placement():
    stock_id = int(request.form.get('stock_id'))
    last_price = float(request.form.get('last_price'))
    mid = float(request.form.get('mid'))
    trans_qty = float(request.form.get('trans_qty'))
    open_interest = float(request.form.get('open_interest'))
    bid1 = float(request.form.get('bid1'))
    bid2 = float(request.form.get('bid2'))
    bid3 = float(request.form.get('bid3'))
    bid4 = float(request.form.get('bid4'))
    bid5 = float(request.form.get('bid5'))
    ask1 = float(request.form.get('ask1'))
    ask2 = float(request.form.get('ask2'))
    ask3 = float(request.form.get('ask3'))
    ask4 = float(request.form.get('ask4'))
    ask5 = float(request.form.get('ask5'))
    bid1vol = int(request.form.get('bid1vol'))
    bid2vol = int(request.form.get('bid2vol'))
    bid3vol = int(request.form.get('bid3vol'))
    bid4vol = int(request.form.get('bid4vol'))
    bid5vol = int(request.form.get('bid5vol'))
    ask1vol = int(request.form.get('ask1vol'))
    ask2vol = int(request.form.get('ask2vol'))
    ask3vol = int(request.form.get('ask3vol'))
    ask4vol = int(request.form.get('ask4vol'))
    ask5vol = int(request.form.get('ask5vol'))

    # prediction
    result = model.predict(np.array(
        [stock_id, last_price, mid, trans_qty, open_interest, bid1, bid2, bid3, bid4, bid5, ask1, ask2, ask3, ask4, ask5, bid1vol,
         bid2vol, bid3vol, bid4vol, bid5vol, ask1vol, ask2vol, ask3vol, ask4vol, ask5vol]).reshape(1, 25))
    if result == 1:
        fresult = "Up 👍"
    else:
        fresult = "Down 👎"

    return str(fresult)


if __name__ == '__main__':
    app.run(debug=True)
