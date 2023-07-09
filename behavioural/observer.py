# Observer pattern

class TwitchChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)
    
    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

from abc import ABC, abstractmethod

class TwitchSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass

class TwitchUser(TwitchSubscriber):
    def __init__(self, name):
        self.name = name
    
    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")

def demo():
    channel = TwitchChannel("Codinghub")

    channel.subscribe(TwitchUser("sub1"))
    channel.subscribe(TwitchUser("sub2"))
    channel.subscribe(TwitchUser("sub3"))

    channel.notify("A new stream has started released")
