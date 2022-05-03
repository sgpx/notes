import AsyncStorage from "@react-native-async-storage/async-storage";
import persistReducer from "redux-persist/es/persistReducer";

const persistConfig = {
  key: "root",
  storage: AsyncStorage,
};

const rootReducer = (state = {}, action) => {
  console.log(action);
  if (action.type === "change") {
    return { ...state, ...action.payload };
  }
  return state;
};

const persistedReducer = persistReducer(persistConfig, rootReducer);
export default persistedReducer;
