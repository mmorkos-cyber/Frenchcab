const testService = require("../services/testService.js");

async function getTest(req,res){

    console.log("Récupération des centrales");

    try{

        const plants = await testService.getTests();

        console.log("test récupérée");

        res.json({
            success:true,
            data:plants
        });


    }catch(error){

        console.error("Erreur test :", error.message);

        res.status(500).json({
            success:false,
            message:"Impossible de récupérer le test",
            status:500
        });

    }
}

module.exports = {getTest};