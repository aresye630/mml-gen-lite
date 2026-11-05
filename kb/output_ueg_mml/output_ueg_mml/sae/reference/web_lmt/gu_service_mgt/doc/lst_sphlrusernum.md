# 查询Service Partition虚拟HLR最大用户数(LST SPHLRUSERNUM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于在vRouting Partition/vRouting\_Service Partition下查询Service Partition虚拟HLR最大用户数的配置信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称                | 参数说明                                                           |
|:-------|:--------------------|:---------------------------------------------------------------|
| PID    | Service Partition标识 | 用于指示系统需要按照哪个Service Partition标识来查询Service Partition虚拟HLR最大用户数。 |
| HLRSN  | HLR序列号              | 用于指示系统需要按照哪个HLR序列号来查询Service Partition虚拟HLR最大用户数。              |

## 使用实例

查询Service Partition虚拟HLR最大用户数：

```
LST SPHLRUSERNUM: PID=1, HLRSN=1;
```

```
%%LST SPHLRUSERNUM: PID=1, HLRSN=1;%%
RETCODE = 0 SUCCESS0001:操作成功

                 MAXUSERNUM = 10000
              MAXEPSUSERNUM = 20000
              MAXIMSUSERNUM = 0

Total count = 3

There is together 1 report

---    END
```