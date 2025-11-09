from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo: str, epoca: str):
        if museo == "Nessun filtro":
            museo = None
        if epoca == "Nessun filtro":
            epoca = None

        if museo:
            id_museo = self._museo_dao.get_id_by_nome(museo)
        else:
            id_museo = None

        return self._artefatto_dao.get_artefatti_filtrati(id_museo, epoca)

    # --- EPOCHE ---
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        artefatti = self._artefatto_dao.get_all_artefatti()
        if artefatti is None:
            return None
        epoche = list({a.epoca for a in artefatti})
        epoche.sort()
        return epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        musei = self._museo_dao.get_all_musei()
        return musei

