/* eslint-disable camelcase */
/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';
import { fetchLabData } from '../actions/labyrithns';

const initialState = {
  list: [],
  selected: undefined,
  loading: 'loading',
  mouses: [],
  error: null
};

const labyrinthslice = createSlice({
  name: 'labyrinth',
  initialState,
  reducers: {
    setLabyrinth: (state, action) => {
      state.selected = action.payload;
    },
    setMousesInit: (state, action) => {
      state.mouses = action.payload;
    },
    setMouses: (state, action) => {
      const { id, current_room } = action.payload;
      const existingMouseIndex = state.mouses.findIndex((mouse) => mouse.id === id);
      state.mouses[existingMouseIndex].room = current_room;
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

export const { setLabyrinth, setMousesInit, setMouses } = labyrinthslice.actions;

export default labyrinthslice.reducer;
