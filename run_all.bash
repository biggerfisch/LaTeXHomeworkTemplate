#!/usr/bin/env bash
	
for f in problem_*.py; do
    python3 "$f" > "${f%.py}.out"
done
