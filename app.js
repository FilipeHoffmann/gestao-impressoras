const express = require('express');
const app = express();
const contratosRoutes = require('./api/contratos');
const secretariasRoutes = require('./api/secretarias')
const itensRoutes = require('./api/itens')
const produtosRoutes = require('./api/produtos')

const PORT = process.env.PORT || 3000;

app.use('/contratos', contratosRoutes);
app.use('/secretarias', secretariasRoutes);
app.use('/itens', itensRoutes)
app.use('/produtos', produtosRoutes)

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
