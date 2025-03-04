# pack


```
root@user-Latitude-5440:/proj/demos/packDemo2# /usr/lib/imx500-tools/packager/imx500-package.sh -i packerOut.zip -o ./
Archive:  /proj/demos/packDemo2/packerOut.zip
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/sdpsA.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/sdpsC.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/cfgA.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/cfgC.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/dnnParams.xsd  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/dnnParams.xml  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/l2staticData.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/verTable.txt  
  inflating: /tmp/imx500-tools.yttMmCLyMC/packer_output/manifest.json  
/tmp/imx500-tools.yttMmCLyMC /proj/demos/packDemo2
/usr/lib/imx500-tools/postconverter/CustomNetwork/input_format.json File exists!!
/tmp/imx500-tools.yttMmCLyMC/packer_output /tmp/imx500-tools.yttMmCLyMC
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
   Name: yolov8n_imx
   Type: 
      Input Tensor0
         Name = Placeholder.input.uid1:0
         ID = 0
         L2 Offset = 260480
         Shift  = 0
         Scale  = 0.00390625
         Format  = UNSIGNED
         Persistency  = 0
         Num of Dimensions  = 3
         Dimension0 = (size/serOrder/padding)3/2/0
         Dimension1 = (size/serOrder/padding)640/1/0
         Dimension2 = (size/serOrder/padding)640/0/0
     Output Tensor1
         ID = 1
         L2 Offset = 281984
         Name = -83-/MultiClassNMS:0
         bitsPerElement = 8
         shift = 0
         scale = 0.00390625
         format = UNSIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
     Output Tensor2
         ID = 2
         L2 Offset = 280960
         Name = -84-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         format = SIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
     Output Tensor3
         ID = 3
         L2 Offset = 279936
         Name = -85-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         format = SIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)1/0/0
     Output Tensor0
         ID = 0
         L2 Offset = 260480
         Name = -86-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 0.03125
         format = SIGNED
         Num of Dimensions  = 2
         Dimension0 = (size/serOrder/padding)300/0/0
         Dimension1 = (size/serOrder/padding)4/1/0
================================
 L2 Memory Details 
Total Memory Size:8388480
Reserved Memory Size:1024
Runtime Memory Size:5523456
Coefficeints Memory Size:2604544
================================
dnn_params.bin generated!!
=======================
Creating AP Params from XML
Num of Networks = 1
================================
   ID: 0
   Name: yolov8n_imx
   Type: 
  Num of Input Tensors :1
      Input Tensor0
         Name = Placeholder.input.uid1:0
         ID = 0
         Num of Dimensions  = 3
         Dimension0 = (size/serOrder/padding)3/2/0
         Dimension1 = (size/serOrder/padding)640/1/0
         Dimension2 = (size/serOrder/padding)640/0/0
      Output Tensor1
         ID = 1
         Name = -83-/MultiClassNMS:0
         bitsPerElement = 8
         shift = 0
         scale = 0.00390625
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
      Output Tensor2
         ID = 2
         Name = -84-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
      Output Tensor3
         ID = 3
         Name = -85-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)1/0/0
      Output Tensor0
         ID = 0
         Name = -86-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 0.03125
         Num of Dimensions  = 2
         Dimension0 = (size/serOrder/padding)300/0/0
         Dimension1 = (size/serOrder/padding)4/1/0
ap_params.bin generated!!
AP Param size:604
filename: /usr/lib/imx500-tools/postconverter/CustomNetwork/input_format.json
InputFormatInfo[ ordinal=0, format=RGB]
networkInfoVersion:020400
tmp_kscale[0] =1.0
kscale[0] =1024
tmp_kshift[0] =0.0
kshift[0] =0
clip_min[0] =0clip_max[0] =255
tmp_kscale[1] =1.0
kscale[1] =1024
tmp_kshift[1] =0.0
kshift[1] =0
clip_min[1] =0clip_max[1] =255
tmp_kscale[2] =1.0
kscale[2] =1024
tmp_kshift[2] =0.0
kshift[2] =0
clip_min[2] =0clip_max[2] =255
Network Info generated!!
filename: manifest.json
dnnModelVersion = 0314150000000000
/tmp/imx500-tools.yttMmCLyMC
  adding: post_conv_output/ (stored 0%)
  adding: post_conv_output/l2staticData.bin (deflated 24%)
  adding: post_conv_output/ap_params.bin (deflated 53%)
  adding: post_conv_output/dnn_params.bin (deflated 51%)
  adding: post_conv_output/cfgA.bin (deflated 72%)
  adding: post_conv_output/cfgC.bin (stored 0%)
  adding: post_conv_output/sdpsC.bin (deflated 87%)
  adding: post_conv_output/network_info.txt (deflated 75%)
  adding: post_conv_output/sdpsA.bin (deflated 86%)
  adding: post_conv_output/deployManifest.json (deflated 65%)
post_conv_output.zip generated!!
Archive:  post_conv_output.zip
   creating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/l2staticData.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/ap_params.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/dnn_params.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/cfgA.bin  
 extracting: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/cfgC.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/sdpsC.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/network_info.txt  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/sdpsA.bin  
  inflating: /tmp/imx500-tools.yttMmCLyMC/CustomNetwork/post_conv_output/deployManifest.json  
/proj/demos/packDemo2
/tmp/imx500-tools.yttMmCLyMC/CustomNetwork /proj/demos/packDemo2
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
/proj/demos/packDemo2
Packaged model is in:
/proj/demos/packDemo2
```

## tree


```
|-- [2.8M]  network.rpk
|-- [2.0M]  packerOut.zip
```
