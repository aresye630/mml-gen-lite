# 显示NSSF收发消息内部统计（DSP NSSFMSGSTAT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NSSF**

该命令用于查询NSSF收发消息内部统计。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

运营商想要查询NSSF收发消息内部统计信息，执行此命令。

```
DSP NSSFMSGSTAT:;
%%DSP NSSFMSGSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
功能实体名称                                      发送消息数目     接收消息数目
[uncpod-0]nssf/cellcore/cell-service-NssfExecSvc  6                6
[uncpod-1]nssf/cellcore/cell-service-NssfExecSvc  0                0
[uncpod-2]nssf/cellcore/cell-service-NssfExecSvc  2                1
(结果个数 = 3)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                |
|:--------|:-------------------------------------|
| 功能实体名称  | 该参数用于表示功能实体名称，所有实体的收发消息之和为整网元的收发消息数。 |
| 发送消息数目  | 该参数用于表示发送消息数目。                       |
| 接收消息数目  | 该参数用于表示接收消息数目。                       |