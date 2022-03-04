
MSC
-----
MSC系统是各控制边缘视频的控制台，该系统可以查看连接上的视频设备基本信息及控制视频流的推送，实现公网查看内网视频。系统后台采用python语言开发，前端界面使用vue开发。系统集成流媒体服务器，支持RTMP的视频流格式，部署后可向服务器推流和拉流。服务器收到推流消息和停止推流消息可配置接口地址接受消息。同时集成mqtt消息队列，内网服务器订阅队列可以实现内外网通信，方便控制内网设备。

项目集成：
-------
1、流媒体服务器srs（Simple RTMP Server)
2、消息队列mqtt



主要功能点：
-----------

1、按需推流，可指定摄像头的视频流推送地址，实现开始推流，结束推流，节省带宽流量
2、查看设备信息
3、查看流信息
4、查看边缘网关