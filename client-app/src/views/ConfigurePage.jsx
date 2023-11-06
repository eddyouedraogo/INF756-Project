import React, { useState } from 'react';
import { Grid, SpaceBetween, Button, Box, Alert } from '@cloudscape-design/components';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import CustumLayout from '../layout';
import SelectLabyrinth from '../components/labyrinths/SelectLabyrinth';
import RuleSelector from '../components/rules/Selector';
import MouseCouter from '../components/mouses/Counter';
import MouseIntelligenceSelector from '../components/mouses/Selector';

export default function ConfigurePage() {
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState('');
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const selectedStupid = useSelector((state) => state.mouse.selected_stupid);
  const selectedSmart = useSelector((state) => state.mouse.selected_smart);
  const selectedItems = useSelector((state) => state.rule.selected);
  const mouseCounter = useSelector((state) => state.mouse.list);

  const gotoReviewPage = () => {
    setErrorMessage('');

    if (!selectedLabyrinth) {
      setErrorMessage('Veuillez sélectionner une labyrinthe');
      return;
    }

    if (selectedItems.length === 0) {
      setErrorMessage('Veuillez sélectionner une règle pour la simulation');
      return;
    }

    if (mouseCounter.length < 2) {
      setErrorMessage('Veuillez ajouter au moins deux souris');
      return;
    }

    const selectedMouses = selectedSmart.length + selectedStupid.length;

    if (selectedMouses < 2) {
      setErrorMessage("Veuillez choisir l'intelligence pour au moins deux souris");
      return;
    }

    navigate('/review');
  };

  return (
    <CustumLayout title='Etape 1' subtitle='Configurer la simulation'>
      <SpaceBetween size='xxl'>
        {errorMessage !== '' && (
          <Alert statusIconAriaLabel='Error' type='error' header='Error de configuration'>
            {errorMessage}
          </Alert>
        )}
        <Box float='right' textAlign='center'>
          <Button onClick={gotoReviewPage}>Suivant </Button>
        </Box>
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
        <Box float='right' textAlign='center'>
          <Button onClick={gotoReviewPage}>Suivant </Button>
        </Box>
      </SpaceBetween>
    </CustumLayout>
  );
}
