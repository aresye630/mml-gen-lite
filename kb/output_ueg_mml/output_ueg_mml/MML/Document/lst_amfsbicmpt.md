# 查询AMF服务化接口兼容性参数（LST AMFSBICMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF服务化接口兼容性参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识    | 参数名称    | 参数说明                                                                                                                                                                                                                                                        |
|:--------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SBITYPE | 服务化接口类型 | 可选必选说明：可选参数  参数含义：该参数用于指定服务化接口类型，根据接口类型来确认是否需要配置相应的消息接口兼容性。  数据来源：全网规划 取值范围： N8（AMF与UDM之间的接口）N11（AMF与SMF之间的接口）N12（AMF与AUSF之间的接口）N14（AMF与AMF之间的接口）N15（AMF与PCF之间的接口）N17（AMF与5G-EIR之间的接口）N20（AMF与SMSF之间的接口）N22（AMF与NSSF之间的接口）N50（AMF与CBCF之间的接口）  默认值：无  配置原则：无 |

## 使用实例

查询AMF服务化接口兼容性参数，执行如下命令：

```
%%LST AMFSBICMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                     时区变更是否通知SMF  =  否
                   是否给SMSF携带RATTYPE  =  否
                      是否携带RedCap指示  =  是
                    是否携带eDRX私有信元  =  否
                         是否携带PcfRfsp  =  否
                          是否携带动态NI  =  是
  是否携带UE Radio Capability for Paging  =  是
                   N15接口是否携带hpcfId  =  是
                    N14接口是否携带pcfId  =  是
                 N14接口是否携带pcfSetId  =  是
           N14接口是否携带pcfAmPolicyUri  =  是
   N14接口是否携带amPolicyReqTriggerList  =  是
                   N14接口是否携带hpcfId  =  是
               N14接口是否携带smfSelInfo  =  是
N14接口是否携带PEIPS信元以及寻呼分组标识  =  否
           N14接口是否携带pcfUePolicyUri  =  是
   N14接口是否携带uePolicyReqTriggerList  =  是
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                              | 输出项解释                                                                                     |
|:-----------------------------------|:------------------------------------------------------------------------------------------|
| N15接口是否携带hpcfId                    | 该参数用于控制用户创建AM策略偶联时，AMF是否携带hpcfId信元给AM-PCF。                                                |
| 时区变更是否通知SMF                        | 该参数用于控制AMF是否单独在向SMF发送Update SM Context Request消息更新时区或者夏令时信息。随路消息中携带时区和夏令时信息不受本参数控制。       |
| 是否给SMSF携带RATTYPE                   | 该参数用于控制AMF向SMSF发送Nsmsf_SMService_Activate Request消息时是否携带ratType信元。                        |
| 是否携带RedCap指示                       | 该参数用于控制RedCap用户的5G内Inter移动性流程中，AMF和对端AMF交互用户上下文时UeContext信元中是否携带redCapInd子信元。             |
| 是否携带eDRX私有信元                       | 该参数用于控制AMF Pool迁移流程中，AMF向目标AMF传递用户上下文时UeContext信元中是否携带eDRX相关的私有信元，包括eDRX寻呼周期和寻呼窗口时长。      |
| 是否携带PcfRfsp                        | 该参数用于控制用户的5G内Inter移动性流程中，AMF和对端AMF交互用户上下文时UeContext信元中是否携带pcfRfsp子信元。                     |
| 是否携带动态NI                           | 该参数用于控制Inter AMF流程与POOL迁移流程中老侧AMF是否在UeContext携带中携带AM-PCF下发的签约动态NI。                        |
| 是否携带UE Radio Capability for Paging | 该参数用于控制5G内Inter移动性流程中，AMF和对端AMF交互用户上下文时UeContext信元中是否携带UE Radio Capability for Paging子信元。 |
| N14接口是否携带pcfId                     | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfId信元给新侧AMF。                                        |
| N14接口是否携带pcfSetId                  | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfSetId信元给新侧AMF。                                     |
| N14接口是否携带pcfAmPolicyUri            | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfAmPolicyUri信元给新侧AMF。                               |
| N14接口是否携带amPolicyReqTriggerList    | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带amPolicyReqTriggerList信元给新侧AMF。                       |
| N14接口是否携带hpcfId                    | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带hpcfId信元给新侧AMF。                                       |
| N14接口是否携带smfSelInfo                | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带smfSelInfo信元给新侧AMF。                                   |
| N14接口是否携带PEIPS信元以及寻呼分组标识           | 该参数用于控制AMF Pool迁移流程中，AMF向目标AMF传递用户上下文时UeContext信元中是否携带PEIPS信元以及寻呼分组标识。                    |
| N14接口是否携带pcfUePolicyUri            | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfUePolicyUri信元给新侧AMF。                               |
| N14接口是否携带uePolicyReqTriggerList    | 该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带uePolicyReqTriggerList信元给新侧AMF。                       |