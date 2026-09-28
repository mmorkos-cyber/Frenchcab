const express = require("express");

const router = express.Router();
const testControllers = require("../controllers/testController");



router.get("/", testControllers.getTest);


module.exports = router;