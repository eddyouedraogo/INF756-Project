import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Multiselect, FormField } from '@cloudscape-design/components';
import { setStupid } from '../../redux/reducers/MouseReducer';

export default function LowIntelligenceSelector() {
  const mouses = useSelector((state) => state.mouse.list_stupid);
  const selectedOptions = useSelector((state) => state.mouse.selected_stupid);
  const dispatch = useDispatch();

  const select = (detail) => {
    const selectedItems = detail.selectedOptions.map((item) => item.value);
    dispatch(setStupid(selectedItems));
  };

  const transformOption = (mouse) => {
    return {
      label: `souris ${mouse}`,
      value: mouse
    };
  };

  return (
    <FormField label='Intelligence 2'>
      <Multiselect
        selectedOptions={selectedOptions.map(transformOption)}
        onChange={({ detail }) => select(detail)}
        options={mouses.map(transformOption)}
        placeholder='Choisir les souris'
      />
    </FormField>
  );
}
