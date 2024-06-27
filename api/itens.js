const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [contratos] = await connection.execute('SELECT id_contrato, DATE_FORMAT(data_inicial, "%d-%m-%Y") AS data_inicial, DATE_FORMAT(data_final, "%d-%m-%Y") AS data_final, DATE_FORMAT(data_final_atual, "%d-%m-%Y") AS data_final_atual FROM `gestao-impressoras`.contratos;')
        const [aditivos] = await connection.execute('SELECT * FROM aditivos');
        res.json({ contratos, aditivos });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;