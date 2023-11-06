import React from 'react';
import { Grid, SpaceBetween, Button, Box } from '@cloudscape-design/components';
import { Link } from 'react-router-dom';
import CustumLayout from '../layout';

export default function SimulationPage() {
  return (
    <CustumLayout>
      <SpaceBetween size='xxl'>
        <Grid gridDefinition={[{ colspan: 7 }, { colspan: 5 }]}>
          <div>Simulation en cours</div>
          <div>Etat de la simulation</div>
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
