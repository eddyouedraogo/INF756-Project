import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './reducers/MouseReducer';
import ruleReducer from './reducers/RuleReducer';
import labyrinthReducer from './reducers/LabyrinthReducer';

const store = configureStore({
  reducer: {
    mouse: counterReducer,
    rule: ruleReducer,
    labyrinth: labyrinthReducer
  }
});
export default store;
