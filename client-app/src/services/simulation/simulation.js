const lauchSimulation = async (data) => {
  const response = await fetch(`${process.env.REACT_APP_SIMULATION_API_BASE_URL}simulation/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  if (!response.ok) {
    throw new Error('Error');
  }
  await new Promise((r) => {
    setTimeout(r, 500);
  });
  const result = await response.json();
  return result;
};

export default lauchSimulation;
