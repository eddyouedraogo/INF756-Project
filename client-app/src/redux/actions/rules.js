import { createAsyncThunk } from '@reduxjs/toolkit';
import fetchRules from '../../services/rules/rules';

export const fetchData = createAsyncThunk('data/fetchData', async () => {
  return fetchRules();
});
