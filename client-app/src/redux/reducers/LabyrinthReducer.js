/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';
import { fetchLabData } from '../actions/labyrithns';

const initialState = {
  list: [],
  selected: undefined,
  loading: 'loading',
  error: null
};

const labyrinthslice = createSlice({
  name: 'labyrinth',
  initialState,
  reducers: {
    setLabyrinth: (state, action) => {
      state.selected = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchLabData.pending, (state) => {
        state.loading = 'loading';
      })
      .addCase(fetchLabData.fulfilled, (state, action) => {
        state.loading = 'finished';
        state.list = action.payload;
        state.error = null;
      })
      .addCase(fetchLabData.rejected, (state, action) => {
        state.loading = 'finished';
        state.error = action.error.message;
      });
  }
});

export const { setLabyrinth } = labyrinthslice.actions;

export default labyrinthslice.reducer;
