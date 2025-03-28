# Learn Odoo 17

- [Learn Odoo 17](#learn-odoo-17)
- [ToolStacks](#toolstacks)
- [Setup](#setup)
  - [Pre-commit(ruff)](#pre-commitruff)
  - [Manual pre-commit](#manual-pre-commit)
  - [Commit msg standard](#commit-msg-standard)
    - [install](#install)
- [Run](#run)
  - [Container](#container)
- [Source](#source)

# ToolStacks
- Code Quality
  - pyproject.toml
  - ruff
  - code spell
  - precommit(.pre-commit-config.yaml)
  - commit-lint

# Setup
## Pre-commit(ruff)
```bash
pip install ruff pre-commit && pre-commit install
```

## Manual pre-commit
```bash
pre-commit run --all-files
```

## Commit msg standard
### install
```bash
pip install commitizen
```

use `cz`
```bash
cz commit
```

# Run
## Container
```bash
make local-dev
```
now we can access [http://localhost:10017](http://localhost:10017)


# Source
[odoo-17-docker-compose](https://github.com/minhng92/odoo-17-docker-compose)
