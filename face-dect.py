# coding=utf-8
# 这是使用dlib的人脸检测
import cv2
import dlib
import sys
import argparse

parser = argparse.ArgumentParser(description='face detection')
parser.add_argument('-vp','--video', default="",
                    help='path to video,example: -vp /home/uses/xx.mp4"')
parser.add_argument('-s','--scale',type=float, default=0.5,
                    help='resize the video,Range of value:[0,1]')
parser.add_argument('-sf','--skipFrame', default=2, type=int,
                    help='the number of skip frame')

global args
args = parser.parse_args()


def face_dect(video_path="qr.mp4",skip_frame=2,scale=0.5,sample=1,upsample_time=0):

    # 初始化dlib人脸检测器
    detector = dlib.get_frontal_face_detector()

    cv2.namedWindow("win",cv2.WINDOW_AUTOSIZE)
    cap=cv2.VideoCapture(video_path)
    i=0 #计数 帧率
    while cap.isOpened():
        i=i+1
        ret,cv_img=cap.read()
        if not (i % skip_frame==0):
            pass
        # OpenCV默认是读取为BGR图像，而dlib需要的是EGB图像，因此这一步转换不能少
        img_tmp = cv2.resize(cv_img, None, fx=scale, fy=scale, interpolation=sample) #INTER_LINEAR=1,INTER_CUBIC = 2

        img = cv2.cvtColor(img_tmp, cv2.COLOR_BGR2RGB)

        #检测人脸
        dets = detector(img,upsample_time)
        print("Number of faces detected: {}".format(len(dets)))
        for i, d in enumerate(dets):
            cv2.rectangle(cv_img,
                          (int(d.left()/scale),int(d.top()/scale)),
                               (int(d.right()/scale), int(d.bottom()/scale)),
                                (0, 255, 0),
                                1)
        cv2.imshow('win', cv_img)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    #1. video_path="qr.mp4"
    #2. skip_frame=2
    #3. scale=0.5
    #4. sample=1,
    #5. upsampe_time=0 人脸检测上采样次数
    #video_path="qr.mp4"
    #skip_frame1=5
    #scale1=0.8
    #sample1=1
    #upsample_time1=0 #人脸检测上采样次数

    if not args.video:
        print("please input video path (at least),example: -vp /home/uses/xx.mp4")
    else:
        face_dect(video_path=args.video,
                  skip_frame=args.skipFrame,
                  scale=args.scale)


