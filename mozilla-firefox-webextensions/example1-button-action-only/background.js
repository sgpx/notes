const mainfunc = async () => {
  const res = await browser.tabs.query({ active: true, currentWindow: true });
  const currentTab = res[0];
  const link = currentTab.url; //window?.location?.href;
  const title = currentTab.title; // document.querySelector("title")?.innerText;

  const body = JSON.stringify({
    title,
    link,
  });

  const headers = { "Content-Type": "application/json" };

  fetch("http://localhost:3000/", {
    method: "POST",
    mode: "cors",
    body,
    headers,
  })
    .then(() => {})
    .catch(() => {});
};

browser.browserAction.onClicked.addListener(mainfunc);
