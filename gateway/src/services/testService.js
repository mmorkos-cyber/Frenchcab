const axios = require("axios");


async function getTests() {

    console.log("URL Python :", process.env.BACKEND_URL);

    try {

        const response = await axios.get(
            `${process.env.BACKEND_URL}/test`
        );

        return response.data;

    } catch (error) {

        console.log(error.message);

        throw new Error(
            "Impossible de contacter l'API Python"
        );

    }

}

module.exports = {getTests};