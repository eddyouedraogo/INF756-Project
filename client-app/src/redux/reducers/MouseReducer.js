/* eslint-disable no-param-reassign */

import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  list: [],
  list_smart: [],
  list_stupid: [],
  selected_smart: [],
  selected_stupid: []
};

const mouseSlice = createSlice({
  name: 'mouse',
  initialState,
  reducers: {
    increment: (state) => {
      const count = state.list.length + 1;
      state.list.push(count);
      state.list_smart.push(count);
      state.list_stupid.push(count);
    },
    decrement: (state) => {
      const count = state.list.length;
      state.list.pop();
      state.list_stupid.splice(count - 1, 1);
      state.selected_stupid.splice(count - 1, 1);
      state.list_smart.splice(count - 1, 1);
      state.selected_smart.splice(count - 1, 1);
    },
    setSmart(state, action) {
      const newSmartItems = action.payload;
      state.selected_smart = newSmartItems;

      // Supprimer les éléments sélectionnés de "list_smart"
      state.list_stupid = state.list.filter((item) => !state.selected_smart.includes(item));
    },
    setStupid(state, action) {
      const newStupidItems = action.payload;
      state.selected_stupid = newStupidItems;
      // Supprimer les éléments sélectionnés de "list_stupid"
      state.list_smart = state.list.filter((item) => !state.selected_stupid.includes(item));
    }
  }
});

export const { increment, decrement, setSmart, setStupid } = mouseSlice.actions;

export default mouseSlice.reducer;
