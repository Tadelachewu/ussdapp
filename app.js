app.post('/ussd', (req, res) => {
  const { sessionId, phoneNumber, text } = req.body;
  let response = '';

  if (text === '') {
    response = `CON Welcome to Tadele Bank
1. Check Balance
2. Send Money`;
  } else if (text === '1') {
    response = `END Your balance is 1000 ETB`;
  } else {
    response = `END Invalid input`;
  }

  res.set('Content-Type', 'text/plain');
  res.send(response);
});
