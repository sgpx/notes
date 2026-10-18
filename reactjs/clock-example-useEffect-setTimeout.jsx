import { useEffect, useState } from "react";

export default function App() {
  const [time, setTime] = useState(null);

  useEffect(() => {
    setTimeout(() => {
      setTime(new Date().getTime());
    }, 1000);
  }, [time]);

  return (
    <div>
      <div>{time}</div>
      <div>{new Date(time).toString()}</div>
    </div>
  );
}
