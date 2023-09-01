import psycopg2
from datetime import datetime

conn = psycopg2.connect(host='172.18.0.3', dbname='postgres', user='root', password='root', port=5432)


cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS vehiculos')
cur.execute('DROP TABLE IF EXISTS registro')

cur.execute('''CREATE TABLE IF NOT EXISTS vehiculos (
                    Placa INT PRIMARY KEY,
                    Modelo VARCHAR(50) NOT NULL,
                    Color VARCHAR(50) NOT NULL,
                    Nombre VARCHAR(50) NOT NULL,
                    Apellido VARCHAR(50) NOT NULL,
                    Hora VARCHAR(50) NOT NULL)''')

cur.execute('''CREATE TABLE IF NOT EXISTS registro (
                    Placa INT,
                    Modelo VARCHAR(50) NOT NULL,
                    Estado VARCHAR(50) NOT NULL,
                    Hora VARCHAR(50) NOT NULL)''')

insert_values = [
    (2, 'Ford Mustang', 'Azul', 'Carlos', 'Sanchez', '10:00:00'),
    (4, 'BMW Serie 3', 'Blanco', 'Reyshawn', 'Lawrence', '11:00:00'),
    (5, 'Mercedes-Benz Clase E', 'Rojo', 'Marco', 'Lopez', '12:00:00')
]

cur.executemany('''INSERT INTO vehiculos (Placa, Modelo, Color, Nombre, Apellido, Hora)
                VALUES (%s, %s, %s, %s, %s, %s)''', insert_values)


conn.commit()

print("------REGISTRO DE AUTOS------")
cur.execute('SELECT * FROM vehiculos')
for record in cur.fetchall():
    print(record)
    
print("hola mundo")

def Actualizar_Registro():
    while True:
        Opcion = int(input('''Que desea hacer?: 
                        
                        1. Registrar entrada
                        2. Registrar salida
                        3. Historial
                        4. Salir
                        '''))
        if Opcion == 1:
            Estado = "Entrada"
            Placa = int(input('Ingrese el numero de placa: '))
            Modelo = input('Ingrese el modelo del auto: ')
            Color = input('Ingrese el color del auto: ')
            Nombre = input('Ingrese el nombre del propetario: ')
            Apellido = input('Ingrese el apellido del propetario: ')
            Hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            insert_script = f"INSERT INTO registro (Placa, Modelo, Estado, Hora) VALUES ('{Placa}', '{Modelo}','{Estado}', '{Hora}')"
            cur.execute(insert_script)
            conn.commit()

            insert_script = f"INSERT INTO vehiculos (Placa, Modelo, Color, Nombre, Apellido, Hora) VALUES ('{Placa}', '{Modelo}', '{Color}', '{Nombre}', '{Apellido}', '{Hora}')"
            cur.execute(insert_script)
            conn.commit()
            
            print("------REGISTRO DE AUTOS------")
            cur.execute('SELECT * FROM vehiculos')
            for record in cur.fetchall():
                print(record)
            
        elif Opcion == 2:
            Estado = "Salida"
            Placa = int(input('Ingrese el numero de placa: '))
            Modelo = input('Ingrese el modelo del auto: ')
            delete_script = f"DELETE FROM vehiculos WHERE Placa = '{Placa}' AND Modelo = '{Modelo}'"
            cur.execute(delete_script)
            conn.commit()

            Hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            insert_script = f"INSERT INTO registro (Placa, Modelo, Estado, Hora) VALUES ('{Placa}', '{Modelo}','{Estado}', '{Hora}')"
            cur.execute(insert_script)
            conn.commit()

            print("------REGISTRO DE AUTOS------")
            cur.execute('SELECT * FROM vehiculos')
            for record in cur.fetchall():
                print(record)
        elif Opcion == 3:
            print("------REGISTRO DE SALIDAS Y ENTRADAS------")
            cur.execute('SELECT * FROM registro')
            for record in cur.fetchall():
                print(record)

        else:
            print("Hasta pronto")
            break

Actualizar_Registro()

cur.close()
conn.close()