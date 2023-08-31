class Observer:
    def update(self, message):
        pass


class WeatherStation:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class Display(Observer):
    def update(self, message):
        print(f"Display received message: {message}")


# Usage
weather_station = WeatherStation()

d1 = Display()
d2 = Display()

weather_station.add_observer(d1)
weather_station.add_observer(d2)

weather_station.notify_observers("Temperature is 25°C")
