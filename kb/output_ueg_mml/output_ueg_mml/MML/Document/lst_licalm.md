# 查询License告警阈值(LST LICALM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询License容量告警配置数据。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                             |
|:--------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LICITEM | License控制项 | 可选必选说明：可选参数 该参数表示查询License控制项的告警阈值数据，当不输入参数值时，表示查询所有License控制项的告警阈值数据。 取值范围：AUSF_Basic_TPS(AUSF Basic TPS)AAA_Basic_TPS(AAA_Basic_TPS)BSF_Basic_TPS(BSF_Basic_TPS)AP_Basic_TPS(AP_Basic_TPS)  说明： “AAA_Basic_TPS(AAA_Basic_TPS)”，“BSF_Basic_TPS(BSF_Basic_TPS)”和“AP_Basic_TPS(AP_Basic_TPS)”仅在Full-stack虚机场景下支持。 |

## 使用实例

- 查询AUSF TPS License控制项的告警阈值数据：

  ```
  LST LICALM: LICITEM=AUSF_Basic_TPS;
  ```

  ```
  %%LST LICALM: LICITEM=AUSF_Basic_TPS;%%
  RETCODE = 0  操作成功

     License控制项  =  AUSF_Basic_TPS
      预警告警门限  =  44
  预警告警恢复门限  =  43
      过载告警门限  =  49
  过载告警恢复门限  =  48
  (结果个数 = 1)

  ---    END
  ```
- 查询所有控制项的告警阈值数据：

  ```
  LST LICALM:;
  ```

  ```
  %%LST LICALM:;%%
  RETCODE = 0  操作成功

  操作结果如下:
  -------------
  License控制项   预警告警门限  预警告警恢复门限  过载告警门限  过载告警恢复门限  

  AUSF_Basic_TPS  45            44                50            49                
  AAA_Basic_TPS   45            44                50            49                
  BSF_Basic_TPS   45            44                50            49                
  AP_Basic_TPS    45            44                50            49                
  (结果个数 = 4)

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET LICALM**命令的参数说明。