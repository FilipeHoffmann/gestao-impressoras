const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute('SELECT * FROM secretarias');
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { secretaria } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO secretarias (secretaria) VALUES (?)',
            [secretaria]
        );
        res.status(201).json({ id: result.insertId, secretaria });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { secretaria } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE secretarias SET secretaria = ? WHERE id_secretaria = ?',
            [secretaria, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Secretaria não encontrada');
        };

        res.status(200).json({ id, secretaria });
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
            'DELETE FROM secretarias WHERE id_secretaria = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Secretaria não encontrada');
        };

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;