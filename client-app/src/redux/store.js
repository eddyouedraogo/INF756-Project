import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './reducers/MouseReducer';

const store = configureStore({
  reducer: {
    mouse: counterReducer
  }
});
export default store;
