const express = require("express");

const router = express.Router();
const testControllers = require("../controllers/testControllers");



router.get("/", testControllers.getPlants);


module.exports = router;