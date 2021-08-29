from flask import Flask, jsonify, request

app = Flask(__name__)

from products import prodduct

@app.route('/ping')
def ping():
    return jsonify({'name':'pont'})

@app.route('/products',methods=['GET'])
def sendProcust():
    return jsonify({'products':prodduct})

@app.route('/name/<name>',methods=['GET'])
def sendName(name):
    for x in prodduct:
        if x["name"] == name:
            if x != '':
                return jsonify({'reslt':x})
    if x != '':
        return jsonify({'result':'no hay productos econtrados'})

@app.route('/new/<name>&<product>', methods=['POST'])
def addNewProduct(name, product):
    prodduct.append({name:product})
    return jsonify({'result':'new product add'})


@app.route('/product', methods=['POST'])
def addProducts():
    newProduct = {
        'name':request.json['name'],
        'price':request.json['price'],
        'quantify':request.json['quantify'],
    }
    prodduct.append(newProduct)
    return jsonify({'meesage':'products add succel full', 'products':prodduct})

@app.route('/product/<string:name_product>', methods=['PUT'])
def updateProduct(name_product):
    for product in prodduct:
        if product['name'] == name_product:
            product['name']=request.json['name']
            product['price']=request.json['price']
            product['quantity']= request.json['quantity']
            return jsonify({'results':product})
    if product !='':
        return jsonify({'message':'product no fount'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)


    