#监控系统
EdgeGallery的样例应用，监控系统对外提供两个API，服务使用者可以上传人员照片，并在一定时间后调用人员活动信息获取接口，以获得人员的活动情况。
##添加人员接口
###功能介绍
向监控系统添加一个监测人员，人员添加后，监控系统将在监控范围内进行识别，识别到相关人员，将记录人员活动信息
####请求消息
```
URI: /v1/monitoring/persons
Method：POST
```
参数说明

| 参数名称 | 参数类型 | 是否必须 |参数说明 |
|----------|---------|---------|--------|
| file | form-data | 是 | 上传的图像文件，需要以人员名命名 |

请求参考示例：
无
####响应消息
响应参数说明

|参数名称 | 参数类型 | 参数描述 |
|--------|--------|--------|
|name | string| 人员名称 |
| image | string |人员图片|
响应参考实例：
```
{
    "name": "zhanghailong",
	"image": "zhanghailong.jpg"
}
```
##查询人员接口
###功能介绍
查询监控系统中的人员列表
####请求消息
```
URI: /v1/monitoring/persons
Method：GET
```
参数说明

NA

请求参考示例：
无
####响应消息
响应参数说明

|参数名称 | 参数类型 | 参数描述 |
|--------|--------|--------|
|         | array| 人员数组|
| +name | string| 人员名称 |
|  +image | string |人员图片|
响应参考实例：
```
[
  {
      "name": "zhanghailong",
	"image": "zhanghailong.jpg"
  }
]
```

##删除人员接口
###功能介绍
删除监控系统中的人员
####请求消息
```
URI: /v1/monitoring/persons/{personname}
Method：DELETE
```
参数说明
| 参数名称 | 参数类型 | 是否必须 |参数说明 |
|----------|---------|---------|--------|
| personname | string | 是 | 待删除的人员名|


请求参考示例：
无
####响应消息
响应参数说明

NA

##查询人员活动信息接口
###功能介绍
添加图片一段时间后，服务调用方可以通过该接口查询人员的活动信息
####请求消息
```
URI: /monitoring/v1/messages
Method: POST
```
参数说明

| 参数名称 | 参数类型 | 是否必须 |参数说明 |
|----------|---------|---------|--------|
|   |string Array | 是 | 查询的人员名列表 |

请求参考示例：
```
[
   "zhanghailong","chenchuanyu"
]

```
####响应消息
响应参数说明

|参数名称 | 参数类型 | 参数描述 |
|--------|--------|--------|
| | Array | 活动信息列表
|+personName | string| 人员名称 |
| +traces | Array |人员活动信息列表|
| ++traceId |integer |活动信息号 |
|++ Location | string | 活动位置 ，即出现在哪个摄像头前 |
|++time | string | 活动时间 |
响应参考实例：
```
[
    {
        "personName":"zhanghailong",
        "traces":[
            {
                "traceId":"1",
                "Location":"华为培训中心大门前",
                "time":"2020-12-11 10:35:22"
            },
            {
                "traceId":"2",
                "Location":"华为百草园门口",
                "time":"2020-12-11 11:20:10"
            }
        ]
    }
]
```
##查询单个人员活动信息接口
###功能介绍
添加图片一段时间后，服务调用方可以通过该接口查询人员的活动信息
####请求消息
```
URI: /v1/monitoring/persons/{personname}/messages
Method: GET
```
参数说明

参数说明
| 参数名称 | 参数类型 | 是否必须 |参数说明 |
|----------|---------|---------|--------|
| personname | string | 是 | 待删除的人员名|

请求参考示例：
NA

####响应消息
响应参数说明

|参数名称 | 参数类型 | 参数描述 |
|--------|--------|--------|
|personName | string| 人员名称 |
| traces | Array |人员活动信息列表|
| +traceId |integer |活动信息号 |
|+ Location | string | 活动位置 ，即出现在哪个摄像头前 |
|+time | string | 活动时间 |
响应参考实例：
```
    {
        "personName":"zhanghailong",
        "traces":[
            {
                "traceId":"1",
                "Location":"华为培训中心大门前",
                "time":"2020-12-11 10:35:22"
            },
            {
                "traceId":"2",
                "Location":"华为百草园门口",
                "time":"2020-12-11 11:20:10"
            }
        ]
    }
```
