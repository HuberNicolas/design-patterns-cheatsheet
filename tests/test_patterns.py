import pytest

import abstract_class
import patterns
from behavioural.iterator import BinaryTreeIterator, build_tree, inorder
from behavioural.observer import TwitchChannel, TwitchSubscriber
from behavioural.strategy import RemoveEvenStrategy, RemoveNegativeStrategy, RemoveOddStrategy, Values
from creational.builder import Architect, HouseBuilder
from creational.factory import HouseFactory, Skyscraper, Treehouse
from creational.singleton import Radio, RadioSettings
from structural.adapter import EuropeanPowerOutlet, SwissPlug, SwissToEuropeanAdapter
from structural.decorator import BasicCoffee, MilkCoffeeDecorator, SugarCoffeeDecorator
from structural.facade import StackFacade


@pytest.mark.parametrize("name", [name for group in patterns.PATTERNS.values() for name in group])
def test_every_demo_runs(name, capsys):
    assert patterns.main([name]) == 0
    assert name.upper() in capsys.readouterr().out


def test_unknown_pattern_fails():
    assert patterns.main(["nope"]) == 1


def test_iterator_inorder():
    expected = [4, 2, 5, 1, 6, 3, 7]
    assert list(BinaryTreeIterator(build_tree())) == expected
    assert list(inorder(build_tree())) == expected


def test_observer_unsubscribe():
    class Recorder(TwitchSubscriber):
        def __init__(self):
            self.events = []

        def send_notification(self, channel, event):
            self.events.append((channel, event))

    channel, sub = TwitchChannel("c"), Recorder()
    channel.subscribe(sub)
    channel.notify("one")
    channel.unsubscribe(sub)
    channel.notify("two")
    assert sub.events == [("c", "one")]


def test_strategies():
    values = Values([-3, -2, -1, 0, 1, 2, 3])
    assert values.filter(RemoveNegativeStrategy()) == [0, 1, 2, 3]
    assert values.filter(RemoveEvenStrategy()) == [-3, -1, 1, 3]
    assert values.filter(RemoveOddStrategy()) == [-2, 0, 2]


def test_builder_resets_between_builds():
    builder = HouseBuilder()
    first = builder.with_pool().floors(2).build()
    second = builder.build()
    assert (first.pool, first.floors) == (True, 2)
    assert (second.pool, second.floors) == (False, 1)
    assert Architect(builder).family_house().garage


def test_factory():
    factory = HouseFactory()
    assert isinstance(factory.create_oak_treehouse("brown"), Treehouse)
    assert factory.create_steel_skyscraper(500).material == "steel"
    assert isinstance(factory.create_glass_skyscraper(300), Skyscraper)


def test_singleton_is_shared():
    assert RadioSettings.get_settings() is RadioSettings.get_settings()
    Radio().set_volume(11)
    assert Radio().settings.volume == 11


def test_adapter():
    outlet = EuropeanPowerOutlet()
    with pytest.raises(AttributeError):
        outlet.plug(SwissPlug())
    outlet.plug(SwissToEuropeanAdapter(SwissPlug()))
    assert outlet.plugged_in is not None


def test_decorator_stacks():
    coffee = SugarCoffeeDecorator(MilkCoffeeDecorator(BasicCoffee()))
    assert coffee.get_description() == "Coffee, Milk, Sugar"
    assert coffee.get_cost() == pytest.approx(2.8)


def test_facade_resizes():
    stack = StackFacade()
    for n in range(5):
        stack.push(n)
    assert stack.size() == 5
    assert [stack.pop() for _ in range(5)] == [4, 3, 2, 1, 0]
    assert stack.is_empty() and stack.pop() is None


def test_abstract_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        abstract_class.Plane("x")
