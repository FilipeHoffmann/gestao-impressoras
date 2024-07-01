const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM aditivos_itens");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { descricao, quantidade, valor, id_item, id_aditivo, id_secretaria } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO aditivos_itens (descricao, quantidade, valor, id_item, id_aditivo, id_secretaria) VALUES (?, ?, ?, ?, ?, ?)',
            [descricao, quantidade, valor, id_item, id_aditivo, id_secretaria]
        );
        res.status(201).json({ id: result.insertId, descricao, quantidade, valor, id_item, id_aditivo, id_secretaria });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { descricao, quantidade, valor, id_item, id_aditivo, id_secretaria } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE aditivos_itens SET descricao = ?, quantidade = ?, valor = ?, id_item = ?, id_aditivo = ?, id_secretaria = ? WHERE id_aditivo_item = ?',
            [descricao, quantidade, valor, id_item, id_aditivo, id_secretaria, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Aditivo item não encontrado');
        }

        res.status(200).json({ id, descricao, quantidade, valor, id_item, id_aditivo, id_secretaria });
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
            'DELETE FROM aditivos_itens WHERE id_aditivo_item = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Aditivo item não encontrado');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;