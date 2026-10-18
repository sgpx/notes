interface indexProp {
  posts: Array<number>;
  title: String;
  content: String;
}

export default function Home(props: indexProp) {
  return (
    <div>
      home
      {props.posts.map((x) => (
        <div key={x}>{x}</div>
      ))}
    </div>
  );
}

export async function getStaticProps() {
  const res = await fetch("http://localhost:3002/");
  const d = await res.json(); // [1,2,3,4];
  return { props: { posts: d.posts } };
}
