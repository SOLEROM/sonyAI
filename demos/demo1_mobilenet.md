# demo1 mobilenet

run

```
rpicam-hello -t 0s
     --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json 
     --viewfinder-width 1920 --viewfinder-height 1080 
     --framerate 30
```


### imx500_mobilenet_ssd.json

* declares a post-processing pipeline that contains two stages
    * imx500_object_detection
    * object_detect_draw_cv

```
{
    "imx500_object_detection":
    {
        "max_detections" : 5,
        "threshold" : 0.6,
        "network_file": "/usr/share/imx500-models/imx500_network_ssd_mobilenetv2_fpnlite_320x320_pp.rpk",

        "save_input_tensor":
        {
            "filename": "/home/pi/input_tensor.raw",
            "num_tensors": 10,
            "norm_val": [384, 384, 384, 0],
            "norm_shift": [0, 0, 0, 0]
        },

        "temporal_filter":
        {
            "tolerance": 0.1,
            "factor": 0.2,
            "visible_frames": 4,
            "hidden_frames": 2
        },
    
        "classes":
        [
            "person",
            "bicycle",
            "car",
        ...
        ......
            "teddy bear",
            "hair drier",
            "toothbrush"
        ]
    },

    "object_detect_draw_cv":
    {
        "line_thickness" : 2
    }
}

```

## temporal_filter ???

The raw inference output data of this network can be quite noisy, so this stage also preforms some temporal filtering and applies hysteresis. To disable this filtering, remove the temporal_filter config block.