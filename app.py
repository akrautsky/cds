import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text


from flask import Flask,request,app,jsonify,url_for,render_template

app = Flask(__name__)

my_saved_model = tf.keras.models.load_model(
    ('myModel.h5'),
    custom_objects = {'KerasLayer': hub.KerasLayer}
)


@app.route('/')
def home():
    return render_template('home.html')

