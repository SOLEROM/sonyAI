# pack


on pi:

```
/usr/lib/imx500-tools/packager/imx500-package.sh -i packerOut.zip -o ./
Archive:  /home/user/packDemo3/packerOut.zip
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/sdpsA.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/sdpsC.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/cfgA.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/cfgC.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/dnnParams.xsd  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/dnnParams.xml  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/l2staticData.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/verTable.txt  
  inflating: /tmp/imx500-tools.QN6vncN3bj/packer_output/manifest.json  
/tmp/imx500-tools.QN6vncN3bj ~/packDemo3
/usr/lib/imx500-tools/postconverter/CustomNetwork/input_format.json File exists!!
/tmp/imx500-tools.QN6vncN3bj/packer_output /tmp/imx500-tools.QN6vncN3bj
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
   Name: yolov8n-face_imx
   Type: 
      Input Tensor0
         Name = Placeholder.input.uid1:0
         ID = 0
         L2 Offset = 347680
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
         L2 Offset = 351776
         Name = -87-/MultiClassNMS:0
         bitsPerElement = 8
         shift = 0
         scale = 0.00390625
         format = UNSIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
     Output Tensor2
         ID = 2
         L2 Offset = 352800
         Name = -88-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         format = SIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
     Output Tensor3
         ID = 3
         L2 Offset = 350752
         Name = -89-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         format = SIGNED
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)1/0/0
     Output Tensor0
         ID = 0
         L2 Offset = 354848
         Name = -90-/MultiClassNMS:0
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
Runtime Memory Size:5524480
Coefficeints Memory Size:2516320
================================
dnn_params.bin generated!!
=======================
Creating AP Params from XML
Num of Networks = 1
================================
   ID: 0
   Name: yolov8n-face_imx
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
         Name = -87-/MultiClassNMS:0
         bitsPerElement = 8
         shift = 0
         scale = 0.00390625
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
      Output Tensor2
         ID = 2
         Name = -88-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)300/0/0
      Output Tensor3
         ID = 3
         Name = -89-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 1.0
         Num of Dimensions  = 1
         Dimension0 = (size/serOrder/padding)1/0/0
      Output Tensor0
         ID = 0
         Name = -90-/MultiClassNMS:0
         bitsPerElement = 16
         shift = 0
         scale = 0.03125
         Num of Dimensions  = 2
         Dimension0 = (size/serOrder/padding)300/0/0
         Dimension1 = (size/serOrder/padding)4/1/0
ap_params.bin generated!!
AP Param size:608
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
/tmp/imx500-tools.QN6vncN3bj
  adding: post_conv_output/ (stored 0%)
  adding: post_conv_output/l2staticData.bin (deflated 18%)
  adding: post_conv_output/ap_params.bin (deflated 52%)
  adding: post_conv_output/dnn_params.bin (deflated 51%)
  adding: post_conv_output/cfgA.bin (deflated 84%)
  adding: post_conv_output/cfgC.bin (deflated 83%)
  adding: post_conv_output/sdpsC.bin (deflated 87%)
  adding: post_conv_output/network_info.txt (deflated 74%)
  adding: post_conv_output/sdpsA.bin (deflated 86%)
  adding: post_conv_output/deployManifest.json (deflated 65%)
post_conv_output.zip generated!!
Archive:  post_conv_output.zip
   creating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/l2staticData.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/ap_params.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/dnn_params.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/cfgA.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/cfgC.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/sdpsC.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/network_info.txt  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/sdpsA.bin  
  inflating: /tmp/imx500-tools.QN6vncN3bj/CustomNetwork/post_conv_output/deployManifest.json  
~/packDemo3
/tmp/imx500-tools.QN6vncN3bj/CustomNetwork ~/packDemo3
Starting...Please wait a few seconds.
[Converter Version] 031415
[Network ID] 000000
[Model Major Version] 00
[Model Minor Version] 00
[DNN_LOADER] set nw info from file 
~/packDemo3
Packaged model is in:
/home/user/packDemo3


```
