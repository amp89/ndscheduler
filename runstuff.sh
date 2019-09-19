make clean
python setup.py install
export NDSCHEDULER_SETTINGS_MODULE=simple_scheduler.settings
./venv/bin/python simple_scheduler/scheduler.py
