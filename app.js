const express = require('express');
const app = express();
const db = require('./db');

app.get('/', (req, res) => {
    res.send('');
});

app.get('/', (req, res) => {
    res.send('');
});

app.get('/', (req, res) => {
    res.send('');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
