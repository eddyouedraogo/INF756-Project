import { createAsyncThunk } from '@reduxjs/toolkit';
import { fetchLabyrinths, fetchLabyrinthBySize } from '../../services/labyrinths/labyrinths';

export const fetchLabData = createAsyncThunk('data/fetchLabData', async () => {
  return fetchLabyrinths();
});

export const fetchRoomData = createAsyncThunk('data/fetchRoomData', async (size) => {
  return fetchLabyrinthBySize(size);
});
