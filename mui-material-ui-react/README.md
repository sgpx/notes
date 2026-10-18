# themeprovider example

```
import { AppBar, createTheme, ThemeProvider } from "@mui/material";

const theme = createTheme({
  palette: {
    primary: { main: "rgba(255,255,255,1)" },
    secondary: { main: "rgba(255,0,0,1)" },
  },
});

const ThemeProviderExample = () => {
  return (
    <ThemeProvider theme={theme}>
      <AppBar color="secondary" style={{}}>
        123
      </AppBar>
    </ThemeProvider>
  );
};

export default ThemeProviderExample;
```

