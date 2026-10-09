# Documentation

One page per pattern. Each page has the intent, a class diagram, how the example in this repo works, when to use
the pattern, and what is different in Python.

| Group | Pattern | Page | Code |
|---|---|---|---|
| Behavioural | Iterator | [iterator.md](behavioural/iterator.md) | [iterator.py](../behavioural/iterator.py) |
| Behavioural | Observer | [observer.md](behavioural/observer.md) | [observer.py](../behavioural/observer.py) |
| Behavioural | Strategy | [strategy.md](behavioural/strategy.md) | [strategy.py](../behavioural/strategy.py) |
| Creational | Builder | [builder.md](creational/builder.md) | [builder.py](../creational/builder.py) |
| Creational | Factory | [factory.md](creational/factory.md) | [factory.py](../creational/factory.py) |
| Creational | Singleton | [singleton.md](creational/singleton.md) | [singleton.py](../creational/singleton.py) |
| Structural | Adapter | [adapter.md](structural/adapter.md) | [adapter.py](../structural/adapter.py) |
| Structural | Decorator | [decorator.md](structural/decorator.md) | [decorator.py](../structural/decorator.py) |
| Structural | Facade | [facade.md](structural/facade.md) | [facade.py](../structural/facade.py) |
| Basics | Abstract classes vs. interfaces | [abstract-classes-vs-interfaces.md](abstract-classes-vs-interfaces.md) | [abstract_class.py](../abstract_class.py), [interface.py](../interface.py) |

**Groups** (from the "Gang of Four" book):

- **Creational** patterns deal with how objects are created.
- **Structural** patterns deal with how classes and objects are combined.
- **Behavioural** patterns deal with how objects communicate and share responsibilities.

## Quick comparison

Patterns that look alike in code:

| Patterns | Difference |
|---|---|
| Adapter vs. Decorator vs. Facade | All wrap something. Adapter **changes** the interface, Decorator **keeps** it and adds behaviour, Facade **simplifies** a whole subsystem. |
| Factory vs. Builder | Factory creates an object in one call. Builder creates it in several steps, useful when there are many optional parts. |
| Strategy vs. Observer | Strategy swaps **one** algorithm the object uses. Observer informs **many** objects about a change. |
