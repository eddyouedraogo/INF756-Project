import React from 'react';
import {
  AppLayout,
  ContentLayout,
  Container,
  Header,
  SpaceBetween
} from '@cloudscape-design/components';

export default function CustumLayout({ children, title, subtitle }) {
  return (
    <AppLayout
      navigationHide
      toolsHide
      content={
        <ContentLayout
          header={
            <SpaceBetween size='m'>
              <Header variant='h1' description='Simulateur de vol piloté par IA '>
                Simulus
              </Header>
            </SpaceBetween>
          }
        >
          <Container
            header={
              <Header variant='h2' description={subtitle}>
                {title}
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
