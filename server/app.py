from flask import Flask, jsonify
from flask_cors import CORS
import os
import base64

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/photos', methods=['GET'])
def getPhotos():
    photo_dir = './photos/'
    photos = []
    for filename in os.listdir(photo_dir):
        f = os.path.join(photo_dir, filename)
        with open(f, "rb") as image:
            data = image.read()
            data = base64.b64encode(data)
            photos.append({
                'name': filename,
                'src': 'data:image/jpg;base64,{}'.format(data.decode("ascii"))}
            )
    return jsonify(photos)


if __name__ == '__main__':
    app.run(debug=True)
