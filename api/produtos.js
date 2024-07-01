const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM produtos");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { id_produto, descricao, franquia_pb, franquia_color, tipo, copia_locacao, color } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO produtos (id_produto, descricao, franquia_pb, franquia_color, tipo, copia_locacao, color) VALUES (?, ?, ?, ?, ?, ?, ?)',
            [id_produto, descricao, franquia_pb, franquia_color, tipo, copia_locacao, color]
        );
        res.status(201).json({ id: result.insertId, id_produto, descricao, franquia_pb, franquia_color, tipo, copia_locacao, color });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { descricao, franquia_pb, franquia_color, tipo, copia_locacao, color } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE produtos SET descricao = ?, franquia_pb = ?, franquia_color = ?, tipo = ?, copia_locacao = ?, color = ? WHERE id_produto = ?',
            [descricao, franquia_pb, franquia_color, tipo, copia_locacao, color, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Produto não encontrado');
        };

        res.status(200).json({ id });
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
            'DELETE FROM produtos WHERE id_produto = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Produto não encontrado');
        };

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;