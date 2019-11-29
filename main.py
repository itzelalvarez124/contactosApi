from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
bd = mysql.connector.connect(host='localhost', user='itzel', passwd='itzel124', database='contactos')

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
    else:
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto(avatar, nombre, correo, telefono, facebook, instagram, twitter) VALUES(%s, %s, %s, %s, %s, %s, %s) "
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

@app.route('/agenda/:id',methods=["DELETE","PUT"])
def contactos1():
    if request.method == "DELETE":
        cur = mysql.connector.cursor()
        cur.execute('DELETE FROM contacto WHERE id = {0}'.format(id))
        bd.commit();
app.run(debug=True)
