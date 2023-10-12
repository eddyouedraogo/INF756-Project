import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './reducers/MouseReducer';
import ruleReducer from './reducers/RuleReducer';

const store = configureStore({
  reducer: {
    mouse: counterReducer,
    rule: ruleReducer
  }
});
export default store;
