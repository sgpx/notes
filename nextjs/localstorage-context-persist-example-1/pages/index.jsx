import { Fragment, useContext } from "react";
import { AProv, AContext } from "../AProv";

const ActualPage = () => {
  const acval = useContext(AContext);

  return (
    <Fragment>
      <button
        onClick={() => {
          console.log(acval);
          acval.setToken("123");
        }}
      >
        set
      </button>
      <div>acval : {acval?.token || "nothing"}</div>
    </Fragment>
  );
};

const IndexPage = () => {
  return (
    <AProv>
      <ActualPage />
    </AProv>
  );
};

export default IndexPage;
