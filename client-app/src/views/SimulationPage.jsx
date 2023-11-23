import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Grid, SpaceBetween, Button, Box, Spinner } from '@cloudscape-design/components';
import { Link } from 'react-router-dom';
import CustumLayout from '../layout';
import { fetchRoomData } from '../redux/actions/labyrithns';
import Labyrinth from '../components/labyrinths/Labyrinth';

export default function SimulationPage() {
  const dispatch = useDispatch();
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const rooms = useSelector((state) => state.rooms.list);
  const loading = useSelector((state) => state.rooms.loading);

  useEffect(() => {
    try {
      const size = selectedLabyrinth.label.split('-')[1].trim();
      dispatch(fetchRoomData(size));
    } catch (error) {
      console.log(error);
    }
  }, [dispatch]);

  return (
    <CustumLayout>
      <SpaceBetween size='xxs'>
        <Grid gridDefinition={[{ colspan: 8 }, { colspan: 4 }]}>
          <div>
            {loading === 'finished' ? (
              <Labyrinth data={rooms} />
            ) : (
              <Box textAlign='center' margin={{ top: 'xxxl' }}>
                <Spinner size='large' />
              </Box>
            )}
          </div>
          <div> {}</div>
        </Grid>
        <Box textAlign='center'>
          <Link to='/'>
            <Button>Quitter</Button>
          </Link>
        </Box>
      </SpaceBetween>
    </CustumLayout>
  );
}
