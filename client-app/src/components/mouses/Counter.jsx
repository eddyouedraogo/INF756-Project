import { Button, SpaceBetween, FormField, Badge, Box } from '@cloudscape-design/components';
import { useDispatch, useSelector } from 'react-redux';
import { increment, decrement } from '../../redux/reducers/MouseReducer';

export default function Counter() {
  const dispatch = useDispatch();
  const mouses = useSelector((state) => state.mouse.list);

  return (
    <Box margin={{ left: 'xxxl' }}>
      <FormField label='Nombre de souris'>
        <SpaceBetween direction='horizontal' size='xxl' alignItems='center'>
          <Button iconName='add-plus' onClick={() => dispatch(increment())} />
          <Box margin={{ top: 'xxs' }}>
            <Badge>{mouses.length}</Badge>
          </Box>
          <Button iconName='status-stopped' onClick={() => dispatch(decrement())} />
        </SpaceBetween>
      </FormField>
    </Box>
  );
}
