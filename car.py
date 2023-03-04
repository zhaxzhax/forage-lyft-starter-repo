from interface.serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return battery.needs_service() or engine.needs_service()
