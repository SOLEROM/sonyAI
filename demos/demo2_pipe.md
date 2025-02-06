

rpicam-vid -t 2s -o a.mp4 --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json --viewfinder-width 1920 --viewfinder-height 1080 --framerate 30 -n -v 2
ffmpeg -i a.mp4 -frames:v 1 out.png
