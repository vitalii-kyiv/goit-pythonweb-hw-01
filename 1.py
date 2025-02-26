from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make: str = make
        self.model: str = model
        self.region: str = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


us_factory: VehicleFactory = USVehicleFactory()
eu_factory: VehicleFactory = EUVehicleFactory()

vehicle1: Car = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2: Motorcycle = eu_factory.create_motorcycle("BMW", "R1250")
vehicle2.start_engine()
