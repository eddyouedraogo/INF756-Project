import { createAsyncThunk } from '@reduxjs/toolkit';
import { fetchObjectives } from '../../services/labyrinths/objectives';

export const fetchObjectivesbData = createAsyncThunk('data/fetchObjectivesbData', async () => {
  return fetchObjectives();
});
