import React from 'react';
import '../styles/ContractForm.css';

function ContractForm({ newContract, handleInputChange, handleSubmit }) {
    return (
        <form onSubmit={handleSubmit}>
            <input
                type="number"
                name="id_contrato"
                value={newContract.id_contrato}
                onChange={handleInputChange}
                placeholder="ID Contrato"
                required
            />
            <input
                type="date"
                name="data_inicial"
                value={newContract.data_inicial}
                onChange={handleInputChange}
                required
            />
            <input
                type="date"
                name="data_final"
                value={newContract.data_final}
                onChange={handleInputChange}
                required
            />
            <input
                type="date"
                name="data_final_atual"
                value={newContract.data_final_atual}
                onChange={handleInputChange}
                required
            />
            <button type="submit">Criar Contrato</button>
        </form>
    );
}

export default ContractForm;
