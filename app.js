const express = require('express');
const app = express();
const createConnection = require('./db');

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/contratos', async (req, res) => {
    try {
        const connection = await createConnection();
        const [results] = await connection.execute('SELECT * FROM contratos');
        res.json({ results });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

app.post('/contratos', async (req, res) => {
    const { id_contrato, data_inicial, data_final, data_final_atual } = req.body;

    if (!id_contrato || !data_inicial || !data_final || !data_final_atual) {
        return res.status(400).send('Todos os campos são obrigatórios');
    }

    try {
        const connection = await createConnection();
        const [result] = await connection.execute(
            'INSERT INTO contratos (id_contrato, data_inicial, data_final, data_final_atual) VALUES (?, ?, ?, ?)',
            [id_contrato, data_inicial, data_final, data_final_atual]
        );
        res.status(201).json({ id: result.insertId, id_contrato, data_inicial, data_final, data_final_atual });
    } catch (error) {
        console.error('Error executing query', error);
        res.status(500).send('Internal Server Error');
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});