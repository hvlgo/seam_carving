## 文件结构

* src
  * Seam_Carving.py
* bin
  * requirement.txt
  * readme.md
  * 1.png 2.png 3.png 4.png 5.png 6.png 7.png
  * out1.png out2.png out3.png out4.png out5.png out6.png out7.png
* report.pdf
* hw7.pdf

### 各个文件的作用

Seam_Carving.py 实现了Seam_Carving算法

使用方式为 `python Seam_Carving.py -i <path of input picture> -o <path of output picture> -r <ratio>`

其中 <path of input picture> 是必选参数，<path of output picture> 和 <ratio>是可选参数，默认为 `./output.png`  以及 `0.5`

例如 `python Seam_Carving.py -i 1.png -o out.png -r 0.8`将会将 1.png 使用 Seam_Carving 算法压缩宽和高为原来的0.8倍，输出 out.png

同时，由于图片较大时运行时间较长，所以让控制台输出了当前图片的尺寸以及最后总共用的时间

hw7.pdf 是证明题

report.pdf 是实验报告

requirement.txt 是依赖的库

1.png 2.png 3.png 4.png 5.png 6.png 7.png 是各个尺寸的压缩前的图片

out1.png out2.png out3.png out4.png out5.png out6.png out7.png是对应的采用0.5压缩倍率的压缩后的图片
