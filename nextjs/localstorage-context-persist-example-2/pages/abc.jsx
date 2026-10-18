import { Fragment, useContext } from "react";
import { AContext } from "../AProv";

const AbcPage = () => {
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

export default AbcPage;
