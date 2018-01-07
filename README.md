安装python 库
opencv >3.1 dlib=19.4

使用:

python face-dect.py -vp /path/to/video/xx.mp4

可选参数

-sf 2 , 跳跃检测，每隔2帧 检测一次，越大卡顿效果越明显

-s 0.5 取值范围 0～1,值越大，精度越高，速度越慢，值越小，精度越低，速度越快

