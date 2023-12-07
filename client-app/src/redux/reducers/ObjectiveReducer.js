/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';
import { fetchObjectivesbData } from '../actions/objectives';

const initialState = {
  list: [],
  loading: 'loading',
  error: null
};

const objectiveSlice = createSlice({
  name: 'rooms',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchObjectivesbData.pending, (state) => {
        state.loading = 'loading';
      })
      .addCase(fetchObjectivesbData.fulfilled, (state, action) => {
        state.loading = 'finished';
        state.list = action.payload;
        state.error = null;
      })
      .addCase(fetchObjectivesbData.rejected, (state, action) => {
        state.loading = 'finished';
        state.error = action.error.message;
      });
  }
});

export default objectiveSlice.reducer;
