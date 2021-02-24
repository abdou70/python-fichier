import mysql.connector as MS

try:
    conn = MS.connect(host="localhost",database="angularapi",user="root",password="")
    cursor = conn.cursor()


    emetteur = "INSERT INTO emetteur(nom,prenom,telephone,montant_envoyer) VALUES('Diop','Mor','776957616',25000)"
    cursor.execute(emetteur)
    conn.commit()

    emetteur="SELECT * FROM emetteur"
    cursor.execute(emetteur)

    emetteurs = cursor.fetchall()

    for emett in emetteurs :
        print("Prenom :{}" .format(emett[2]))


except MS.Error as err:
    print(err)

finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()