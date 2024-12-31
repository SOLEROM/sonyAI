# Evb install

## repo tools

```
sudo apt install imx500-all imx500-tools
sudo apt install python3-opencv python3-munkres

sudo apt install -y build-essential libffi-dev libssl-dev zlib1g-dev libbz2-dev \
                    libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev \
                    xz-utils tk-dev liblzma-dev python3-pip python3-venv
```


## demo proj

```
git clone https://github.com/raspberrypi/picamera2

sudo apt install python3-opencv python3-munkres
sudo apt install -y python3-picamera2
```

## add model toolkit

```
python3 -m venv venvTorch
source venvTorch/bin/activate

sudo apt-get install -y libopenblas-dev libblas-dev m4 cmake cython python3-yaml
pip install numpy==1.26.0
pip install torch torchvision torchaudio
pip install tensorflow
pip install model-compression-toolkit

```