# 查询指定用户范围的S1模式信令抑制策略(LST S1SMARTPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询指定用户范围的S1模式信令抑制策略。

#### 注意事项

无

#### 本地用户权限

manage-ug; system-ug; monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称     | 参数说明                                                                                                                                          |
|:----------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE  | 用户范围     | 可选必选说明：必选参数 参数含义：该参数用于指定用户检测范围。 数据来源：整网规划 取值范围： IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。MSISDN_PREFIX（指定MSISDN前缀）：表示用户范围通过MSISDN前缀指定。 默认值：无    |
| IMSIPRE   | IMSI前缀   | 可选必选说明：条件必选参数 参数含义：该参数用于指定IMSI前缀以区分不同的用户群。 前提条件：该参数只有“SUBRANGE（用户范围）”为“IMSI_PREFIX（指定IMSI前缀）”时，该参数才有效。 数据来源：整网规划 取值范围：5～15位十进制字符串 默认值：无       |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：条件必选参数 参数含义：该参数用于指定MSISDN前缀以区分不同的用户群。 前提条件：该参数只有“SUBRANGE（用户范围）”为“MSISDN_PREFIX（指定MSISDN前缀）”时，该参数才有效。 数据来源：整网规划 取值范围：5～15位十进制字符串 默认值：无 |

#### 使用实例

查询“IMSI前缀”为“123456789”的指定用户范围的S1模式信令抑制策略的配置记录：

```
LST S1SMARTPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456789";
```

```
%%LST S1SMARTPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456789";%%
 RETCODE = 0  Operation succeeded

 The result is as follows
 ------------------------
                        用户范围  =  IMSI Prefix
                        IMSI前缀  =  123456789
                      MSISDN前缀  =  NULL
          附着异常识别门限（次）  =  30
          附着异常测量周期（秒）  =  3600
        附着异常抑制时长（分钟）  =  60
                    附着抑制措施  =  NULL
                    附着拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
      服务请求异常识别门限（次）  =  100
      服务请求异常测量周期（秒）  =  3600
    服务请求异常抑制时长（分钟）  =  60
                服务请求抑制措施  =  NULL
                服务请求拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
  控制面服务请求异常识别门限(次)  =  100
  控制面服务请求异常测量周期(秒)  =  3600
控制面服务请求异常抑制时长(分钟)  =  60
          控制面服务请求抑制措施  =  NULL
          控制面服务请求拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
         PDN连接异常识别门限（次）=  30
       PDN连接异常测量周期（秒）  =  3600
     PDN连接异常抑制时长（分钟）  =  60
                  PDN连接抑制措施 =  NULL
                 PDN连接拒绝原因  =  MULTI_PDN_FOR_APN_NOT_ALLOWED_55
           Backoff Timer分配开关  =  关闭
      Back off timer最小值（秒）  =  660
      Back off timer最大值（秒）  =  3000
                     Parking APN  =  NULL
                    抑制分离原因  =  NO_SUITABLE_CELLS_IN_TA_15
             Parking APN唤醒措施  =  网络侧去激活
 (Number of results = 1)
  ---    END
```

#### 输出结果说明

参见ADD S1SMARTPLCY的参数说明。