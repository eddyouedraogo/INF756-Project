import React from 'react';

export default function Room({ roomNumber, isLabEntrance, isLabExit, availableExits, size }) {
  const roomClassNames = `${size >= 10 ? 'room-small' : 'room'} ${
    isLabEntrance ? 'no-top-border' : ''
  } ${isLabExit ? 'no-bottom-border' : ''} ${
    availableExits.includes(roomNumber - 1) ? 'no-left-border' : ''
  } ${availableExits.includes(roomNumber + 1) ? 'no-right-border' : ''} ${
    availableExits.includes(roomNumber + size) ? 'no-bottom-border' : ''
  } ${availableExits.includes(roomNumber - size) ? 'no-top-border' : ''}`;
  return (
    <button type='button' className={roomClassNames}>
      {roomNumber}
    </button>
  );
}
