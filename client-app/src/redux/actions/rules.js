import { createAsyncThunk } from '@reduxjs/toolkit';
import fetchRules from '../../services/rules/rules';

export const fetchRuleData = createAsyncThunk('data/fetchRuleData', async () => {
  return fetchRules();
});
