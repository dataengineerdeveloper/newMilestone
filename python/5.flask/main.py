from flask import Flask,  request

app =  Flask("youtube")

@app.route("/olamundo", methods= ["GET"])
def olamundoi():
    return {"ola": "Mundo"}


@app.route("/cadastro/usuario",methods=["POST"])
def cadastraIsuario():
    
    body = request.get_json()
    
    print(body)
    
    
    return{"id": 0}


app.run()