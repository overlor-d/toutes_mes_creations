import sqlite3

conn=sqlite3.connect("movie_db.db")

def Search(request):
    cursor=conn.cursor()
    if not isinstance(request, int):
        request="%"+request+"%"
    cursor.execute('SELECT * FROM Film WHERE nom LIKE ? OR genre LIKE ? OR company LIKE ? OR main LIKE ? OR directeur LIKE ? OR scenariste LIKE ? OR year LIKE ? OR pays LIKE ?',(request,request,request,request,request,request,request,request,))
    rows=cursor.fetchall()
    if rows!=[]:
        return rows
    cursor.close()
    return False

def Login(user,mdp):
    cursor=conn.cursor()
    cursor.execute('SELECT motdepasse FROM Client WHERE pseudo=?',(user,))
    rows=cursor.fetchall()
    if rows==[]:
        return "Ton pseudo n'est pas enregistré"
    if rows[0][0]==mdp:
        return True
    else:
        return False

def Register(nom,prenom,mdp,pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT pseudo FROM Client WHERE pseudo=?',(pseudo,))
    rows=cursor.fetchall()
    if rows!=[]:
        return "Ton pseudo est déjà enregistré"
    cursor.execute('INSERT INTO Client(nom,prenom,motdepasse,pseudo) VALUES (?,?,?,?)',(nom,prenom,mdp,pseudo,))
    conn.commit()
    cursor.close()
    print("Compte créé !")

def DeleteUser(pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=?',(pseudo,))
    rows=cursor.fetchall()
    cursor.execute('DELETE FROM Client WHERE n_user=?',(rows[0][0],))
    conn.commit()
    cursor.close()
    print("Compte supprimé !")

def StatutFilm(pseudo,film):
    cursor=conn.cursor()
    cursor.execute('SELECT n_film FROM Film WHERE nom=?',(film,))
    nfilm=cursor.fetchall()[0][0]
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT statut FROM Filmographie WHERE n_user=? AND n_film=?',(nuser,nfilm,))
    rows=cursor.fetchall()
    print(rows)
    if rows==[]:
        cursor.execute('INSERT INTO Filmographie VALUES (?,?,?)',(1,nfilm,0,))
        conn.commit()
        return "Statut modifié"
    if rows[0][0]==0:
        cursor.execute('UPDATE Filmographie SET statut=? WHERE n_user=? AND n_film=?',(1,nuser,nfilm,))
        conn.commit()
        return "Statut modifié"

def VoirStatut(pseudo,film):
    cursor=conn.cursor()
    cursor.execute('SELECT n_film FROM Film WHERE nom=?',(film,))
    nfilm=cursor.fetchall()[0][0]
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT statut FROM Filmographie WHERE n_user=? AND n_film=?',(nuser,nfilm,))
    rows=cursor.fetchall()[0][0]
    if rows==[]:
        attente=False
        vu=False
    if rows==0:
        attente=True
        vu=False
    if rows==1:
        attente=True
        vu=True
    return attente,vu

def AttenteFilm(pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT Film.* FROM Filmographie JOIN Film ON Filmographie.n_film=Film.n_film WHERE n_user=? AND statut=0',(nuser,))
    rows=cursor.fetchall()
    if rows!=[]:
        return rows
    return False

def VuFilm(pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT Film.* FROM Filmographie JOIN Film ON Filmographie.n_film=Film.n_film WHERE n_user=? and statut=1',(nuser,))
    rows=cursor.fetchall()
    if rows!=[]:
        return rows
    return False