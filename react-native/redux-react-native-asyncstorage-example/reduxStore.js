import { configureStore } from "@reduxjs/toolkit";
import persistStore from "redux-persist/es/persistStore";
import persistedReducer from "./persistedReducer";
import { createStore } from "redux";
// const store = configureStore({ reducer: persistedReducer });
export const store = createStore(persistedReducer);
export const persistor = persistStore(store);