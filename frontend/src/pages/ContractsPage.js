import React, { useState, useEffect } from 'react';
import ContractList from '../components/ContractList';
import ContractForm from '../components/ContractForm';
import EditContractModal from '../components/EditContractModal';
import '../styles/App.css';

function ContractsPage() {
    const [contracts, setContracts] = useState([]);
    const [newContract, setNewContract] = useState({
        id_contrato: '',
        data_inicial: '',
        data_final: '',
        data_final_atual: ''
    });
    const [editModalOpen, setEditModalOpen] = useState(false);
    const [currentContract, setCurrentContract] = useState(null);

    useEffect(() => {
        fetchContracts();
    }, []);

    const fetchContracts = async () => {
        try {
            const response = await fetch('http://192.168.0.159:5000/contratos');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            console.log('Fetched Contracts:', data);
            setContracts(data);
        } catch (error) {
            console.error('Error fetching contracts:', error);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewContract({ ...newContract, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://192.168.0.159:5000/contratos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newContract),
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const createdContract = await response.json();
            setContracts([...contracts, createdContract]);
            setNewContract({
                id_contrato: '',
                data_inicial: '',
                data_final: '',
                data_final_atual: ''
            });
        } catch (error) {
            console.error('Error creating contract:', error);
        }
    };

    const handleEdit = (contract) => {
        setCurrentContract(contract);
        setEditModalOpen(true);
    };

    const handleSave = async (updatedContract) => {
        try {
            const response = await fetch(`http://192.168.0.159:5000/contratos/${updatedContract.id_contrato}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedContract),
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const updatedContracts = contracts.map(contract =>
                contract.id_contrato === updatedContract.id_contrato ? updatedContract : contract
            );
            setContracts(updatedContracts);
            setEditModalOpen(false);
        } catch (error) {
            console.error('Error updating contract:', error);
        }
    };

    const handleDelete = async (id) => {
        try {
            const response = await fetch(`http://192.168.0.159:5000/contratos/${id}`, {
                method: 'DELETE',
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const updatedContracts = contracts.filter(contract => contract.id_contrato !== id);
            setContracts(updatedContracts);
        } catch (error) {
            console.error('Error deleting contract:', error);
        }
    };

    return (
        <div>
            <h1>Contratos</h1>
            <ContractForm
                newContract={newContract}
                handleInputChange={handleInputChange}
                handleSubmit={handleSubmit}
            />
            <ContractList
                contracts={contracts}
                handleEdit={handleEdit}
                handleDelete={handleDelete}
            />
            {editModalOpen && (
                <EditContractModal
                    contract={currentContract}
                    show={editModalOpen}
                    onClose={() => setEditModalOpen(false)}
                    onSave={handleSave}
                />
            )}
        </div>
    );
}

export default ContractsPage;
