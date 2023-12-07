import React from 'react';
import '../../styles/index.css';
import Row from './Row';

export default function Labyrinth({ data }) {
  const sortedLabyrinthe = [...data].sort((a, b) => a.room_number - b.room_number);

  const elementsPerRow = Math.ceil(Math.sqrt(sortedLabyrinthe.length));

  const rooms = [];

  for (let i = 0; i < sortedLabyrinthe.length; i += elementsPerRow) {
    rooms.push({ id: i, rooms: sortedLabyrinthe.slice(i, i + elementsPerRow) });
  }

  return (
    <div className='labyrinth'>
      <div className=''>
        {rooms.map((row) => (
          <Row key={row.id} rooms={row.rooms} size={elementsPerRow} />
        ))}
      </div>
    </div>
  );
}
