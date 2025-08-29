const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.send("FileChecker Regex API is running 🚀");
});

app.post("/check", (req, res) => {
  const text = req.body.text || "";
  const regex = /^FileChecker_\d+$/;
  res.json({
    input: text,
    matched: regex.test(text)
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
