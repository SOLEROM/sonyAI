# convert

run in venv

```
> imxconv-pt -i ./qmodel.onnx -o convertOutput/ --overwrite-output

2025-03-02 06:35:36.443778: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-03-02 06:35:36.489156: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2025-03-02 06:35:36.489198: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2025-03-02 06:35:36.490344: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2025-03-02 06:35:36.496581: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2025-03-02 06:35:37.294451: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
2025-03-02 06:35:39,353 INFO : Running version 1.10.0 [/home/user/proj/imx500/venvBuildImx500/lib/python3.11/site-packages/uni/common/logger.py:148]
2025-03-02 06:35:39,353 INFO : Converting qmodel.onnx [/home/user/proj/imx500/venvBuildImx500/lib/python3.11/site-packages/uni/common/logger.py:148]
2025-03-02 06:35:43,762 INFO : Wrote outputs to /tmp/tmpqxwgdm9z/qmodel.uni-pytorch.um.pb [/home/user/proj/imx500/venvBuildImx500/lib/python3.11/site-packages/uni/common/logger.py:148]
2025-03-02 06:35:43,778 INFO : Converted successfully [/home/user/proj/imx500/venvBuildImx500/lib/python3.11/site-packages/uni/common/logger.py:148]
2025-03-02 06:35:44,436 INFO : CODE: [START] Starting SDSPconv
2025-03-02 06:36:03,565 INFO : ConvFe conversion finished successfully
2025-03-02 06:36:04,231 INFO : CBE component - DspConvParser has started conversion.
2025-03-02 06:36:04,446 INFO : Dsp-Dnn-Parser finished successfully !
2025-03-02 06:36:06,566 INFO : LogicModel generated successfully ! 
2025-03-02 06:36:06,567 INFO : LogicModel path is: /home/user/proj/imx500/packDemo1/convertOutput/tempConverterFm2Lm/qmodel
2025-03-02 06:36:06,569 INFO : DspConvParser runs: 2367 [msec]
2025-03-02 06:36:06,569 INFO : CBE component - DspConvParser finished conversion.
2025-03-02 06:36:29,315 INFO : Converter Backend successfully completed!
2025-03-02 06:36:29,315 INFO : Conversion time is 22.64 Seconds
2025-03-02 06:36:30,233 INFO : packer zip successfully generated under /home/user/proj/imx500/packDemo1/convertOutput/packerOut.zip
2025-03-02 06:36:30,261 INFO : CODE: [OUTPUT] Output is in /home/user/proj/imx500/packDemo1/convertOutput
2025-03-02 06:36:30,285 INFO : CODE: [DONE] Done (45s)

```

### convertOutput
```
convertOutput/
├── dnnParams.xml
├── packerOut.zip
├── qmodel_MemoryReport.json
└── qmodel.pbtxt

```


### packerOut.zip

```
├── cfgA.bin
├── cfgC.bin
├── dnnParams.xml
├── dnnParams.xsd
├── l2staticData.bin
├── manifest.json
├── sdpsA.bin
├── sdpsC.bin
└── verTable.txt

```

### qmodel_MemoryReport.json


```
{
  "Memory Report": {
    "Name": "qmodel",
    "Runtime Memory Physical Size": "1.60MB",
    "Model Memory Physical Size": "3.51MB",
    "Reserved Memory": "1.00KB",
    "Memory Usage": "5.11MB",
    "Total Memory Available On Chip": "8.00MB",
    "Memory Utilization": "64%",
    "Fit In Chip": true,
    "Input Persistent": true,
    "Networks": [
      {
        "Hash": "qmodel",
        "Name": "qmodel",
        "Runtime Memory Physical Size": "1.60MB",
        "Model Memory Physical Size": "3.51MB",
        "Input Persistence Cost": "151.00KB"
      }
    ]
  }
}

```

