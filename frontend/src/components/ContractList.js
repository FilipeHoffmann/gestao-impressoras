import React from 'react';
import '../styles/ContractList.css';

function ContractList({ contracts, handleEdit, handleDelete }) {
    return (
        <ul>
            {contracts.map(contract => (
                <li key={contract.id_contrato}>
                    ID: {contract.id_contrato} - Data Inicial: {contract.data_inicial} até {contract.data_final} / Data Final Atual: {contract.data_final_atual}
                    <button onClick={() => handleEdit(contract)}>Editar</button>
                    <button onClick={() => handleDelete(contract.id_contrato)}>Excluir</button>
                </li>
            ))}
        </ul>
    );
}

export default ContractList;
