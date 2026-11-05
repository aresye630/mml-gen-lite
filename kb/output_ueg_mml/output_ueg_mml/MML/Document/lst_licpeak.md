# 查询License话务高峰信息(LST LICPEAK)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询License话务高峰信息：

- 若要查询所有License的全部峰值情况，请不要输入“License控制项”、“年份”参数。
- 若要查询对应License的对应年份的峰值情况，请输入“License控制项”、“年份”参数。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                 |
|:---------|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LICITEM  | License控制项 | 可选必选说明：可选参数 参数含义：用于返回License控制项名称。 取值范围：AUSF_Basic_TPS(AUSF Basic TPS)AAA_Basic_TPS(AAA_Basic_TPS)BSF_Basic_TPS(BSF_Basic_TPS)AP_Basic_TPS(AP_Basic_TPS) 默认值：无。 配置原则： “AAA_Basic_TPS(AAA_Basic_TPS)”，“BSF_Basic_TPS(BSF_Basic_TPS)”和“AP_Basic_TPS(AP_Basic_TPS)”仅在Full-stack虚机场景下支持。 |
| PEAKYEAR | 年份         | 可选必选说明：可选参数 参数含义：用于指定License控制项信息存储的年份，区分新数据还是旧数据。 取值范围： THIS_YEAR：存储年份为今年，是新数据。LAST_YEAR：存储年份为去年，是旧数据。 默认值：无。 配置原则：无。                                                                                                                                                               |

## 使用实例

1. 设置参数“LICITEM”取值为“AUSF\_Basic\_TPS”，“PEAKYEAR”取值为“THIS\_YEAR”，执行**LST LICPEAK**命令，此时显示对应License的对应年份的峰值情况：

   ```
   %%LST LICPEAK: LICITEM=AUSF_Basic_TPS, PEAKYEAR=THIS_YEAR;%%
   RETCODE = 0  操作成功

   License控制项   年份       日期        峰值TPS  过载次数  License已使用高峰次数  
   AUSF Basic TPS  THIS_YEAR  2019-10-31  300      300       0                      
   AUSF Basic TPS  THIS_YEAR  2019-11-01  9000     14        0                      
   (结果个数 = 2)

   ---    END
   ```
2. 不设置“LICITEM”参数和“PEAKYEAR”参数，执行**LST LICPEAK**命令，此时显示所有License的全部峰值情况：

   ```
   %%LST LICPEAK:;%%
   RETCODE = 0  操作成功

   License控制项   年份       日期        峰值TPS  过载次数  License已使用高峰次数 
   AUSF Basic TPS  THIS_YEAR  2019-10-31  300      300       0        
   AUSF Basic TPS  THIS_YEAR  2019-11-01  9000     14        0                     
   AUSF Basic TPS  LAST_YEAR  2019-10-31  300      1352      0 
   AAA_Basic_TPS   THIS_YEAR  2024-06-05  0        0         0                      
   AAA_Basic_TPS   THIS_YEAR  2024-06-06  0        0         0
   (结果个数 = 5)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD LICPEAK**命令的参数说明。