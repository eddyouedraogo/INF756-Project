const fetchRules = async () => {
  const response = await fetch(`${process.env.REACT_APP_SIMULATION_API_BASE_URL}ruleSetItems`);
  if (!response.ok) {
    throw new Error('Error');
  }
  await new Promise((r) => {
    setTimeout(r, 500);
  });
  const data = await response.json();
  return data;
};

export default fetchRules;
