# from flask import Flask, request, jsonify
# from flask_cors import CORS
import utilToUse
from flask import Flask, request, jsonify
from flask_cors import CORS

# import pdb




def autoRunFunction():
    num=utilToUse.getTodaysDate()
    print(num)
    # pdb.set_trace()


app = Flask(__name__)
CORS(app)

@app.route('/yourEndpoint', methods=['POST'])
def handlePostRequest():
    if request.is_json:
        data = request.get_json()
        key = data.get('key')
        anotherKey = data.get('anotherKey')
        
        responseData = {
            'message': 'Received POST data'
        }
        return jsonify(responseData), 200
    else:
        return 'Invalid JSON data', 400

if __name__ == '__main__':
    autoRunFunction()
    app.run(debug=True)
    






"""
// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Specify the HTTP method, URL, and whether the request should be asynchronous
xhr.open("POST", "http://127.0.0.1:5000/yourEndpoint", true);

// Set the request headers (if needed)
xhr.setRequestHeader("Content-Type", "application/json"); // Adjust as needed

// Define a callback function to handle the response
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        // Handle the response data here
        var responseData = JSON.parse(xhr.responseText);
        console.log(responseData);
    }
};

// Create a JSON object with the data you want to send
var data = {
    key: "value",
    anotherKey: "anotherValue"
};

// Convert the data to a JSON string
var jsonData = JSON.stringify(data);

// Send the POST request with the data
xhr.send(jsonData);
"""