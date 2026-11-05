# 查询Inter-AMF流控参数（LST INTERAMFFC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询Inter-AMF接入流控功能的相关参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询Inter-AMF单POD接入流控参数，执行如下命令：

```
%%LST INTERAMFFC:;%%
RETCODE = 0  操作成功

结果如下
--------
           Inter-AMF接入流控功能开关  =  开启
Registration Request流控阈值作用范围  =  单POD
 Registration Request速率门限(个/秒)  =  300
     Service Request流控阈值作用范围  =  单POD
      Service Request速率门限(个/秒)  =  300
                      告警上报周期数  =  3
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                         | 输出项解释                                               |
|:------------------------------|:----------------------------------------------------|
| Inter-AMF接入流控功能开关             | 用于开启或关闭Inter-AMF接入流控功能。                             |
| Registration Request流控阈值作用范围  | 该参数用于设置Registration Request消息流控阈值的作用范围。             |
| Registration Request速率门限(个/秒) | 用于设置Registration Request速率门限。                       |
| Service Request流控阈值作用范围       | 该参数用于设置Service Request消息流控阈值的作用范围。                  |
| Service Request速率门限(个/秒)      | 用于设置Service Request速率门限。                            |
| 告警上报周期数                       | 该参数用于设置连续几个5秒周期处于流控态上报“ALM-100251 Inter-AMF流控起控”告警。 |