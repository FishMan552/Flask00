from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)

    # 备注1、
    # 备注2
