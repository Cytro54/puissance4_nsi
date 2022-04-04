import sqlite3
			
class p4_basesdedonnee():
    def __init__(self):
        self.conn = sqlite3.connect('base_de_donnees.db')
        self.cur = conn.cursor()
        

    def ajoutdejoueuroumodificationdelabasededonee(self, nom_joueur, score):
        nvx_data = (nom_joueur, score)
        self.cur.execute("INSERT INTO TOP_SCORE(nom,score) VALUES(?, ?)", nvx_data)
        self.conn.commit()


    def recupererlesmeilleursscores(self):

        self.cur.execute('SELECT * FROM TOP_SCORE')
        self.conn.commit()
        listescore = self.cur.fetchall()
        return listescore

    def supprimer(self,trucasupprimer):
        suppr = trucasupprimer
        self.cur.execute('DELETE FROM TOP_SCORE WHERE nom = ?', suppr)
        self.conn.commit()


    def fin_programme(self):
        self.cur.close()
        self.conn.close()

b1 = p4_basesdedonnee()
b1.ajoutdejoueuroumodificationdelabasededonee("josh", 12)
print(b1.recupererlesmeilleursscores())
b1.supprimer("josh")
b1.fin_programme()