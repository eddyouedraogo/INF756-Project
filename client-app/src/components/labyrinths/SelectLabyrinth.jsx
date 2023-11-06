import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Select, FormField } from '@cloudscape-design/components';
import { setLabyrinth } from '../../redux/reducers/LabyrinthReducer';
import { fetchLabData } from '../../redux/actions/labyrithns';

export default function SelectLabyrinth() {
  const dispatch = useDispatch();

  const labyrinths = useSelector((state) => state.labyrinth.list);
  const loading = useSelector((state) => state.labyrinth.loading);
  const selectedOption = useSelector((state) => state.labyrinth.selected);

  useEffect(() => {
    if (labyrinths.length === 0) {
      dispatch(fetchLabData());
    }
  }, [dispatch]);

  const transformOption = (labyrinth) => {
    return {
      label: labyrinth.name,
      value: labyrinth.id
    };
  };
  return (
    <FormField label='Sélectionner une labyrinthe'>
      <Select
        selectedOption={selectedOption}
        statusType={loading}
        loadingText='Loading labyrinths'
        onChange={({ detail }) => dispatch(setLabyrinth(detail.selectedOption))}
        options={labyrinths.map(transformOption)}
      />
    </FormField>
  );
}
