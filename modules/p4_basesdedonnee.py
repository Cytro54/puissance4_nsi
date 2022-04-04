import sqlite3
			
class p4_basesdedonnee():
    def __init__():
        conn = sqlite3.connect('base_de_donnees.db')
        cur = conn.cursor()
        

    def ajoutdejoueuroumodificationdelabasededonee(self, nom_joueur, score):
        nvx_data = (nom_joueur, score))
        cur.execute("INSERT INTO TOP_SCORE(nom,score) VALUES(?, ?)", nvx_data)
        conn.commit()


    def recupererlesmeilleursscores(self):

        conn = sqlite3.connect('base_de_donnees.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM TOP_SCORE')
        conn.commit()
        listescore = cur.fetchall()
        return listescore
    def fin_programme(self):
        cur.close()
        conn.close()