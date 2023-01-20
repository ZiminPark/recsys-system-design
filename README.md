# recsys-system-design
> Minimal System Design for Various Recommender System Scenario(Batch, Real-Time, Bandit, A/B, etc...

## Explanation
checkout https://zimmy.gitbook.io/rec/

## File Structure
```bash
.
├── LICENSE
├── Makefile                # commands
├── build                   # build information e.g.) Dockerfile
├── README.md
├── requirements-dev.txt    # package information
├── setup.cfg               # configurations for formatting & linting & unit-test
├── backend                 # source code for backend location
├── streamlit               # source code for streamlit instead of frontend  
└── test
    └── utest         # unit tests location
```

## Commands
```bash
$ make setup    # initial setup for the project
$ make format   # format python scripts
$ make lint     # lint python scripts
$ make utest    # run unit tests
$ make cov      # open coverage report (after `make utest`)
```

