import Link from "next/link";

const refData = Array(100)
  .fill(0)
  .map((_, n) => ({ id: n, text: `item ${n} :  ${Math.random() * Math.pow(10, 6)}` }));

const HomePage = ({ data, nkey, pkey }) => (
  <>
    {pkey !== null ? <Link href={`?n=${pkey}`}>prev</Link> : null}
    {data.map((x) => (
      <div key={x.id}>
        {x.id} - {x.text}
      </div>
    ))}
    {nkey !== null ? <Link href={`?n=${nkey}`}>next</Link> : null}
  </>
);

export default HomePage;

export async function getServerSideProps(ctx) {
  const a = ctx?.query?.n;
  const i = a ? parseInt(a) : 0;
  const pkey = i > 0 ? i - 10 : null;
  const nkey = i < refData.length - 10 ? i + 10 : null;
  console.log(i, i + 10);
  const dataSlice = refData.slice(i, i + 10);
  return { props: { data: dataSlice, nkey, pkey } };
}
