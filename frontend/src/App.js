import React, { useState, useEffect } from 'react';

function App() {
  const [contracts, setContracts] = useState([]);
  const [newContract, setNewContract] = useState({
    id_contrato: '',
    data_inicial: '',
    data_final: '',
    data_final_atual: ''
  });

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

  return (
    <div className="App">
      <h1>Contratos</h1>
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
        <button type="submit">Create Contract</button>
      </form>
      <ul>
        {contracts.map(contract => (
          <li key={contract.id_contrato}>
            {contract.id_contrato} - {contract.data_inicial} to {contract.data_final} - {contract.data_final_atual}
            <button>Editar</button><button>Excluir</button></li>
        ))}
      </ul>
    </div>
  );
}

export default App;
