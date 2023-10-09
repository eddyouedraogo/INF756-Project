/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';
import { fetchData } from '../actions/rules';

const initialState = {
  list: [],
  selected: [],
  loading: false,
  error: null
};

const mouseSlice = createSlice({
  name: 'rule',
  initialState,
  reducers: {
    setRule: (state, action) => {
      state.selected = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchData.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchData.fulfilled, (state, action) => {
        state.loading = false;
        state.list = action.payload;
        state.error = null;
      })
      .addCase(fetchData.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  }
});

export const { setRule } = mouseSlice.actions;

export default mouseSlice.reducer;
