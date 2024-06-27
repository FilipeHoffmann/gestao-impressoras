const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute('SELECT * FROM aditivos');
        res.json({ results });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;