#!/bin/bash
set -e

if [ -d pyrav4l2 ]; then python3 -m yapf -ipr pyrav4l2/; fi
test $(git status --porcelain | wc -l) -eq 0 || { git diff; false; }
