const axios = require("axios");
const fs = require("fs");

fs.readFile("link.txt", "utf-8", function (err, data) {
  if (err) {
    console.error("Error reading the file:", err);
    return;
  }

  const url = data;
  
  getHTMLCode();

  async function getHTMLCode() {
    try {
      const response = await axios.get(url);
      
      // Utilizo el .data para obtener solamente el código html y no el resto de información que contiene el response
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  }
});
