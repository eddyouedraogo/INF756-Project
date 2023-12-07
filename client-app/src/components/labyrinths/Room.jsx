/* eslint-disable no-unused-vars */
/* eslint-disable camelcase */
import React from 'react';
import { useSelector } from 'react-redux';
import { getObjectiveId } from '../../helpers/index';

export default function Room({ room, size }) {
  const { room_number, is_lab_entrance, is_lab_exit, available_exits, objective_id } = room;
  const imageSource = `/objectives/${getObjectiveId(objective_id)}`;
  const mouses = useSelector((state) => state.labyrinth.mouses);
  const objectivesStatus = useSelector((state) => state.labyrinth.objectivesStatus);

  const isObjectiveCompleted = objectivesStatus.some((obj) => obj.room === room_number);

  const roomClassNames = `${size >= 10 ? 'room-small' : 'room'} ${
    is_lab_entrance ? 'no-top-border' : ''
  } ${is_lab_exit ? 'no-bottom-border' : ''} ${
    available_exits.includes(room_number - 1) ? 'no-left-border' : ''
  } ${available_exits.includes(room_number + 1) ? 'no-right-border' : ''} ${
    available_exits.includes(room_number + size) ? 'no-bottom-border' : ''
  } ${available_exits.includes(room_number - size) ? 'no-top-border' : ''}`;
  return (
    <button type='button' className={roomClassNames}>
      {mouses.map(
        (mouse, index) =>
          mouse.room === room_number && (
            <img
              key={Math.random()}
              src={`/rat_${index + 1}.png`}
              alt=''
              style={{ width: '50%', height: '50%' }}
            />
          )
      )}
      {!isObjectiveCompleted && objective_id && (
        <img src={imageSource} alt='' style={{ width: '50%', height: '50%' }} />
      )}
    </button>
  );
}
