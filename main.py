from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
bd = mysql.connector.connect(host='b3bpqfwcyyibc1kljkhx-mysql.services.clever-cloud.com', user='uzza0q27mmzfhmp4', passwd='bJMsTvzHS2yMT6ENcMZo', database='b3bpqfwcyyibc1kljkhx')

cursor = bd.cursor()



@app.route('/agenda/',methods=["GET", "POST"])
def contactos():
    if request.method == "GET":
        contactos = []
        query = "SELECT * FROM contacto"
        cursor.execute(query)

        for contacto in cursor.fetchall():
            d = {
                'id': contacto[0],
                'avatar': contacto[1],
                'nombre': contacto[2],
                'correo': contacto[3],
                'telefono': contacto[4],
                'facebook': contacto[5],
                'instagram': contacto[6],
                'twitter': contacto[7]
            }
            contactos.append(d)
            # print(contacto)
        print(contactos)
        return jsonify(contactos)
    elif request.method == "POST":
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto(avatar, nombre, correo, telefono, facebook, instagram, twitter) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        print(query)
        cursor.execute(query, (data['avatar'],
                               data['nombre'],
                               data['correo'],
                               data['telefono'],
                               data['facebook'],
                               data['instagram'],
                               data['twitter'] ))
        bd.commit()

        if cursor.rowcount:
            return jsonify({'data': 'Ok'})
        else:
            return jsonify({'data': 'Error'})


@app.route('/agenda/<string:id>', methods=['DELETE'])
def delete(id):

    query = 'DELETE FROM contacto WHERE id = {0}'.format(id)

    cursor.execute(query)
    bd.commit()

    if cursor.rowcount:
        return jsonify({'data': 'Ok'})
    else:
        return jsonify({'data': 'Error'})


app.run(debug=True)
