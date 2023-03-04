from battery import *
from engine import *

class CarFactory():
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = new CapuletEngine(last_service_mileage,current_mileage)
        battery = new SpindlerBattery(current_date,last_service_date)
        return new Car(battery,engine)

    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = new WilloughbyEngine(last_service_mileage,current_mileage)
        battery = new SpindlerBattery(current_date,last_service_date)
        return new Car(battery,engine)

    def create_palindrome(current_date,last_service_date,warming_light_on):
        engine = new SternmanEngine(warming_light_on)
        battery = new SpindlerBattery(current_date,last_service_date)
        return new Car(battery,engine)

    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = new WilloughbyEngine(last_service_mileage,current_mileage)
        battery = new NubbinBattery(current_date,last_service_date)
        return new Car(battery,engine)

    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage):
        engine = new CapuletEngine(last_service_mileage,current_mileage)
        battery = new NubbinBattery(current_date,last_service_date)
        return new Car(battery,engine)