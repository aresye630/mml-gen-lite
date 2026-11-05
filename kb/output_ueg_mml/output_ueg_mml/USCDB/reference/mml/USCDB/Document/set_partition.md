# 设置Partition信息(SET PARTITION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

- 该命令属于高危命令，该操作将设置本局PARTITION信息，操作不当将导致业务中断、数据丢失等重大事故。因此执行该命令前，需要与华为技术支持确认后才可以实施。
- 该操作为系统高危操作，需要第二个具有二次授权权限的用户授权后才能执行该操作。请输入授权用户名和密码。

该命令用于为本端的USCDB网元设置对应的Partition信息。

该命令的使用场景：

- 开局场景：用于开局（Global-Local组网或混合组网）时，根据指导书要求，设置本局的Partition信息。
- 网络改造场景：非Global-Local组网或非混合组网改造成Global-Local组网或混合组网时，根据改造指导书步骤，设置本局的Partition信息。

## 注意事项

- 在一个网元内多次执行该命令后，实际的Partition信息以最后一次设置的Partition信息为准。若Partition标识发生变更，需要重启网元才能生效。
- 该命令不允许进行批操作。
- 该命令必须在华为技术支持工程师指导下使用，严禁私自执行。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PARTITIONID | Partition标识 | 用于定义USCDB本端网元的Partition标识。 该参数的配置原则： 一个USCDB网元内最多只能设置一个Partition标识。 主用USCDB和容灾USCDB的Partition标识需要保持一致。 非主用容灾关系的USCDB局点的Partition标识必须不同。 取值范围：1～250 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ROLE        | Partition角色 | 用于定义USCDB本端网元的Partition角色。 该参数的配置原则： 一个USCDB网元只能设定一个Partition角色。 云部署组网下的所有Partition中，有且只能设置一个“Partition角色”为“vRouting”或“vRouting_Service”的Partition。 本端网元的“Partition角色”为“vRouting”时，“远端Partition角色”不能为“Routing”或“vRouting_Service”。本端网元的“Partition角色”为“vService”时，“远端Partition角色”不能为“Routing”、“Service”或“Routing_Service”。本端网元的“Partition角色”为“vRouting_Service”时，“远端Partition角色”不能为“Routing”或“vRouting”。本端网元的“Partition角色”为“vRouting_Service_Region”时，“远端Partition角色”不能为“Routing”或“Routing_Service”。 取值范围： vRouting(云版本路由) vService(云版本服务) vRouting_Service(云版本路由_服务) vRouting_Service_Region(云版本区域路由_服务) 默认值：无。 配置原则：如果存在虚拟远端Location的配置，“ROLE”输入参数必须为“vRouting_Service”或者“vRouting”。 |

## 使用实例

1. 开局场景下，有两个USCDB主用局A和B，它们对应的容灾局为A1和B1，需要设置云部署组网，Partition角色为1个vRouting\_Service和1个vService。此时需要进行如下配置：
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
   4. 在局点A和A1分别执行**ADD RPARTITION**命令，添加远端Partition信息。其中，远端Partition对应的局点B和B1的“Location标识”分别为“81”、“83”。

      ```
      ADD RPARTITION: RPARTITIONID=2, RLOCID=81, RROLE=vService;
      ```

      ```
      ADD RPARTITION: RPARTITIONID=2, RLOCID=83, RROLE=vService;
      ```
   5. 根据运营商规划，执行**SET RPARTITIONPARA**命令，修改局间状态开关，将局间状态开关设置成“停复制和校验”。

      ```
      SET RPARTITIONPARA: PARANAME=INTERPARTSTATUS, SERVICETYPE="SUP-FE", RPARTITIONID=2, PARAVALUE=2;
      ```
2. 开局场景下，操作员添加了错误的Partition角色，需要将Partition角色重新修改成“vRouting\_Service”。此时需要执行如下配置。

   ```
   SET PARTITION: PARTITIONID=1, ROLE=vRouting_Service;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                                                              | 原因分析                                                                                                       | 处理建议                                                                                                                                     |
|-------:|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| 260008 | 参数未修改。请至少指定一个待修改的参数。                                                               | 输入的参数在系统中已配置。                                                                                              | 通过LST PARTITION命令查询已设置的Partition信息，然后重新执行该命令，确保本次输入的参数不与已设置的任何一组参数完全相同。                                                                  |
| 260150 | 参数PARTITIONID指定的partition标识与远端partition标识重复。                                       | 输入的“Partition标识”与已配置的“远端Partition标识”不能重复。                                                                  | 通过LST RPARTITION命令查询已配置的“远端Partition标识”，正确填写“Partition标识”，然后重新执行本命令。                                                                     |
| 260157 | 本地partition角色和远端partition角色不能相同。                                                   | 输入的“Partition角色”与已配置的“远端Partition角色”不能相同。                                                                  | 通过LST RPARTITION命令查询已配置的远端Partition角色，正确填写“Partition角色”，然后重新执行本命令。                                                                       |
| 260424 | 本端网元的partition角色为vRouting时，远端partition角色不能为Routing、vRouting_Service。               | 当“远端Partition角色”是“Routing”或“vRouting_Service”时，配置的本端网元的“Partition角色”是“vRouting”。                           | 通过LST RPARTITION命令查询“远端Partition角色”，如果“远端Partition角色”为“Routing”或“vRouting_Service”时，本端网元的“Partition角色”不能配置为“vRouting”。                   |
| 260425 | 本端网元的partition角色为vService时，远端partition角色不能为Routing、Service、Routing_Service。        | 当“远端Partition角色”是“Routing”、“Service”或“Routing_Service”时，配置的本端网元的“Partition角色”是“vService”。                  | 通过LST RPARTITION命令查询“远端Partition角色”，如果“远端Partition角色”为“Routing”、“Service”或“Routing_Service”时，本端网元的“Partition角色”不能配置为“vService”。          |
| 260426 | 本端网元的partition角色为vRouting_Service时，远端partition角色不能为Routing、vRouting。               | 当“远端Partition角色”是“Routing”或“vRouting”时，配置的本端网元的“Partition角色”是“vRouting_Service”。                           | 通过LST RPARTITION命令查询“远端Partition角色”，如果“远端Partition角色”为“Routing”或“vRouting”时，本端网元的“Partition角色”不能配置为“vRouting_Service”。                   |
| 260427 | 本端网元的partition角色为vRouting_Service_Region时，远端partition角色不能为Routing、Routing_Service。 | 当“远端Partition角色”是“Routing”或“Routing_Service”时，配置的本端网元的“Partition角色”是“vRouting_Service_Region”。             | 通过LST RPARTITION命令查询“远端Partition角色”，如果“远端Partition角色”为“Routing”或“Routing_Service”时，本端网元的“Partition角色”不能配置为“vRouting_Service_Region”。     |
| 260517 | 当Partition模式为全局路由BE转发时，Partition角色必须为Service或vRouting_Service。                     | 若当前“Partition模式”为“GLOBALROUTEBETRANS(全局路由BE转发)”，则不允许将“Partition角色”设置为“vRouting”或“vRouting_Service_Region”。 | 通过LST PARTITIONMODE命令查询当前“Partition模式”，如果“Partition模式”为“GLOBALROUTEBETRANS(全局路由BE转发)”时，“Partition角色”只允许设置为“vService”或“vRouting_Service”。 |
| 260530 | 配置了虚拟远端Location的局点，只能设置分区角色为vRouting_Service或者vRouting。                            | 只支持在分区角色为vRouting_Service或者vRouting的局点上配置虚拟远端Location。                                                     | 请将“ROLE”输入参数改为“vRouting_Service”或者“vRouting”。                                                                                            |
| 260531 | 参数Partition标识指定的Partition标识与虚拟远端Location的Partition标识重复。                            | 输入的“Partition标识”与已配置的虚拟远端Location的“远端Partition标识”不能重复。                                                     | 通过LST VRLOCATION命令查询已配置的虚拟远端Location的Partition信息，重新执行本命令。                                                                                |
| 260563 | 当Partition模式为全局本地时，Partition角色必须为vService或vRouting_Service。                        | 若当前“Partition模式”为“GLOBALLOCAL(全局本地)”，则不允许将“Partition角色”设置为“vRouting”或“vRouting_Service_Region”。            | 通过LST PARTITIONMODE命令查询当前“Partition模式”，如果“Partition模式”为“GLOBALLOCAL(全局本地)”时，“Partition角色”只允许设置为“vService”或“vRouting_Service”。            |