import React, { useState, useEffect } from 'react';
import '../styles/EditContractModal.css';

function EditContractModal({ contract, show, onClose, onSave }) {
    const [updatedContract, setUpdatedContract] = useState({ ...contract });

    useEffect(() => {
        setUpdatedContract({ ...contract });
    }, [contract]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUpdatedContract({ ...updatedContract, [name]: value });
    };

    const handleSave = () => {
        onSave(updatedContract);
    };

    if (!show) {
        return null;
    }

    return (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>Editar Contrato</h2>
                <form>
                    <input
                        type="number"
                        name="id_contrato"
                        value={updatedContract.id_contrato}
                        onChange={handleInputChange}
                        placeholder="ID Contrato"
                        disabled
                    />
                    <input
                        type="date"
                        name="data_inicial"
                        value={updatedContract.data_inicial}
                        onChange={handleInputChange}
                        required
                    />
                    <input
                        type="date"
                        name="data_final"
                        value={updatedContract.data_final}
                        onChange={handleInputChange}
                        required
                    />
                    <input
                        type="date"
                        name="data_final_atual"
                        value={updatedContract.data_final_atual}
                        onChange={handleInputChange}
                        required
                    />
                    <button type="button" onClick={handleSave}>Save</button>
                </form>
            </div>
        </div>
    );
}

export default EditContractModal;
