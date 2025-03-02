
## install

on PI:

```
sudo apt-get install python3.11  python3.11-venv

git clone https://github.com/SonySemiconductorSolutions/aitrios-rpi-sample-apps.git
cd aitrios-rpi-sample-apps/
python3.11 -m venv venv --system-site-packages
source venv/bin/activate
cd examples/line-monitor/
pip install -e .

run:
    line_monitor.py

```
