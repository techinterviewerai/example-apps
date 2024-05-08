from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook_example', methods=['POST'])
def example_post_route():
    data = request.json
    print(data)
    return {"message": "Data received successfully"}, 200

if __name__ == "__main__":
    app.run(debug=True)
