import React from 'react';
import '../styles/ContractList.css';

function ContractList({ contracts, handleEdit, handleDelete }) {
    return (
        <ul>
            {contracts.map(contract => (
                <li key={contract.id_contrato}>
                    {contract.id_contrato} - {contract.data_inicial} até {contract.data_final} / {contract.data_final_atual}
                    <button onClick={() => handleEdit(contract)}>Editar</button>
                    <button onClick={() => handleDelete(contract.id_contrato)}>Excluir</button>
                </li>
            ))}
        </ul>
    );
}

export default ContractList;
