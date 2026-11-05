# 查询容灾探测配置数据(LST DETECTCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询容灾探测配置数据的基本信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

为了查询主用局配置的容灾探测数据信息，需要执行如下命令：

```
LST DETECTCFG:;
```

```
%%LST DETECTCFG:;%%
RETCODE = 0 SUCCESS0001:操作成功

"REDUNDANCY_DETECT_TYPE"
                           23G = TRUE
                           EPS = FALSE
                           IMS = FALSE
      REDUNDANCY_DETECT_PERIOD = 5
        REDUNDANCY_DETECT_IMSI = NULL
       REDUNDANCY_DETECT_VLRNO = 222222222
     REDUNDANCY_DETECT_MMEHOST = NULL
    REDUNDANCY_DETECT_MMEREALM = NULL
    REDUNDANCY_DETECT_CSCFHOST = NULL
   REDUNDANCY_DETECT_CSCFREALM = NULL

Total count = 10

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。各参数含义请参见**SET DETECTCFG**命令的参数说明。