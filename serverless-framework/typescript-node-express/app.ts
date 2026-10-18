import express, { Express, Request, Response } from "express";
import cors from "cors";

const app: Express = express();
app.use(cors());

app.get("/", (req: Request, res: Response) => {
  console.log(req.path, req.method);
  res.json({ text: "OK" });
});

app.get("/test", (_: Request, res: Response) => res.send("test OK"));

export default app;