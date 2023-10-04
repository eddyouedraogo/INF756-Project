import React from 'react';
import {
  AppLayout,
  ContentLayout,
  Container,
  Header,
  SpaceBetween
} from '@cloudscape-design/components';

export default function CustumLayout({ children }) {
  return (
    <AppLayout
      content={
        <ContentLayout
          header={
            <SpaceBetween size='m'>
              <Header variant='h1' description='Simulateur de vol piloté par lIA '>
                Simulus
              </Header>
            </SpaceBetween>
          }
        >
          <Container
            header={
              <Header variant='h2' description='Configurer la simulation'>
                Etape 1
              </Header>
            }
          >
            {children}
          </Container>
        </ContentLayout>
      }
    />
  );
}
