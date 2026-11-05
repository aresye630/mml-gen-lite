# 查询5G定位服务参数（LST NGLCSPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF的定位服务功能的相关参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

无

## 使用实例

查询5G定位服务的参数，执行如下命令：

```
%%LST NGLCSPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
           定位服务功能开关  =  关闭
5G位置信息表老化定时器(min)  =  60
             5G定位服务策略  =  协议模式定位
          启用连接态LRC流程  =  否
          是否携带GUAMI信息  =  否
 是否校验LCS Correlation ID  =  否
                是否重选LMF  =  否
               是否使用SUPI  =  否
               是否使用GPSI  =  否
           园区定位增强开关  =  关闭
          缺省的LMF群组标识  =  NULL
               是否使用切片  =  否
    是否携带lcsQosClass信息  =  否
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                  | 输出项解释                                                                                                                        |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| 定位服务功能开关               | 该参数用于开启和关闭5G定位服务功能。                                                                                                          |
| 5G位置信息表老化定时器(min)      | 该参数用于设置AMF的位置信息表的老化定时器。当前该功能尚未实现。                                                                                            |
| 5G定位服务策略               | 该参数用于设置AMF的定位服务策略。                                                                                                           |
| 启用连接态LRC流程             | 该参数用于控制AMF收到GMLC的Namf_Location_ProvidePositioningInfo Request消息时，如果UE处于连接态，是否需要发起Location Reporting Control(LRC)流程获取最新的NCGI。 |
| 是否携带GUAMI信息            | 该参数用于控制AMF在Namf_Communication_N2InfoNotify Request和Namf_Communication_N1MessageNotify Request消息中是否携带为UE服务的GUAMI信息。           |
| 是否校验LCS Correlation ID | 该参数用于使能LCS Correlation ID校验功能。 LCS Correlation ID由AMF分配，用于标识一次定位流程，由AMF在发起LMF精准定位流程中传递给LMF，开启此功能可以避免LMF伪造场景带来的安全可靠问题。        |
| 是否重选LMF                | 该参数用于指定当AMF选择某个LMF进行定位流程，如果对端返回5xx原因值时，是否重新选择新的LMF再次重试业务请求。                                                                  |
| 是否使用SUPI               | 该参数用于指定是否使用用户的SUPI作为目标LMF的选择条件。                                                                                              |
| 是否使用GPSI               | 该参数用于指定是否使用用户的GPSI作为目标LMF的选择条件。                                                                                              |
| 园区定位增强开关               | 该参数用于控制AMF在MT-LR或周期性定位流程中，是否优先使用GMLC在Namf_Location_ProvidePositioningInfo Request消息中携带的lmfId去发现指定LMF。                        |
| 缺省的LMF群组标识             | 该参数用于指定缺省的LMF群组标识。当该参数非空时，定位流程AMF会使用本参数发现LMF。                                                                                |
| 是否使用切片                 | 该参数用于指定是否使用用户的切片作为目标LMF的选择条件。                                                                                                |
| 是否携带lcsQosClass信息      | 该参数用于控制AMF在Nlmf_Location_DetermineLocation Request消息中是否携带lcsQosClass信息。                                                      |