from hazard import submit

# Run only one episode on the training set
submit(output_dir="outputs/", env_name="fire", agent="mcts", port=1071, max_test_episode=1,)
       # perceptional: bool = False,  # turn on this for the perceptional version of HAZARD
       #  effect_on_agents: bool = False,  # turn on this to let hazard affect agents
       #  run_on_test: bool = False,  # turn off to run on test set

# Run on full test set
#submit(output_dir="outputs/", env_name="fire", agent="mcts", port=10826, max_test_episode=25, run_on_test=True)
       # perceptional: bool = False,  # turn on this for the perceptional version of HAZARD
       #  effect_on_agents: bool = False,  # turn on this to let hazard affect agents
       #  run_on_test: bool = False,  # turn off to run on test set
