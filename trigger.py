
class Trigger:
    def __init__(self):
        self._simvar = None
        self._event = None

    def bind_to_simvar(self, simvar: str):
        self._simvar = simvar

    def bind_to_event(self, event):
        self._event = event

    @property
    def bound_simvar(self):
        return self._simvar

    def on_simvar_data(self, data):
        if self._event:
            if data == 1.0:
                self._event(True)
            else:
                self._event(False)
