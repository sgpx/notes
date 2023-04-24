#!/usr/bin/env node

const nextChar = (x) => String.fromCharCode(x.charCodeAt(0) + 1);
const processData = (ws) => {
  let rowId = "A";
  let columnId = 1;

  while (true) {
    let breakUpper = false;
    for (let rowId = "A"; rowId != "C"; rowId = nextChar(rowId)) {
      const cellId = rowId + columnId;
      const txt = ws.getCell(cellId).value?.toString();
      if (!txt) {
        breakUpper = true;
        break;
      }
      console.log(cellId, txt);
    }
    if (breakUpper) break;
    else columnId += 1;
  }
};

const main = async () => {
  const filename = "i.xlsx";
  const ExcelJS = require("ExcelJS");
  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(filename);
  const worksheetId = Array.from(workbook._worksheets).pop().id;
  const worksheet = workbook.getWorksheet(worksheetId);
  processData(worksheet);
};

main();
