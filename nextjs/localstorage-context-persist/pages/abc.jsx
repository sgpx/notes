import { Fragment, useContext } from "react";
import { AProv, AContext } from "../AProv";

const ActualPage = () => {
  const acval = useContext(AContext);

  return (
    <Fragment>
      <div>abc</div>
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

const AbcPage = () => {
  return (
    <AProv>
      <ActualPage />
    </AProv>
  );
};

export default AbcPage;
