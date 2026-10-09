import sys

import abstract_class
import behavioural.iterator
import behavioural.observer
import behavioural.strategy
import creational.builder
import creational.factory
import creational.singleton
import interface
import structural.adapter
import structural.decorator
import structural.facade

PATTERNS = {
    "Behavioural Patterns": {
        "iterator": behavioural.iterator.demo,
        "observer": behavioural.observer.demo,
        "strategy": behavioural.strategy.demo,
    },
    "Creational Patterns": {
        "builder": creational.builder.demo,
        "factory": creational.factory.demo,
        "singleton": creational.singleton.demo,
    },
    "Structural Patterns": {
        "adapter": structural.adapter.demo,
        "decorator": structural.decorator.demo,
        "facade": structural.facade.demo,
    },
    "Abstract Classes vs. Interfaces": {
        "abstract_class": abstract_class.demo,
        "interface": interface.demo,
    },
}


def main(selected: list[str]) -> int:
    known = {name for group in PATTERNS.values() for name in group}
    unknown = [name for name in selected if name not in known]
    if unknown:
        print(f"Unknown pattern(s): {', '.join(unknown)}. Choose from: {', '.join(sorted(known))}")
        return 1

    for group, demos in PATTERNS.items():
        demos = {name: demo for name, demo in demos.items() if not selected or name in selected}
        if not demos:
            continue
        print(f"\n{group}")
        for name, demo in demos.items():
            print(f"\n{name.upper()}")
            demo()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
