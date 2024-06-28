const express = require('express');
const app = express();
const contratosRoutes = require('./api/contratos');
const secretariasRoutes = require('./api/secretarias')
const produtosRoutes = require('./api/produtos')
const itensRoutes = require('./api/itens')
const aditivosRoutes = require('./api/aditivos')
const aditivos_itensRoutes = require('./api/aditivos_itens')
const aditivos_excedentesRoutes = require('./api/aditivos_excedentes')
const excedentesRoutes = require('./api/excedentes')

const PORT = process.env.PORT || 3000;

app.use('/contratos', contratosRoutes);
app.use('/secretarias', secretariasRoutes);
app.use('/produtos', produtosRoutes)
app.use('/itens', itensRoutes)
app.use('/aditivos', aditivosRoutes)
app.use('/aditivos_itens', aditivos_itensRoutes)
app.use('/aditivos_excedentes', aditivos_excedentesRoutes)
app.use('/excedentes', excedentesRoutes)

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
