# 设置模块状态（SET MODULESTATUS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于设置一个平面上的所有的模块状态。

## 注意事项

该命令在升级或补丁时会自动执行，其他场景下严禁使用。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                               |
|:--------|:-------|:-------------------------------------------------------------------------------------------------------------------|
| PLNID   | 平面ID   | 用于标识平面ID。 取值范围：0～1。 默认值：无。                                                                                         |
| MT      | 模块类型   | 用于标识模块类型。 取值范围：DPU(DPU) DSG(DSG)BSG(BSG)CCU(CCU)PAU(PAU)HSF(HSF)NSF(NSF)ACF(ACF)APF(APF)ERU(ERU)：该模块类型为预留值。 默认值：无。 |
| SETTYPE | 模块状态   | 用于标识模块状态。 取值范围：ACTIVE：激活。INACTIVE：去激活。 默认值：无。                                                                      |
| UPGTYPE | 升级类型   | 用于标识升级类型。 取值范围：VER：升级。CPATCH：冷补丁。 默认值：无。                                                                           |

## 使用实例

```
SET MODULESTATUS: PLNID=0, MT=DPU, SETTYPE=ACTIVE;
```

```
%%SET MODULESTATUS: PLNID=0, MT=DPU, SETTYPE=ACTIVE;%%
RETCODE = 0  操作成功
---    END
```

## 输出结果说明

无。