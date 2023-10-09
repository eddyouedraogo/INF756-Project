import React from 'react';
import { Grid, SpaceBetween } from '@cloudscape-design/components';
import CustumLayout from '../layout';
import SelectLabyrinth from '../components/labyrinths/SelectLabyrinth';
import RuleSelector from '../components/rules/Selector';
import MouseCouter from '../components/mouses/Counter';
import MouseIntelligenceSelector from '../components/mouses/Selector';

export default function ConfigurePage() {
  return (
    <CustumLayout>
      <Grid gridDefinition={[{ colspan: 5 }, { colspan: 2 }, { colspan: 5 }]}>
        <div>
          <SpaceBetween size='xxl'>
            <SelectLabyrinth />
            <RuleSelector />
          </SpaceBetween>
        </div>
        <div>
          <MouseCouter />{' '}
        </div>
        <div>
          <MouseIntelligenceSelector />
        </div>
      </Grid>
    </CustumLayout>
  );
}
