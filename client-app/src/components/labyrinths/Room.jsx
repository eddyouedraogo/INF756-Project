/* eslint-disable camelcase */
import React from 'react';
import { useSelector } from 'react-redux';
import { getObjectiveId } from '../../helpers/index';

export default function Room({ room, size }) {
  const { room_number, is_lab_entrance, is_lab_exit, available_exits, objective_id } = room;
  const imageSource = `/objectives/${getObjectiveId(objective_id)}`;
  const selectedRoomNumber = useSelector((state) => state.labyrinth.selectedRoomNumber);

  const roomClassNames = `${size >= 10 ? 'room-small' : 'room'} ${
    is_lab_entrance ? 'no-top-border' : ''
  } ${is_lab_exit ? 'no-bottom-border' : ''} ${
    available_exits.includes(room_number - 1) ? 'no-left-border' : ''
  } ${available_exits.includes(room_number + 1) ? 'no-right-border' : ''} ${
    available_exits.includes(room_number + size) ? 'no-bottom-border' : ''
  } ${available_exits.includes(room_number - size) ? 'no-top-border' : ''}`;
  return (
    <button type='button' className={roomClassNames}>
      {room_number}
      {objective_id && <img src={imageSource} alt='' style={{ width: '50%', height: '50%' }} />}
      {selectedRoomNumber === room_number && (
        <img src='/rat.png' alt='' style={{ width: '30%', height: '30%' }} />
      )}
    </button>
  );
}
