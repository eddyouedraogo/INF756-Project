import * as React from 'react';
import { SpaceBetween } from '@cloudscape-design/components';
import MaxIntelligenceSelector from './MaxIntelligenceSelector';
import LowIntelligenceSelector from './LowIntelligenceSelector';

export default function Selector() {
  return (
    <SpaceBetween size='xxl'>
      <MaxIntelligenceSelector />
      <LowIntelligenceSelector />
    </SpaceBetween>
  );
}
