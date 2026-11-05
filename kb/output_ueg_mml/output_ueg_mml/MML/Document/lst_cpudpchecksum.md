# 查询UNC发送的UDP报文是否携带checksum（LST CPUDPCHECKSUM）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来查询UNC发送的UDP报文是否携带checksum。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询UNC发送的UDP报文是否携带checksum：

```
%%LST CPUDPCHECKSUM:;%%
RETCODE = 0  操作成功

结果如下
--------
    UDP Type = DHCP
Checksum开关 = 不使能   
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称      | 输出项解释                       |
|:-----------|:----------------------------|
| UDP Type   | 指定是何种类型的报文。                 |
| Checksum开关 | 指定UNC发送的UDP报文中是否携带checksum。 |