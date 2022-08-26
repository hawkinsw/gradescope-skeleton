#!/usr/bin/env bash

# From the baseline container provided by Gradescope, add
# python 3. This addition might no longer be necessary now
# that they support Ubuntu 22.04, but better safe than sorry.
apt-get install -y python3 python3-pip python3-dev

# Now, pip install all the requirements that we might need
# in order to do our grading.
pip3 install -r /autograder/source/requirements.txt
