<div align="center">

# Design Patterns Cheatsheet

**Common design patterns, each in one short, runnable Python file**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-none-brightgreen)
[![CI](https://github.com/HuberNicolas/design-patterns-cheatsheet/actions/workflows/ci.yml/badge.svg)](https://github.com/HuberNicolas/design-patterns-cheatsheet/actions/workflows/ci.yml)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?logo=ruff&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-yellow)

[Patterns](#patterns) · [Quick start](#quick-start) · [Documentation](docs/README.md)

</div>

A personal cheatsheet I wrote in July 2023 to revise the classic "Gang of Four" patterns. Every pattern lives in its
own file with a small, concrete example (Twitch subscribers, houses, coffee, power plugs) and a `demo()` function.

> [!NOTE]
> All descriptions are provided without warranty. The examples are kept small on purpose; they show the idea of a
> pattern, not production code. The original 2023 version is tagged [`v1.0.0`](https://github.com/HuberNicolas/design-patterns-cheatsheet/tree/v1.0.0).

## Contents

- [Patterns](#patterns)
- [Quick start](#quick-start)
- [Repository structure](#repository-structure)
- [Development](#development)
- [Sources](#sources)
- [License](#license)

## Patterns

| Group | Pattern | In one sentence | Code | Docs |
|---|---|---|---|---|
| 🔁 Behavioural | **Iterator** | Access the elements of a collection one by one without exposing its structure. | [iterator.py](behavioural/iterator.py) | [📖](docs/behavioural/iterator.md) |
| 🔁 Behavioural | **Observer** | When one object changes, all its subscribers are notified automatically. | [observer.py](behavioural/observer.py) | [📖](docs/behavioural/observer.md) |
| 🔁 Behavioural | **Strategy** | Put interchangeable algorithms in their own classes and choose one at runtime. | [strategy.py](behavioural/strategy.py) | [📖](docs/behavioural/strategy.md) |
| 🏗️ Creational | **Builder** | Build a complex object step by step. | [builder.py](creational/builder.py) | [📖](docs/creational/builder.md) |
| 🏗️ Creational | **Factory** | Create objects through a method, so callers do not depend on concrete classes. | [factory.py](creational/factory.py) | [📖](docs/creational/factory.md) |
| 🏗️ Creational | **Singleton** | Make sure there is only one instance and provide a global access point. | [singleton.py](creational/singleton.py) | [📖](docs/creational/singleton.md) |
| 🧩 Structural | **Adapter** | Convert one interface into the one a client expects. | [adapter.py](structural/adapter.py) | [📖](docs/structural/adapter.md) |
| 🧩 Structural | **Decorator** | Add behaviour to an object by wrapping it, without changing its class. | [decorator.py](structural/decorator.py) | [📖](docs/structural/decorator.md) |
| 🧩 Structural | **Facade** | Offer a simple interface to a complex subsystem. | [facade.py](structural/facade.py) | [📖](docs/structural/facade.md) |
| 📐 Basics | **Abstract classes vs. interfaces** | "Is a" with shared code vs. "can do" with only a contract. | [abstract_class.py](abstract_class.py), [interface.py](interface.py) | [📖](docs/abstract-classes-vs-interfaces.md) |

Each docs page has the intent, a class diagram, a walkthrough of the example, when to use the pattern and what is
different in Python. The [docs index](docs/README.md#quick-comparison) also compares patterns that look alike.

## Quick start

Requires Python 3.10 or newer. There are no dependencies.

Run all demos:

```bash
python patterns.py
```

Run only some of them:

```bash
python patterns.py observer decorator
```

Valid names: `iterator`, `observer`, `strategy`, `builder`, `factory`, `singleton`, `adapter`, `decorator`, `facade`,
`abstract_class`, `interface`.

## Repository structure

| Path | Content |
|---|---|
| [`patterns.py`](patterns.py) | Runs the demos |
| [`behavioural/`](behavioural) | Iterator, Observer, Strategy |
| [`creational/`](creational) | Builder, Factory, Singleton |
| [`structural/`](structural) | Adapter, Decorator, Facade |
| [`abstract_class.py`](abstract_class.py), [`interface.py`](interface.py) | Abstract classes vs. interfaces |
| [`docs/`](docs) | One page per pattern |
| [`tests/`](tests) | Tests for every pattern and demo |

Each pattern file follows the same layout: a `# <Name> Pattern` header, the classes, and a `demo()` function at the
end. Expected output is written next to the `print()` calls as `# Output: ...`.

## Development

The development tools are managed with [uv](https://docs.astral.sh/uv/).

| Task | Command |
|---|---|
| Run the tests | `uv run pytest` |
| Lint | `uv run ruff check .` |
| Format | `uv run ruff format .` |

CI runs the linter, the tests and all demos on Python 3.10 to 3.14 ([`ci.yml`](.github/workflows/ci.yml)).

To add a pattern: create `<group>/<pattern>.py` with a `demo()` function, register it in `PATTERNS` in
[`patterns.py`](patterns.py), add a test and a page in [`docs/`](docs).

## Sources

- "Software Construction", University of Zurich, Fall 2020 (Prof. Alberto Bacchelli)
- [Refactoring.Guru: Design Patterns](https://refactoring.guru/design-patterns)
- [NeetCode: 8 Design Patterns](https://neetcode.io/courses/lessons/8-design-patterns)
- [Spring Framework Guru: Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/)
- Eric Freeman, Elisabeth Robson: *Head First Design Patterns*, O'Reilly
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides: *Design Patterns: Elements of Reusable Object-Oriented
  Software*, Addison-Wesley, 1994

## License

[MIT](LICENSE) © 2023 Nicolas Huber
