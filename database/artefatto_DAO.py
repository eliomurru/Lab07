from logging import exception

import mysql

from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        self.cnx = ConnessioneDB.get_connection()

    def get_all_artefatti(self):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT * FROM artefatto"
            cursor.execute(query)
            result = cursor.fetchall()
            if not result:
                return None
            else:
                ArtefattoList = [Artefatto(*a) for a in result]
                return ArtefattoList
        except Exception:
            return None

    def get_artefatti_by_museum(self, id_museum):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT * FROM artefatto WHERE id_museo= %s"
            cursor.execute(query, (id_museum,))
            result = cursor.fetchall()
            if not result:
                return None
            else:
                ArtefattoList = [Artefatto(*a) for a in result]
                return ArtefattoList
        except Exception:
            return None

    def get_artefatti_by_epoca(self, epoca):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT * FROM artefatto WHERE epoca= %s"
            cursor.execute(query, (epoca,))
            result = cursor.fetchall()
            if not result:
                return None
            else:
                ArtefattoList = [Artefatto(*a) for a in result]
                return ArtefattoList
        except Exception:
            return None

    def get_artefatti_filtrati(self, id_museo=None, epoca=None):
        try:
            cursor = self.cnx.cursor()
            query = """
                SELECT * FROM artefatto
                WHERE id_museo = COALESCE(%s, id_museo)
                  AND epoca = COALESCE(%s, epoca);
            """
            cursor.execute(query, (id_museo, epoca))
            result = cursor.fetchall()
            if not result:
                return None
            ArtefattoList = [Artefatto(*a) for a in result]
            return ArtefattoList
        except Exception:
            return None