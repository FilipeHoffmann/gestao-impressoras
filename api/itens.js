const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM itens");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const { id_item, descricao, quantidade, saldo, valor_atual, id_contrato, id_produto, id_secretaria } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute('INSERT INTO itens (id_item,descricao,quantidade,saldo,valor_atual,id_contrato,id_produto,id_secretaria) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            [id_item, descricao, quantidade, saldo, valor_atual, id_contrato, id_produto, id_secretaria]
        );
        res.status(201).json({ id: result.insertId, id_item, descricao, quantidade, saldo, valor_atual, id_contrato, id_produto, id_secretaria });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const { descricao, quantidade, saldo, valor_atual, id_contrato, id_produto, id_secretaria } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE itens SET descricao = ?, quantidade = ?, saldo = ?, valor_atual = ?, id_contrato = ?, id_produto = ?, id_secretaria = ? WHERE id_item = ?',
            [descricao, quantidade, saldo, valor_atual, id_contrato, id_produto, id_secretaria, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Item não encontrado');
        };

        res.status(200).json({ id, descricao, quantidade, saldo, valor_atual, id_contrato, id_produto, id_secretaria });
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
            'DELETE FROM itens WHERE id_item = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Item não encontrado');
        };

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;