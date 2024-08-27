from abc import ABC

from Observer.Observer import Observer

class Subject:
    def __init__(self):
        self.observers: list[Observer] = []

    def registerObserver(self, observer: Observer):
        self.observers.remove(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()
