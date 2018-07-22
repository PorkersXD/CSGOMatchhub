/* Importing modules */
const express = require('express');
const HLTV = require('hltv-api');
const app = express();


/* Starting application on port 3000*/
app.listen(3000, function() {
  console.log('Listening on port 3000...');
});


function main() {

  /* Loads results and returns them to the page */ 
  app.get('/', function(req, res) {
    HLTV.getResults(function(results) {
      return res.json(results);
    });
  });
  console.log('Results Loaded')

 
  /* setTimeout(edetection, 60000)*/ 
}

/* Function to catch errors and reboot in case of error */
function edetection() { 
  try {
     main();

  } catch (err) {
   console.log(err);
   console.log('Relaunching...');
   edetection();
  }
}

edetection()