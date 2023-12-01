import React from 'react';
import Room from './Room'; // Assurez-vous d'importer correctement le composant Room

export default function Row({ rooms, size }) {
  return (
    <div className='labyrinth-row'>
      {rooms.map((room) => (
        <Room key={room.id} room={room} size={size} />
      ))}
    </div>
  );
}
