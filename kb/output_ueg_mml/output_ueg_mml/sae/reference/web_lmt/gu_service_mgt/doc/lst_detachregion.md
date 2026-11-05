# 查询退网区域（LST DETACHREGION）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询退网区域数据。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                          |
|:-----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| REGIONTYPE | 区域类型   | 可选必选说明：必选参数 参数含义：用于标识查询退网区域的区域类型。 取值范围 ALLOWMMELIST：支持MME控制用户2G退网。NOTALLOWMMELIST：支持MME控制用户2G不退网。ALLVPLMNLIST：支持VPLMN控制用户2G退网。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询“区域类型”为“ALLOWMMELIST”的退网区域信息。

   ```
   LST DETACHREGION: REGIONTYPE=ALLOWMMELIST;
   ```

   ```
   %%LST DETACHREGION: REGIONTYPE=ALLOWMMELIST;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   REGION              MMEHOST
   ALLOWMMELIST        mmec11.mmegi0429.mme.epc.mne000.m00460.3gppnetworkorg
   ALLOWMMELIST        mmec11.mmegi0430.mme.epc.mne000.m00460.3gppnetworkorg

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。