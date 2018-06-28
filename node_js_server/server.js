const express = require('express');
const HLTV = require('hltv-api');
const app = express();
/*
console.log('MATCHES')
app.get('/', function(req, res) {
  HLTV.getNews(function(news) {
    return res.json(news);
  });
});
*/

console.log('Loading Results')
app.get('/', function(req, res) {
  HLTV.getResults(function(results) {
    return res.json(results);
  });
});

/*
console.log('MATCH ID')
app.get('/:matchId(*)', function(req, res) {
  HLTV.getMatches(matchId, function(stats) {
    return res.json(stats);
  });
});
*/
app.listen(3000, function() {
  console.log('Listening on port 3000...');
});
