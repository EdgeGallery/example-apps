# SRS

![](http://ossrs.net/gif/v1/sls.gif?site=github.com&path=/srs/srs3)
[![](https://circleci.com/gh/ossrs/srs/tree/3.0release.svg?style=svg&circle-token=1ef1d5b5b0cde6c8c282ed856a18199f9e8f85a9)](https://circleci.com/gh/ossrs/srs/tree/3.0release)
[![](https://codecov.io/gh/ossrs/srs/branch/3.0release/graph/badge.svg)](https://codecov.io/gh/ossrs/srs/branch/3.0release)
[![](https://cloud.githubusercontent.com/assets/2777660/22814959/c51cbe72-ef92-11e6-81cc-32b657b285d5.png)](https://github.com/ossrs/srs/wiki/v1_CN_Contact#wechat)

SRS/3.0，[OuXuli][release3]，是一个流媒体集群，支持RTMP/HLS/WebRTC/SRT/GB28181，高效、稳定、易用，简单而快乐。<br/>
SRS is a RTMP/HLS/WebRTC/SRT/GB28181 streaming cluster, high efficiency, stable and simple.

> Remark: Although SRS is licenced under [MIT][LICENSE], but there are some depended libraries which are distributed using their own licenses, please read [License Mixing][LicenseMixing].

<a name="product"></a>
## Usage

**>>> Step 1:** Get SRS.

```
git clone https://gitee.com/winlinvip/srs.oschina.git srs &&
cd srs/trunk && git remote set-url origin https://github.com/ossrs/srs.git && git pull
```

> Note: We use [mirrors(gitee)](#mirrors) here, but it's also ok to directly clone by `git clone https://github.com/ossrs/srs.git && cd srs/trunk`

**>>> Step 2:** Build SRS.

```
./configure && make
```

> Remark: Recommend to use Centos7 64bits, please read wiki([CN][v3_CN_Build],[EN][v3_EN_Build]).

> Note: You can also build SRS in docker, please read [docker][docker-dev].

**>>> Step 3:** Run SRS 

```
./objs/srs -c conf/srs.conf
```

**>>> Whatever**, you can also directly run SRS in [docker][docker-srs3]:

```
docker run -p 1935:1935 -p 1985:1985 -p 8080:8080 \
    registry.cn-hangzhou.aliyuncs.com/ossrs/srs:3
```

> Note: Again, we use [ACR](https://cr.console.aliyun.com/) here, you can directly run in docker hub by `docker run -p 1935:1935 -p 1985:1985 -p 8080:8080 ossrs/srs:3`

**>>> From here,** strongly recommend to read bellow wikis:

* Usage: How to delivery RTMP?([CN][v1_CN_SampleRTMP], [EN][v1_EN_SampleRTMP])
* Usage: How to delivery RTMP Edge Cluster?([CN][v3_CN_SampleRTMPCluster], [EN][v3_EN_SampleRTMPCluster])
* Usage: How to create a RTMP Origin Cluster?([CN][v3_CN_SampleOriginCluster], [EN][v3_EN_SampleOriginCluster])
* Usage: How to delivery HTTP FLV Live Streaming?([CN][v3_CN_SampleHttpFlv], [EN][v3_EN_SampleHttpFlv])
* Usage: How to delivery HTTP FLV Live Streaming Cluster?([CN][v3_CN_SampleHttpFlvCluster], [EN][v3_EN_SampleHttpFlvCluster])
* Usage: How to delivery HLS?([CN][v3_CN_SampleHLS], [EN][v3_EN_SampleHLS])
* Usage: How to delivery HLS for other codec?([CN][v3_CN_SampleTranscode2HLS], [EN][v3_EN_SampleTranscode2HLS])
* Usage: How to transode RTMP stream by FFMPEG?([CN][v2_CN_SampleFFMPEG], [EN][v2_EN_SampleFFMPEG])
* Usage: How to forward stream to other servers?([CN][v3_CN_SampleForward], [EN][v3_EN_SampleForward])
* Usage: How to deploy in low lantency mode?([CN][v3_CN_SampleRealtime], [EN][v3_EN_SampleRealtime])
* Usage: How to ingest file/stream/device to RTMP?([CN][v1_CN_SampleIngest], [EN][v1_EN_SampleIngest])
* Usage: How to delivery HLS by SRS HTTP server?([CN][v3_CN_SampleHTTP], [EN][v3_EN_SampleHTTP])
* Usage: How to publish h.264 raw stream as RTMP? ([CN][v3_CN_SrsLibrtmp2], [EN][v3_EN_SrsLibrtmp2])
* Usage: How to improve edge performance by multiple CPUs? ([CN][v3_CN_REUSEPORT], [EN][v3_EN_REUSEPORT])
* Usage: Why choose SRS? About the milestone and product plan? ([CN][v1_CN_Product], [EN][v1_EN_Product])
* Usage: How to file bug or chat with us? ([CN][v1_CN_Contact], [EN][v1_EN_Contact])

<a name="srs-30-wiki"></a>
## Wiki

Please select according to languages:

* [SRS 3.0 English Wiki][v3_EN_Home]
* [SRS 3.0 Chinese Wiki][v3_CN_Home]

For previous versions, please read:

* [SRS 2.0 English Wiki][v2_EN_Home]
* [SRS 2.0 Chinese Wiki][v2_CN_Home]
* [SRS 1.0 English Wiki][v1_EN_Home]
* [SRS 1.0 Chinese Wiki][v1_CN_Home]

## Features

- [x] Using coroutine by ST, it's really simple and stupid enough.
- [x] Support cluster which consists of origin ([CN][v1_CN_DeliveryRTMP],[EN][v1_EN_DeliveryRTMP]) and edge([CN][v3_CN_Edge], [EN][v3_EN_Edge]) server and uses RTMP as default transport protocol.
- [x] Origin server supports remuxing RTMP to HTTP-FLV([CN][v3_CN_SampleHttpFlv], [EN][v3_EN_SampleHttpFlv]) and HLS([CN][v3_CN_DeliveryHLS], [EN][v3_EN_DeliveryHLS]).
- [x] Edge server supports remuxing RTMP to HTTP-FLV([CN][v3_CN_SampleHttpFlv], [EN][v3_EN_SampleHttpFlv]). As for HLS([CN][v3_CN_DeliveryHLS], [EN][v3_EN_DeliveryHLS]) edge server, recomment to use HTTP edge server, such as [NGINX](http://nginx.org/).
- [x] Support HLS with audio-only([CN][v3_CN_DeliveryHLS2], [EN][v3_EN_DeliveryHLS2]), which need to build the timestamp from AAC samples, so we enhanced it please read [#547][bug #547].
- [x] Support HLS with mp3(h.264+mp3) audio codec, please read [bug #301][bug #301].
- [x] Support remuxing RTMP to http FLV/MP3/AAC/TS live streaming, please read wiki([CN][v2_CN_DeliveryHttpStream], [EN][v2_CN_DeliveryHttpStream]).
- [x] Support ingesting([CN][v1_CN_Ingest], [EN][v1_EN_Ingest]) other protocols to SRS by FFMPEG.
- [x] Support RTMP long time(>4.6hours) publishing/playing, with the timestamp corrected.
- [x] Support publishing h264 raw stream([CN][v3_CN_SrsLibrtmp2], [EN][v3_EN_SrsLibrtmp2]) by srs-librtmp([CN][v3_CN_SrsLibrtmp], [EN][v3_EN_SrsLibrtmp]).
- [x] Support publishing aac adts raw stream([CN][v3_CN_SrsLibrtmp3], [EN][v3_EN_SrsLibrtmp3]) by srs-librtmp([CN][v3_CN_SrsLibrtmp], [EN][v3_EN_SrsLibrtmp]).
- [x] Support native HTTP server([CN][v3_CN_SampleHTTP], [EN][v3_EN_SampleHTTP]) for http api and http live streaming.
- [x] Support HTTP CORS for js in http api and http live streaming.
- [x] Support HTTP API([CN][v3_CN_HTTPApi], [EN][v3_EN_HTTPApi]) for system management.
- [x] Support HTTP callback([CN][v3_CN_HTTPCallback], [EN][v3_EN_HTTPCallback]) for authentication and integration.
- [x] Support DVR([CN][v3_CN_DVR], [EN][v3_EN_DVR]) to record live streaming to FLV file.
- [x] Support DVR control module like NGINX-RTMP, please read [#459][bug #459].
- [x] Support EXEC like NGINX-RTMP, please read [bug #367][bug #367].
- [x] Support security strategy including allow/deny publish/play IP([CN][v2_CN_Security], [EN][v2_EN_Security]).
- [x] Support low latency(0.1s+) transport model, please read [bug #257][bug #257].
- [x] Support gop-cache([CN][v3_CN_LowLatency2], [EN][v3_EN_LowLatency2]) for player fast startup.
- [x] Support Vhost([CN][v1_CN_RtmpUrlVhost], [EN][v1_EN_RtmpUrlVhost]) and \_\_defaultVhost\_\_.
- [x] Support reloading([CN][v1_CN_Reload], [EN][v1_EN_Reload]) to apply changes of config.
- [x] Support listening at multiple ports.
- [x] Support forwarding([CN][v3_CN_Forward], [EN][v3_EN_Forward]) from master to slave server.
- [x] Support transcoding([CN][v3_CN_FFMPEG], [EN][v3_EN_FFMPEG]) live streaming by FFMPEG.
- [x] All wikis are writen in [Chinese][v3_CN_Home] and [English][v3_EN_Home]. 
- [x] Enhanced json, replace NXJSON(LGPL) with json-parser(BSD), read [#904][bug #904].
- [x] Support valgrind and latest ARM by patching ST, read [ST#1](https://github.com/ossrs/state-threads/issues/1) and [ST#2](https://github.com/ossrs/state-threads/issues/2).
- [x] Support tracable and session-based log([CN][v1_CN_SrsLog], [EN][v1_EN_SrsLog]).
- [x] High concurrency and performance([CN][v1_CN_Performance], [EN][v1_EN_Performance]), 6000+ connections(200kbps), CPU 82%, 203MB.
- [x] Enhanced complex error code with description and stack, read [#913][bug #913].
- [x] Enhanced RTMP url  which supports vhost in stream, read [#1059][bug #1059].
- [x] Support origin cluster, please read [#464][bug #464], [RTMP 302][bug #92].
- [x] Support listen at IPv4 and IPv6, read [#460][bug #460].
- [x] Support SO_REUSEPORT, to improve edge server performance, read [#775][bug #775].
- [x] Improve test coverage for core/kernel/protocol/service.
- [x] [Experimental] Support docker by [srs-docker](https://github.com/ossrs/srs-docker).
- [x] [Experimental] Support DVR in MP4 format, read [#738][bug #738].
- [x] [Experimental] Support MPEG-DASH, the future live streaming protocol, read [#299][bug #299].
- [x] [Experimental] Support pushing MPEG-TS over UDP, please read [bug #250][bug #250].
- [x] [Experimental] Support pushing RTSP, please read [bug #133][bug #133].
- [x] [Experimental] Support pushing FLV over HTTP POST, please read [wiki]([CN][v2_CN_Streamer2], [EN][v2_EN_Streamer2]).
- [x] [Experimental] Support multiple processes by [dolphin][srs-dolphin] or [oryx][oryx].
- [x] [Experimental] Support a simple [mgmt console][console], please read [srs-ngb][srs-ngb].
- [x] [Experimental] Support RTMP client library: srs-librtmp([CN][v3_CN_SrsLibrtmp], [EN][v3_EN_SrsLibrtmp])
- [x] [Experimental] Support HTTP RAW API, please read [#459][bug #459], [#470][bug #470], [#319][bug #319].
- [x] [Deprecated] Support Adobe HDS(f4m), please read wiki([CN][v2_CN_DeliveryHDS], [EN][v2_EN_DeliveryHDS]) and [#1535][bug #1535].
- [x] [Deprecated] Support bandwidth testing([CN][v1_CN_BandwidthTestTool], [EN][v1_EN_BandwidthTestTool]), please read [#1535][bug #1535].
- [x] [Deprecated] Support Adobe FMS/AMS token traverse([CN][v3_CN_DRM2], [EN][v3_EN_DRM2]) authentication, please read [#1535][bug #1535].
- [ ] Enhanced forwarding with vhost and variables.
- [ ] Support source cleanup for idle streams.
- [ ] Support H.265 by pushing H.265 over RTMP, deliverying in HLS, read [#465][bug #465].
- [ ] Support HLS+, the HLS edge server, please read [#466][bug #466] and [#468][bug #468].
- [ ] Support UDP protocol such as QUIC or KCP in cluster.
- [ ] Support H.264+Opus codec for WebRTC.
- [ ] Support publishing stream by WebRTC.
- [ ] Support playing stream by WebRTC.

> Remark: About the milestone and product plan, please read ([CN][v1_CN_Product], [EN][v1_EN_Product]) wiki.

<a name="history"></a>
<a name="change-logs"></a>

## V3 changes

* <strong>v3.0, 2020-06-27, [3.0 release0(3.0.141)][r3.0r0] released. 122674 lines.</strong>
* v3.0, 2020-03-30, For [#1672][bug #1672], fix dvr close file failed bug. 3.0.140
* <strong>v3.0, 2020-03-29, [3.0 beta4(3.0.139)][r3.0b4] released. 122674 lines.</strong>
* v3.0, 2020-03-28, Support multiple OS/Platform build cache. 3.0.139
* v3.0, 2020-03-28, For [#1250][bug #1250], support macOS, OSX, MacbookPro, Apple Darwin. 3.0.138
* v3.0, 2020-03-21, For [#1629][bug #1629], fix kickoff FLV client bug. 3.0.137
* v3.0, 2020-03-21, For [#1619][bug #1619], configure without utest by default. 3.0.136
* v3.0, 2020-03-21, For [#1651][bug #1651], fix return pnwrite of srs_write_large_iovs. 3.0.135
* <strong>v3.0, 2020-03-18, [3.0 beta3(3.0.134)][r3.0b3] released. 122509 lines.</strong>
* v3.0, 2020-03-12, For [#1635][bug #1635], inotify watch ConfigMap for reload. 3.0.134
* v3.0, 2020-03-12, For [#1635][bug #1635], support auto reaload config by inotify. 3.0.129
* v3.0, 2020-03-12, For [#1630][bug #1630], disable cache for stream changing, and drop dup header. 3.0.128
* v3.0, 2020-03-12, For [#1594][bug #1594], detect and disable daemon for docker. 3.0.127
* v3.0, 2020-03-12, For [#1634][bug #1634], always check status in thread loop. 3.0.126
* v3.0, 2020-03-11, For [#1634][bug #1634], refactor output with datetime for ingest/encoder/exec. 3.0.125
* v3.0, 2020-03-11, For [#1634][bug #1634], fix quit by accident SIGTERM while killing FFMPEG. 3.0.124
* <strong>v3.0, 2020-03-05, [3.0 beta2(3.0.123)][r3.0b2] released. 122170 lines.</strong>
* v3.0, 2020-02-21, For [#1598][bug #1598], support SLB health checking by TCP. 3.0.123
* v3.0, 2020-02-21, Fix bug for librtmp client ipv4/ipv6 socket. 3.0.122
* v3.0, 2020-02-18, For [#1579][bug #1579], support start/final wait for gracefully quit. 3.0.121
* v3.0, 2020-02-18, For [#1579][bug #1579], support force gracefully quit. 3.0.120
* v3.0, 2020-02-18, For [#1579][bug #1579], support gracefully quit. 3.0.119
* v3.0, 2020-02-17, For [#1601][bug #1601], flush async on_dvr/on_hls events before stop. 3.0.118
* <strong>v3.0, 2020-02-14, [3.0 beta1(3.0.117)][r3.0b1] released. 121964 lines.</strong>
* v3.0, 2020-02-14, For [#1595][bug #1595], migrating streaming from ossrs.net to r.ossrs.net. 3.0.117
* v3.0, 2020-02-05, For [#665][bug #665], fix HTTP-FLV reloading bug. 3.0.116
* v3.0, 2020-02-05, For [#1592][bug #1592], fix terminal echo off by redirect process stdin. 3.0.115
* v3.0, 2020-02-04, For [#1186][bug #1186], refactor security check. 3.0.114
* v3.0, 2020-02-04, Fix [#939][bug #939], response right A/V flag in FLV header. 3.0.113
* v3.0, 2020-02-04, For [#939][bug #939], always enable fast FLV streaming.
* <strong>v3.0, 2020-02-02, [3.0 beta0(3.0.112)][r3.0b0] released. 121709 lines.</strong>
* v3.0, 2020-01-29, Support isolate version file. 3.0.112
* v3.0, 2020-01-29, Fix [#1206][bug #1206], dispose ingester while server quiting. 3.0.111
* v3.0, 2020-01-28, Fix [#1230][bug #1230], racing condition in source fetch or create. 3.0.110
* v3.0, 2020-01-27, Fix [#1303][bug #1303], do not dispatch previous meta when not publishing. 3.0.109
* v3.0, 2020-01-26, Allow use libst.so for ST is MPL license.
* v3.0, 2020-01-26, Fix [#607][bug #607], set RTMP identifying recursive depth to 3.
* v3.0, 2020-01-25, Fix [#878][bug #878], remove deprecated #EXT-X-ALLOW-CACHE for HLS. 3.0.108
* v3.0, 2020-01-25, Fix [#703][bug #703], drop video data util sps/pps. 3.0.107
* v3.0, 2020-01-25, Fix [#1108][bug #1108], reap DVR tmp file when unpublish. 3.0.106
* <strong>v3.0, 2020-01-21, [3.0 alpha9(3.0.105)][r3.0a9] released. 121577 lines.</strong>
* v3.0, 2020-01-21, Fix [#1221][bug #1221], remove complex configure options. 3.0.104
* v3.0, 2020-01-21, Fix [#1547][bug #1547], support crossbuild for ARM/MIPS.
* v3.0, 2020-01-21, For [#1547][bug #1547], support setting cc/cxx/ar/ld/randlib tools. 3.0.103
* v3.0, 2020-01-19, For [#1580][bug #1580], fix cid range problem. 3.0.102
* v3.0, 2020-01-19, For [#1070][bug #1070], define FLV CodecID for [AV1][bug #1070] and [opus][bug #307]. 3.0.101
* v3.0, 2020-01-16, For [#1575][bug #1575], correct RTMP redirect as tcUrl, add redirect2 as RTMP URL. 3.0.100
* v3.0, 2020-01-15, For [#1509][bug #1509], decrease the fast vector init size from 64KB to 64B. 3.0.99
* v3.0, 2020-01-15, For [#1509][bug #1509], release coroutine when source is idle. 3.0.98
* <strong>v3.0, 2020-01-10, [3.0 alpha8(3.0.97)][r3.0a8] released. 121555 lines.</strong>
* v3.0, 2020-01-09, For [#1042][bug #1042], improve test coverage for service. 3.0.97
* v3.0, 2020-01-08, Merge [#1554][bug #1554], support logrotate copytruncate. 3.0.96
* v3.0, 2020-01-05, Always use string instance to avoid crash risk. 3.0.95
* v3.0, 2020-01-05, For [#460][bug #460], fix ipv6 hostport parsing bug. 3.0.94
* v3.0, 2020-01-05, For [#460][bug #460], fix ipv6 intranet address filter bug. 3.0.93
* v3.0, 2020-01-05, For [#1543][bug #1543], use getpeername to retrieve client ip. 3.0.92
* v3.0, 2020-01-02, For [#1042][bug #1042], improve test coverage for config. 3.0.91
* v3.0, 2019-12-30, Fix mp4 security issue, check buffer when required size is variable.
* <strong>v3.0, 2019-12-29, [3.0 alpha7(3.0.90)][r3.0a7] released. 116356 lines.</strong>
* v3.0, 2019-12-29, For [#1255][bug #1255], support vhost/domain in query string for HTTP streaming. 3.0.90
* v3.0, 2019-12-29, For [#299][bug #299], increase dash segment size for avsync issue. 3.0.89
* v3.0, 2019-12-27, For [#299][bug #299], fix some bugs in dash, it works now. 3.0.88
* v3.0, 2019-12-27, For [#1544][bug #1544], fix memory leaking for complex error. 3.0.87
* v3.0, 2019-12-27, Add links for flv.js, hls.js and dash.js.
* v3.0, 2019-12-26, For [#1105][bug #1105], http server support mp4 range.
* v3.0, 2019-12-26, For [#1105][bug #1105], dvr mp4 supports playing on Chrome/Safari/Firefox. 3.0.86
* <strong>v3.0, 2019-12-26, [3.0 alpha6(3.0.85)][r3.0a6] released. 116056 lines.</strong>
* v3.0, 2019-12-26, For [#1488][bug #1488], pass client ip to http callback. 3.0.85
* v3.0, 2019-12-25, For [#1537][bug #1537], [#1282][bug #1282], support aarch64 for armv8. 3.0.84
* v3.0, 2019-12-25, For [#1538][bug #1538], fresh chunk allow fmt=0 or fmt=1. 3.0.83
* v3.0, 2019-12-25, Remove FFMPEG and NGINX, please use [srs-docker](https://github.com/ossrs/srs-docker) instead. 3.0.82
* v3.0, 2019-12-25, For [#1537][bug #1537], remove cross-build, not used patches, directly build st.
* v3.0, 2019-12-24, For [#1508][bug #1508], support chunk length and content in multiple parts.
* v3.0, 2019-12-23, Merge SRS2 for running srs-librtmp on Windows. 3.0.80
* v3.0, 2019-12-23, For [#1535][bug #1535], deprecate Adobe FMS/AMS edge token traversing([CN][v3_CN_DRM2], [EN][v3_EN_DRM2]) authentication. 3.0.79
* v3.0, 2019-12-23, For [#1535][bug #1535], deprecate BWT(bandwidth testing)([CN][v1_CN_BandwidthTestTool], [EN][v1_EN_BandwidthTestTool]). 3.0.78
* v3.0, 2019-12-23, For [#1535][bug #1535], deprecate Adobe HDS(f4m)([CN][v2_CN_DeliveryHDS], [EN][v2_EN_DeliveryHDS]). 3.0.77
* v3.0, 2019-12-20, Fix [#1508][bug #1508], http-client support read chunked response. 3.0.76
* v3.0, 2019-12-20, For [#1508][bug #1508], refactor srs_is_digital, support all zeros.
* <strong>v3.0, 2019-12-19, [3.0 alpha5(3.0.75)][r3.0a5] released. 115362 lines.</strong>
* v3.0, 2019-12-19, Refine the RTMP iovs cache increasing to much faster.
* v3.0, 2019-12-19, Fix [#1524][bug #1524], memory leak for amf0 strict array. 3.0.75
* v3.0, 2019-12-19, Fix random build failed bug for modules.
* v3.0, 2019-12-19, Fix [#1520][bug #1520] and [#1223][bug #1223], bug for origin cluster 3+ servers. 3.0.74
* v3.0, 2019-12-18, For [#1042][bug #1042], add test for RAW AVC protocol.
* v3.0, 2019-12-18, Detect whether flash enabled for srs-player. 3.0.73
* v3.0, 2019-12-17, Fix HTTP CORS bug when sending response for OPTIONS. 3.0.72
* v3.0, 2019-12-17, Enhance HTTP response write for final_request.
* v3.0, 2019-12-17, Refactor HTTP stream to disconnect client when unpublish.
* v3.0, 2019-12-17, Fix HTTP-FLV and VOD-FLV conflicting bug.
* v3.0, 2019-12-17, Refactor HttpResponseWriter.write, default to single text mode.
* v3.0, 2019-12-16, For [#1042][bug #1042], add test for HTTP protocol.
* <strong>v3.0, 2019-12-13, [3.0 alpha4(3.0.71)][r3.0a4] released. 112928 lines.</strong>
* v3.0, 2019-12-12, For [#547][bug #547], [#1506][bug #1506], default hls_dts_directly to on. 3.0.71
* v3.0, 2019-12-12, SrsPacket supports converting to message, so can be sent by one API.
* v3.0, 2019-12-11, For [#1042][bug #1042], cover RTMP client/server protocol.
* v3.0, 2019-12-11, Fix [#1445][bug #1445], limit the createStream recursive depth. 3.0.70
* v3.0, 2019-12-11, For [#1042][bug #1042], cover RTMP handshake protocol.
* v3.0, 2019-12-11, Fix [#1229][bug #1229], fix the security risk in logger. 3.0.69
* v3.0, 2019-12-11, For [#1229][bug #1229], fix the security risk in HDS. 3.0.69
* v3.0, 2019-12-05, Fix [#1506][bug #1506], support directly turn FLV timestamp to TS DTS. 3.0.68
* <strong>v3.0, 2019-11-30, [3.0 alpha3(3.0.67)][r3.0a3] released. 110864 lines.</strong>
* v3.0, 2019-12-01, Fix [#1501][bug #1501], use request coworker for origin cluster. 3.0.67
* <strong>v3.0, 2019-11-30, [3.0 alpha2(3.0.66)][r3.0a2] released. 110831 lines.</strong>
* v3.0, 2019-11-30, Fix [#1501][bug #1501], use request coworker for origin cluster. 3.0.66
* v3.0, 2019-11-30, Random tid for docker. 3.0.65
* v3.0, 2019-11-30, Refine debug info for edge. 3.0.64
* v3.0, 2019-10-30, Cover protocol stack RTMP. 3.0.63
* v3.0, 2019-10-23, Cover JSON codec. 3.0.62
* v3.0, 2019-10-13, Use http://ossrs.net as homepage.
* v3.0, 2019-10-10, Cover AMF0 codec. 3.0.61
* <strong>v3.0, 2019-10-07, [3.0 alpha1(3.0.60)][r3.0a1] released. 107962 lines.</strong>
* v3.0, 2019-10-06, Support log rotate by init.d command. 3.0.60
* v3.0, 2019-10-06, We prefer ipv4, only use ipv6 if ipv4 is disabled. 3.0.59
* v3.0, 2019-10-05, Support systemctl service for CentOS7. 3.0.58
* v3.0, 2019-10-04, Disable SO_REUSEPORT if not supported. 3.0.57
* <strong>v3.0, 2019-10-04, [3.0 alpha0(3.0.56)][r3.0a0] released. 107946 lines.</strong>
* v3.0, 2019-10-04, Support go-oryx rtmplb with [proxy protocol](https://github.com/ossrs/go-oryx/wiki/RtmpProxy). 3.0.56
* v3.0, 2019-10-03, Fix [#775][bug #775], Support SO_REUSEPORT to improve edge performance. 3.0.54
* v3.0, 2019-10-03, For [#467][bug #467], Remove KAFKA producer. 3.0.53
* v3.0, 2019-05-14, Covert Kernel File reader/writer. 3.0.52
* v3.0, 2019-04-30, Refine typo in files. 3.0.51
* v3.0, 2019-04-25, Upgrade http-parser from 2.1 to 2.9.2 and cover it. 3.0.50
* v3.0, 2019-04-22, Refine in time unit. 3.0.49
* v3.0, 2019-04-07, Cover ST Coroutine and time unit. 3.0.48
* v3.0, 2019-04-06, Merge [#1304][bug #1304], Fix ST coroutine pull error. 3.0.47
* v3.0, 2019-04-05, Merge [#1339][bug #1339], Support HTTP-FLV params. 3.0.46
* v3.0, 2018-11-11, Merge [#1261][bug #1261], Support `_definst_` for Wowza. 3.0.44
* v3.0, 2018-08-26, SRS [console](https://github.com/ossrs/srs-ngb) support both [Chinese](http://ossrs.net:1985/console/ng_index.html) and [English](http://ossrs.net:1985/console/en_index.html).
* v3.0, 2018-08-25, Fix [#1093][bug #1093], Support HLS encryption. 3.0.42
* v3.0, 2018-08-25, Fix [#1051][bug #1051], Drop ts when republishing stream. 3.0.41
* v3.0, 2018-08-12, For [#1202][bug #1202], Support edge/forward to Aliyun CDN. 3.0.40
* v3.0, 2018-08-11, For [#910][bug #910], Support HTTP FLV with HTTP callback. 3.0.39
* v3.0, 2018-08-05, Refine HTTP-FLV latency, support realtime mode.3.0.38
* v3.0, 2018-08-05, Fix [#1087][bug #1087], Ignore iface without address. 3.0.37
* v3.0, 2018-08-04, For [#1110][bug #1110], Support params in http callback. 3.0.36
* v3.0, 2018-08-02, Always use vhost in stream query, the unify uri. 3.0.35
* v3.0, 2018-08-02, For [#1031][bug #1031], SRS edge support douyu.com. 3.0.34
* v3.0, 2018-07-22, Replace hex to string to match MIT license. 3.0.33
* v3.0, 2018-07-22, Replace base64 to match MIT license. 3.0.32
* v3.0, 2018-07-22, Replace crc32 IEEE and MPEG by pycrc to match MIT license. 3.0.31
* v3.0, 2018-07-21, Replace crc32 IEEE by golang to match MIT license. 3.0.30
* v3.0, 2018-02-16, Fix [#464][bug #464], support RTMP origin cluster. 3.0.29
* v3.0, 2018-02-13, Fix [#1057][bug #1057], switch to simple handshake. 3.0.28
* v3.0, 2018-02-13, Fix [#1059][bug #1059], merge from 2.0, supports url with vhost in stream. 3.0.27
* v3.0, 2018-01-01, Fix [#913][bug #913], support complex error. 3.0.26
* v3.0, 2017-06-04, Fix [#299][bug #299], support experimental MPEG-DASH. 3.0.25
* v3.0, 2017-05-30, Fix [#821][bug #821], support MP4 file parser. 3.0.24
* v3.0, 2017-05-30, Fix [#904][bug #904], replace NXJSON(LGPL) with json-parser(BSD). 3.0.23
* v3.0, 2017-04-16, Fix [#547][bug #547], support HLS audio in TS. 3.0.22
* v3.0, 2017-03-26, Fix [#820][bug #820], extract service for modules. 3.0.21
* v3.0, 2017-03-02, Fix [#786][bug #786], simply don't reuse object. 3.0.20
* v3.0, 2017-03-01, For [#110][bug #110], refine thread object. 3.0.19
* v3.0, 2017-02-12, Fix [#301][bug #301], user must config the codec in right way for HLS. 3.0.18
* v3.0, 2017-02-07, fix [#738][bug #738], support DVR general mp4. 3.0.17
* v3.0, 2017-01-19, for [#742][bug #742], refine source, meta and origin hub. 3.0.16
* v3.0, 2017-01-17, for [#742][bug #742], refine source, timeout, live cycle. 3.0.15
* v3.0, 2017-01-11, fix [#735][bug #735], config transform refer_publish invalid. 3.0.14
* v3.0, 2017-01-06, for [#730][bug #730], support config in/out ack size. 3.0.13
* v3.0, 2017-01-06, for [#711][bug #711], support perfile for transcode. 3.0.12
* v3.0, 2017-01-05, Fix [#727][bug #727], patch ST for valgrind and ARM. 3.0.11
* v3.0, 2017-01-05, for [#324][bug #324], always enable hstrs. 3.0.10
* v3.0, 2016-12-15, fix [#717][bug #717], [#691][bug #691], http api/static/stream support cors. 3.0.9
* v3.0, 2016-12-08, Fix [#105][bug #105], support log rotate signal SIGUSR1. 3.0.8
* v3.0, 2016-12-07, fix typo and refine grammar. 3.0.7
* v3.0, 2015-10-20, fix [#502][bug #502], support snapshot with http-callback or transcoder. 3.0.5
* v3.0, 2015-09-19, support amf0 and json to convert with each other.
* v3.0, 2015-09-19, json objects support dumps to string.
* v3.0, 2015-09-14, fix [#459][bug #459], support dvr raw api. 3.0.4
* v3.0, 2015-09-14, fix [#459][bug #459], dvr support apply filter for ng-control dvr module.
* v3.0, 2015-09-14, fix [#319][bug #319], http raw api support update global and vhost. 3.0.3
* v3.0, 2015-08-31, fix [#319][bug #319], http raw api support query global and vhost.
* v3.0, 2015-08-28, fix [#471][bug #471], api response the width and height. 3.0.2
* v3.0, 2015-08-25, fix [#367][bug #367], support nginx-rtmp exec. 3.0.1

## V2 changes

* <strong>v2.0, 2020-01-25, [2.0 release8(2.0.272)][r2.0r8] released. 87292 lines.</strong>
* v2.0, 2020-01-08, Merge [#1554][bug #1554], support logrotate copytruncate. 2.0.272
* v2.0, 2020-01-05, Merge [#1551][bug #1551], fix memory leak in RTSP stack. 2.0.270
* v2.0, 2019-12-26, For [#1488][bug #1488], pass client ip to http callback. 2.0.269
* v2.0, 2019-12-23, Fix [srs-librtmp #22](https://github.com/ossrs/srs-librtmp/issues/22), parse vhost splited by single seperator. 2.0.268
* v2.0, 2019-12-23, Fix [srs-librtmp #25](https://github.com/ossrs/srs-librtmp/issues/25), build srs-librtmp on windows. 2.0.267
* v2.0, 2019-12-13, Support openssl versions greater than 1.1.0. 2.0.266
* <strong>v2.0, 2019-11-29, [2.0 release7(2.0.265)][r2.0r7] released. 86994 lines.</strong>
* v2.0, 2019-11-29, For [srs-docker](https://github.com/ossrs/srs-docker/tree/master/2.0), install Cherrypy without sudo. 2.0.265
* v2.0, 2019-04-06, For [#1304][bug #1304], Default HSTRS to on. 2.0.264
* <strong>v2.0, 2019-04-05, [2.0 release6(2.0.263)][r2.0r6] released. 86994 lines.</strong>
* v2.0, 2019-04-05, Merge [#1312][bug #1312], Fix GCC7 build error, this statement may fall through. 2.0.263
* v2.0, 2019-04-05, Merge [#1339][bug #1339], Support HTTP-FLV params. 2.0.262
* v2.0, 2018-12-01, Merge [#1274][bug #1274], Upgrade to FFMPEG 4.1 and X264 157. 2.0.261
* v2.0, 2018-11-11, Merge [#1261][bug #1261], Support `_definst_` for Wowza. 2.0.260
* v2.0, 2018-11-11, Merge [#1263][bug #1263], Fix string trim bug. 2.0.259
* <strong>v2.0, 2018-10-28, [2.0 release5(2.0.258)][r2.0r5] released. 86916 lines.</strong>
* v2.0, 2018-10-28, Fix [#1250][bug #1250], Support build on OSX10.14 Mojave. 2.0.258
* v2.0, 2018-10-08, Merge [#1236][bug #1236], Fix sleep bug in us. 2.0.257
* v2.0, 2018-10-08, Merge [#1237][bug #1237], Support param for transcoder. 2.0.256
* <strong>v2.0, 2018-08-12, [2.0 release4(2.0.255)][r2.0r4] released. 86915 lines.</strong>
* v2.0, 2018-08-12, For [#1202][bug #1202], Support edge/forward to Aliyun CDN. 2.0.255 
* v2.0, 2018-08-11, For [#910][bug #910], Support HTTP FLV with HTTP callback. 2.0.254
* v2.0, 2018-08-11, For [#1110][bug #1110], Refine params in http callback. 2.0.253
* v2.0, 2018-08-05, Refine HTTP-FLV latency, support realtime mode. 2.0.252
* v2.0, 2018-08-04, For [#1110][bug #1110], Support params in http callback. 2.0.251
* v2.0, 2018-08-02, For [#1031][bug #1031], SRS edge support douyu.com. 2.0.250
* v2.0, 2018-07-21, Merge [#1119][bug #1119], fix memory leak. 2.0.249
* <strong>v2.0, 2018-07-18, [2.0 release3(2.0.248)][r2.0r3] released. 86775 lines.</strong>
* v2.0, 2018-07-17, Merge [#1176][bug #1176], fix scaned issues. 2.0.248
* v2.0, 2018-02-28, Merge [#1077][bug #1077], fix crash for edge HLS. 2.0.247
* v2.0, 2018-02-13, Fix [#1059][bug #1059], support vhost in stream parameters. 2.0.246
* v2.0, 2018-01-07, Merge [#1045][bug #1045], fix [#1044][bug #1044], TCP connection alive detection. 2.0.245
* v2.0, 2018-01-04, Merge [#1039][bug #1039], fix bug of init.d script.
* v2.0, 2018-01-01, Merge [#1033][bug #1033], allow user to add some specific flags. 2.0.244
* <strong>v2.0, 2017-06-10, [2.0 release2(2.0.243)][r2.0r2] released. 86670 lines.</strong>
* v2.0, 2017-05-29, Merge [#899][bug #899] to fix [#893][bug #893], ts PES ext length. 2.0.243
* v2.0, 2017-05-01, Fix [#865][bug #865], shouldn't remove ts/m3u8 when hls_dispose disabled. 2.0.242
* v2.0, 2017-04-30, Fix [#636][bug #636], FD leak for requesting empty HTTP stream. 2.0.241
* v2.0, 2017-04-23, Fix [#851][bug #851], HTTP API support number of video frames for FPS. 2.0.240
* <strong>v2.0, 2017-04-18, [2.0 release1(2.0.239)][r2.0r1] released. 86515 lines.</strong>
* v2.0, 2017-04-18, Fix [#848][bug #848], crash at HTTP fast buffer grow. 2.0.239
* v2.0, 2017-04-15, Fix [#844][bug #844], support Haivision encoder. 2.0.238
* v2.0, 2017-04-15, Merge [#846][bug #846], fix fd leak for FLV stream caster. 2.0.237
* v2.0, 2017-04-15, Merge [#841][bug #841], avoid the duplicated sps/pps in ts. 2.0.236
* v2.0, 2017-04-09, Fix [#834][bug #834], crash for TS context corrupt. 2.0.235
* <strong>v2.0, 2017-03-03, [2.0 release0(2.0.234)][r2.0r0] released. 86373 lines.</strong>
* v2.0, 2017-02-25, for [#730][bug #730], remove the test code. 2.0.234
* v2.0, 2017-02-09, fix [#503][bug #503] disable utilities when reload a source. 2.0.233
* v2.0, 2017-01-22, for [#752][bug #752] release the io then free it for kbps. 2.0.232
* v2.0, 2017-01-18, fix [#750][bug #750] use specific error code for dns resolve. 2.0.231
* <strong>v2.0, 2017-01-18, [2.0 beta4(2.0.230)][r2.0b4] released. 86334 lines.</strong>
* v2.0, 2017-01-18, fix [#749][bug #749], timestamp overflow for ATC. 2.0.230
* v2.0, 2017-01-11, fix [#740][bug #740], convert ts aac audio private stream 1 to common. 2.0.229
* v2.0, 2017-01-11, fix [#588][bug #588], kbps interface error. 2.0.228
* v2.0, 2017-01-11, fix [#736][bug #736], recovery the hls dispose. 2.0.227
* v2.0, 2017-01-10, refine hls html5 video template.
* v2.0, 2017-01-10, fix [#635][bug #635], hls support NonIDR(open gop). 2.0.226
* v2.0, 2017-01-06, for [#730][bug #730], reset ack follow flash player rules. 2.0.225
* v2.0, 2016-12-15, for [#513][bug #513], remove hls ram from srs2 to srs3+. 2.0.224
* <strong>v2.0, 2016-12-13, [2.0 beta3(2.0.223)][r2.0b3] released. 86685 lines.</strong>
* v2.0, 2016-12-13, fix [#713][bug #713], disable the source cleanup. 2.0.223
* v2.0, 2016-12-13, fix [#713][bug #713], refine source to avoid critical fetch and create. 2.0.222
* <strong>v2.0, 2016-11-09, [2.0 beta2(2.0.221)][r2.0b2] released. 86691 lines.</strong>
* v2.0, 2016-11-05, fix [#654][bug #654], crash when source cleanup for edge. 2.0.221
* v2.0, 2016-10-26, fix [#666][bug #666], crash when source cleanup for http-flv. 2.0.220
* v2.0, 2016-10-10, fix [#661][bug #661], close fd after thread stopped. 2.0.219
* v2.0, 2016-09-23, support asprocess for oryx. 2.0.218
* v2.0, 2016-09-23, support change work_dir for oryx.
* v2.0, 2016-09-15, fix [#640][bug #640], typo for rtmp type. 2.0.217
* v2.0, 2016-09-12, fix fast stream error bug. 2.0.216
* <strong>v2.0, 2016-09-09, [2.0 beta1(2.0.215)][r2.0b1] released. 89941 lines.</strong>
* v2.0, 2016-09-09, refine librtmp comments about NALUs. 2.0.215
* v2.0, 2016-09-05, fix memory leak at source. 2.0.214
* v2.0, 2016-09-05, fix memory leak at handshake. 2.0.213
* v2.0, 2016-09-04, support valgrind for [patched st](https://github.com/ossrs/state-threads/issues/2).
* v2.0, 2016-09-03, support all arm for [patched st](https://github.com/ossrs/state-threads/issues/1). 2.0.212
* v2.0, 2016-09-01, workaround [#511][bug #511] the fly stfd in close. 2.0.211
* v2.0, 2016-08-30, comment the pcr.
* v2.0, 2016-08-18, fix [srs-librtmp#4](https://github.com/ossrs/srs-librtmp/issues/4) filter frame.
* v2.0, 2016-08-10, fix socket timeout for librtmp.
* v2.0, 2016-08-08, fix the crash by srs_info log.
* <strong>v2.0, 2016-08-06, [2.0 beta0(2.0.210)][r2.0b0] released. 89704 lines.</strong>
* v2.0, 2016-05-17, fix the sps pps parse bug.
* v2.0, 2016-01-13, fix http reader bug, support infinite chunked. 2.0.209
* v2.0, 2016-01-09, merge [#559][pr #559] fix memory leak bug. 2.0.208
* v2.0, 2016-01-09, merge [#558][pr #558] add tcUrl for on_publish.
* v2.0, 2016-01-05, add keyword XCORE for coredump to identify the version. 2.0.207
* <strong>v2.0, 2015-12-23, [2.0 alpha3(2.0.205)][r2.0a3] released. 89544 lines.</strong>
* v2.0, 2015-12-22, for [#509][bug #509] always alloc big object at heap. 2.0.205
* v2.0, 2015-12-22, for [#418][bug #418] ignore null connect props to make RED5 happy. 2.0.204
* v2.0, 2015-12-22, for [#546][bug #546] thread terminate normally dispose bug. 2.0.203
* v2.0, 2015-12-22, for [#541][bug #541] failed when chunk size too small. 2.0.202
* v2.0, 2015-12-15, default hls_on_error to continue. 2.0.201
* v2.0, 2015-11-16, for [#518][bug #518] fix fd leak bug when fork. 2.0.200
* v2.0, 2015-11-05, for [#511][bug #511] fix bug for restart thread. 2.0.199
* v2.0, 2015-11-02, for [#515][bug #515] use srs_freepa and SrsAutoFreeA for array. 2.0.198
* v2.0, 2015-10-28, for [ExoPlayer #828][exo #828], remove duration for live.
* v2.0, 2015-10-28, for [ExoPlayer #828][exo #828], add av tag in flv header. 2.0.197
* v2.0, 2015-10-27, for [#512][bug #512] partial hotfix the hls pure audio. 2.0.196
* <strong>v2.0, 2015-10-08, [2.0 alpha2(2.0.195)][r2.0a2] released. 89358 lines.</strong>
* v2.0, 2015-10-04, for [#448][bug #448] fix the bug of response of http hooks. 2.0.195
* v2.0, 2015-10-01, for [#497][bug #497] response error when client not found to kickoff. 2.0.194
* v2.0, 2015-10-01, for [#495][bug #495] decrease the srs-librtmp size. 2.0.193
* v2.0, 2015-09-23, for [#485][bug #485] error when arm glibc 2.15+ or not i386/x86_64/amd64. 2.0.192
* v2.0, 2015-09-23, for [#485][bug #485] srs for respberrypi and cubieboard. 2.0.191
* v2.0, 2015-09-21, fix [#484][bug #484] hotfix the openssl build script 2.0.190
* <strong>v2.0, 2015-09-14, [2.0 alpha1(2.0.189)][r2.0a1] released. 89269 lines.</strong>
* v2.0, 2015-09-14, fix [#474][bug #474] config to donot parse width/height from sps. 2.0.189
* v2.0, 2015-09-14, for [#474][bug #474] always release publish for source.
* v2.0, 2015-09-14, for [#458][bug #458] http hooks use source thread cid. 2.0.188
* v2.0, 2015-09-14, for [#475][bug #475] fix http hooks crash for st context switch. 2.0.187
* v2.0, 2015-09-09, support reload utc_time. 2.0.186
* <strong>v2.0, 2015-08-23, [2.0 alpha0(2.0.185)][r2.0a0] released. 89022 lines.</strong>
* v2.0, 2015-08-22, HTTP API support JSONP by specifies the query string callback=xxx.
* v2.0, 2015-08-20, fix [#380][bug #380], srs-librtmp send sequence header when sps or pps changed.
* v2.0, 2015-08-18, close [#454][bug #454], support obs restart publish. 2.0.184
* v2.0, 2015-08-14, use reduce_sequence_header for stream control.
* v2.0, 2015-08-14, use send_min_interval for stream control. 2.0.183
* v2.0, 2015-08-12, enable the SRS_PERF_TCP_NODELAY and add config tcp_nodelay. 2.0.182
* v2.0, 2015-08-11, for [#442][bug #442] support kickoff connected client. 2.0.181
* v2.0, 2015-07-21, for [#169][bug #169] support default values for transcode. 2.0.180
* v2.0, 2015-07-21, fix [#435][bug #435] add pageUrl for HTTP callback on_play.
* v2.0, 2015-07-20, refine the hls, ignore packet when no sequence header. 2.0.179
* v2.0, 2015-07-16, for [#441][bug #441] use 30s timeout for first msg. 2.0.178
* v2.0, 2015-07-14, refine hls disable the time jitter, support not mix monotonically increase. 2.0.177
* v2.0, 2015-07-01, fix [#433][bug #433] fix the sps parse bug. 2.0.176
* v2.0, 2015-06-10, fix [#425][bug #425] refine the time jitter, correct (-inf,-250)+(250,+inf) to 10ms. 2.0.175
* v2.0, 2015-06-10, fix [#424][bug #424] fix aggregate timestamp bug. 2.0.174
* v2.0, 2015-06-06, fix [#421][bug #421] drop video for unkown RTMP header.
* v2.0, 2015-06-05, fix [#420][bug #420] remove ts for hls ram mode.
* v2.0, 2015-05-30, fix [#209][bug #209] cleanup hls when stop and timeout. 2.0.173.
* v2.0, 2015-05-29, fix [#409][bug #409] support pure video hls. 2.0.172.
* v2.0, 2015-05-28, support [srs-dolphin][srs-dolphin], the multiple-process SRS.
* v2.0, 2015-05-24, fix [#404][bug #404] register handler then start http thread. 2.0.167.
* v2.0, 2015-05-23, refine the thread, protocol, kbps code. 2.0.166
* v2.0, 2015-05-23, fix [#391][bug #391] copy request for async call.
* v2.0, 2015-05-22, fix [#397][bug #397] the USER_HZ maybe not 100. 2.0.165
* v2.0, 2015-05-22, for [#400][bug #400], parse when got entire http header, by feilong. 2.0.164.
* v2.0, 2015-05-19, merge from bravo system, add the rtmfp to bms(commercial srs). 2.0.163.
* v2.0, 2015-05-10, support push flv stream over HTTP POST to SRS.
* v2.0, 2015-04-20, support ingest hls live stream to RTMP.
* v2.0, 2015-04-15, for [#383][bug #383], support mix_correct algorithm. 2.0.161.
* v2.0, 2015-04-13, for [#381][bug #381], support reap hls/ts by gop or not. 2.0.160.
* v2.0, 2015-04-10, enhanced on_hls_notify, support HTTP GET when reap ts.
* v2.0, 2015-04-10, refine the hls deviation for floor algorithm.
* v2.0, 2015-04-08, for [#375][bug #375], fix hls bug, keep cc continous between ts files. 2.0.159.
* v2.0, 2015-04-04, for [#304][bug #304], rewrite annexb mux for ts, refer to apple sample. 2.0.157.
* v2.0, 2015-04-03, enhanced avc decode, parse the sps get width+height. 2.0.156.
* v2.0, 2015-04-03, for [#372][bug #372], support transform vhost of edge 2.0.155.
* v2.0, 2015-03-30, for [#366][bug #366], config hls to disable cleanup of ts. 2.0.154.
* v2.0, 2015-03-31, support server cycle handler. 2.0.153.
* v2.0, 2015-03-31, support on_hls for http hooks. 2.0.152.
* v2.0, 2015-03-31, enhanced hls, support deviation for duration. 2.0.151.
* v2.0, 2015-03-30, for [#351][bug #351], support config the m3u8/ts path for hls. 2.0.149.
* v2.0, 2015-03-17, for [#155][bug #155], osx(darwin) support demo with nginx and ffmpeg. 2.0.143.
* v2.0, 2015-03-15, start [2.0release branch][branch2], 80773 lines.
* v2.0, 2015-03-14, fix [#324][bug #324], support hstrs(http stream trigger rtmp source) edge mode. 2.0.140.
* v2.0, 2015-03-14, for [#324][bug #324], support hstrs(http stream trigger rtmp source) origin mode. 2.0.139.
* v2.0, 2015-03-12, fix [#328][bug #328], support adobe hds. 2.0.138.
* v2.0, 2015-03-10, fix [#155][bug #155], support osx(darwin) for mac pro. 2.0.137.
* v2.0, 2015-03-08, fix [#316][bug #316], http api provides stream/vhost/srs/server bytes, codec and count. 2.0.136.
* v2.0, 2015-03-08, fix [#310][bug #310], refine aac LC, support aac HE/HEv2. 2.0.134.
* v2.0, 2015-03-06, for [#322][bug #322], fix http-flv stream bug, support multiple streams. 2.0.133.
* v2.0, 2015-03-06, refine http request parse. 2.0.132.
* v2.0, 2015-03-01, for [#179][bug #179], revert dvr http api. 2.0.128.
* v2.0, 2015-02-24, for [#304][bug #304], fix hls bug, write pts/dts error. 2.0.124
* v2.0, 2015-02-19, refine dvr, append file when dvr file exists. 2.0.122.
* v2.0, 2015-02-19, refine pithy print to more easyer to use. 2.0.121.
* v2.0, 2015-02-18, fix [#133][bug #133], support push rtsp to srs. 2.0.120.
* v2.0, 2015-02-17, the join maybe failed, should use a variable to ensure thread terminated. 2.0.119.
* v2.0, 2015-02-15, for [#304][bug #304], support config default acodec/vcodec. 2.0.118.
* v2.0, 2015-02-15, for [#304][bug #304], rewrite hls/ts code, support h.264+mp3 for hls. 2.0.117.
* v2.0, 2015-02-12, for [#304][bug #304], use stringstream to generate m3u8, add hls_td_ratio. 2.0.116.
* v2.0, 2015-02-11, dev code ZhouGuowen for 2.0.115.
* v2.0, 2015-02-10, for [#311][bug #311], set pcr_base to dts. 2.0.114.
* v2.0, 2015-02-10, fix [the bug][p21] of ibmf format which decoded in annexb.
* v2.0, 2015-02-10, for [#310][bug #310], downcast aac SSR to LC. 2.0.113
* v2.0, 2015-02-03, fix [#136][bug #136], support hls without io(in ram). 2.0.112
* v2.0, 2015-01-31, for [#250][bug #250], support push MPEGTS over UDP to SRS. 2.0.111
* v2.0, 2015-01-29, build libfdk-aac in ffmpeg. 2.0.108
* v2.0, 2015-01-25, for [#301][bug #301], hls support h.264+mp3, ok for vlc. 2.0.107
* v2.0, 2015-01-25, for [#301][bug #301], http ts stream support h.264+mp3. 2.0.106
* v2.0, 2015-01-25, hotfix [#268][bug #268], refine the pcr start at 0, dts/pts plus delay. 2.0.105
* v2.0, 2015-01-25, hotfix [#151][bug #151], refine pcr=dts-800ms and use dts/pts directly. 2.0.104
* v2.0, 2015-01-23, hotfix [#151][bug #151], use absolutely overflow to make jwplayer happy. 2.0.103
* v2.0, 2015-01-22, for [#293][bug #293], support http live ts stream. 2.0.101.
* v2.0, 2015-01-19, for [#293][bug #293], support http live flv/aac/mp3 stream with fast cache. 2.0.100.
* v2.0, 2015-01-18, for [#293][bug #293], support rtmp remux to http flv live stream. 2.0.99.
* v2.0, 2015-01-17, fix [#277][bug #277], refine http server refer to go http-framework. 2.0.98
* v2.0, 2015-01-17, for [#277][bug #277], refine http api refer to go http-framework. 2.0.97
* v2.0, 2015-01-17, hotfix [#290][bug #290], use iformat only for rtmp input. 2.0.95
* v2.0, 2015-01-08, hotfix [#281][bug #281], fix hls bug ignore type-9 send aud. 2.0.93
* v2.0, 2015-01-03, fix [#274][bug #274], http-callback support on_dvr when reap a dvr file. 2.0.89
* v2.0, 2015-01-03, hotfix to remove the pageUrl for http callback. 2.0.88
* v2.0, 2015-01-03, fix [#179][bug #179], dvr support custom filepath by variables. 2.0.87
* v2.0, 2015-01-02, fix [#211][bug #211], support security allow/deny publish/play all/ip. 2.0.86
* v2.0, 2015-01-02, hotfix [#207][bug #207], trim the last 0 of log. 2.0.85
* v2.0, 2014-01-02, fix [#158][bug #158], http-callback check http status code ok(200). 2.0.84
* v2.0, 2015-01-02, hotfix [#216][bug #216], http-callback post in application/json content-type. 2.0.83
* v2.0, 2014-01-02, fix [#263][bug #263], srs-librtmp flv read tag should init size. 2.0.82
* v2.0, 2015-01-01, hotfix [#270][bug #270], memory leak for http client post. 2.0.81
* v2.0, 2014-12-12, fix [#266][bug #266], aac profile is object id plus one. 2.0.80
* v2.0, 2014-12-29, hotfix [#267][bug #267], the forward dest ep should use server. 2.0.79
* v2.0, 2014-12-29, hotfix [#268][bug #268], the hls pcr is negative when startup. 2.0.78
* v2.0, 2014-12-22, hotfix [#264][bug #264], ignore NALU when sequence header to make HLS happy. 2.0.76
* v2.0, 2014-12-20, hotfix [#264][bug #264], support disconnect publish connect when hls error. 2.0.75
* v2.0, 2014-12-12, fix [#257][bug #257], support 0.1s+ latency. 2.0.70
* v2.0, 2014-12-08, update wiki for mr([EN][v3_EN_LowLatency#merged-read], [CN][v3_CN_LowLatency#merged-read]) and mw([EN][v3_EN_LowLatency#merged-write], [CN][v3_CN_LowLatency#merged-write]).
* v2.0, 2014-12-07, fix [#251][bug #251], 10k+ clients, use queue cond wait and fast vector. 2.0.67
* v2.0, 2014-12-05, fix [#251][bug #251], 9k+ clients, use fast cache for msgs queue. 2.0.57
* v2.0, 2014-12-04, fix [#241][bug #241], add mw(merged-write) config. 2.0.53
* v2.0, 2014-12-04, for [#241][bug #241], support mr(merged-read) config and reload. 2.0.52.
* v2.0, 2014-12-04, enable [#241][bug #241] and [#248][bug #248], +25% performance, 2.5k publisher. 2.0.50
* v2.0, 2014-12-04, fix [#248][bug #248], improve about 15% performance for fast buffer. 2.0.49
* v2.0, 2014-12-03, fix [#244][bug #244], conn thread use cond to wait for recv thread error. 2.0.47.
* v2.0, 2014-12-02, merge [#239][p23], traverse the token before response connect. 2.0.45.
* v2.0, 2014-12-02, srs-librtmp support hijack io apis for st-load. 2.0.42.
* v2.0, 2014-12-01, for [#237][bug #237], refine syscall for recv, supports 1.5k clients. 2.0.41.
* v2.0, 2014-11-30, add qtcreate project file trunk/src/qt/srs/srs-qt.pro. 2.0.39.
* v2.0, 2014-11-29, fix [#235][bug #235], refine handshake, replace union with template method. 2.0.38.
* v2.0, 2014-11-28, fix [#215][bug #215], add srs_rtmp_dump tool. 2.0.37.
* v2.0, 2014-11-25, update PRIMARY, AUTHORS, CONTRIBUTORS rule. 2.0.32.
* v2.0, 2014-11-24, fix [#212][bug #212], support publish aac adts raw stream. 2.0.31.
* v2.0, 2014-11-22, fix [#217][bug #217], remove timeout recv, support 7.5k+ 250kbps clients. 2.0.30.
* v2.0, 2014-11-21, srs-librtmp add rtmp prefix for rtmp/utils/human apis. 2.0.29.
* v2.0, 2014-11-21, refine examples of srs-librtmp, add srs_print_rtmp_packet. 2.0.28.
* v2.0, 2014-11-20, fix [#212][bug #212], support publish audio raw frames. 2.0.27
* v2.0, 2014-11-19, fix [#213][bug #213], support compile [srs-librtmp on windows](https://github.com/winlinvip/srs.librtmp), [bug #213][bug #213]. 2.0.26
* v2.0, 2014-11-18, all wiki translated to English. 2.0.23.
* v2.0, 2014-11-15, fix [#204][bug #204], srs-librtmp drop duplicated sps/pps(sequence header). 2.0.22.
* v2.0, 2014-11-15, fix [#203][bug #203], srs-librtmp drop any video before sps/pps(sequence header). 2.0.21.
* v2.0, 2014-11-15, fix [#202][bug #202], fix memory leak of h.264 raw packet send in srs-librtmp. 2.0.20.
* v2.0, 2014-11-13, fix [#200][bug #200], deadloop when read/write 0 and ETIME. 2.0.16.
* v2.0, 2014-11-13, fix [#194][bug #194], writev multiple msgs, support 6k+ 250kbps clients. 2.0.15.
* v2.0, 2014-11-12, fix [#194][bug #194], optmized st for timeout recv. pulse to 500ms. 2.0.14.
* v2.0, 2014-11-11, fix [#195][bug #195], remove the confuse code st_usleep(0). 2.0.13.
* v2.0, 2014-11-08, fix [#191][bug #191], configure --export-librtmp-project and --export-librtmp-single. 2.0.11.
* v2.0, 2014-11-08, fix [#66][bug #66], srs-librtmp support write h264 raw packet. 2.0.9.
* v2.0, 2014-10-25, fix [#185][bug #185], AMF0 support 0x0B the date type codec. 2.0.7.
* v2.0, 2014-10-24, fix [#186][bug #186], hotfix for bug #186, drop connect args when not object. 2.0.6.
* v2.0, 2014-10-24, rename wiki/xxx to wiki/v1_CN_xxx. 2.0.3.
* v2.0, 2014-10-19, fix [#184][bug #184], support AnnexB in RTMP body for HLS. 2.0.2
* v2.0, 2014-10-18, remove supports for OSX(darwin). 2.0.1.
* v2.0, 2014-10-16, revert github srs README to English. 2.0.0.

## V1 changes

* <strong>v1.0, 2014-12-05, [1.0 release(1.0.10)][r1.0r0] released. 59391 lines.</strong>
* <strong>v1.0, 2014-10-09, [1.0 beta(1.0.0)][r1.0b0] released. 59316 lines.</strong>
* v1.0, 2014-10-08, fix [#151][bug #151], always reap ts whatever audio or video packet. 0.9.223.
* v1.0, 2014-10-08, fix [#162][bug #162], failed if no epoll. 0.9.222.
* v1.0, 2014-09-30, fix [#180][bug #180], crash for multiple edge publishing the same stream. 0.9.220.
* v1.0, 2014-09-26, fix hls bug, refine config and log, according to clion of jetbrains. 0.9.216. 
* v1.0, 2014-09-25, fix [#177][bug #177], dvr segment add config dvr_wait_keyframe. 0.9.213.
* v1.0, 2014-08-28, fix [#167][bug #167], add openssl includes to utest. 0.9.209.
* v1.0, 2014-08-27, max connections is 32756, for st use mmap default. 0.9.209
* v1.0, 2014-08-24, fix [#150][bug #150], forward should forward the sequence header when retry. 0.9.208.
* v1.0, 2014-08-22, for [#165][bug #165], refine dh wrapper, ensure public key is 128bytes. 0.9.206.
* v1.0, 2014-08-19, for [#160][bug #160], support forward/edge to flussonic, disable debug_srs_upnode to make flussonic happy. 0.9.201.
* v1.0, 2014-08-17, for [#155][bug #155], refine for osx, with ssl/http, disable statistics. 0.9.198.
* v1.0, 2014-08-06, fix [#148][bug #148], simplify the RTMP handshake key generation. 0.9.191.
* v1.0, 2014-08-06, fix [#147][bug #147], support identify the srs edge. 0.9.190.
* <strong>v1.0, 2014-08-03, [1.0 mainline7(0.9.189)][r1.0a7] released. 57432 lines.</strong>
* v1.0, 2014-08-03, fix [#79][bug #79], fix the reload remove edge assert bug. 0.9.189.
* v1.0, 2014-08-03, fix [#57][bug #57], use lock(acquire/release publish) to avoid duplicated publishing. 0.9.188.
* v1.0, 2014-08-03, fix [#85][bug #85], fix the segment-dvr sequence header missing. 0.9.187.
* v1.0, 2014-08-03, fix [#145][bug #145], refine ffmpeg log, check abitrate for libaacplus. 0.9.186.
* v1.0, 2014-08-03, fix [#143][bug #143], fix retrieve sys stat bug for all linux. 0.9.185.
* v1.0, 2014-08-02, fix [#138][bug #138], fix http hooks bug, regression bug. 0.9.184.
* v1.0, 2014-08-02, fix [#142][bug #142], fix tcp stat slow bug, use /proc/net/sockstat instead, refer to 'ss -s'. 0.9.183.
* v1.0, 2014-07-31, fix [#141][bug #141], support tun0(vpn network device) ip retrieve. 0.9.179.
* v1.0, 2014-07-27, support partially build on OSX(Darwin). 0.9.177
* v1.0, 2014-07-27, api connections add udp, add disk iops. 0.9.176
* v1.0, 2014-07-26, complete config utest. 0.9.173
* v1.0, 2014-07-26, fix [#124][bug #124], gop cache support disable video in publishing. 0.9.171.
* v1.0, 2014-07-23, fix [#121][bug #121], srs_info detail log compile failed. 0.9.168.
* v1.0, 2014-07-19, fix [#119][bug #119], use iformat and oformat for ffmpeg transcode. 0.9.163.
* <strong>v1.0, 2014-07-13, [1.0 mainline6(0.9.160)][r1.0a6] released. 50029 lines.</strong>
* v1.0, 2014-07-13, refine the bandwidth check/test, add as/js library, use srs-librtmp for linux tool. 0.9.159
* v1.0, 2014-07-12, complete rtmp stack utest. 0.9.156
* v1.0, 2014-07-06, fix [#81][bug #81], fix HLS codec info, IOS ok. 0.9.153.
* v1.0, 2014-07-06, fix [#103][bug #103], support all aac sample rate. 0.9.150.
* v1.0, 2014-07-05, complete kernel utest. 0.9.149
* v1.0, 2014-06-30, fix [#111][bug #111], always use 31bits timestamp. 0.9.143.
* v1.0, 2014-06-28, response the call message with null. 0.9.137
* v1.0, 2014-06-28, fix [#110][bug #110], thread start segment fault, thread cycle stop destroy thread. 0.9.136
* v1.0, 2014-06-27, fix [#109][bug #109], fix the system jump time, adjust system startup time. 0.9.135
* <strong>v1.0, 2014-06-27, [1.0 mainline5(0.9.134)][r1.0a5] released. 41573 lines.</strong>
* v1.0, 2014-06-27, SRS online 30days with RTMP/HLS.
* v1.0, 2014-06-25, fix [#108][bug #108], support config time jitter for encoder non-monotonical stream. 0.9.133
* v1.0, 2014-06-23, support report summaries in heartbeat. 0.9.132
* v1.0, 2014-06-22, performance refine, support [3k+][v1_CN_Performance#performancereport4k] connections(270kbps). 0.9.130
* v1.0, 2014-06-21, support edge [token traverse][v3_CN_DRM#tokentraverse], fix [#104][bug #104]. 0.9.129
* v1.0, 2014-06-19, add connections count to api summaries. 0.9.127
* v1.0, 2014-06-19, add srs bytes and kbps to api summaries. 0.9.126
* v1.0, 2014-06-18, add network bytes to api summaries. 0.9.125
* v1.0, 2014-06-14, fix [#98][bug #98], workaround for librtmp ping(fmt=1,cid=2 fresh stream). 0.9.124
* v1.0, 2014-05-29, support flv inject and flv http streaming with start=bytes. 0.9.122
* <strong>v1.0, 2014-05-28, [1.0 mainline4(0.9.120)][r1.0a4] released. 39200 lines.</strong>
* v1.0, 2014-05-27, fix [#87][bug #87], add source id for full trackable log. 0.9.120
* v1.0, 2014-05-27, fix [#84][bug #84], unpublish when edge disconnect. 0.9.119
* v1.0, 2014-05-27, fix [#89][bug #89], config to /dev/null to disable ffmpeg log. 0.9.117
* v1.0, 2014-05-25, fix [#76][bug #76], allow edge vhost to add or remove. 0.9.114
* v1.0, 2014-05-24, Johnny contribute [ossrs.net](http://ossrs.net). karthikeyan start to translate wiki to English.
* v1.0, 2014-05-22, fix [#78][bug #78], st joinable thread must be stop by other threads, 0.9.113
* v1.0, 2014-05-22, support amf0 StrictArray(0x0a). 0.9.111.
* v1.0, 2014-05-22, support flv parser, add amf0 to librtmp. 0.9.110
* v1.0, 2014-05-22, fix [#74][bug #74], add tcUrl for http callback on_connect, 0.9.109
* v1.0, 2014-05-19, support http heartbeat, 0.9.107
* <strong>v1.0, 2014-05-18, [1.0 mainline3(0.9.105)][r1.0a3] released. 37594 lines.</strong>
* v1.0, 2014-05-18, support http api json, to PUT/POST. 0.9.105
* v1.0, 2014-05-17, fix [#72][bug #72], also need stream_id for send_and_free_message. 0.9.101
* v1.0, 2014-05-17, rename struct to class. 0.9.100
* v1.0, 2014-05-14, fix [#67][bug #67] pithy print, stage must has a age. 0.9.98
* v1.0, 2014-05-13, fix mem leak for delete[] SharedPtrMessage array. 0.9.95
* v1.0, 2014-05-12, refine the kbps calc module. 0.9.93
* v1.0, 2014-05-12, fix bug [#64][bug #64]: install_dir=DESTDIR+PREFIX
* v1.0, 2014-05-08, fix [#36][bug #36]: never directly use \*(int32_t\*) for arm.
* v1.0, 2014-05-08, fix [#60][bug #60]: support aggregate message
* v1.0, 2014-05-08, fix [#59][bug #59], edge support FMS origin server. 0.9.92
* v1.0, 2014-05-06, fix [#50][bug #50], ubuntu14 build error.
* v1.0, 2014-05-04, support mips linux.
* v1.0, 2014-04-30, fix bug [#34][bug #34]: convert signal to io thread. 0.9.85
* v1.0, 2014-04-29, refine RTMP protocol completed, to 0.9.81
* <strong>v1.0, 2014-04-28, [1.0 mainline2(0.9.79)][r1.0a2] released. 35255 lines.</strong>
* v1.0, 2014-04-28, support full edge RTMP server. 0.9.79
* v1.0, 2014-04-27, support basic edge(play/publish) RTMP server. 0.9.78
* v1.0, 2014-04-25, add donation page. 0.9.76
* v1.0, 2014-04-21, support android app to start srs for internal edge. 0.9.72
* v1.0, 2014-04-19, support tool over srs-librtmp to ingest flv/rtmp. 0.9.71
* v1.0, 2014-04-17, support dvr(record live to flv file for vod). 0.9.69
* v1.0, 2014-04-11, add speex1.2 to transcode flash encoder stream. 0.9.58
* v1.0, 2014-04-10, support reload ingesters(add/remov/update). 0.9.57
* <strong>v1.0, 2014-04-07, [1.0 mainline(0.9.55)][r1.0a0] released. 30000 lines.</strong>
* v1.0, 2014-04-07, support [ingest][v1_CN_SampleIngest] file/stream/device.
* v1.0, 2014-04-05, support [http api][v3_CN_HTTPApi] and [http server][v2_CN_HTTPServer].
* v1.0, 2014-04-03, implements http framework and api/v1/version.
* v1.0, 2014-03-30, fix bug for st detecting epoll failed, force st to use epoll.
* v1.0, 2014-03-29, add wiki [Performance for RaspberryPi][v1_CN_RaspberryPi].
* v1.0, 2014-03-29, add release binary package for raspberry-pi. 
* v1.0, 2014-03-26, support RTMP ATC for HLS/HDS to support backup(failover).
* v1.0, 2014-03-23, support daemon, default start in daemon.
* v1.0, 2014-03-22, support make install/install-api and uninstall.
* v1.0, 2014-03-22, add ./etc/init.d/srs, refine to support make clean then make.
* v1.0, 2014-03-21, write pid to ./objs/srs.pid.
* v1.0, 2014-03-20, refine hls code, support pure audio HLS.
* v1.0, 2014-03-19, add vn/an for FFMPEG to drop video/audio for radio stream.
* v1.0, 2014-03-19, refine handshake, client support complex handshake, add utest.
* v1.0, 2014-03-16, fix bug on arm of st, the sp change from 20 to 8, for respberry-pi, @see [commit][p22]
* v1.0, 2014-03-16, support ARM([debian armhf, v7cpu][v1_CN_SrsLinuxArm]) with rtmp/ssl/hls/librtmp.
* v1.0, 2014-03-12, finish utest for amf0 codec.
* v1.0, 2014-03-06, add gperftools for mem leak detect, mem/cpu profile.
* v1.0, 2014-03-04, add gest framework for utest, build success.
* v1.0, 2014-03-02, add wiki [srs-librtmp][v3_CN_SrsLibrtmp], [SRS for arm][v1_CN_SrsLinuxArm], [product][v1_CN_Product]
* v1.0, 2014-03-02, srs-librtmp, client publish/play library like librtmp.
* v1.0, 2014-03-01, modularity, extract core/kernel/rtmp/app/main module.
* v1.0, 2014-02-28, support arm build(SRS/ST), add ssl to 3rdparty package.
* v1.0, 2014-02-28, add wiki [BuildArm][v3_CN_Build], [FFMPEG][v3_CN_FFMPEG], [Reload][v1_CN_Reload]
* v1.0, 2014-02-27, add wiki [LowLatency][v3_CN_LowLatency], [HTTPCallback][v3_CN_HTTPCallback], [ServerSideScript][v1_CN_ServerSideScript], [IDE][v2_CN_IDE]
* v1.0, 2014-01-19, add wiki [DeliveryHLS][v3_CN_DeliveryHLS]
* v1.0, 2014-01-12, add wiki [HowToAskQuestion][v1_CN_HowToAskQuestion], [RtmpUrlVhost][v1_CN_RtmpUrlVhost]
* v1.0, 2014-01-11, fix jw/flower player pause bug, which send closeStream actually.
* v1.0, 2014-01-05, add wiki [Build][v3_CN_Build], [Performance][v1_CN_Performance], [Forward][v3_CN_Forward]
* v1.0, 2014-01-01, change listen(512), chunk-size(60000), to improve performance.
* v1.0, 2013-12-27, merge from wenjie, the bandwidth test feature.
* <strong>v0.9, 2013-12-25, [v0.9][r0.9] released. 20926 lines.</strong>
* v0.9, 2013-12-25, fix the bitrate bug(in Bps), use enhanced microphone.
* v0.9, 2013-12-22, demo video meeting or chat(SRS+cherrypy+jquery+bootstrap).
* v0.9, 2013-12-22, merge from wenjie, support banwidth test.
* v0.9, 2013-12-22, merge from wenjie: support set chunk size at vhost level
* v0.9, 2013-12-21, add [players][player] for play and publish.
* v0.9, 2013-12-15, ensure the HLS(ts) is continous when republish stream.
* v0.9, 2013-12-15, fix the hls reload bug, feed it the sequence header.
* v0.9, 2013-12-15, refine protocol, use int64_t timestamp for ts and jitter.
* v0.9, 2013-12-15, support set the live queue length(in seconds), drop when full.
* v0.9, 2013-12-15, fix the forwarder reconnect bug, feed it the sequence header.
* v0.9, 2013-12-15, support reload the hls/forwarder/transcoder.
* v0.9, 2013-12-14, refine the thread model for the retry threads.
* v0.9, 2013-12-10, auto install depends tools/libs on centos/ubuntu.
* <strong>v0.8, 2013-12-08, [v0.8][r0.8] released. 19186 lines.</strong>
* v0.8, 2013-12-08, support [http hooks][v3_CN_HTTPCallback]: on_connect/close/publish/unpublish/play/stop.
* v0.8, 2013-12-08, support multiple http hooks for a event.
* v0.8, 2013-12-07, support http callback hooks, on_connect.
* v0.8, 2013-12-07, support network based cli and json result, add CherryPy 3.2.4.
* v0.8, 2013-12-07, update http/hls/rtmp load test tool [SB][srs-bench], use SRS rtmp sdk.
* v0.8, 2013-12-06, support max_connections, drop if exceed.
* v0.8, 2013-12-05, support log_dir, write ffmpeg log to file.
* v0.8, 2013-12-05, fix the forward/hls/encoder bug.
* <strong>v0.7, 2013-12-03, [v0.7][r0.7] released. 17605 lines.</strong>
* v0.7, 2013-12-01, support dead-loop detect for forwarder and transcoder.
* v0.7, 2013-12-01, support all ffmpeg filters and params.
* v0.7, 2013-11-30, support live stream transcoder by ffmpeg.
* v0.7, 2013-11-30, support --with/without -ffmpeg, build ffmpeg-2.1.
* v0.7, 2013-11-30, add ffmpeg-2.1, x264-core138, lame-3.99.5, libaacplus-2.0.2.
* <strong>v0.6, 2013-11-29, [v0.6][r0.6] released. 16094 lines.</strong>
* v0.6, 2013-11-29, add performance summary, 1800 clients, 900Mbps, CPU 90.2%, 41MB.
* v0.6, 2013-11-29, support forward stream to other edge server.
* v0.6, 2013-11-29, support forward stream to other origin server.
* v0.6, 2013-11-28, fix memory leak bug, aac decode bug.
* v0.6, 2013-11-27, support --with or --without -hls and -ssl options.
* v0.6, 2013-11-27, support AAC 44100HZ sample rate for iphone, adjust the timestamp.
* <strong>v0.5, 2013-11-26, [v0.5][r0.5] released. 14449 lines.</strong>
* v0.5, 2013-11-24, support HLS(m3u8), fragment and window.
* v0.5, 2013-11-24, support record to ts file for HLS.
* v0.5, 2013-11-21, add ts_info tool to demux ts file.
* v0.5, 2013-11-16, add rtmp players(OSMF/jwplayer5/jwplayer6).
* <strong>v0.4, 2013-11-10, [v0.4][r0.4] released. 12500 lines.</strong>
* v0.4, 2013-11-10, support config and reload the pithy print.
* v0.4, 2013-11-09, support reload config(vhost and its detail).
* v0.4, 2013-11-09, support reload config(listen and chunk_size) by SIGHUP(1).
* v0.4, 2013-11-09, support longtime(>4.6hours) publish/play.
* v0.4, 2013-11-09, support config the chunk_size.
* v0.4, 2013-11-09, support pause for live stream.
* <strong>v0.3, 2013-11-04, [v0.3][r0.3] released. 11773 lines.</strong>
* v0.3, 2013-11-04, support refer/play-refer/publish-refer.
* v0.3, 2013-11-04, support vhosts specified config.
* v0.3, 2013-11-02, support listen multiple ports.
* v0.3, 2013-11-02, support config file in nginx-conf style.
* v0.3, 2013-10-29, support pithy print log message specified by stage.
* v0.3, 2013-10-28, support librtmp without extended-timestamp in 0xCX chunk packet.
* v0.3, 2013-10-27, support cache last gop for client fast startup.
* <strong>v0.2, 2013-10-25, [v0.2][r0.2] released. 10125 lines.</strong>
* v0.2, 2013-10-25, support flash publish.
* v0.2, 2013-10-25, support h264/avc codec by rtmp complex handshake.
* v0.2, 2013-10-24, support time jitter detect and correct algorithm
* v0.2, 2013-10-24, support decode codec type to cache the h264/avc sequence header.
* <strong>v0.1, 2013-10-23, [v0.1][r0.1] released. 8287 lines.</strong>
* v0.1, 2013-10-23, support basic amf0 codec, simplify the api using c-style api.
* v0.1, 2013-10-23, support shared ptr msg for zero memory copy.
* v0.1, 2013-10-22, support vp6 codec with rtmp protocol specified simple handshake.
* v0.1, 2013-10-20, support multiple flash client play live streaming.
* v0.1, 2013-10-20, support FMLE/FFMPEG publish live streaming.
* v0.1, 2013-10-18, support rtmp message2chunk protocol(send\_message).
* v0.1, 2013-10-17, support rtmp chunk2message protocol(recv\_message).

## Releases

* 2020-06-27, [Release v3.0-r0][r3.0r0], 3.0 release0, 3.0.141, 122674 lines.
* 2020-03-29, [Release v3.0-b3][r3.0b4], 3.0 beta4, 3.0.139, 122674 lines.
* 2020-03-18, [Release v3.0-b3][r3.0b3], 3.0 beta3, 3.0.134, 122509 lines.
* 2020-03-05, [Release v3.0-b2][r3.0b2], 3.0 beta2, 3.0.123, 122170 lines.
* 2020-02-14, [Release v3.0-b1][r3.0b1], 3.0 beta1, 3.0.117, 121964 lines.
* 2020-02-02, [Release v3.0-b0][r3.0b0], 3.0 beta0, 3.0.112, 121709 lines.
* 2020-01-21, [Release v3.0-a9][r3.0a9], 3.0 alpha9, 3.0.105, 121577 lines.
* 2020-01-10, [Release v3.0-a8][r3.0a8], 3.0 alpha8, 3.0.97, 121555 lines.
* 2019-12-29, [Release v3.0-a7][r3.0a7], 3.0 alpha7, 3.0.90, 116356 lines.
* 2019-12-26, [Release v3.0-a6][r3.0a6], 3.0 alpha6, 3.0.85, 116056 lines.
* 2019-12-19, [Release v3.0-a5][r3.0a5], 3.0 alpha5, 3.0.75, 115362 lines.
* 2019-12-13, [Release v3.0-a4][r3.0a4], 3.0 alpha4, 3.0.71, 112928 lines.
* 2019-11-30, [Release v3.0-a3][r3.0a3], 3.0 alpha3, 3.0.67, 110864 lines.
* 2019-11-30, [Release v3.0-a2][r3.0a2], 3.0 alpha2, 3.0.66, 110831 lines.
* 2019-10-07, [Release v3.0-a1][r3.0a1], 3.0 alpha1, 3.0.60, 107962 lines.
* 2019-10-04, [Release v3.0-a0][r3.0a0], 3.0 alpha0, 3.0.56, 107946 lines.
* 2017-03-03, [Release v2.0-r0][r2.0r0], 2.0 release0, 2.0.234, 86373 lines.
* 2016-11-13, [Release v2.0-b3][r2.0b3], 2.0 beta3, 2.0.223, 86685 lines.
* 2016-11-09, [Release v2.0-b2][r2.0b2], 2.0 beta2, 2.0.221, 86691 lines.
* 2016-09-09, [Release v2.0-b1][r2.0b1], 2.0 beta1, 2.0.215, 89941 lines.
* 2016-08-06, [Release v2.0-b0][r2.0b0], 2.0 beta0, 2.0.210, 89704 lines.
* 2015-12-23, [Release v2.0-a3][r2.0a3], 2.0 alpha3, 2.0.205, 89544 lines.
* 2015-10-08, [Release v2.0-a2][r2.0a2], 2.0 alpha2, 2.0.195, 89358 lines.
* 2015-09-14, [Release v2.0-a1][r2.0a1], 2.0 alpha1, 2.0.189, 89269 lines.
* 2015-08-23, [Release v2.0-a0][r2.0a0], 2.0 alpha0, 2.0.185, 89022 lines.
* 2015-05-23, [Release v1.0-r4][r1.0r4], bug fixed, 1.0.32, 59509 lines.
* 2015-03-19, [Release v1.0-r3][r1.0r3], bug fixed, 1.0.30, 59511 lines.
* 2015-02-12, [Release v1.0-r2][r1.0r2], bug fixed, 1.0.27, 59507 lines.
* 2015-01-15, [Release v1.0-r1][r1.0r1], bug fixed, 1.0.21, 59472 lines.
* 2014-12-05, [Release v1.0-r0][r1.0r0], all bug fixed, 1.0.10, 59391 lines.
* 2014-10-09, [Release v0.9.8][r1.0b0], all bug fixed, 1.0.0, 59316 lines.
* 2014-08-03, [Release v0.9.7][r1.0a7], config utest, all bug fixed. 57432 lines.
* 2014-07-13, [Release v0.9.6][r1.0a6], core/kernel/rtmp utest, refine bandwidth(as/js/srslibrtmp library). 50029 lines.
* 2014-06-27, [Release v0.9.5][r1.0a5], refine perf 3k+ clients, edge token traverse, 30days online. 41573 lines.
* 2014-05-28, [Release v0.9.4][r1.0a4], support heartbeat, tracable log, fix mem leak and bugs. 39200 lines.
* 2014-05-18, [Release v0.9.3][r1.0a3], support mips, fms origin, json(http-api). 37594 lines.
* 2014-04-28, [Release v0.9.2][r1.0a2], support [dvr][v3_CN_DVR], android, [edge][v3_CN_Edge]. 35255 lines.
* 2014-04-07, [Release v0.9.1][r1.0a0], support [arm][v1_CN_SrsLinuxArm], [init.d][v1_CN_LinuxService], http [server][v2_CN_HTTPServer]/[api][v3_CN_HTTPApi], [ingest][v1_CN_SampleIngest]. 30000 lines.
* 2013-12-25, [Release v0.9.0][r0.9], support bandwidth test, player/encoder/chat [demos][v1_CN_SampleDemo]. 20926 lines.
* 2013-12-08, [Release v0.8.0][r0.8], support [http hooks callback][v3_CN_HTTPCallback], update [SB][srs-bench]. 19186 lines.
* 2013-12-03, [Release v0.7.0][r0.7], support [live stream transcoding][v3_CN_FFMPEG]. 17605 lines.
* 2013-11-29, [Release v0.6.0][r0.6], support [forward][v3_CN_Forward] stream to origin/edge. 16094 lines.
* 2013-11-26, [Release v0.5.0][r0.5], support [HLS(m3u8)][v3_CN_DeliveryHLS], fragment and window. 14449 lines.
* 2013-11-10, [Release v0.4.0][r0.4], support [reload][v1_CN_Reload] config, pause, longtime publish/play. 12500 lines.
* 2013-11-04, [Release v0.3.0][r0.3], support [vhost][v1_CN_RtmpUrlVhost], refer, gop cache, listen multiple ports. 11773 lines.
* 2013-10-25, [Release v0.2.0][r0.2], support [rtmp][v1_CN_RTMPHandshake] flash publish, h264, time jitter correct. 10125 lines.
* 2013-10-23, [Release v0.1.0][r0.1], support [rtmp FMLE/FFMPEG publish][v1_CN_DeliveryRTMP], vp6. 8287 lines.
* 2013-10-17, Created.

## Compare

Comparing with other media servers, SRS is much better and stronger, for details please read Product([CN][v1_CN_Compare]/[EN][v1_EN_Compare]).

<a name="stream-delivery"></a>
**Stream Delivery**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   RTMP        |   Stable  |   Stable  |   Stable  |   Stable  |   Stable  |
|   HLS         |   Stable  |   Stable  |   X       |   Stable  |   Stable  |
|   HTTP FLV    |   Stable  |   X       |   X       |   X       |   X       |
|   HLS(aonly)  |   Stable  |   X       |   X       |   Stable  |   Stable  |
|   HDS         | Experiment|   X       |   X       |   Stable  |   Stable  |
|   MPEG-DASH   | Experiment|   X       |   X       |   X       |   X       |
|   HTTP Server |   Stable  |   Stable  |   X       |   X       |   Stable  |

<a name="cluster"></a>
**Cluster**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   RTMP Edge   |   Stable  |   X       |   X       |   Stable  |   X       |
|   RTMP Backup |   Stable  |   X       |   X       |   X       |   X       |
|   VHOST       |   Stable  |   X       |   X       |   Stable  |   Stable  |
|   Reload      |   Stable  |   X       |   X       |   X       |   X       |
|   Forward     |   Stable  |   X       |   X       |   X       |   X       |
|   ATC         |   Stable  |   X       |   X       |   X       |   X       |
|   Docker      |   Stable  |   X       |   X       |   X       |   X       |

<a name="stream-service"></a>
**Stream Service**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   DVR         |   Stable  |   Stable  |   X       |   X       |   Stable  |
|   DVR API     |   Stable  |   Stable  |   X       |   X       |   X       |
|   DVR MP4     |   Stable  |   X       |   X       |   X       |   X       |
|   EXEC        |   Stable  |   Stable  |   X       |   X       |   X       |
|   Transcode   |   Stable  |   X       |   X       |   X       |   Stable  |
|   HTTP API    |   Stable  |   Stable  |   X       |   X       |   Stable  |
| HTTP RAW API  |   Stable  |   X       |   X       |   X       |   X       |
|   HTTP hooks  |   Stable  |   X       |   X       |   X       |   X       |
|   GopCache    |   Stable  |   X       |   X       |   Stable  |   X       |
|   Security    |   Stable  |   Stable  |   X       |   X       |   Stable  |
| Token Traverse|   Stable  |   X       |   X       |   Stable  |   X       |

<a name="efficiency"></a>
**Efficiency**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   Concurrency |   7.5k    |   3k      |   2k      |   2k      |   3k      |
|MultipleProcess| [Stable][v3_CN_ReusePort] |   Stable  |   X       |   X       |   X       |
|   RTMP Latency|   0.1s    |   3s      |   3s      |   3s      |   3s      |
|   HLS Latency |   10s     |   30s     |   X       |   30s     |   30s     |

<a name="stream-caster"></a>
**Stream Caster**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   Ingest      |   Stable  |   X       |   X       |   X       |   X       |
|   Push MPEGTS | Experiment|   X       |   X       |   X       |   Stable  |
|   Push RTSP   | Experiment|   X       |   Stable  |   X       |   Stable  |
| Push HTTP FLV | Experiment|   X       |   X       |   X       |   X       |

<a name="debug-system"></a>
**Debug System**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   BW check    |   Stable  |   X       |   X       |   X       |   X       |
| Tracable Log  |   Stable  |   X       |   X       |   X       |   X       |

<a name="docs"></a>
**Docs**

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   Demos       |   Stable  |   X       |   X       |   X       |   X       |
|   WIKI(EN+CN) |   Stable  |  EN only  |   X       |   X       |   Stable  |

<a name="others"></a>
**Others** 

|   Feature     |   SRS     |   NGINX   | CRTMPD    | AMS       |   WOWZA   |
|   ----------- |   ------- |   -----   | --------- | --------  |   ------  |
|   ARM/MIPS    |   Stable  |   Stable  |   X       |   X       |   X       |
| Client Library|   Stable  |   X       |   X       |   X       |   X       |

Remark:

1. Concurrency: We only benchmark the concurrency of single process.
1. MultipleProcess: SRS supports multiple processes by [go-oryx][oryx].
1. HLS aonly: HLS supports audio only mode without video stream.
1. BW check: The bandwidth check feature is used to detect the bandwidth between server and client.
1. Security: The security includes access control, token authentication and referer check.
1. Reload: SRS and Nginx supports reload, but nginx-rtmp doesn't.

## Performance

The performance benchmark data and corelative commits are listed here.

* See also: [Performance for x86/x64 Test Guide][v1_CN_Performance].
* See also: [Performance for RaspberryPi][v1_CN_RaspberryPi].
* For multiple processes performance, read [#775: REUSEPORT][bug #775] or OriginCluster([CN][v3_EN_OriginCluster]/[EN][v3_EN_OriginCluster]) or [go-oryx][oryx].

<a name="play-rtmp-benchmark"></a>
**Play RTMP benchmark**

The data for playing RTMP was benchmarked by [SB][srs-bench]:


|   Update      |    SRS    |    Clients    |     Type      |    CPU    |  Memory   | Commit        |
| ------------- | --------- | ------------- | ------------- | --------- | --------  | ------------  |
|   2014-12-07  |   2.0.67  |   10k(10000)  |   players     |   95%     |   656MB   |   [code][p12] |
|   2014-12-05  |   2.0.57  |   9.0k(9000)  |   players     |   90%     |   468MB   |   [code][p11] |
|   2014-12-05  |   2.0.55  |   8.0k(8000)  |   players     |   89%     |   360MB   |   [code][p10] |
|   2014-11-22  |   2.0.30  |   7.5k(7500)  |   players     |   87%     |   320MB   |   [code][p9]  |
|   2014-11-13  |   2.0.15  |   6.0k(6000)  |   players     |   82%     |   203MB   |   [code][p8]  |
|   2014-11-12  |   2.0.14  |   3.5k(3500)  |   players     |   95%     |   78MB    |   [code][p7]  |
|   2014-11-12  |   2.0.14  |   2.7k(2700)  |   players     |   69%     |   59MB    |   -           |
|   2014-11-11  |   2.0.12  |   2.7k(2700)  |   players     |   85%     |   66MB    |   -           |
|   2014-11-11  |   1.0.5   |   2.7k(2700)  |   players     |   85%     |   66MB    |   -           |
|   2014-07-12  |   0.9.156 |   2.7k(2700)  |   players     |   89%     |   61MB    |   [code][p6]  |
|   2014-07-12  |   0.9.156 |   1.8k(1800)  |   players     |   68%     |   38MB    |   -           |
|   2013-11-28  |   0.5.0   |   1.8k(1800)  |   players     |   90%     |   41M     |   -           |

<a name="publish-rtmp-benchmark"></a>
**Publish RTMP benchmark**

The data for publishing RTMP was benchmarked by [SB][srs-bench]:

|   Update      |    SRS    |    Clients    |     Type      |    CPU    |  Memory   | Commit        |
| ------------- | --------- | ------------- | ------------- | --------- | --------  | ------------  |
|   2014-12-04  |   2.0.52  |   4.0k(4000)  |   publishers  |   80%     |   331MB   |   [code][p5]  |
|   2014-12-04  |   2.0.51  |   2.5k(2500)  |   publishers  |   91%     |   259MB   |   [code][p4]  |
|   2014-12-04  |   2.0.49  |   2.5k(2500)  |   publishers  |   95%     |   404MB   |   [code][p3]  |
|   2014-12-04  |   2.0.49  |   1.4k(1400)  |   publishers  |   68%     |   144MB   |   -           |
|   2014-12-03  |   2.0.48  |   1.4k(1400)  |   publishers  |   95%     |   140MB   |   [code][p2]  |
|   2014-12-03  |   2.0.47  |   1.4k(1400)  |   publishers  |   95%     |   140MB   |   -           |
|   2014-12-03  |   2.0.47  |   1.2k(1200)  |   publishers  |   84%     |   76MB    |   [code][p1]  |
|   2014-12-03  |   2.0.12  |   1.2k(1200)  |   publishers  |   96%     |   43MB    |   -           |
|   2014-12-03  |   1.0.10  |   1.2k(1200)  |   publishers  |   96%     |   43MB    |   -           |

<a name="play-http-flv-benchmark"></a>
**Play HTTP FLV benchmark**

The data for playing HTTP FLV was benchmarked by [SB][srs-bench]:


|   Update      |    SRS    |    Clients    |     Type      |    CPU    |  Memory   | Commit        |
| ------------- | --------- | ------------- | ------------- | --------- | --------  | ------------  |
|   2014-05-25  |   2.0.171 |   6.0k(6000)  |   players     |   84%     |   297MB   |   [code][p20] |
|   2014-05-24  |   2.0.170 |   3.0k(3000)  |   players     |   89%     |   96MB    |   [code][p19] |
|   2014-05-24  |   2.0.169 |   3.0k(3000)  |   players     |   94%     |   188MB   |   [code][p18] |
|   2014-05-24  |   2.0.168 |   2.3k(2300)  |   players     |   92%     |   276MB   |   [code][p17] |
|   2014-05-24  |   2.0.167 |   1.0k(1000)  |   players     |   82%     |   86MB    |   -           |

<a name="latency-benchmark"></a>
**Latency benchmark**

The latency between encoder and player with realtime config([CN][v3_CN_LowLatency], [EN][v3_EN_LowLatency]):
|   

|   Update      |    SRS    |    VP6    |  H.264    |  VP6+MP3  | H.264+MP3 |
| ------------- | --------- | --------- | --------- | --------- | --------  |
|   2014-12-16  |   2.0.72  |   0.1s    |   0.4s    |[0.8s][p15]|[0.6s][p16]|
|   2014-12-12  |   2.0.70  |[0.1s][p13]|[0.4s][p14]|   1.0s    |   0.9s    |
|   2014-12-03  |   1.0.10  |   0.4s    |   0.4s    |   0.9s    |   1.2s    |

> 2018-08-05, [c45f72e](https://github.com/ossrs/srs/commit/c45f72ef7bac9c7cf85b9125fc9e3aafd53f396f), Refine HTTP-FLV latency, support realtime mode. 2.0.252

We used FMLE as encoder for benchmark. The latency of server was 0.1s+, 
and the bottleneck was the encoder. For more information, read 
[bug #257][bug #257-c0].

<a name="hls-overhead"></a>
**HLS overhead**

About the overhead of HLS overhead, we compared FFMPEG and SRS.

| Bitrate   |   Duration    |   FLV(KB)     |   HLS(KB)     |   Overhead    |
| -------   |   --------    |   -------     |   --------    |   ---------   |
| 275kbps   |   600s        |   11144       |   12756       |   14.46%      |
| 260kbps   |   1860s       |   59344       |   68004       |   14.59%      |
| 697kbps   |   60s         |   5116        |   5476        |   7.03%       |
| 565kbps   |   453s        |   31316       |   33544       |   7.11%       |
| 565kbps   |   1813s       |   125224      |   134140      |   7.12%       |
| 861kbps   |   497s        |   52316       |   54924       |   4.98%       |
| 857kbps   |   1862s       |   195008      |   204768      |   5.00%       |
| 1301kbps  |   505s        |   80320       |   83676       |   4.17%       |
| 1312kbps  |   1915s       |   306920      |   319680      |   4.15%       |
| 2707kbps  |   600s        |   198356      |   204560      |   3.12%       |
| 2814kbps  |   1800s       |   618456      |   637660      |   3.10%       |
| 2828kbps  |   60s         |   20716       |   21356       |   3.08%       |
| 2599kbps  |   307s        |   97580       |   100672      |   3.16%       |
| 2640kbps  |   1283s       |   413880      |   426912      |   3.14%       |
| 5254kbps  |   71s         |   45832       |   47056       |   2.67%       |
| 5147kbps  |   370s        |   195040      |   200280      |   2.68%       |
| 5158kbps  |   1327s       |   835664      |   858092      |   2.68%       |

The HLS overhead is calc by: (HLS - FLV) / FLV * 100%.

The overhead should be larger than this benchmark(48kbps audio is best overhead), for we fix the [#512][bug #512].

## Architecture

SRS always use the simplest architecture to solve complex domain problems.

* System arch: the system structure and arch.
* Modularity arch: the main modularity of SRS.
* Stream arch: the stream dispatch arch of SRS.

## System Architecture

```
+------------------------------------------------------+
|                    Application                       |
|            Origin/Edge/HTTP-FLV/StreamCaster         |
+---------------+---------------+-----------+----------+
|   RAW API/    |     EXEC/     |  DVR/HLS  | FLV/TS/  |
|   API/hook    |   Transcoder  |  HDS/DASH | AMF0/JSON|
+---------------+---------------+-----------+ RTMP/RTSP|
|  http-parser  |  FFMPEG/x264  |  NGINX/ts | protocol |
+---------------+---------------+-----------+----------+
|              Network(state-threads)                  |
+------------------------------------------------------+
|    All Linux/Unix(RHEL,CentOS,Ubuntu,Fedora...)      |
+------------------------------------------------------+
```

## Modularity Architecture

```
+------------------------------------------------------+
|    SRS server    |   Programs in Main or Research    |
+------------------------------------------------------+
|  App(For SRS)    | Modules(1) |   research/librtmp   |
+------------------------------------------------------+
|    Service(C/S apps over ST)  | Libs(Export librtmp) |
+------------------------------------------------------+
|   Protocol Stack(RTMP/HTTP/RTSP/JSON/AMF/Format)     |
+------------------------------------------------------+
|      Kernel(File, Codec, Stream, LB services)        |
+------------------------------------------------------+
|         Core(Macros and very low-level APIs)         |
+------------------------------------------------------+
```

Remark:

1. Modules: SRS supports code-level modularity, read [modules][modules].

## Stream Architecture

```
+---------+              +----------+
| Publish |              |  Deliver |
+---|-----+              +----|-----+
+----------------------+-------------------------+----------------+
|     Input            | SRS(Simple RTMP Server) |     Output     |
+----------------------+-------------------------+----------------+
|                      |   +-> DASH -------------+-> DASH player  |
|    Encoder(1)        |   +-> RTMP/HDS  --------+-> Flash player |
|  (FMLE,FFMPEG, -rtmp-+->-+-> HLS/HTTP ---------+-> M3U8 player  |
|  Flash,XSPLIT,       |   +-> FLV/MP3/Aac/Ts ---+-> HTTP player  |
|  ......)             |   +-> Fowarder ---------+-> RTMP server  |
|                      |   +-> Transcoder -------+-> RTMP server  |
|                      |   +-> EXEC(5) ----------+-> External app |
|                      |   +-> DVR --------------+-> FLV file     |
|                      |   +-> BandwidthTest ----+-> Flash        |
+----------------------+                         |                |
|  MediaSource(2)      |                         |                |
|  (RTSP,FILE,         |                         |                |
|   HTTP,HLS,   --pull-+->-- Ingester(3) -(rtmp)-+-> SRS          |
|   Device,            |                         |                |
|   ......)            |                         |                |
+----------------------+                         |                |
|  MediaSource(2)      |                         |                |
|  (RTSP,FILE,         |                         |                |
|   HTTP,HLS,   --push-+->-- Streamer(4) -(rtmp)-+-> SRS          |
|   Device,            |                         |                |
|   ......)            |                         |                |
+----------------------+-------------------------+----------------+

```

Remark:

1. Encoder: Encoder pushs RTMP stream to SRS.
1. MediaSource: Supports any media source, ingesting by ffmpeg.
1. Ingester: Forks a ffmpeg(or other tools) to ingest as rtmp to SRS, please read [Ingest][v1_CN_Ingest].
1. Streamer: Remuxs other protocols to RTMP, please read [Streamer][v2_CN_Streamer].
1. EXEC: Like NGINX-RTMP, EXEC forks external tools for events, please read [ng-exec][v3_CN_NgExec].

## AUTHORS

There are two types of people that have contributed to the SRS project:

* Maintainers: Contribute and maintain important features. SRS always remembers and thanks you by writing your names in stream metadata.
* [Contributors][authors]: Submit patches, report bugs, add translations, help answer newbie questions, and generally make SRS much better.

Maintainers of SRS project:

* [Winlin](https://github.com/winlinvip): All areas of streaming server and documents.
* [Wenjie](https://github.com/wenjiegit): The focus of his work is on the [HDS](https://github.com/simple-rtmp-server/srs/wiki/v2_CN_DeliveryHDS) module.
* [Runner365](https://github.com/runner365): The focus of his work is on the [SRT](https://github.com/simple-rtmp-server/srs/wiki/v4_CN_SRTWiki) module.

A big THANK YOU goes to:

* All friends of SRS for [big supports][bigthanks].
* Genes amd Mabbott for creating [st][st]([state-threads][st2]).
* [Michael Talyanksy](https://github.com/michaeltalyansky) for introducing ST to us.

## Mirrors

OSChina: [https://gitee.com/winlinvip/srs.oschina][oschina], the GIT usage([CN][v1_CN_Git], [EN][v1_EN_Git])

```
git clone https://gitee.com/winlinvip/srs.oschina.git srs &&
cd srs && git remote set-url origin https://github.com/ossrs/srs.git && git pull
```

> Remark: For users in China, recomment to use mirror from CSDN or OSChina, because they are much faster.

Gitlab: [https://gitlab.com/winlinvip/srs-gitlab][gitlab], the GIT usage([CN][v1_CN_Git], [EN][v1_EN_Git])

```
git clone https://gitlab.com/winlinvip/srs-gitlab.git srs &&
cd srs && git remote set-url origin https://github.com/ossrs/srs.git && git pull
```

Github: [https://github.com/ossrs/srs][srs], the GIT usage([CN][v1_CN_Git], [EN][v1_EN_Git])

```
git clone https://github.com/ossrs/srs.git
```

| Branch | Cost | Size | CMD |
| --- | --- | --- | --- |
| 3.0release | 2m19.931s | 262MB | git clone -b 3.0release https://gitee.com/winlinvip/srs.oschina.git |
| 3.0release | 0m56.515s | 95MB | git clone -b 3.0release --depth=1 https://gitee.com/winlinvip/srs.oschina.git |
| develop | 2m22.430s | 234MB | git clone -b develop https://gitee.com/winlinvip/srs.oschina.git |
| develop | 0m46.421s | 42MB | git clone -b develop --depth=1 https://gitee.com/winlinvip/srs.oschina.git |
| min | 2m22.865s | 217MB | git clone -b min https://gitee.com/winlinvip/srs.oschina.git |
| min | 0m36.472s | 11MB | git clone -b min --depth=1 https://gitee.com/winlinvip/srs.oschina.git |

## System Requirements

Supported operating systems and hardware:

* All Linux, both 32 and 64 bits
* Other OS, such as Windows, please use [docker][docker-srs3].

Beijing, 2013.10<br/>
Winlin
