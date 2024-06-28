const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM contadores");
        res.json({ results });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { cont_pb, cont_color, data, id_impressora } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO contadores (cont_pb, cont_color, data, id_impressora) VALUES (?, ?, ?, ?)',
            [cont_pb, cont_color, data, id_impressora]
        );
        res.status(201).json({ id: result.insertId, cont_pb, cont_color, data, id_impressora });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { cont_pb, cont_color, data, id_impressora } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE contadores SET cont_pb = ?, cont_color = ?, data = ?, id_impressora = ? WHERE id_contador = ?',
            [cont_pb, cont_color, data, id_impressora, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Contador não encontrado');
        }

        res.status(200).json({ id, cont_pb, cont_color, data, id_impressora });
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
            'DELETE FROM contadores WHERE id_contador = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Contador não encontrado');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;