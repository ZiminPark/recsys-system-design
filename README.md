## Explanation
checkout https://zimmy.gitbook.io/rec/

## File Structure
```bash
.
├── LICENSE
├── Makefile          # commands
├── README.md
├── requirements.txt  # package information
├── setup.cfg         # configurations for formatting & linting & unit-test
├── backend           # source code for backend location
├── streamlit         # source code for streamlit instead of frontend  
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

## Configurations
`setup.cfg` states all configurations for formatting & linting & unit-test.

## Verifications
- per commit: pre-commit hook runs formatting and linting.
- per pull-request: GitHub Actions check formatting, linting, and unit-test results.

## Recommended Repository Settings
#### Restriction on multi-commit pushes
`Settings` -> `General` -> `Merge botton` -> `Allow squash merging` ONLY
<img width="796" src="https://user-images.githubusercontent.com/14961526/152031596-a329a74c-add7-4d1c-ada5-d0279da16195.png">

#### Branch Protection Rules
`Settings` -> `Branches` -> `Branch protection rules` -> `Add rule`
- Branch name pattern: `main`
- Require a pull request before merging & Require approvals
- Require status checks to pass before merging & Require branches to be up to date before merging
- Include administrators
