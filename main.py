from flask import Flask, render_template, request
from datubaze import visiDati, pievienotDatus, iegutDatus

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/iepriekseja')
def iepriekseja():
    return render_template('iepriekseja.html')

@app.route('/parametri')
def parametri():
    id = request.args.get('id')
    title = request.args.get('title')
    status = request.args.get('status')
    print("ID:", id)
    print("Title:", title)
    print("Status:", status)
    return "param"

@app.route('/saskaitit')
def saskaitit():
    sk1 = request.args.get('sk1')
    sk2 = request.args.get('sk2')
    # print("sk1", type(sk1))
    # print("sk2", type(sk2))
    if sk1 is not None and sk2 is not None:
        if sk1.isdigit() and sk2.isdigit():
            sum = int(sk1) + int(sk2)
            return f"Summa ir {sum}"
        else:
            return "Kāds no parametriem nav skaitlis!"

    else:
        return "Neatradu parametrus"


@app.route('/meklet')
def meklet():
    parametrs = request.args.get('vaicajums')
    rezultats = []
    if parametrs is not None:
        with open("titanic.csv", "r", encoding="utf-8") as f:
            for rindina in f.readlines():
                if parametrs in rindina:
                    rezultats.append(rindina)

    return rezultats

######## RECEPTES
@app.route('/receptes')
def receptes():
    return render_template('receptes.html')

@app.route('/biesu')
def biesu():
    return render_template('biesu.html')

@app.route('/burkanu')
def burkanu():
    return render_template('burkanu.html')

@app.route('/grauzdinu')
def grauzdinu():
    return render_template('grauzdinu.html')    

@app.route('/kontakti', methods = ['GET', 'POST'])
def kontakti():
    msg = ""
    if request.method == 'POST':
        firstname = request.form.get('first-name')
        lastname =  request.form.get('last-name')
        email = request.form.get('email')
        text = request.form.get('text')
        # rindina prieks CSV
        line = f"{firstname},{lastname},{email},{text}\n"

        #rindina prieks DB ieraksta
        dbLine = {'vards':firstname, 'uzvards':lastname, 'epasts':email, 'zina':text}

        #rakstam iekšā CSV failā
        with open("zinas.csv", "a", encoding="utf-8") as f:
            f.write(line)

        #rakstam iekšā Datubāzē
        pievienotDatus(dbLine)
        
        msg = "Paldies! Jūsu ziņa saņemta!"

    return render_template('kontakti.html', message = msg)


@app.route('/dataCSV')
def dataCSV():
    data = []
    with open("zinas.csv", "r", encoding="utf-8") as f:
        for rindina in f.readlines():
            data.append(rindina.strip().split(','))

    return render_template('data.html', zinas = data)

@app.route('/dataDB')
def dataDB():
    vards = request.args.get('vards')
    if vards:
        # Mēs gribam meklēt
        data = iegutDatus(vards)
    else:
        # Nav parametra, negribam meklēt - atgriežam visu.
        data = visiDati()

    return render_template('dataDB.html', zinas = data, vards = vards)



if __name__ == '__main__':
    app.run(debug = True)