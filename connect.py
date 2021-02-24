import sqlite3

connection=sqlite3.connect("base.db")
cursor=connection.cursor()


#########_______ Lire tous les donnees de la base de donnee ##################______
# cursor.execute('SELECT * FROM user')

# print(cursor.fetchall())

cursor.execute('INSERT INTO user(nom,prenom,telephone)VALUES("Mbow","Cheikhe",772001976)')
connection.commit()
print("nouvel utilisateur ajouter avec success")

connection.close()