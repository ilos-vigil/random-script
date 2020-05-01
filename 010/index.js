const express = require('express');
const app = express();
const jwt = require('jsonwebtoken');

app.use(express.urlencoded({
    extended: true
}));

app.get('/api/createtoken', async (req, res) => {
    let email = req.query.email;
    let username = req.query.username;

    if (email === undefined || username === undefined){
        res.send({
            status: 400,
            message: 'Tidak ada param query email dan/atau username'
        });
    } else {
        const token = jwt.sign({
            'email': email,
            'username': username
        }, process.env.SECRET_KEY_JWT);
        res.send({
            status: 200,
            token: token
        });
    }
});

app.get('/api/verifytoken', async (req, res) => {
    let token = req.query.token;

    if (!token) {
        res.status(401).send({message: 'Token tidak ditemukan'});
    }else{
        try {
            user = jwt.verify(token, process.env.SECRET_KEY_JWT);
            res.status(401).send({message: 'Token valid!'});
        } catch (err) {
            res.status(401).send({message: 'Token tidak valid!'});
        }
    }
})

app.listen(process.env.PORT, function () {
    console.log(`Listening to port ${process.env.PORT}`);
})