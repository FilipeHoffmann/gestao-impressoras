const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM aditivos");
        res.json({ results });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { id_aditivo, descricao, data_inicial, data_final, situacao, id_contrato } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO aditivos (id_aditivo, descricao, data_inicial, data_final, situacao, id_contrato) VALUES (?, ?, ?, ?, ?, ?)',
            [id_aditivo, descricao, data_inicial, data_final, situacao, id_contrato]
        );
        res.status(201).json({ id: result.insertId, id_aditivo, descricao, data_inicial, data_final, situacao, id_contrato });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { descricao, data_inicial, data_final, situacao, id_contrato } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE aditivos SET descricao = ?, data_inicial = ?, data_final = ?, situacao = ?, id_contrato = ? WHERE id_aditivo = ?',
            [descricao, data_inicial, data_final, situacao, id_contrato, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Aditivo não encontrado');
        }

        res.status(200).json({ id, descricao, data_inicial, data_final, situacao, id_contrato });
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
            'DELETE FROM aditivos WHERE id_aditivo = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Aditivo não encontrado');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;
