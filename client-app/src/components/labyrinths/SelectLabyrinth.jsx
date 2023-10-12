import React from 'react';
import { Select, FormField } from '@cloudscape-design/components';
import useFetchLabyrinth from '../../hooks/labyrinths/useLabyrinths';

export default function SelectLabyrinth() {
  const [selectedOption, setSelectedOption] = React.useState({});

  const { data, loading } = useFetchLabyrinth();

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
        onChange={({ detail }) => setSelectedOption(detail.selectedOption)}
        options={data.map(transformOption)}
      />
    </FormField>
  );
}
