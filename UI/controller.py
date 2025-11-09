import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()
        if musei:
            musei_opts = [ft.dropdown.Option("Nessun filtro")] + [ft.dropdown.Option(m.nome) for m in musei]
        else:
            musei_opts = [ft.dropdown.Option("Nessun filtro")]
        if epoche:
            epoche_opts = [ft.dropdown.Option("Nessun filtro")] + [ft.dropdown.Option(e) for e in epoche]
        else:
            epoche_opts = [ft.dropdown.Option("Nessun filtro")]
        self._view.museo_dropdown.options = musei_opts
        self._view.epoca_dropdown.options = epoche_opts

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_museo_change(self, e):
        value = e.control.value
        self.museo_selezionato = None if value == "Nessun filtro" else value

    def on_epoca_change(self, e):
        value = e.control.value
        self.epoca_selezionata = None if value == "Nessun filtro" else value

    # AZIONE: MOSTRA ARTEFATTI
    def show_artefatti(self, e):
        """
        Mostra gli artefatti in base ai filtri selezionati.
        """
        artefatti = self._model.get_artefatti_filtrati(
            museo=self.museo_selezionato,
            epoca=self.epoca_selezionata
        )
        self._view.lista_artefatti.controls.clear()
        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato per i criteri selezionati.")
        else:
            for a in artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(str(a)))

        self._view.page.update()
