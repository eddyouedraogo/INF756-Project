export const fetchObjectives = async () => {
  const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}v1/objectives`);
  if (!response.ok) {
    throw new Error('Error');
  }
  await new Promise((r) => {
    setTimeout(r, 2000);
  });
  const data = await response.json();
  return data;
};
