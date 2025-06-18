const puppeteer = require("puppeteer");
const XLSX = require("xlsx");
const path = require("path");
const fs = require("fs");

(async () => {
  // פתיחת דפדפן
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // נלך לאתר שמראה שערי מטבע (למשל בנק ישראל)
  await page.goto("https://www.boi.org.il/en/Markets/ExchangeRates/");

  // נאתר את שערי המטבע
  const rates = await page.evaluate(() => {
    const getRate = (label) => {
      const cell = Array.from(document.querySelectorAll("td")).find(td => td.textContent.includes(label));
      return cell ? cell.nextElementSibling.textContent.trim() : null;
    };

    return {
      USD: getRate("Dollar"),
      EUR: getRate("Euro"),
      ILS: "1" // קבוע
    };
  });

  await browser.close();

  // קריאה לקובץ האקסל
  const filePath = path.resolve("C:/Users/idanp/OneDrive/שולחן העבודה/automation/practice.xlsx");
  const workbook = XLSX.readFile(filePath);
  const sheet = workbook.Sheets[workbook.SheetNames[0]];

  // כתיבת שערים בתאים ליד כל שורה
  const data = XLSX.utils.sheet_to_json(sheet, { header: 1 });
  data[0].push("USD", "EUR", "ILS"); // הוספת כותרות

  for (let i = 1; i < data.length; i++) {
    data[i].push(rates.USD, rates.EUR, rates.ILS);
  }

  const newSheet = XLSX.utils.aoa_to_sheet(data);
  workbook.Sheets[workbook.SheetNames[0]] = newSheet;

  // שמירה חזרה לקובץ
  XLSX.writeFile(workbook, filePath);
  console.log("✔ שערי מטבעות נוספו לקובץ practice.xlsx בהצלחה!");
})();
