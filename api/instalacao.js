const express = require('express');
const router = express.Router();
const createConnection = require('../db');

router.use(express.json());

router.get('/', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute("SELECT * FROM instalacao");
        res.json(results);
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.post('/', async (req, res) => {
    const {
        local_instalacao, endereco, transformador, responsavel, ip,
        data_instalacao, cont_instalacao, data_retirada, cont_retirada,
        id_item, id_impressora
    } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO instalacao (local_instalacao, endereco, transformador, responsavel, ip, data_instalacao, cont_instalacao, data_retirada, cont_retirada, id_item, id_impressora) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            [local_instalacao, endereco, transformador, responsavel, ip, data_instalacao, cont_instalacao, data_retirada, cont_retirada, id_item, id_impressora]
        );
        res.status(201).json({
            id: result.insertId, local_instalacao, endereco, transformador,
            responsavel, ip, data_instalacao, cont_instalacao, data_retirada,
            cont_retirada, id_item, id_impressora
        });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

router.put('/:id', async (req, res) => {
    const { id } = req.params;
    const {
        local_instalacao, endereco, transformador, responsavel, ip,
        data_instalacao, cont_instalacao, data_retirada, cont_retirada,
        id_item, id_impressora
    } = req.body;

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'UPDATE instalacao SET local_instalacao = ?, endereco = ?, transformador = ?, responsavel = ?, ip = ?, data_instalacao = ?, cont_instalacao = ?, data_retirada = ?, cont_retirada = ?, id_item = ?, id_impressora = ? WHERE id_instalacao = ?',
            [local_instalacao, endereco, transformador, responsavel, ip, data_instalacao, cont_instalacao, data_retirada, cont_retirada, id_item, id_impressora, id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Instalação não encontrada');
        }

        res.status(200).json({
            id, local_instalacao, endereco, transformador, responsavel, ip,
            data_instalacao, cont_instalacao, data_retirada, cont_retirada,
            id_item, id_impressora
        });
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
            'DELETE FROM instalacao WHERE id_instalacao = ?',
            [id]
        );

        if (result.affectedRows === 0) {
            return res.status(404).send('Instalação não encontrada');
        }

        res.status(200).json({ result });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;