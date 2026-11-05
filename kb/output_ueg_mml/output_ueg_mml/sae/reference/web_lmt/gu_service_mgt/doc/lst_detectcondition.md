# 查询检测条件(LST DETECTCONDITION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统配置的IMEI轨迹变化异常用户筛选条件。

系统根据配置将指定时间内，位置信息发生多次变化的用户视为可疑用户，并记录该用户信息（包含位置信息）到IMEI变化轨迹异常用户记录结果文件。方便运营商快速识别定位可疑用户，提高客户网络安全能力。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询系统配置的IMEI轨迹变化异常用户筛选条件记录。

```
LST DETECTCONDITION:;
```

```
+++    USCDB        2024-04-18 19:39:23
PGW    #009553
%%LST DETECTCONDITION:;%%
RETCODE = 0 SUCCESS0001:Operation is successful
                      INTERVAL = 120
                         TIMES = 3
                     STARTHOUR = 1
                   STARTMINUTE = 0
                    FILEPREFIX = result
                   STORAGETIME = 180
Total count = 6
There is together 1 report
---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET DETECTCONDITION**命令的参数说明。