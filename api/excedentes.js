const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM excedentes");
        res.json({ results });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { quantidade, saldo, valor_atual, id_produto } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO excedentes (quantidade, saldo, valor_atual, id_produto) VALUES (?, ?, ?, ?)',
            [quantidade, saldo, valor_atual, id_produto]
        );
        res.status(201).json({ id: result.insertId, quantidade, saldo, valor_atual, id_produto });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { quantidade, saldo, valor_atual, id_produto } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE excedentes SET quantidade = ?, saldo = ?, valor_atual = ?, id_produto = ? WHERE id_excedente = ?',
            [quantidade, saldo, valor_atual, id_produto, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Excedente não encontrado');
        }

        res.status(200).json({ id, quantidade, saldo, valor_atual, id_produto });
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
            'DELETE FROM excedentes WHERE id_excedente = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Excedente não encontrado');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;