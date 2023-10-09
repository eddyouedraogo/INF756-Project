import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Multiselect, FormField } from '@cloudscape-design/components';
import { setSmart } from '../../redux/reducers/MouseReducer';

export default function MaxIntelligenceSelector() {
  const mouses = useSelector((state) => state.mouse.list_smart);
  const selectedOptions = useSelector((state) => state.mouse.selected_smart);
  const dispatch = useDispatch();

  const select = (detail) => {
    const selectedItems = detail.selectedOptions.map((item) => item.value);
    dispatch(setSmart(selectedItems));
  };

  const transformOption = (mouse) => {
    return {
      label: `souris ${mouse}`,
      value: mouse
    };
  };

  return (
    <FormField label='Intelligence maximale'>
      <Multiselect
        selectedOptions={selectedOptions.map(transformOption)}
        onChange={({ detail }) => select(detail)}
        options={mouses.map(transformOption)}
        placeholder='Choisir les souris'
      />
    </FormField>
  );
}
