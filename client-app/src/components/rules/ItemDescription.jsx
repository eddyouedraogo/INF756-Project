import React from 'react';
import { Box } from '@cloudscape-design/components';

export default function ItemDescription({ description }) {
  return (
    <Box margin={{ vertical: 'xs' }}>
      <div className='card-section-description' dangerouslySetInnerHTML={{ __html: description }} />
    </Box>
  );
}
