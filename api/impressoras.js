const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM impressoras");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { marca_modelo } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO impressoras (marca_modelo) VALUES (?)',
            [marca_modelo]
        );
        res.status(201).json({ id: result.insertId, marca_modelo });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { marca_modelo } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE impressoras SET marca_modelo = ? WHERE id_impressora = ?',
            [marca_modelo, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Impressora não encontrada');
        }

        res.status(200).json({ id, marca_modelo });
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
            'DELETE FROM impressoras WHERE id_impressora = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Impressora não encontrada');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;