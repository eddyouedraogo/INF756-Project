import React from 'react';
import { useSelector } from 'react-redux';
import {
  Grid,
  SpaceBetween,
  Button,
  Box,
  FormField,
  Badge,
  Cards
} from '@cloudscape-design/components';
import { Link } from 'react-router-dom';
import CustumLayout from '../layout';
import ItemDescription from '../components/rules/ItemDescription';

export default function ReviewPage() {
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const selectedStupid = useSelector((state) => state.mouse.selected_stupid);
  const selectedSmart = useSelector((state) => state.mouse.selected_smart);
  const selectedItems = useSelector((state) => state.rule.selected);

  return (
    <CustumLayout title='Etape 2' subtitle='Résumé de vos sélections'>
      <SpaceBetween size='xxl'>
        <Box float='left' textAlign='center'>
          <Link to='/configure'>
            <Button>Retour </Button>
          </Link>
        </Box>
        <Grid gridDefinition={[{ colspan: 4 }, { colspan: 5 }]}>
          <div>
            <SpaceBetween size='xxl'>
              <FormField label='Labyrinthe'>
                <Box margin={{ top: 'x' }}>
                  <Badge>{selectedLabyrinth?.label}</Badge>
                </Box>
              </FormField>
              <FormField label='Nombre de souris'>
                <Badge>{selectedSmart.length + selectedStupid.length}</Badge>
              </FormField>
              <SpaceBetween size='xxl'>
                <FormField label='Intelligence maximale'>
                  <SpaceBetween direction='horizontal' size='xxs'>
                    {selectedSmart.map((item) => (
                      <Button key={item}>souris {item}</Button>
                    ))}
                  </SpaceBetween>
                </FormField>
                <FormField label='Intelligence normale'>
                  <SpaceBetween direction='horizontal' size='xxs'>
                    {selectedStupid.map((item) => (
                      <Button key={item}>souris {item}</Button>
                    ))}
                  </SpaceBetween>
                </FormField>
              </SpaceBetween>
            </SpaceBetween>
          </div>
          <FormField label='les règles à appliquer'>
            <Box margin={{ vertical: 'xl' }}>
              <Cards
                selectionType='single'
                trackBy='id'
                visibleSections={['name', 'description']}
                selectedItems={selectedItems}
                cardDefinition={{
                  header: null,
                  sections: [
                    {
                      id: 'id',
                      header: 'id',
                      content: (item) => item.id
                    },
                    {
                      id: 'name',
                      header: '',
                      // eslint-disable-next-line react/no-unstable-nested-components
                      content: (item) => <Badge color='blue'> {item.name}</Badge>
                    },
                    {
                      id: 'description',
                      header: '',
                      // eslint-disable-next-line react/no-unstable-nested-components
                      content: (item) => <ItemDescription description={item.description} />
                    }
                  ]
                }}
                cardsPerRow={[{ cards: 1 }, { minWidth: 500, cards: 2 }]}
                items={selectedItems}
              />
            </Box>
          </FormField>
        </Grid>
        <Box textAlign='center'>
          <Link to='/simulation'>
            <Button>Lancer la simulation </Button>
          </Link>
        </Box>
      </SpaceBetween>
    </CustumLayout>
  );
}
