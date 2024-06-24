# machine learning toolbox

<img src="docs/malt.png" width="200" align="right">

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)

## Installation

```
pip install git+https://github.com/mhyatt000/malt
```

## Usage

* can be imported as modules
* can/SHOULD be copy-pasted as needed

## Code Structure

```
├── malt
│   ├── data        # data processing and loading
│   ├── env
│   │   └── wrapper
│   ├── hf          # huggingface tools
│   ├── hydra       # hydra config tools... resolvers and things
│   ├── model
│   │   ├── hub     # models that are ready for training pipeline
│   │   ├── module  # model pieces and building blocks
│   │   └── net     # model architectures with no bells and whistles
│   ├── pl          # pytorch lightning
│   ├── u           # utils that dont fit anywhere else
│   └── wandb       # wandb and logging
```

### MINT - MultI Node Training

```
└── mint
    └── scripts     # so that you don't have to sign onto each node annoyingly
```

## Contributing

please do that
