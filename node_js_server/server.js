const express = require('express');
const HLTV = require.resolve('hltv-api');
const app = express();

app.get('/', function(req, res) {
  HLTV.getResults(function(results) {
    return res.json(results);
  });
});
console.log('Results Loaded')

app.listen(3000, function() {
  console.log('Running on port 3000, eg.) 192.168.1.1:3000');
});
