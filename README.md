## walk_start_pack
The src folder for setup nao_walking. Changes in nao_ik/nao_ik/src/bnuman/ik_bhuman.cpp in 114, 115 lines, this corresponds to 88 degrees for hands parallel to body. Requirements: nao_lola package.
# In ros2 workspace:

git clone https://github.com/Starkit-SPL/walk_start_pack.git ./src/

# Then:

colcon build

# After from this ros2 workspace:


./src/runWalk
