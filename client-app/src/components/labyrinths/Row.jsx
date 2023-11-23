import React from 'react';
import Room from './Room'; // Assurez-vous d'importer correctement le composant Room

export default function Row({ rooms, size }) {
  return (
    <div className='labyrinth-row'>
      {rooms.map((room) => (
        <Room
          key={room.id}
          roomNumber={room.room_number}
          isLabEntrance={room.is_lab_entrance}
          isLabExit={room.is_lab_exit}
          availableExits={room.available_exits}
          size={size}
        />
      ))}
    </div>
  );
}
