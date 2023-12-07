export const fetchObjectives = async () => {
  const response = await fetch(`${process.env.REACT_APP_OBJETS_API_BASE_URL}objective`);
  if (!response.ok) {
    throw new Error('Error');
  }
  await new Promise((r) => {
    setTimeout(r, 500);
  });
  const data = await response.json();
  return data;
};
