from flask import Flask

app=Flask(__name__)

@app.route('/messagesrepo,methods=['POST'])
def takeInputDate():
    
    return 'Hello,World'

if __name__=='__main__':
    app.run()
    



// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Specify the HTTP method, URL, and whether the request should be asynchronous
xhr.open("POST", "http://127.0.0.1:5000/your_endpoint", true);

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
