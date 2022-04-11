import sqlite3
			
class p4_basesdedonnee():
    def __init__(self):

        self.conn = sqlite3.connect('base_de_donnees.db')
        self.cur = self.conn.cursor()
        

    def ajoutdejoueuroumodificationdelabasededonee(self, nom_joueur, score):

        nvx_data = (nom_joueur, score)
        self.cur.execute("INSERT INTO TOP_SCORE(nom,score) VALUES(?, ?)", nvx_data)
        self.conn.commit()


    def afficherlesmeilleursscores(self):

        self.cur.execute('SELECT * FROM TOP_SCORE')
        self.conn.commit()
        listescore = self.cur.fetchall()
        
        print("==== HIGH SCORE ====")
        for i in listescore:
            id, nom, score    = i
            print(f"{nom} :  {score}")
            
    def supprimerunscore(self):
        self.cur.execute('SELECT * FROM TOP_SCORE')
        self.conn.commit()
        listescore = self.cur.fetchall()

    def fin_programme(self):

        self.cur.close()
        self.conn.close()
