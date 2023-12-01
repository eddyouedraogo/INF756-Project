const lauchSimulation = async (data) => {
  const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}v1/simulation`, {
    // const response = await fetch(`http://localhost:8080/simulation/`, {
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
    setTimeout(r, 2000);
  });
  const result = await response.json();
  return result;
};

export default lauchSimulation;
