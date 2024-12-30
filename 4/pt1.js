const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
});

rl.on('line', (line) => {
    console.log(line);
});

rl.on('close', (input) => {
    console.log(end, input);
});