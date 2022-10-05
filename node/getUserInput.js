process.stdout.write("hello. what is your name? ")

process.stdin.on('data', (data) => {
    console.log("hello " + data.toString())
    process.exit()
});

process.on('exit', () => [
    console.log('thanks for the info!')
]);

