# 查询APN访问控制参数（LST CPAPNACCESSCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于查询APN访问控制策略相关参数信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------|
| APN    | APN名称  | 可选必选说明：可选参数  参数含义：该参数用于指示APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。  默认值：无  配置原则：  该参数使用ADD CPAPN命令配置生成。 |

## 使用实例

该命令支持全局查询。当需要查询指定APN名称为huawei.com的访问控制参数信息时，可以执行如下命令

```
%%LST CPAPNACCESSCTRL: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
                               APN名称  =  huawei.com
      SMF/PGW/GGSN拜访用户接入功能开关  =  使能
                   最大带宽(兆比特/秒)  =  0
               最大保证带宽(兆比特/秒)  =  0
                           最大PDP数目  =  0
              不携带MSISDN用户激活策略  =  使能
       Apn-restriction本地校验功能开关  =  使能
               Apn-restriction功能开关  =  不使能
                 Apn-restriction最大值  =  0
              用户选择模式检查功能开关  =  不使能
           SMF用户选择模式检查功能开关  =  不使能
                 Ms提供APN用户激活策略  =  不使能
         Ms/Network提供APN用户激活策略  =  使能
            Network提供APN用户激活策略  =  不使能
     SMF/SGW上控制漫游用户接入功能开关  =  使能
     SMF/SGW上控制拜访用户接入功能开关  =  使能
SMF/PGW/GGSN上控制漫游用户接入功能开关  =  使能
                不携带IMSI用户激活策略  =  继承全局
                   APN跨省漫游限制开关  =  不使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                                                                                                                                                                                        |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN名称                      | 该参数用于指示APN名称。                                                                                                                                                                                                |
| SMF/P-GW/GGSN拜访用户接入功能开关    | 该参数用于指示是否允许拜访用户接入GGSN或PGW-C或SMF的指定APN。                                                                                                                                                                       |
| 最大带宽(兆比特/秒)                | 该参数用于指示最大带宽(GBR)。                                                                                                                                                                                            |
| 最大保证带宽(兆比特/秒)              | 该参数用于指示最大保证带宽(GBR)。                                                                                                                                                                                          |
| 最大PDP数目                    | 该参数用于指示APN下允许激活的最大PDP上下文数，包含2345G承载数，0表示不控。                                                                                                                                                                  |
| 不携带MSISDN用户激活策略            | 该参数用于指示APN下是否允许不携带MSISDN的用户激活。                                                                                                                                                                               |
| Apn-restriction本地校验功能开关    | 该参数用于指示当开启支持Apn-restriction功能时是否支持对Apn-restriction的本地校验。                                                                                                                                                     |
| Apn-restriction功能开关        | 该参数用于指示是否支持Apn-restriction功能。用来确定该APN下的用户是否可以在别的APN上建立上下文。                                                                                                                                                   |
| Apn-restriction最大值         | 该参数用于指示允许接入的Apn-restriction的最大值。                                                                                                                                                                             |
| 用户选择模式检查功能开关               | 该参数用于指示是否检查2/3/4G用户携带的选择模式信息。                                                                                                                                                                                |
| SMF用户选择模式检查功能开关            | 该参数用于指示是否检查通过SMF接入的用户携带的选择模式信息。                                                                                                                                                                              |
| Ms提供APN用户激活策略              | 该参数用于指示当用户激活消息中携带的Selection Mode取值为1或者用户创建SM上下文消息中携带的信元DnnSelectionMode为UE_DNN_NOT_VERIFIED时，是否允许用户激活。Selection Mode取值为1或者UE_DNN_NOT_VERIFIED，表示激活消息中携带的APN属于如下类型：MS provided APN，subscription not verified。 |
| Ms/Network提供APN用户激活策略      | 该参数用于指示当用户激活消息中携带的Selection Mode取值为0或者用户创建SM上下文消息中携带的信元DnnSelectionMode为VERIFIED时，是否允许用户激活。Selection Mode取值为0或者VERIFIED，表示激活消息中携带的APN属于如下类型：MS or network provided APN， subscribed verified。                 |
| Network提供APN用户激活策略         | 该参数用于指示当用户激活消息中携带的Selection Mode取值为2或者用户创建SM上下文消息中携带的信元DnnSelectionMode为NW_DNN_NOT_VERIFIED时，是否允许用户激活。Selection Mode取值为2，表示激活消息中携带的APN属于如下类型：Network provided APN，subscription not verified。                 |
| SMF/S-GW上控制漫游用户接入功能开关      | 该参数用于指示是否允许漫游用户接入SGW-C或者Proxy SGW-C或者V-SMF的指定APN。                                                                                                                                                            |
| SMF/S-GW上控制拜访用户接入功能开关      | 该参数用于指示SGW-C或者Proxy SGW-C或者I-SMF指定APN是否允许拜访用户接入。                                                                                                                                                             |
| SMF/P-GW/GGSN上控制漫游用户接入功能开关 | 该参数用于指示GGSN或者PGW-C或者H-SMF指定APN是否允许漫游用户接入。                                                                                                                                                                    |
| 不携带IMSI用户激活策略              | 该参数用于指定APN下是否允许不携带IMSI的用户激活。                                                                                                                                                                                 |
| APN跨省漫游限制开关                | 该参数用于控制是否开启APN跨省漫游限制策略。当开关开启后，专用APN/DNN用户跨省漫游时会话继续保持，PDN/PDU会话速率限制为0。该参数可以与ADD APNWHITENODE配合使用。                                                                                                             |