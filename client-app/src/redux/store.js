import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './reducers/MouseReducer';
import ruleReducer from './reducers/RuleReducer';
import labyrinthReducer from './reducers/LabyrinthReducer';
import roomReducer from './reducers/RoomReducer';

const store = configureStore({
  reducer: {
    mouse: counterReducer,
    rule: ruleReducer,
    labyrinth: labyrinthReducer,
    rooms: roomReducer
  }
});
export default store;
