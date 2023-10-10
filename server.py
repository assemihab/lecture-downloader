# from flask import Flask, request, jsonify
# from flask_cors import CORS
import utilToUse
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

# import pdb

file_path = 'E:\projects\lectures downloader\lastDate.txt'
groupID='LWLZdL20Z11B0zI5SPUndn'

def autoRunFunction(file_path,groupID):
    utilToUse.openGroup(groupID)
    utilToUse.openTheConsole()
    utilToUse.getFormattedDate(file_path)
    
    # pdb.set_trace()
def writeCommand():
    pass
    # utilToUse.writeCommand()
    # pdb.set_tra
app= Flask(__name__)

CORS(app)

@app.route('/yourEndpoint', methods=['POST'])
def handlePostRequest():
    if request.is_json:
        data = request.get_json()
        
        date = data.get('key')
        formattedDate=utilToUse.wrtieTheLatestDate(date)
        with open(file_path, 'w') as f:
            f.write(formattedDate)
        
        responseData = {
            'message': 'Received POST data'
        }
        return jsonify(responseData), 200
    else:
        return 'Invalid JSON data', 400

if __name__ == '__main__':
    # autoRunFunction(file_path,groupID)
    writeCommandThread=threading.Thread(target=writeCommand)
    serverThread=threading.Thread(target=app.run(debug=False))
    # serverThread.daemon=True
    writeCommandThread.start()
    serverThread.start()
    # import time
    # time.sleep(5)

    # app.run(debug=True)
    #I want to run the server in the backGround and open new thread for write commands function
    # writeCommand()
    






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