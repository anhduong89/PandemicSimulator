"""duong mod edit PandemicSim"""

from tqdm import trange

import pandemic_simulator_1 as ps
import csv

def run_pandemic_gym_env() -> None:
    """Here we execute the gym envrionment wrapped simulator using austin regulations,
    a small town config and default person routines."""

    print('\nA tutorial that runs the OpenAI Gym environment wrapped simulator', flush=True)

    # init globals
    ps.init_globals(seed=0)

    # select a simulator config
    sim_config = ps.sh.small_town_config

    # make env
    env = ps.env.PandemicGymEnv.from_config(sim_config, pandemic_regulations=ps.sh.swedish_regulations)

    # setup viz
    viz = ps.viz.GymViz.from_config(sim_config=sim_config)

    # run stage-0 action steps in the environment
    env.reset()
    fname='data_age_group.csv'
    with open(fname, 'w+', newline='') as file: 
        file.truncate()
    # with f as file:   
    #     write = csv.writer(file)
    #     write.writerows(['unsusceptible', 'susceptible', 'exposed', 'pre_asymp', 'pre_symp', 'asymp', 'symp', 'needs_hospitalization', 'hospitalized', 'recovered', 'deceased'])   
         
    for _ in trange(3, desc='Simulating day'):      
        obs, reward, done, aux = env.step(action=0)  # here the action is the discrete regulation stage identifier
        
        # writing the data into the file
        with open(fname, 'w+', newline='') as file:   
            write = csv.writer(file)
            write.writerows(env.output_as_group())
        exit()
    # generate plots



if __name__ == '__main__':
    run_pandemic_gym_env()
