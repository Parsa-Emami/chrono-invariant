# ChronoInvariant

Detect duplicate, missing and unexpected scheduled instants across time-zone boundaries.

**Status** Local proof of concept. See the [roadmap](ROADMAP.md) for product acceptance criteria and release status.

## Overview

Teams with recurring scheduling need to verify execution across time zones, DST folds and gaps independently of frameworks.

## Quickstart

Requires Python 3.11 or later. Use a system Python installation. The core uses only its standard library and reads local files.
Install your operating system's IANA time-zone data package if Europe/Amsterdam is unavailable.

```sh
git clone https://github.com/Parsa-Emami/chrono-invariant.git
cd chrono-invariant
python3 check.py examples/pass.json
python3 check.py examples/finding.json
python3 -m unittest discover -s tests -v
```

The second command deliberately exits with status 1 and reports `duplicate_execution`.

- [CLI contract and examples](docs/cli.md)
- [Architecture](docs/architecture.md) and [threat model](docs/threat-model.md)
- [Project rules](RULES.md), [roadmap](ROADMAP.md), and [contributing](CONTRIBUTING.md)
- [Security reporting](SECURITY.md) and [license](LICENSE)
- [Published documentation](https://parsa-emami.github.io/chrono-invariant/)
