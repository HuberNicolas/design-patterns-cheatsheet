# Observer Pattern

from abc import ABC, abstractmethod


class TwitchSubscriber(ABC):
    @abstractmethod
    def send_notification(self, channel: str, event: str) -> None: ...


class TwitchChannel:
    def __init__(self, name: str):
        self.name = name
        self.subscribers: list[TwitchSubscriber] = []

    def subscribe(self, sub: TwitchSubscriber) -> None:
        self.subscribers.append(sub)

    def unsubscribe(self, sub: TwitchSubscriber) -> None:
        self.subscribers.remove(sub)

    def notify(self, event: str) -> None:
        for sub in self.subscribers:
            sub.send_notification(self.name, event)


class TwitchUser(TwitchSubscriber):
    def __init__(self, name: str):
        self.name = name

    def send_notification(self, channel: str, event: str) -> None:
        print(f"User {self.name} received notification from {channel}: {event}")


# Usage
def demo():
    channel = TwitchChannel("Codinghub")

    sub1, sub2, sub3 = TwitchUser("sub1"), TwitchUser("sub2"), TwitchUser("sub3")
    channel.subscribe(sub1)
    channel.subscribe(sub2)
    channel.subscribe(sub3)
    channel.notify("A new stream has started")

    channel.unsubscribe(sub2)
    channel.notify("The stream has ended")  # sub2 is no longer notified
