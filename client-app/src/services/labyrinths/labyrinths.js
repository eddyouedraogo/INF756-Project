export const fetchLabyrinths = async () => {
  const response = await fetch(`${process.env.REACT_APP_OBJETS_API_BASE_URL}labyrinth`);
  if (!response.ok) {
    throw new Error('Error');
  }
  await new Promise((r) => {
    setTimeout(r, 500);
  });
  const data = await response.json();
  return data;
};

export const fetchLabyrinthBySize = async (size) => {
  const response = await fetch(
    `${process.env.REACT_APP_OBJETS_API_BASE_URL}labyrinth?labyrinth_size=${size}`
  );
  if (!response.ok) {
    throw new Error('Error');
  }
  await new Promise((r) => {
    setTimeout(r, 500);
  });
  const data = await response.json();
  return data;
};
