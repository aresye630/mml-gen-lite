# 查询NEF全局订阅信息(LST NEFANYUEINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询数据库中所有用户漫游变更的NEF监视事件：

UDM与NEF通过N52接口进行订阅消息的交互。NEF发送订阅请求消息到UDM，UDM发现订阅的externalGroupId为AnyUE时，当用户发生漫游则触发漫游状态上报NEF。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询所有用户请求订阅的NEF监视事件信息：

```
LST NEFANYUEINFO: ;
```

```
%%LST NEFANYUEINFO:;%%
RETCODE = 0 SUCCESS0001:Operation is successful
NEFSUBID          NEFURL                                                                                                               REFID_ROAM                    UPDATE_TIME
63802a6d2f0c0079  http://10.185.27.42:33000/nudm-ee/callbackreference/v1/anyUE/ee-subscriptions/0894a118120d08811c120800e7412558fc5400 1                             2022-11-25 10:37:33
Total count = 1
There is together 1 report
---    END
```

## 输出结果说明

| 参数名称        | 参数描述                             |
|:------------|:---------------------------------|
| NEFSUBID    | 用于返回数据库中配置漫游变更监视事件的所在NEF的数据记录索引。 |
| NEFURL      | 用于返回漫游变更监视事件上报NEF的地址。            |
| REFID_ROAM  | 用户返回数据库中配置漫游变更监视事件的数据记录索引。       |
| UPDATE_TIME | 用于返回数据库中记录的漫游变更监视事件的订阅更新时间。      |