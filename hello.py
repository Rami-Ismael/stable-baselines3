import os

envs_list = [
			 "CartPole-v1",
			 "MountainCar-v0"
]
commands = "python train.py --algo dqn --n-timesteps 1000 --log-interval 100 --env  MountainCar-v0 --seed 42"
for x in envs_list:
    print(x)
    os.system(f"python train.py --algo dqn --n-timesteps 1000 --log-interval 100 --env {x} --seed 42")