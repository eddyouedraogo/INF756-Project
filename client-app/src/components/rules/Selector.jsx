import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Cards, FormField, Box, SpaceBetween, Badge } from '@cloudscape-design/components';
import ItemDescription from './ItemDescription';
import { setRule } from '../../redux/reducers/RuleReducer';
import { fetchData } from '../../redux/actions/rules';

export default function Selector() {
  const rules = useSelector((state) => state.rule.list);
  const loading = useSelector((state) => state.rule.loading);
  const selectedItems = useSelector((state) => state.rule.selected);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchData());
  }, [dispatch]);

  const transformData = (rule) => {
    const { id, name, items } = rule;
    return {
      id,
      name,
      description: `<ul>${items.map((item) => `<li>${item.name}</li>`).join('')}</ul>`
    };
  };

  return (
    <FormField label='Sélectionner les règles à appliquer'>
      <Box margin={{ vertical: 'xl' }}>
        <Cards
          loadingText='Loading rules'
          loading={loading}
          selectionType='single'
          trackBy='id'
          visibleSections={['name', 'description']}
          onSelectionChange={({ detail }) => dispatch(setRule(detail.selectedItems))}
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
          items={rules.map(transformData)}
          empty={
            <Box margin={{ vertical: 'xs' }} textAlign='center' color='inherit'>
              <SpaceBetween size='m'>
                <b>Aucune règle trouvée</b>
              </SpaceBetween>
            </Box>
          }
        />
      </Box>
    </FormField>
  );
}
