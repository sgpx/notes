import { AProv } from "../AProv";

export default function App({ Component, pageProps }) {
  return (
    <AProv>
      <Component {...pageProps} />
    </AProv>
  );
}
