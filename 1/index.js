const fs = require('fs');
const cheerio = require('cheerio');

// Read the HTML file
const html = fs.readFileSync('index.html', 'utf8');

// Load HTML content into Cheerio
const $ = cheerio.load(html);

// Extract capitals and states
const capitals = [];
$('div#main ul li').each((index, element) => {
    const capital = $(element).find('.capital').text().trim();
    const state = $(element).find('.state').text().trim();
    capitals.push({ capital, state });
});

// Prepare the result object
const result = {
    capitals,
    summary: {
        numberOfCapitals: capitals.length
    }
};

// Convert to JSON and save to a file
const jsonResult = JSON.stringify(result, null, 2);
fs.writeFileSync('output.json', jsonResult);

console.log('JSON file generated successfully.');