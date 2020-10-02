
process.env.PWD = process.cwd()

const express = require('express')
const exec = require("child_process").exec;
const path = require('path');
const multer = require('multer');
const app = express()
app.use(express.static(process.env.PWD + '/public'));
const port = 8000
app.listen(port, () => {
    console.log("Service is running")
})


const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, '');
    },
    filename: (req, file, cb) => {
        cb(null, `data.csv`);
    }
});

const upload = multer({
    storage
});

app.get('/', (req, res) => res.sendFile(path.join(__dirname + '/index.html')));

app.post('/fileUpload', upload.single('file'), (req, res) => {
    
    exec("python teamCreateAlgorithm.py", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            res.send("Error, check csv file.")
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
});