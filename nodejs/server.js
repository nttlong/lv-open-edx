var request = require('request');
request.post('http://0.0.0.0:8000/web_services/',{
    json: true,
    body:{
        path:"lv@get_list_of_students"
    }
   
}, function (error, response, body) {
    console.log('error:', error); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    console.log('body:', body); // Print the HTML for the Google homepage.
  })
