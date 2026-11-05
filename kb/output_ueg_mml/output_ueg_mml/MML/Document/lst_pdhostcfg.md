# 查询PCRF目的主机配置（LST PDHOSTCFG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询业务处理中需要与目的主机相关的配置。如果需要查询PCRF和AF目的主机的所有配置信息，请不要输入任何参数；如果需要查询某个PCRF或AF目的主机配置信息，请依据参数说明输入查询条件。

## 注意事项

无。

## 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:--------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCRFID        | PCRF标识   | 用于标识PCRF实体，该参数必须先由ADD PCRF命令定义，然后才能在此处索引。 取值范围：1 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| HOSTID        | 目的主机ID   | 目的主机ID。 取值范围：0～511 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| APPTYPE       | 应用类型     | 目的主机的应用类型。 取值说明： PCEFDefaultPCEFDynamicPCEFAFDefaultAFDynamicAF 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DEN           | 目的实体名称   | 目的实体名称。 取值范围：长度不超过128的字符串 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DHN           | 目的主机名    | 目的主机名称。当APPTYPE为DefaultPCEF或DefaultAF时，不能配置。当APPTYPE为DynamicPCEF或DynamicAF时，可以配置为实际主机名的子串，支持上线过程中对主机名的模糊匹配。最多只允许配置8个APPTYPE为DynamicPCEF和8个APPTYPE为DynamicAF的目的主机。主机名按规则匹配。对于Gx接口的请求消息，用户上线过程中使用上行消息中的原Host name优先匹配APPTYPE为PCEF的配置记录。如果匹配PCEF类型失败，就匹配APPTYPE为DynamicPCEF的配置记录，根据上行原Host Name字符串包含配置DHN判断是否匹配，多条记录时按DHN的长度由大到小排序，如果长度相同，优先匹配ID小的。如果上述两种方式都没有匹配成功则使用DefaultPCEF配置，如果没有配置DefaultPCEF，则回应失败CCA，携带错误码DIAMETER_UNKNOWN_PEER 3010。用户在线过程中目的主机配置中DynamicPCEF类型的配置发生变更不影响当前已经在线的用户，新上线的用户按新记录进行匹配。 对于Rx接口的请求消息，用户上线过程中使用上行消息中的原Host name优先匹配APPTYPE为AF的配置记录。如果匹配AF类型失败，就匹配APPTYPE为DynamicAF的配置记录，根据上行原Host Name字符串包含配置DHN判断是否匹配，多条记录时按DHN的长度由大到小排序，如果长度相同，优先匹配ID小的。如果上述两种方式都没有匹配成功则使用DefaultAF配置，如果没有配置DefaultAF，则默认AF能力字典ID为0。用户在线过程中目的主机配置中DynamicAF类型的配置发生变更不影响当前已经在线的用户，新上线的用户按新记录进行匹配。 取值范围：长度不超过127的字符串 默认值：无。 |
| ABILITYDICTID | 能力字典ID   | 用于选择PCEF或AF的能力字典。 取值范围：0～127 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PCEFCAT       | 对端PCEF类别 | 对端PCEF实体的类别，只在多PCEF场景下使用。 取值范围：由ADD PPCEFCAT命令定义的PCRF对端PCEF类别。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PPCEFGROUP    | 对端PCEF组  | 对端PCEF的组信息，可用于多PCEF场景下的PCEF分组。在APPTYPE为DefaultPCEF时，不能配置。 取值说明： NULL(NULL)Group1(Group1)～Group64(Group64) 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| CUSTOMATTR    | 自定义属性    | 用于具体描述一个对端PCEF的自定义属性，以便于扩展。其值域类型为字符串，区分大小写，当APPTYPE取值为PCEF时，可以设置该参数。 取值范围：长度不超过32的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IPDOMAIN      | IP地址域    | 用于标识对端关联的IP地址域。当APPTYPE为PCEF/DefaultPCEF/DynamicPCEF时，该参数才显示且为可选参数。 取值范围：长度为0~255的字符串。 取值说明：如果配置为字符串“NULL”则PCF按未配置处理。 默认值：无。  说明： 本参数不能设置为“NULL”，否则不生效。本参数参与会话绑定时，按“VRM_IPDOMAINSENSITIVE”的取值决定是否大小写敏感。“VRM_IPDOMAINSENSITIVE”取值为“1”时，修改本参数对已在线的Gx会话不生效，对新上线的Gx会话生效。本参数只在“VRM_IPDOMAINSRCFORGX”取值为“1”且SET BINDCFG中“IPV4IPDOMAIN”设置为“Support”时生效。修改“VRM_IPDOMAINSRCFORGX”取值为“1”前，建议先调整“IPDOMAIN”参数为目标值。                                                                                                                                                                                                                                                                                                                                                                                                                      |

## 使用实例

1. 查询所有的PCRF目的主机配置信息。

   ```
   LST PDHOSTCFG:;
   ```

   ```
   %%LST PDHOSTCFG:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
    PCRF标识  目的主机ID  应用类型          目的实体名称              目的主机名                  能力字典ID            对端PCEF类别        对端PCEF组      自定义属性      IP地址域

    1         0           Default PCEF      11                       NULL                        67                     MPCEF01             NULL             NULL           NULL      
    1         2           PCEF              NULL                     10.96.100.236_MPCEF_GGSN6   80                     NULL                NULL             fet            NULL    
    1         4           PCEF              NULL                     etewq                       90                     NULL                NULL             NULL           NULL      
    1         5           PCEF              NULL                     test1                       90                     NULL                NULL             NULL           NULL      
    1         6           PCEF              NULL                     test3                       90                     NULL                NULL             NULL           NULL      
    1         7           PCEF              NULL                     test4                       90                     NULL                NULL             dsfa           NULL  
   (结果个数 = 6)

   ---    END
   ```
2. 查询一条PCRF目的主机配置信息。“PCRF标识”为“1”，“目的主机ID”为“5”。

   ```
   LST PDHOSTCFG: PCRFID=1, HOSTID=5;
   ```

   ```
   %%LST PDHOSTCFG: PCRFID=1, HOSTID=5;%%
   RETCODE = 0  Operation succeeded

   The result is as follows
   ------------------------
                   PCRF标识  =  1
                 目的主机ID  =  5
                   应用类型  =  PCEF
               目的实体名称  =  NULL
                 目的主机名  =  test1
                 能力字典ID  =  90
               对端PCEF类别  =  NULL
                 对端PCEF组  =  NULL
                 自定义属性  =  NULL
                   IP地址域  =  NULL
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

请参见**ADD PDHOSTCFG**命令的参数说明。