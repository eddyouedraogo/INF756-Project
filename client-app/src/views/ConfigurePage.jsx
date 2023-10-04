import React from 'react';
import { Grid } from '@cloudscape-design/components';
import SelectLabyrinth from '../components/labyrinths/SelectLabyrinth';
import CustumLayout from '../layout';

export default function ConfigurePage() {
  return (
    <CustumLayout>
      <Grid gridDefinition={[{ colspan: 4 }, { colspan: 4 }, { colspan: 4 }]}>
        <div>
          <SelectLabyrinth />{' '}
        </div>
        <div> </div>
        <div> </div>
      </Grid>
    </CustumLayout>
  );
}
