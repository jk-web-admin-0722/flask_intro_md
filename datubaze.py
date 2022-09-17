import sqlite3

def visiDati():
    DB = sqlite3.connect('dati.db')
    SQL = DB.cursor()
    SQL.execute("SELECT * FROM dati")

    dati = []
    rezultati = SQL.fetchall()

    for rez in rezultati:
        dati.append([rez[1], rez[2], rez[3], rez[4]])

    return dati

def pievienotDatus(dati):
    DB = sqlite3.connect('dati.db')
    SQL = DB.cursor()
    rez = SQL.execute("INSERT INTO dati (vards, uzvards, epasts, zina) VALUES (:vards, :uzvards, :epasts, :zina)", 
    {'vards':dati['vards'], 'uzvards':dati['uzvards'], 'epasts':dati['epasts'], 'zina':dati['zina']})
    DB.commit()
    
def iegutDatus(vards):
    DB = sqlite3.connect('dati.db')
    SQL = DB.cursor()
    SQL.execute(f"SELECT * FROM dati WHERE vards LIKE '%{vards}%'")

    dati = []
    rezultati = SQL.fetchall()

    for rez in rezultati:
        dati.append([rez[1], rez[2], rez[3], rez[4]])

    return dati

# rindina = {"vards":"Andris", "uzvards":"Bērziņš", "epasts":"andris@berzins.lv", "zina":"nu aiziet"}