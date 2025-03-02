# pack

```
> /usr/lib/imx500-tools/packager/imx500-package.sh -i /proj/packDemo1/packerOut.zip  -o /proj/packDemo1


Archive:  /proj/packDemo1/packerOut.zip
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/sdpsA.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/sdpsC.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/cfgA.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/cfgC.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/dnnParams.xsd  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/dnnParams.xml  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/l2staticData.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/verTable.txt  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/packer_output/manifest.json  
/tmp/imx500-tools.ujmAHWvFh9 /proj/packDemo1
/usr/lib/imx500-tools/postconverter/CustomNetwork/input_format.json File exists!!
/tmp/imx500-tools.ujmAHWvFh9/packer_output /tmp/imx500-tools.ujmAHWvFh9
Check PackerOut Files
./sdpsA.bin File exists!!
./sdpsC.bin File exists!!
./cfgA.bin File exists!!
./cfgC.bin File exists!!
./dnnParams.xml File exists!!
./l2staticData.bin File exists!!
./manifest.json File exists!!
Check PackerOut Files Done!!
Creating DNN Params from XML
Num of Networks = 1
================================
   ID: 0
   Name: qmodel
   Type: 
      Input Tensor0
         Name = Placeholder.input.uid1:0
         ID = 0
         L2 Offset = 3033824
         Shift  = 0
         Scale  = 0.03125
         Format  = SIGNED
         Persistency  = 1
         Num of Dimensions  = 3
         Dimension0 = (size/serOrder/padding)3/2/0
         Dimension1 = (size/serOrder/padding)224/1/0
         Dimension2 = (size/serOrder/padding)224/0/0
     Output Tensor0
         ID = 0
         L2 Offset = 3189472
         Name = ifier_1/layer/Gemm:0
         bitsPerElement = 8
         shift = 0
         scale = 0.0625
         format = SIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)1000/0/0
================================
 L2 Memory Details 
Total Memory Size:8388480
Reserved Memory Size:1024
Runtime Memory Size:1674240
Coefficeints Memory Size:3680416
================================
dnn_params.bin generated!!
=======================
Creating AP Params from XML
Num of Networks = 1
================================
   ID: 0
   Name: qmodel
   Type: 
  Num of Input Tensors :1
      Input Tensor0
         Name = Placeholder.input.uid1:0
         ID = 0
         Num of Dimensions  = 3
         Dimension0 = (size/serOrder/padding)3/2/0
         Dimension1 = (size/serOrder/padding)224/1/0
         Dimension2 = (size/serOrder/padding)224/0/0
      Output Tensor0
         ID = 0
         Name = ifier_1/layer/Gemm:0
         bitsPerElement = 8
         shift = 0
         scale = 0.0625
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)1000/0/0
ap_params.bin generated!!
AP Param size:328
filename: /usr/lib/imx500-tools/postconverter/CustomNetwork/input_format.json
InputFormatInfo[ ordinal=0, format=RGB]
networkInfoVersion:020400
tmp_kscale[0] =1.0
kscale[0] =1024
tmp_kshift[0] =-128.0
kshift[0] =6144
clip_min[0] =384clip_max[0] =127
tmp_kscale[1] =1.0
kscale[1] =1024
tmp_kshift[1] =-128.0
kshift[1] =6144
clip_min[1] =384clip_max[1] =127
tmp_kscale[2] =1.0
kscale[2] =1024
tmp_kshift[2] =-128.0
kshift[2] =6144
clip_min[2] =384clip_max[2] =127
Network Info generated!!
filename: manifest.json
dnnModelVersion = 0314150000000000
/tmp/imx500-tools.ujmAHWvFh9
  adding: post_conv_output/ (stored 0%)
  adding: post_conv_output/l2staticData.bin (deflated 14%)
  adding: post_conv_output/ap_params.bin (deflated 43%)
  adding: post_conv_output/dnn_params.bin (deflated 42%)
  adding: post_conv_output/cfgA.bin (deflated 87%)
  adding: post_conv_output/cfgC.bin (deflated 85%)
  adding: post_conv_output/sdpsC.bin (deflated 87%)
  adding: post_conv_output/network_info.txt (deflated 70%)
  adding: post_conv_output/sdpsA.bin (deflated 85%)
  adding: post_conv_output/deployManifest.json (deflated 65%)
post_conv_output.zip generated!!
Archive:  post_conv_output.zip
   creating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/l2staticData.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/ap_params.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/dnn_params.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/cfgA.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/cfgC.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/sdpsC.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/network_info.txt  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/sdpsA.bin  
  inflating: /tmp/imx500-tools.ujmAHWvFh9/CustomNetwork/post_conv_output/deployManifest.json  
/proj/packDemo1
/tmp/imx500-tools.ujmAHWvFh9/CustomNetwork /proj/packDemo1
Starting...Please wait a few seconds.
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
[Converter Version] 031415
[Network ID] 000000
[Model Major Version] 00
[Model Minor Version] 00
[DNN_LOADER] set nw info from file 
/proj/packDemo1
Packaged model is in:
/proj/packDemo

```

## tree

```
|-- [3.8M]  network.rpk
|-- [3.1M]  packerOut.zip
```