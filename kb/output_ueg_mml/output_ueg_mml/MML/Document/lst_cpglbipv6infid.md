# 查询整机IPv6接口ID配置（LST CPGLBIPV6INFID）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

此命令用于查询IMSI作为用户的IPv6地址Interface ID功能开关配置信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询IMSI作为用户的IPv6地址Interface ID功能配置：

```
%%LST CPGLBIPV6INFID:;%%
RETCODE = 0  操作成功

结果如下
--------
配置IMSI作为IPv6 Interface ID  =  不使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                     | 输出项解释                                      |
|:--------------------------|:-------------------------------------------|
| 配置IMSI作为IPv6 Interface ID | 该参数用于控制开启和关闭IMSI作为用户的IPv6地址Interface ID功能。 |