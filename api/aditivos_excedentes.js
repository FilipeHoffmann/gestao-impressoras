const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM aditivos_excedentes");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { descricao, quantidade, valor, id_aditivo, id_excedente } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO aditivos_excedentes (descricao, quantidade, valor, id_aditivo, id_excedente) VALUES (?, ?, ?, ?, ?)',
            [descricao, quantidade, valor, id_aditivo, id_excedente]
        );
        res.status(201).json({ id: result.insertId, descricao, quantidade, valor, id_aditivo, id_excedente });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { descricao, quantidade, valor, id_aditivo, id_excedente } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE aditivos_excedentes SET descricao = ?, quantidade = ?, valor = ?, id_aditivo = ?, id_excedente = ? WHERE id_aditivo_excedente = ?',
            [descricao, quantidade, valor, id_aditivo, id_excedente, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Aditivo excedente não encontrado');
        }

        res.status(200).json({ id, descricao, quantidade, valor, id_aditivo, id_excedente });
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
            'DELETE FROM aditivos_excedentes WHERE id_aditivo_excedente = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Aditivo excedente não encontrado');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;