const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT id_contrato, DATE_FORMAT(data_inicial, '%d-%m-%Y') AS data_inicial, DATE_FORMAT(data_final, '%d-%m-%Y') AS data_final, DATE_FORMAT(data_final_atual, '%d-%m-%Y') AS data_final_atual FROM `gestao-impressoras`.contratos ORDER BY data_inicial;");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { id_contrato, data_inicial, data_final, data_final_atual } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO contratos (id_contrato, data_inicial, data_final, data_final_atual) VALUES (?, ?, ?, ?)',
            [id_contrato, data_inicial, data_final, data_final_atual]
        );
        res.status(201).json({ id: result.insertId, id_contrato, data_inicial, data_final, data_final_atual });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { data_inicial, data_final, data_final_atual } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE contratos SET data_inicial = ?, data_final = ?, data_final_atual = ? WHERE id_contrato = ?',
            [data_inicial, data_final, data_final_atual, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Contrato não encontrado');
        };

        res.status(200).json({ id, data_inicial, data_final, data_final_atual });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.delete('/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'DELETE FROM contratos WHERE id_contrato = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Contrato não encontrado');
        };

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;
