// Import the required libraries

// Create a new PostgreSQL client

// Connect to the PostgreSQL database
console.log(">>>>123");
setInterval(() => {
const { Client } = require('pg');

const client = new Client({
  user: 'd2user',
  password: 'd2pwd',
  database: 'd2db',
  host: 'db',
  port: 5432,
});

client.connect()
  .then(() => {
    console.log('Connected to the database');

    // Example query
    return client.query('SELECT NOW()');
  })
  .then(result => {
    console.log('Current date and time from the database:', result.rows[0].now);
  })
  .catch(error => {
  })
  .finally(() => {
    // Close the client
    client.end();
  });
}, 5000);
