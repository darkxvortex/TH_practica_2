'use strict';
const express = require('express');
const mongoose = require('mongoose');

const PORT = 8080;
const HOST = '0.0.0.0';
const FLAG = process.env.CHALLENGE_FLAG || "URJC{not_the_real_flag}";

// Configure MongoDB and Mongoose
const MONGO_USER = process.env.MONGO_USER || "root";
const MONGO_PASSWORD = process.env.MONGO_PASSWORD || "password";
const User = mongoose.model('User', new mongoose.Schema({username: String, password: String}));

const initializeDB = async function () {
    await mongoose.connect(`mongodb://mongodb/`, {
        auth: {
            // authSource: "admin",
            username: MONGO_USER,
            password: MONGO_PASSWORD,
        },
        // user: MONGO_USER,
        // pass: MONGO_PASSWORD
    });
    await User.insertMany([
        {username: 'paco', password: 'password1!'},
        {username: 'administradorDeBanes', password: 'URJC{not_this_one}'},
        {username: 'admin', password: FLAG},
        {username: 'fakeadmin', password: 'URJC{nice_try}'},
        {username: 'DoraLaExploradora', password: 'PlataOPlomoSwiper'}
    ]);
}
initializeDB()
    .then(() => console.log("Initialized database"))
    .catch((err) => console.log("Error initializing database", err));

// Configure Express web server
const app = express();
app.use(express.urlencoded({extended: true})); // Allows deserialization of form data

app.get('/', (req, res) => {
    res.send(`
  
  <h1>Unauthorized person detected</h1>
  <h2>Identify yourself, or prepare for the consequences</h2>
   <form action="/login" method="post">
      <div class="container">
        <label for="uname"><b>Username</b></label>
        <input type="text" placeholder="Enter Username" name="username" required>
    
        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" name="password" required>
    
        <button type="submit">Login</button>
        <label>
          <input type="checkbox" checked="checked" name="remember"> Remember me
        </label>
      </div>
    </form> 
  <iframe src="https://giphy.com/embed/9Ft3NkG47dwmA" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>  `);
});

app.get('/health', (req, res) => {
    res.status(200).send('Ok');
});

app.post('/login', async (req, res) => {
    const {username, password} = req.body;

    if (!username || !password) {
        res.status(401).send("<p>Missing form data</p>");
    }
    const user = await User.findOne({username: username, password: password}).exec();
    console.log(`Recv login req with u:'${username}', p:'${password}' --> ${user}`);
    if (!user) {
        res.status(401).send("<iframe src=\"https://giphy.com/embed/xT5LMBOaZw0lRy7V2o\" width=\"480\" height=\"366\" frameBorder=\"0\" class=\"giphy-embed\" allowFullScreen></iframe>");
    } else {
        res.status(200).send("<div class=\"tenor-gif-embed\" data-postid=\"4887893\" data-share-method=\"host\" data-aspect-ratio=\"1.25309\" data-width=\"100%\"></div> <script type=\"text/javascript\" async src=\"https://tenor.com/embed.js\"></script>");
    }
});

app.listen(PORT, HOST, () => {
    console.log(`Running on http://${HOST}:${PORT}`);
});
