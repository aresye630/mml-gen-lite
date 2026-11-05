# 查询APN优先级配置(LST PDPFILTERAPN)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询APN优先级配置。

#### 注意事项

- 该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                        |
|:---------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE | 用户范围   | 可选必选说明：可选参数 该参数用于指定PDP过滤功能适用的用户范围。参考SET PDPFILTERCTL命令。 数据来源：整网规划 取值范围： “ALL_USER(所有用户)”“LOCAL_USER(本网用户)”“FOREIGN_USER(外网用户)”“IMSI_PREFIX(指定IMSI前缀)” 默认值：无 |
| IMSIPRE  | IMSI前缀 | 可选必选说明：条件可选参数 参数含义：该参数用于指定IMSI前缀。 前提条件: 该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”时生效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串。 默认值：无                                      |
| APNNI    | APNNI  | 可选必选说明：可选参数 参数含义：该参数用于指定APNNI名称 数据来源：整网规划 取值范围：1～62位字符串。 默认值：无                                                                                              |

#### 使用实例

1. 查询所有APN优先级记录：

   LST PDPFILTERAPN:;

   ```
   %%LST PDPFILTERAPN:;%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
    用户范围      IMSI前缀  APNNI        优先级  描述  

    指定IMSI前缀  12302     HUAWEI4.COM  1       NULL  
    指定IMSI前缀  12302     HUAWEI5.COM  2       NULL  
    指定IMSI前缀  1230      HUAWEI3.COM  1       NULL  
    本网用户      NULL      HUAWEI2.COM  1       NULL  
    所有用户      NULL      HUAWEI1.COM  1       NULL  
   (结果个数 = 5)

   ---    END
   ```
2. 查询“用户范围”为“指定IMSI范围”，“IMSI前缀”为“12302”的APN优先级记录：

   LST PDPFILTERAPN: SUBRANGE=IMSI\_PREFIX, IMSIPRE="12302";

   ```
   %%LST PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12302";%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
    用户范围      IMSI前缀  APNNI        优先级  描述  

    指定IMSI前缀  12302     HUAWEI4.COM  1       NULL  
    指定IMSI前缀  12302     HUAWEI5.COM  2       NULL  
   (结果个数 = 2)

   ---    END
   ```

#### 输出结果说明

参见**ADD PDPFILTERAPN**的参数说明。