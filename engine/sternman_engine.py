from interface.engine import Engine



class SternmanEngine(Engine):
    def __init__(self, warming_light_on):
        self.warming_light_on = warming_light_on
        
    def needs_service(self):
        return warming_light_on