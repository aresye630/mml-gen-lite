# 显示规格配置项信息（DSP SPECCFGINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、SGW-U、UPF**

该命令用于显示不同微服务中的规格配置项的值。

#### 注意事项

每一行显示一个规格配置项在各个服务生效的值，如果对应的服务未使用则显示“-”。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                          |
|:------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVICENAME | 微服务名称  | 可选必选说明：可选参数 参数含义：该参数用于指定要查询规格配置项的微服务名称。 数据来源：本端规划 取值范围：字符串类型，长度1~127，区分大小写。 默认值：无 配置原则：当不指定微服务名称时，查询结果以Pod类型_微服务名称作为每一列显示；当前指定微服务名称时，查询结果以Pod名称_微服务名称作为每一列显示。 |

#### 使用实例

当需要查询产品内各个服务的规格配置信息时，可以采用以下操作：

```
DSP SPECCFGINFO: SERVICENAME="SessionSGExecSvc";
```

```
RETCODE = 0  操作成功

结果如下
--------
结果

                        ItemName  ssgpod-0_SessionSGExecSvc
                TOTAL_PDP_NUMBER                      10245
                     PDR_PER_PDP                      61470
                TOTAL_PKT_NUMBER                      10000
             MSGBUFF_NODE_NUM_L3                       3000
        CF_PROFILE_ARRAY_PER_PDP                      10245
              FAR_FILTER_PER_PDP                       6147
                   RULE_NAME_NUM                        600
          SM_DOMAIN_NODE_MAX_NUM                      50000
                     BAR_PER_PDP                      10245
             MSGBUFF_NODE_NUM_L2                       5500
                     SRR_PER_PDP                      12294
       HEADEN_BUFFER_RATIO_TO_FD                         15
                     SDF_PER_PDP                      81960
                FAST_FAR_PER_PDP                      10245
             SPECIAL_URR_PER_PDP                      51225
PM_MULTIDNN_DOMAIN_HASH_NODE_NUM                      12256

(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 结果      | 查询结果。   |