
const express = require('express');
const HLTV = require('hltv-api');
const app = express();

app.get('/', function(req, res) {
  HLTV.getResults(function(results) {
    return res.json(results);
  });
});
console.log('Results Loaded')

app.listen(3000, function() {
  console.log('Listening on port 3000...');
});
