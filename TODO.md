# TODO

Open tasks. The repository is already public.

## 1. Modernisation (v2.0.0)

- [x] Tag the original July 2023 state as `v1.0.0`
- [x] Rewrite Builder as a real step-by-step builder (it was a copy of the Factory example)
- [x] Make the Adapter convert an interface and print a result (the demo printed nothing)
- [x] Show the actual difference between abstract classes and interfaces (both files were identical), add `Protocol`
- [x] Fix the Observer interface signature, add `unsubscribe()`
- [x] Rename to PEP 8 names, add type hints, fix typos in output
- [x] Let `patterns.py` run single patterns
- [x] Add `pyproject.toml` with uv, Ruff, pytest and CI for Python 3.10 to 3.14
- [x] Add `docs/` with one page per pattern and Mermaid class diagrams
- [x] Add the MIT license

## 2. Before pushing

- [ ] Rewrite the old university e-mail in the commit metadata, then force-push `master` and the tags
- [ ] Create GitHub releases for `v1.0.0` and `v2.0.0`
- [ ] Set the repository description and topics
- [ ] Check that CI is green on GitHub

## 3. Ideas (optional)

- [ ] More patterns: Command, State, Template Method, Composite, Proxy
