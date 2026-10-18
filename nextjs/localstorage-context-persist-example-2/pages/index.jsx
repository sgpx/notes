import { Fragment, useContext } from "react";
import { AContext } from "../AProv";

const IndexPage = () => {
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

export default IndexPage;
