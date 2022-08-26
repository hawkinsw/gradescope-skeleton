#!/usr/bin/env bash

# First, delete the old autograder zip file.
rm -rf autograder.zip

# Second, create the autograder zip file with all the required files.
# The files listed here are the ones that are *absolutely* required.
zip -r autograder.zip\
  setup.sh\
  requirements.txt\
  run_autograder\
  run_tests.py\
  tests/*.py

