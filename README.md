<img src="docs/\_static/img/logo.png" align="right" width="40%"/>

[![pipeline status](https://gitlab.com/araffin/stable-baselines3/badges/master/pipeline.svg)](https://gitlab.com/araffin/stable-baselines3/-/commits/master) [![Documentation Status](https://readthedocs.org/projects/stable-baselines/badge/?version=master)](https://stable-baselines3.readthedocs.io/en/master/?badge=master) [![coverage report](https://gitlab.com/araffin/stable-baselines3/badges/master/coverage.svg)](https://gitlab.com/araffin/stable-baselines3/-/commits/master)
[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Stable Baselines3

Stable Baselines3 (SB3) is a set of reliable implementations of reinforcement learning algorithms in PyTorch. It is the next major version of [Stable Baselines](https://github.com/hill-a/stable-baselines).

You can read a detailed presentation of Stable Baselines3 in the [v1.0 blog post](https://araffin.github.io/post/sb3/) or our [JMLR paper](https://jmlr.org/papers/volume22/20-1364/20-1364.pdf).


These algorithms will make it easier for the research community and industry to replicate, refine, and identify new ideas, and will create good baselines to build projects on top of. We expect these tools will be used as a base around which new ideas can be added, and as a tool for comparing a new approach against existing ones. We also hope that the simplicity of these tools will allow beginners to experiment with a more advanced toolset, without being buried in implementation details.

**Note: despite its simplicity of use, Stable Baselines3 (SB3) assumes you have some knowledge about Reinforcement Learning (RL).** You should not utilize this library without some practice. To that extent, we provide good resources in the [documentation](https://stable-baselines3.readthedocs.io/en/master/guide/rl.html) to get started with RL.

## Main Features

**The performance of each algorithm was tested** (see *Results* section in their respective page),
you can take a look at the issues [#48](https://github.com/DLR-RM/stable-baselines3/issues/48) and [#49](https://github.com/DLR-RM/stable-baselines3/issues/49) for more details.


| **Features**                | **Stable-Baselines3** |
| --------------------------- | ----------------------|
| State of the art RL methods | :heavy_check_mark: |
| Documentation               | :heavy_check_mark: |
| Custom environments         | :heavy_check_mark: |
| Custom policies             | :heavy_check_mark: |
| Common interface            | :heavy_check_mark: |
| `Dict` observation space support  | :heavy_check_mark: |
| Ipython / Notebook friendly | :heavy_check_mark: |
| Tensorboard support         | :heavy_check_mark: |
| PEP8 code style             | :heavy_check_mark: |
| Custom callback             | :heavy_check_mark: |
| High code coverage          | :heavy_check_mark: |
| Type hints                  | :heavy_check_mark: |


### Planned features

Please take a look at the [Roadmap](https://github.com/DLR-RM/stable-baselines3/issues/1) and [Milestones](https://github.com/DLR-RM/stable-baselines3/milestones).

## Migration guide: from Stable-Baselines (SB2) to Stable-Baselines3 (SB3)

A migration guide from SB2 to SB3 can be found in the [documentation](https://stable-baselines3.readthedocs.io/en/master/guide/migration.html).

## Documentation

Documentation is available online: [https://stable-baselines3.readthedocs.io/](https://stable-baselines3.readthedocs.io/)

## Integrations

Stable-Baselines3 has some integration with other libraries/services like Weights & Biases for experiment tracking or Hugging Face for storing/sharing trained models. You can find out more in the [dedicated section](https://stable-baselines3.readthedocs.io/en/master/guide/integrations.html) of the documentation.


## RL Baselines3 Zoo: A Training Framework for Stable Baselines3 Reinforcement Learning Agents

[RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) is a training framework for Reinforcement Learning (RL).

It provides scripts for training, evaluating agents, tuning hyperparameters, plotting results and recording videos.

In addition, it includes a collection of tuned hyperparameters for common environments and RL algorithms, and agents trained with those settings.

Goals of this repository:

1. Provide a simple interface to train and enjoy RL agents
2. Benchmark the different Reinforcement Learning algorithms
3. Provide tuned hyperparameters for each environment and RL algorithm
4. Have fun with the trained agents!

Github repo: https://github.com/DLR-RM/rl-baselines3-zoo

Documentation: https://stable-baselines3.readthedocs.io/en/master/guide/rl_zoo.html

## SB3-Contrib: Experimental RL Features

We implement experimental features in a separate contrib repository: [SB3-Contrib](https://github.com/Stable-Baselines-Team/stable-baselines3-contrib)

This allows SB3 to maintain a stable and compact core, while still providing the latest features, like Recurrent PPO (PPO LSTM), Truncated Quantile Critics (TQC), Quantile Regression DQN (QR-DQN) or PPO with invalid action masking (Maskable PPO).

Documentation is available online: [https://sb3-contrib.readthedocs.io/](https://sb3-contrib.readthedocs.io/)


## Installation

**Note:** Stable-Baselines3 supports PyTorch >= 1.11

### Prerequisites
Stable Baselines3 requires Python 3.7+.

#### Windows 10

To install stable-baselines on Windows, please look at the [documentation](https://stable-baselines3.readthedocs.io/en/master/guide/install.html#prerequisites).


### Install using pip
Install the Stable Baselines3 package:
```
pip install stable-baselines3[extra]
```
**Note:** Some shells such as Zsh require quotation marks around brackets, i.e. `pip install 'stable-baselines3[extra]'` ([More Info](https://stackoverflow.com/a/30539963)).

This includes an optional dependencies like Tensorboard, OpenCV or `atari-py` to train on atari games. If you do not need those, you can use:
```
pip install stable-baselines3
```

Please read the [documentation](https://stable-baselines3.readthedocs.io/) for more details and alternatives (from source, using docker).


## Example

Most of the library tries to follow a sklearn-like syntax for the Reinforcement Learning algorithms.

Here is a quick example of how to train and run PPO on a cartpole environment:
```python
import gym

from stable_baselines3 import PPO

env = gym.make("CartPole-v1")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()

env.close()
```

Or just train a model with a one liner if [the environment is registered in Gym](https://github.com/openai/gym/wiki/Environments) and if [the policy is registered](https://stable-baselines3.readthedocs.io/en/master/guide/custom_policy.html):

```python
from stable_baselines3 import PPO

model = PPO("MlpPolicy", "CartPole-v1").learn(10_000)
```

Please read the [documentation](https://stable-baselines3.readthedocs.io/) for more examples.


## Try it online with Colab Notebooks !

All the following examples can be executed online using Google colab notebooks:

- [Full Tutorial](https://github.com/araffin/rl-tutorial-jnrr19)
- [All Notebooks](https://github.com/Stable-Baselines-Team/rl-colab-notebooks/tree/sb3)
- [Getting Started](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/stable_baselines_getting_started.ipynb)
- [Training, Saving, Loading](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/saving_loading_dqn.ipynb)
- [Multiprocessing](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/multiprocessing_rl.ipynb)
- [Monitor Training and Plotting](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/monitor_training.ipynb)
- [Atari Games](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/atari_games.ipynb)
- [RL Baselines Zoo](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/rl-baselines-zoo.ipynb)
- [PyBullet](https://colab.research.google.com/github/Stable-Baselines-Team/rl-colab-notebooks/blob/sb3/pybullet.ipynb)


## Implemented Algorithms

| **Name**         | **Recurrent**      | `Box`          | `Discrete`     | `MultiDiscrete` | `MultiBinary`  | **Multi Processing**              |
| ------------------- | ------------------ | ------------------ | ------------------ | ------------------- | ------------------ | --------------------------------- |
| ARS<sup>[1](#f1)</sup>   | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :heavy_check_mark: |
| A2C   | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| DDPG  | :x: | :heavy_check_mark: | :x:                | :x:                 | :x:                | :heavy_check_mark: |
| DQN   | :x: | :x: | :heavy_check_mark: | :x:                 | :x:                | :heavy_check_mark: |
| HER   | :x: | :heavy_check_mark: | :heavy_check_mark: | :x:                 | :x:                | :x: |
| PPO   | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |
| QR-DQN<sup>[1](#f1)</sup>  | :x: | :x: | :heavy_check_mark: | :x:                 | :x:                | :heavy_check_mark: |
| RecurrentPPO<sup>[1](#f1)</sup>   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |
| SAC   | :x: | :heavy_check_mark: | :x:                | :x:                 | :x:                | :heavy_check_mark: |
| TD3   | :x: | :heavy_check_mark: | :x:                | :x:                 | :x:                | :heavy_check_mark: |
| TQC<sup>[1](#f1)</sup>   | :x: | :heavy_check_mark: | :x:                | :x:                 | :x: | :heavy_check_mark: |
| TRPO<sup>[1](#f1)</sup>  | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: |
| Maskable PPO<sup>[1](#f1)</sup>   | :x: | :x: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark:  |

<b id="f1">1</b>: Implemented in [SB3 Contrib](https://github.com/Stable-Baselines-Team/stable-baselines3-contrib) GitHub repository.

Actions `gym.spaces`:
 * `Box`: A N-dimensional box that containes every point in the action space.
 * `Discrete`: A list of possible actions, where each timestep only one of the actions can be used.
 * `MultiDiscrete`: A list of possible actions, where each timestep only one action of each discrete set can be used.
 * `MultiBinary`: A list of possible actions, where each timestep any of the actions can be used in any combination.



## Testing the installation
All unit tests in stable baselines3 can be run using `pytest` runner:
```
pip install pytest pytest-cov
make pytest
```

You can also do a static type check using `pytype`:
```
pip install pytype
make type
```

Codestyle check with `flake8`:
```
pip install flake8
make lint
```

## Projects Using Stable-Baselines3

We try to maintain a list of project using stable-baselines3 in the [documentation](https://stable-baselines3.readthedocs.io/en/master/misc/projects.html),
please tell us when if you want your project to appear on this page ;)

## Citing the Project

To cite this repository in publications:

```bibtex
@article{stable-baselines3,
  author  = {Antonin Raffin and Ashley Hill and Adam Gleave and Anssi Kanervisto and Maximilian Ernestus and Noah Dormann},
  title   = {Stable-Baselines3: Reliable Reinforcement Learning Implementations},
  journal = {Journal of Machine Learning Research},
  year    = {2021},
  volume  = {22},
  number  = {268},
  pages   = {1-8},
  url     = {http://jmlr.org/papers/v22/20-1364.html}
}
```

## Maintainers

Stable-Baselines3 is currently maintained by [Ashley Hill](https://github.com/hill-a) (aka @hill-a), [Antonin Raffin](https://araffin.github.io/) (aka [@araffin](https://github.com/araffin)), [Maximilian Ernestus](https://github.com/ernestum) (aka @ernestum), [Adam Gleave](https://github.com/adamgleave) (@AdamGleave), [Anssi Kanervisto](https://github.com/Miffyli) (@Miffyli) and [Quentin Gallouédec](https://gallouedec.com/) (@qgallouedec).

**Important Note: We do not do technical support, nor consulting** and don't answer personal questions per email.
Please post your question on the [RL Discord](https://discord.com/invite/xhfNqQv), [Reddit](https://www.reddit.com/r/reinforcementlearning/) or [Stack Overflow](https://stackoverflow.com/) in that case.


## How To Contribute

To any interested in making the baselines better, there is still some documentation that needs to be done.
If you want to contribute, please read [**CONTRIBUTING.md**](./CONTRIBUTING.md) guide first.

## Acknowledgments

The initial work to develop Stable Baselines3 was partially funded by the project *Reduced Complexity Models* from the *Helmholtz-Gemeinschaft Deutscher Forschungszentren*.

The original version, Stable Baselines, was created in the [robotics lab U2IS](http://u2is.ensta-paristech.fr/index.php?lang=en) ([INRIA Flowers](https://flowers.inria.fr/) team) at [ENSTA ParisTech](http://www.ensta-paristech.fr/en).


Logo credits: [L.M. Tenkes](https://www.instagram.com/lucillehue/)

# Research Section
# ToDo

- [ ] What is the Quantzation Method in the Research 
	- [ ] Ask for the review of the project
- [ ] Clone Stable Baseline 3 add different quantization concept in the model 
	- [ ] add flaq if you want quantization
		- [ ] add a flaq want type of quantization
	- [ ] fuse model
	- [x] prepare my model 
		- [ ] set your backedn
	- [ ] convert my model
	- [ ] test my model is int8
		- [ ] size of the model
		- [ ] inference of the model 
	- [ ] upload your changes to your own github
- [ ] add rl-zoo
	- [ ] train the method 
- [ ] Ask where to share my google Colab for a quantize resnet model 
- [ ] Static Quantization
- [ ] Dynamic Quantization 
- [ ] Make sure the quantize method will work for all algorithm
- [ ] Fix the Render on Fedora Device 

# Open Source Library
- PyTorch
- Stable Baseline 3
	- [DQN appraoch is a Double DQ Learning Appraoch instead of single Deep Q Neural Network](https://huggingface.co/blog/deep-rl-dqn#the-deep-q-network-dqn)
- Weight and Bias 
- Clean RL
- [Stable Baseline Zoo 3](https://github.com/DLR-RM/rl-baselines3-zoo)
# Tools
[[Quantization Drawing 2022-08-29 16.12.05.excalidraw]]
[[Quantize Aware Reinforcment Learning ToDo]]
# Resources
 https://github.com/pytorch/pytorch/issues/74028
(beta) Static Quantization with Eager Mode in PyTorch[](https://pytorch.org/tutorials/advanced/static_quantization_tutorial.html#beta-static-quantization-with-eager-mode-in-pytorch)
https://www.vedereai.com/introduction-to-quantization-on-pytorch/
 - [PyTorch Quantization Aware Training](https://leimao.github.io/blog/PyTorch-Quantization-Aware-Training/)
 - PyTorch Lightning Quantization by Thomas Viehmann
	-  [Training and Edge Optimized Speech Recognition MOdel with PyTorch Lightning](https://medium.com/pytorch-lightning/training-an-edge-optimized-speech-recognition-model-with-pytorch-lightning-a0a6a0c2a413)
# Google Colab
- [Simple QAT Resenet](https://colab.research.google.com/drive/1O9qRw7s6W4uCNK7iDZxRy2N7uukqaL3d)
- [qat](https://colab.research.google.com/drive/12bmRcHvZqCGkP4giMQgstLj90HnPlOGI)
- [PyTorch Quantizse Aware Training example from PyTorch Quantization Documentation.](https://colab.research.google.com/drive/1TX1JYdjTHDg36VXvnrIqntkyaKrz8Lzv?usp=sharing)
# Tips
- [yes, `torch.quantization` is going to be replaced by `torch.ao.quantization` migration is in progress, we’ll make an announcement when it is done ](https://discuss.pytorch.org/t/what-is-the-difference-between-calling-torch-ao-quantize-and-torch-quantize/161245)
#  Update Documentation
- [ ]  pytorch  Quantization Mode Support[](https://pytorch.org/docs/stable/quantization.html#quantization-mode-support)
# Code Help
```Python
import inspect
from IPython.display import Markdown, display

def pretty_print_source(source):
    display(Markdown('```python\n' + source + '\n```'))
    
source = inspect.getsource(QuantLinear.__init__)  
pretty_print_source(source)
```

# Implementation
- I first use stable  baseline allowed to use many diffferent RL algorithm and in different environment. 
	- I can add my  own model in the program. So , I can add quantize aware training in the model 
		- How to add a custome model
- convert the quantize model  to int 8 model
- check the inference process
- check the model performance
# Reinforcement Learning
- the  project need to deep q learning and actor critic model  in 2d and 3d environment 
## Reinforcement Learning  Online Resources
- [ Hugging Face Reinforcement Learning Online Resources](https://github.com/huggingface/deep-rl-class)

#  Quantization
- Quantize Aware Training
- Static Aware Training
- Dynamic Quantization

# Quantize Aware Training

## Example Script
## Train a model
- Double DQ Algorithm
- n timesteps 1000
- log internval 100
- env CarPole-v1
```Text
python train.py --algo dqn --n-timesteps 1000 --log-interval 100 --env CartPole-v1 --seed 42
```
## Recorc the work of the previos Trained Model
``` Python
python -m utils.record_video --algo dqn  --env CartPole-v1  --folder logs -n 1000
```
