from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self.cnx = ConnessioneDB.get_connection()

    def get_all_musei(self):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT * FROM museo"
            cursor.execute(query)
            result = cursor.fetchall()

            if not result:
                return None

            musei = [Museo(*m) for m in result]
            return musei

        except Exception:
            return None
