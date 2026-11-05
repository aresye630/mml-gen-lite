# 显示订阅任务信息（DSP NSSFNSSUBINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NSSF**

该命令用于查询所有AMF的订阅任务信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

当运营商想要查询所有AMF在NSSF上的订阅信息时，执行此命令

```
DSP NSSFNSSUBINFO:;
%%DSP NSSFNSSUBINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
订阅标识                              通知URI                                                                               AMF集合标识    通知事件类型                 订阅有效期    订阅的TAI数目

0004c7d76079f5a24517a4e03d90e484975c  http://10.70.183.1:5160/nnssf-nssaiavailability/v1/nssai-availability/subscriptions/  460-03-01-001  SNSSAI_STATUS_CHANGE_REPORT  1599895763    1
000154b35ab273514635a90f527d3a4a01d1  http://10.70.183.2:5260/nnssf-nssaiavailability/v1/nssai-availability/subscriptions/  460-03-01-001  SNSSAI_STATUS_CHANGE_REPORT  1599895764    1
(结果个数 = 2)

---    END
```

## 输出结果说明

| 输出项名称    | 输出项解释                                                                       |
|:---------|:----------------------------------------------------------------------------|
| 订阅标识     | 该字段表示本次订阅的订阅标识。                                                             |
| 通知URI    | 该字段表示订阅消息通知的URI。                                                            |
| AMF集合标识  | 该字段表示AMF集合的标识。                                                              |
| 通知事件类型   | 该字段表示通知事件类型。 取值说明： SNSSAI_STATUS_CHANGE_REPORT（SNSSAI_STATUS_CHANGE_REPORT） |
| 订阅有效期    | 该字段表示订阅消息的有效期。                                                              |
| 订阅的TAI数目 | 该字段表示订阅的TAI数目。                                                              |