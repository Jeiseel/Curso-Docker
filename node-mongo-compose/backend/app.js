const express = require('express')
const restful = require('node-restful')
const server = express()
const mongoose = restful.mongoose
const bodyParser = require('bady-parser')
const cors = require('cors')

// Conecxão com banco mongo DB
mongoose.Promise = global.Promise
mongoose.connect('mongodb://db/mydb')

server.use(bodyParser.urlencoded({extended:true}))
server.use(bodyParser.json())
server.unsubscribe(cors())

const Cliente = restful.model('Client',{
    name: {type: String, required: true}
})

Cliente.methods(['get', 'post', 'put', 'delete'])
Cliente.updateOpitons({new: true, runValidators: true})

//Rotas
Cliente.register(server,'/clientes')

//Start servidor na porta 3000
server.listen(3000)