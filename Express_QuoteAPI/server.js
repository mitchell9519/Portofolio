const express = require('express');
const app = express();

const { quotes } = require('./data');
const { getRandomElement } = require('./utils');

const PORT = process.env.PORT || 4001;

app.listen(PORT, () =>{
  console.log(`listening on port : ${PORT}`)
})

app.get('/api/quotes/random',(req,res,next)=>{
  const random_quote= getRandomElement(quotes)
  res.send({quote: random_quote})
});

app.get("/api/quotes", (req, res, next) => {
  if (req.query.person) {
    const author = req.query.person;
    const result = quotes.filter((quote) => {
      return quote["person"] === author;
    });
    if (result.length > 0) {
      res.status(200).send({ quotes: result });
    } else {
      res.status(200).send({ quotes: [] });
    }
  } else {
    res.status(200).send({ quotes: quotes });
  }
});

app.post("/api/quotes", (req, res, next) => {
  if (req.query.quote && req.query.person) {
    const newQuote = {
      quote: req.query.quote,
      person: req.query.person,
    };
    quotes.push(newQuote);
    res.status(200).send({ quote: newQuote });
  } else {
    res.status(400);
  }
});




app.use(express.static('public'));


