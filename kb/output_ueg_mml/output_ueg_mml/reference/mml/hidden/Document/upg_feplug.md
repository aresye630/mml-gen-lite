# 升级FE插件（UPG FEPLUG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于升级USCDB存在的FE插件。

## 注意事项

在升级FE插件时，升级框架自动执行该命令。其他场景严禁执行该命令。

## 参数说明

| 参数ID          | 参数名称        | 参数描述                                               |
|:--------------|:------------|:---------------------------------------------------|
| FETYPE        | FE类型        | FE插件包类型。 取值范围：1～1023                               |
| UPFILENAME    | FE插件包名称     | FE插件包名称。                                           |
| TYPE          | FE插件升级类型    | FE插件升级类型。 取值范围：VER：版本升级。FEPLUG：插件包升级。CPATCH：冷补丁升级。 |
| UPGSCRIPTFILE | FE插件数据包名称   | FE插件数据包名称。                                         |
| SDBUPGFILE    | FE插件数据升级包名称 | FE插件数据升级包名称。                                       |
| UPGMOD        | FE插件升级模式    | FE插件升级模式。 取值范围：0～1023。                             |

## 使用实例

```
UPG FEPLUG: UPFILENAME="SUP-FE_PLUGV900R006C00B082.tar", TYPE=FEPLUG, UPGSCRIPTFILE="SUP-FEV900R006C00B082_UPG.tar", SDBUPGFILE="SUP-FE_SUP-FE9820V900R006C00B082_SDB_UPG.tar", UPGMOD=255, FETYPE=33;
```

```
%%UPG FEPLUG: UPFILENAME="SUP-FE_PLUGV900R006C00B082.tar", TYPE=FEPLUG, UPGSCRIPTFILE="SUP-FEV900R006C00B082_UPG.tar", SDBUPGFILE="SUP-FE_SUP-FE9820V900R006C00B082_SDB_UPG.tar", UPGMOD=255, FETYPE=33;%%
RETCODE = 0  操作成功
```

## 输出结果说明

无。