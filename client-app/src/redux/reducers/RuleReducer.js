/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';
import { fetchRuleData } from '../actions/rules';

const initialState = {
  list: [],
  selected: [],
  loading: false,
  error: null
};

const ruleSlice = createSlice({
  name: 'rule',
  initialState,
  reducers: {
    setRule: (state, action) => {
      state.selected = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchRuleData.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchRuleData.fulfilled, (state, action) => {
        state.loading = false;
        state.list = action.payload;
        state.error = null;
      })
      .addCase(fetchRuleData.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  }
});

export const { setRule } = ruleSlice.actions;

export default ruleSlice.reducer;
