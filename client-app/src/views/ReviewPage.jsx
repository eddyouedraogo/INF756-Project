import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
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
import ObjectiveList from '../components/objectives/List';
import { fetchLabyrinthBySize } from '../services/labyrinths/labyrinths';
import { setMousesInit } from '../redux/reducers/LabyrinthReducer';

export default function ReviewPage() {
  const dispatch = useDispatch();
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const selectedStupid = useSelector((state) => state.mouse.selected_stupid);
  const selectedSmart = useSelector((state) => state.mouse.selected_smart);
  const selectedRuleItems = useSelector((state) => state.rule.selected);

  useEffect(() => {
    const fetchDataAndInitializeMouseStatus = async () => {
      const size = selectedLabyrinth.label.split('-')[1].trim();
      const rooms = await fetchLabyrinthBySize(size);
      // Now you can access the updated state
      const labEntranceRoom = rooms.find((room) => room.is_lab_entrance);
      const totalMouse = selectedSmart.length + selectedStupid.length;
      const mouseStatusNew = Array.from({ length: totalMouse }, (_, index) => ({
        id: index + 1,
        room: labEntranceRoom.room_number
      }));

      dispatch(setMousesInit(mouseStatusNew));
    };

    fetchDataAndInitializeMouseStatus();
  }, []);

  return (
    <CustumLayout title='Etape 2' subtitle='Résumé de vos sélections'>
      <SpaceBetween size='xxl'>
        <Box float='right' textAlign='center'>
          <SpaceBetween direction='horizontal' size='xxl'>
            <Link to='/configure'>
              <Button>Retour </Button>
            </Link>
            <Link to='/simulation' variant='primary'>
              <Button variant='primary'> Lancer la simulation </Button>
            </Link>
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
