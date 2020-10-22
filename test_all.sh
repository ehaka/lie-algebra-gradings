#!/bin/bash

rm test.log
sage -t dim7/isom_utilities.py lie_gradings/classification/*.py lie_gradings/gradings/*.py >> test.log
