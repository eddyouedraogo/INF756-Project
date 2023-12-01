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
import { Link, useNavigate } from 'react-router-dom';
import CustumLayout from '../layout';
import ItemDescription from '../components/rules/ItemDescription';
import ObjectiveList from '../components/objectives/List';
// import lauchSimulation from '../services/simulation/simulation';

export default function ReviewPage() {
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const selectedStupid = useSelector((state) => state.mouse.selected_stupid);
  const selectedSmart = useSelector((state) => state.mouse.selected_smart);
  const selectedRuleItems = useSelector((state) => state.rule.selected);
  const navigate = useNavigate();

  const startSimulation = async () => {
    // const data = {
    //   mouses_intelligence: [
    //     { intelligence_id: 1, number_of_mouses: selectedSmart.length },
    //     { intelligence_id: 3, number_of_mouses: selectedStupid.length }
    //   ],
    //   labyrinth_id: selectedLabyrinth?.value,
    //   ruleSet_id: selectedRuleItems[0].id
    // };

    try {
      //  await lauchSimulation(data);
      navigate('/simulation');
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <CustumLayout title='Etape 2' subtitle='Résumé de vos sélections'>
      <SpaceBetween size='xxl'>
        <Box float='right' textAlign='center'>
          <SpaceBetween direction='horizontal' size='xxl'>
            <Link to='/configure'>
              <Button>Retour </Button>
            </Link>
            <Button onClick={startSimulation} variant='primary'>
              Lancer la simulation{' '}
            </Button>
          </SpaceBetween>
        </Box>
        <Grid gridDefinition={[{ colspan: 3 }, { colspan: 4 }, { colspan: 4 }]}>
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
            <Box margin={{ vertical: 'xl', right: 'xl' }}>
              <Cards
                selectionType='single'
                trackBy='id'
                visibleSections={['name', 'description']}
                selectedItems={selectedRuleItems}
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
                items={selectedRuleItems}
              />
            </Box>
          </FormField>
          <Box margin={{ left: 'xxl' }}>
            <h2> Les objectifs</h2>
            <ObjectiveList />
          </Box>
        </Grid>
      </SpaceBetween>
    </CustumLayout>
  );
}
