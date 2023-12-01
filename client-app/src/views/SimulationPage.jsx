/* eslint-disable no-prototype-builtins */
/* eslint-disable no-param-reassign */
/* eslint-disable no-continue */
/* eslint-disable no-restricted-syntax */
import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  Grid,
  SpaceBetween,
  Button,
  Box,
  Spinner,
  TextContent
} from '@cloudscape-design/components';
import { Link, useNavigate } from 'react-router-dom';
import CustumLayout from '../layout';
import { fetchRoomData } from '../redux/actions/labyrithns';
import { setSelectedRoomNumber } from '../redux/reducers/LabyrinthReducer';
import Labyrinth from '../components/labyrinths/Labyrinth';

export default function SimulationPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const rooms = useSelector((state) => state.rooms.list);
  const loading = useSelector((state) => state.rooms.loading);
  // const selectedRoomNumber = useSelector((state) => state.labyrinth.selectedRoomNumber);

  useEffect(() => {
    try {
      const size = selectedLabyrinth.label.split('-')[1].trim();
      dispatch(fetchRoomData(size));
      const entranceRoom = rooms.find((room) => room.is_lab_entrance);
      dispatch(setSelectedRoomNumber(entranceRoom.room_number));
    } catch (error) {
      navigate('/');
    }
  }, [dispatch]);

  const updateRoom = () => {
    const randomRoomNumber = Math.floor(Math.random() * (rooms.length - 1 + 1) + 1);
    dispatch(setSelectedRoomNumber(randomRoomNumber));
  };

  return (
    <CustumLayout>
      <SpaceBetween size='xxs'>
        <Grid gridDefinition={[{ colspan: 7 }, { colspan: 5 }]}>
          <div>
            {loading === 'finished' ? (
              <Labyrinth data={rooms} />
            ) : (
              <Box textAlign='center' margin={{ top: 'xxxl' }}>
                <Spinner size='large' />
              </Box>
            )}
          </div>
          <Box textAlign='center' margin={{ top: 'xxxl' }}>
            <div
              style={{
                minHeight: '550px',
                backgroundColor: '#ccc',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                height: '50vh',
                margin: '0'
              }}
            >
              <TextContent>
                <ul style={{ fontSize: '15px' }}>
                  <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                  <li>Nullam convallis orci ac odio dapibus, nec fringilla turpis interdum.</li>
                  <li>
                    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac
                    turpis egestas.
                  </li>
                  <li>Curabitur vel est vel eros ultrices tincidunt at ut purus.</li>
                  <li>Nunc euismod augue et orci varius, at commodo lectus facilisis.</li>
                  <li>Ut eu augue in justo efficitur commodo nec a ligula.</li>
                  <li>Maecenas sed erat sed ligula cursus vehicula.</li>
                  <li>Proin cursus eros eget quam ullamcorper, vel venenatis nisl bibendum.</li>
                  <li>Vivamus congue urna et felis bibendum, vel fermentum mi dapibus.</li>
                  <li>Sed auctor odio id risus sodales efficitur.</li>
                  <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                  <li>Nullam convallis orci ac odio dapibus, nec fringilla turpis interdum.</li>
                  <li>
                    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac
                    turpis egestas.
                  </li>
                </ul>
              </TextContent>
            </div>
          </Box>
        </Grid>
        <Box textAlign='center'>
          <SpaceBetween direction='horizontal' size='xxl'>
            <Button onClick={updateRoom}>Simuler le déplacement </Button>
            <Link to='/'>
              <Button>Quitter</Button>
            </Link>
          </SpaceBetween>
        </Box>
      </SpaceBetween>
    </CustumLayout>
  );
}
