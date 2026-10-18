import React from "react";

export const AContext = React.createContext({
  token: null,
  setToken: () => {},
});

export const AProv = ({ children }) => {
  const [state, setState] = React.useState("555");
  React.useEffect(() => {
    const d = localStorage.getItem("token");
    d ? setState(d) : null;
  }, []);
  const setTokenLocal = (x) => {
    localStorage.setItem("token", x);
    setState(x);
  };
  return (
    <React.Fragment>
      <AContext.Provider value={{ token: state, setToken: setTokenLocal }}>
        {children}
      </AContext.Provider>
    </React.Fragment>
  );
};
