# 删除远端Partition信息(RMV RPARTITION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该命令属于高危命令，删除远端PARTITION信息会对云部署业务访问产生影响。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于删除USCDB网元已配置的远端Partition信息。

该命令有以下使用场景：

- 操作员已经在本地添加了远端Partition的设置，但此远端的Partition信息配置错误（如：Partition标识或Partition角色与运营商规划的不一致），此时在修改此远端的Partition信息前，必须先通过本命令在本地删除相应的远端Partition信息。
- 增加的远端Partition信息错误（如：命令中设置的远端Partition角色与实际的不一致）。

## 注意事项

- 该命令不允许进行批操作。
- 在混合组网改造过程中，当软参“CDB\_VRSP\_R\_RECONSTRUCTMODE（CDB vRSP\_R改造模式）”取值为“1”时，执行完**RMV RPARTITION**命令之后，需要立即执行**ADD RPARTITION**重新增加远端Partition信息，且“远端Partition标识”、“远端Location标识”需要和删除的远端Partition信息保持一致，“远端Partition角色”变更要求是“vRouting\_Service\_Region(云版本区域路由\_服务)”变更为“vService(云版本服务)”。其中，**RMV RPARTITION**只会将物理库中的远端Partition信息删除，不会删除进程中缓存的远端Partition信息，**ADD RPARTITION**支持更新进程缓存中配置的“远端Partition角色”。

  **说明** 

  仅在混合组网改造过程中需要执行此操作。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                              |
|:-------------|:--------------|:----------------------------------------------------------------------------------|
| RPARTITIONID | 远端Partition标识 | 标识一条远端Partition信息的关键字段之一，用于指定需要删除哪一条远端Partition信息的记录，该参数可以使用LST RPARTITION命令查询获得。 |
| RLOCID       | 远端Location标识  | 标识一条远端Partition信息的关键字段之一，用于指定需要删除哪一条远端Location标识的记录，该参数可以使用LST RPARTITION命令查询获得。  |

## 使用实例

在云部署场景下，A、B两个局点的“Partition角色”配置分别是“vRouting”和“Service”的Partition，且两个Partition间已完成了远端Partition信息的增加，当前需要将A局点的“Partition角色”修改为“vRouting\_Service”，此时需要做如下配置：

1. 在局点B执行**RMV RPARTITION**命令，删除远端的配置信息。

   ```
   RMV RPARTITION: RPARTITIONID=2, RLOCID=100;
   ```
2. 在局点A执行**SET PARTITION**命令，修改“Partition角色”为“vRouting\_Service”的。

   ```
   SET PARTITION: PARTITIONID=2, ROLE=vRouting_Service;
   ```
3. 在局点B重新增加远端Partition信息。

   ```
   ADD RPARTITION: RPARTITIONID=2, RLOCID=100, RROLE=vRouting_Service;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                                   | 原因分析                                  | 处理建议                                                                   |
|-------:|:--------------------------------------------------------|:--------------------------------------|:-----------------------------------------------------------------------|
| 260155 | 该远端partition不存在。                                        | 输入的“远端Partition标识”在系统中未配置。            | 通过LST RPARTITION命令查询已配置的“远端Partition标识”并正确填写，然后重新执行本命令。                |
| 260156 | 参数RLOCID指定的远端location在参数RPARTITIONID指定的远端partition中不存在。 | 输入的“远端Location标识”与“远端Partition标识”不匹配。 | 通过LST RPARTITION命令查询已配置的“远端Partition标识”和“远端Location标识”并正确填写，然后重新执行本命令。 |