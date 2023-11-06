import { createAsyncThunk } from '@reduxjs/toolkit';
import fetchLabyrinths from '../../services/labyrinths/labyrinths';

export const fetchLabData = createAsyncThunk('data/fetchLabData', async () => {
  return fetchLabyrinths();
});
