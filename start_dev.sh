#!/usr/bin/env bash
cd "$(dirname "$0")"
echo "Starting Falcor HR Induction Presenter Console..."
python3 run_dev.py || python run_dev.py
