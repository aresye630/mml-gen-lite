# 增加远端Partition信息(ADD RPARTITION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该命令属于高危命令，增加远端PARTITION信息会对云部署业务访问产生影响。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于为一个USCDB网元设置对应的远端Partition信息。

该命令的使用场景：在云部署场景下，操作员在本端设置远端Partition信息，完成本端USCDB与远端USCDB的对接。

该命令的参数索引关系如图1所示：

**图1** 命令参数的索引关系图

## 注意事项

- 申请“基于混合组网的用户管理”License后才能执行该命令增加远端Partition信息。
- 该命令不允许进行批操作。
- 在混合组网改造过程中，当软参“CDB\_VRSP\_R\_RECONSTRUCTMODE（CDB vRSP\_R改造模式）”取值为“1”时，执行完**RMV RPARTITION**命令之后，需要立即执行**ADD RPARTITION**重新增加远端Partition信息，且“远端Partition标识”、“远端Location标识”需要和删除的远端Partition信息保持一致，“远端Partition角色”变更要求是“vRouting\_Service\_Region(云版本区域路由\_服务)”变更为“vService(云版本服务)”。其中，**RMV RPARTITION**只会将物理库中的远端Partition信息删除，不会删除进程中缓存的远端Partition信息，**ADD RPARTITION**支持更新进程缓存中配置的“远端Partition角色”。

  **说明** 

  仅在混合组网改造过程中需要执行此操作。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPARTITIONID | 远端Partition标识 | 可选必选说明：必选参数 参数含义：用于指定待增加的远端Partition的Partition标识。 取值范围：1～250 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RLOCID       | 远端Location标识  | 可选必选说明：必选参数 参数含义：用于指定待增加的远端Partition所在USCDB网元的Location标识。该参数已经通过ADD RLOCATION配置后在此引用。 取值范围：1～512 默认值：无。 配置原则： 该参数对应的网元必须是USCDB网元。 该参数对应的USCDB网元不允许是本USCDB对应的容灾USCDB。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RROLE        | 远端Partition角色 | 可选必选说明：必选参数 参数含义：用于指定待增加的远端Partition的Partition角色。 取值范围： Routing(路由) Service(服务) Routing_Service(路由_服务) vRouting(云版本路由) vService(云版本服务) vRouting_Service(云版本路由_服务) vRouting_Service_Region(云版本区域路由_服务) 默认值：无。 配置原则： 如果存在虚拟远端Location的配置，“远端Partition角色”输入参数必须为“Service”。 “远端Partition角色”不能与本端的“Partition角色”相同。 待添加的“远端Partition角色”必须与实际的远端Partition角色保持一致。 本端网元的“Partition角色”为“vRouting”时，“远端Partition角色”不能为“Routing”或“vRouting_Service”。本端网元的“Partition角色”为“vService”时，“远端Partition角色”不能为“Routing”、“Service”或“Routing_Service”。本端网元的“Partition角色”为“vRouting_Service”时，“远端Partition角色”不能为“Routing”或“vRouting”。本端网元的“Partition角色”为“vRouting_Service_Region”时，“远端Partition角色”不能为“Routing”或“Routing_Service”。 |
| RBETYPE      | 远端BE网元类型      | 可选必选：可选参数 参数含义：用于指定远端分区的BE网元类型。 取值范围： UDB(UDB)CDB(CDB)UDR(UDR) 默认值：无 配置原则： 当“远端Partition角色”为“Service”或者“Routing_Service”时，“远端BE网元类型”只能是“UDB”， 当“远端Partition角色”为“vService”、“vRouting”、“vRouting_Service”或“vRouting_Service_Region”时，“远端BE网元类型”不能是“UDB”。                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DESCRIPTION  | 描述            | 可选必选：可选参数 参数含义：用于描述待增加的远端Partition。 取值范围：不超过64位的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## 使用实例

开局场景下，有两个USCDB主用局A和B，它们对应的容灾局为A1和B1，需要设置云部署组网，Partition角色为1个vRouting\_Service和1个vService。此时需要进行如下配置：

1. 在局点A和A1分别执行**SET PARTITION**命令，添加1个“Partition角色”为“vRouting\_Service”的Partition信息。

   ```
   SET PARTITION: PARTITIONID=1, ROLE=vRouting_Service;
   ```
2. 在局点B和B1执行**SET PARTITION**命令，添加1个“Partition角色”为“vService”的Partition信息。

   ```
   SET PARTITION: PARTITIONID=2, ROLE=vService;
   ```
3. 在局点A和A1分别执行**ADD RLOCATION**命令，添加远端Location信息。其中，局点B和B1的“Location标识”分别为“81”、“83”。

   ```
   ADD RLOCATION: RLOCID=81, RMT="USCDB", LP=1, REDUNFLAG=Yes;
   ```

   ```
   ADD RLOCATION: RLOCID=83, RMT="USCDB", LP=2, REDUNFLAG=Yes;
   ```
4. 在局点A和A1分别执行**ADD RPARTITION**命令，添加远端Partition信息。其中，远端Partition对应的局点B和B1的“Location标识”分别为“81”、“83”且局点B的BE网元类型是UDR，局点B1的BE网元类型是CDB。

   ```
   ADD RPARTITION: RPARTITIONID=2, RLOCID=81, RROLE=vService, RBETYPE=UDR;
   ```

   ```
   ADD RPARTITION: RPARTITIONID=2, RLOCID=83, RROLE=vService, RBETYPE=CDB;
   ```
5. 根据运营商规划，执行**SET RPARTITIONPARA**命令，修改局间状态开关，将局间状态开关设置成“停复制和校验”。

   ```
   SET RPARTITIONPARA: PARANAME=INTERPARTSTATUS, SERVICETYPE="SUP-FE", RPARTITIONID=2, PARAVALUE=2;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                                                              | 原因分析                                                                                                                                                                                                                                       | 处理建议                                                                                                                                                                                           |
|-------:|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 260096 | 该远端location不存在。                                                                    | 输入的“远端Location标识”在系统中未配置。                                                                                                                                                                                                                  | 通过LST RLOCATION命令查询已设置的远端Location信息，然后重新执行该命令。                                                                                                                                                 |
| 260151 | partition配置不存在。                                                                    | 必须先配置本端Partition，再配置远端Partition。                                                                                                                                                                                                           | 通过SET PARTITION命令设置本端Partition信息，然后重新执行该命令。                                                                                                                                                    |
| 260153 | 该远端location已配置到partition。                                                          | 不允许对远端Partition重复配置。                                                                                                                                                                                                                       | 无需处理。                                                                                                                                                                                          |
| 260154 | 参数RPARTITIONID指定的远端partition标识与本地partition标识重复。                                    | 输入的“远端Partition标识”与本地“Partition标识”必须不同。                                                                                                                                                                                                    | 通过LST PARTITION命令查询已配置的“Partition标识”，正确填写“远端Partition标识”，然后重新执行本命令。                                                                                                                            |
| 260157 | 本地partition角色和远端partition角色不能相同。                                                   | 输入的“远端Partition角色”与本地“Partition角色”必须不同。                                                                                                                                                                                                    | 通过LST PARTITION命令查询已配置的“Partition角色”，正确填写“远端Partition角色”，然后重新执行本命令。                                                                                                                            |
| 260159 | 相同远端Partition标识的角色属性必须定义一致。                                                        | 同一个Partition下的不同Location的“远端Partition角色”必须配置为同一值。                                                                                                                                                                                          | 通过LST RPARTITION命令查询已配置的“远端Partition角色”并正确填写，然后重新执行本命令。                                                                                                                                        |
| 260161 | 参数RLOCID所指定的远端局点网元类型不是USCDB。                                                       | 输入的“远端Location标识”所对应的网元类型只能是USCDB类型。                                                                                                                                                                                                       | 通过LST RLOCATION命令查询已设置的远端Location信息，然后选择USCDB类型的Location重新执行该命令。                                                                                                                               |
| 260164 | 该远端Location为容灾局，不能添加。                                                              | 输入的“远端Location标识”所对应的局点不能为容灾局。                                                                                                                                                                                                             | 通过LST RLOCATION命令查询已设置的远端Location信息，然后选择主用局的Location重新执行该命令。                                                                                                                                   |
| 260424 | 本端网元的partition角色为vRouting时，远端partition角色不能为Routing、vRouting_Service。               | 当本端网元的“Partition角色”是“vRouting”时，配置的“远端Partition角色”是“Routing”或“vRouting_Service”。                                                                                                                                                           | 通过LST PARTITION命令查询本端网元的“Partition角色”，如果本端网元的“Partition角色”是“vRouting”时，不能配置“远端Partition角色”为“Routing”或“vRouting_Service”。                                                                       |
| 260425 | 本端网元的partition角色为vService时，远端partition角色不能为Routing、Service、Routing_Service。        | 当本端网元的“Partition角色”是“vService”时，配置的“远端Partition角色”是“Routing”、“Service”或“Routing_Service”。                                                                                                                                                  | 通过LST PARTITION命令查询本端网元的“Partition角色”，如果本端网元的“Partition角色”是“vService”时，不能配置“远端Partition角色”为“Routing”、“Service”或“Routing_Service”。                                                              |
| 260426 | 本端网元的partition角色为vRouting_Service时，远端partition角色不能为Routing、vRouting。               | 当本端网元的“Partition角色”是“vRouting_Service”时，配置的“远端Partition角色”是“Routing”或“vRouting”。                                                                                                                                                           | 通过LST PARTITION命令查询本端网元的“Partition角色”，如果本端网元的“Partition角色”是“vRouting_Service”时，不能配置“远端Partition角色”为“Routing”或“vRouting”。                                                                       |
| 260427 | 本端网元的partition角色为vRouting_Service_Region时，远端partition角色不能为Routing、Routing_Service。 | 当本端网元的“Partition角色”是“vRouting_Service_Region”时，配置的“远端Partition角色”是“Routing”或“Routing_Service”。                                                                                                                                             | 通过LST PARTITION命令查询本端网元的“Partition角色”，如果本端网元的“Partition角色”是“vRouting_Service_Region”时，不能配置“远端Partition角色”为“Routing”或“Routing_Service”。                                                         |
| 260416 | 本端partition只允许配置一个远端Routing_Service partition。                                     | 当本端网元的“Partition角色”是“vRouting”或“vRouting_Service”且已配置了一个“远端Partition角色”为“Routing_Service”的partition时，本次配置的“远端Partition角色”还是“Routing_Service”。                                                                                              | 请确保满足当本端网元的“Partition角色”是“vRouting”或“vRouting_Service”时，只能配置一个“远端Partition角色”为“Routing_Service”的partition。可以通过LST PARTITION命令查询本端网元的“Partition角色”，通过LST RPARTITION命令查询“远端Partition角色”。         |
| 260414 | 本端partition只允许配置一个远端vRouting或vRouting_Service partition。                           | 当本端网元的“Partition角色”是“vRouting_Service_Region”且已配置了一个“远端Partition角色”为“vRouting”或“vRouting_Service”的partition时，本次配置的“远端Partition角色”还是“vRouting”或“vRouting_Service”。                                                                          | 请确保满足当本端网元的“Partition角色”是“vRouting_Service_Region”时，只能配置一个“远端Partition角色”为“vRouting”或“vRouting_Service”的partition。可以通过LST PARTITION命令查询本端网元的“Partition角色”，通过LST RPARTITION命令查询“远端Partition角色”。 |
| 260415 | 本端partition只允许配置一个远端vRouting_Service_Region partition。                             | 当本端网元的“Partition角色”是“vService”且已配置了一个“远端Partition角色”为“vRouting_Service_Region”的partition时，本次配置的“远端Partition角色”还是“vRouting_Service_Region”。                                                                                                 | 请确保满足当本端网元的“Partition角色”是“vService”时，只能配置一个“远端Partition角色”为“vRouting_Service_Region”的partition。可以通过LST PARTITION命令查询本端网元的“Partition角色”，通过LST RPARTITION命令查询“远端Partition角色”。                    |
| 260470 | 未申请“基于混合组网的用户管理”License，不允许添加远端Partition。                                          | 未申请“基于混合组网的用户管理”License，不允许执行该命令添加远端Partition信息。                                                                                                                                                                                           | 请申请“基于混合组网的用户管理”License后再执行该命令。可以通过登录OM Portal选择“应用管理 > 应用License”查询License文件状态信息，当“混合组网用户管理”取值为“1”时，表示已申请“基于混合组网的用户管理”License。                                                                |
| 260532 | 配置虚拟远端Location标识的分区角色不是Service。                                                    | 虚拟远端Location标识的分区角色必须是Service。                                                                                                                                                                                                             | 请将“RROLE”输入参数改为“Service”。                                                                                                                                                                      |
| 260533 | 配置的远端Partition标识或者远端Location标识不正确。                                                 | ADD RPARTITION命令配置的远端Partition标识、远端Location标识与ADD VRLOCATION命令配置的远端Partition标识、虚拟远端Location标识需要保持一致。                                                                                                                                       | 通过LST VRLOCATION命令查询已设置的虚拟远端Location信息，重新执行该命令。                                                                                                                                                |
| 260633 | RBETYPE类型与分区角色不匹配。                                                                 | 输入的“远端BE网元类型”类型和“远端Partition角色”不匹配。 “远端BE网元类型”参数的填写需要满足以下两个原则： 当“远端Partition角色”为“Service”或者“Routing_Service”时，“远端BE网元类型”只能是“UDB”， 当“远端Partition角色”为“vService”、“vRouting”、“vRouting_Service”或“vRouting_Service_Region”时，“远端BE网元类型”不能是“UDB”。 | 请联系华为技术支持，根据“远端Location标识”获取对应的远端BE网元类型，输入正确的“远端BE网元类型”取值后，再重新执行该命令。                                                                                                                           |
| 483018 | 输入的RBETYPE值非法。                                                                     | 输入的“远端BE网元类型”值非法，取值不是“UDB”、“CDB”、“UDR”其中的一种。                                                                                                                                                                                               | 请联系华为技术支持，根据“远端Location标识”获取对应的远端BE网元类型，输入正确的“远端BE网元类型”取值后，再重新执行该命令。                                                                                                                           |