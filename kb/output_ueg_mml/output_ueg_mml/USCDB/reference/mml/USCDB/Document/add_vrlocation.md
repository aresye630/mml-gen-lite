# 增加虚拟远端Location信息(ADD VRLOCATION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该命令属于高危命令，该操作添加不当的虚拟远端Location映射信息会导致FE访问BE失败。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于增加虚拟远端Location标识，用于标记各远端Location到虚拟远端Location的映射信息。

该命令的使用场景：应用于混合组网演进场景，如果已有多个SP分区的BE的Location标识相同时，在vRSP/vRP上将远端Location标识与虚拟远端Location标识进行唯一映射配置，实现跨区查找时区分实际的远端Location。

该命令的参数索引关系如图1所示。

图1中，SP1和SP2中，BE的Location标识相同(主BE Location标识均为81，备BE Location标识均为82)，为了实现跨区查找时区分实际的远端Location，需要在vRSP上执行该命令将远端Location标识与虚拟远端Location标识进行唯一映射配置。配置参数示例如图中右侧表格所示。

**图1** 虚拟远端Location标识和远端Location标识映射示例

## 注意事项

- 对端Partition下的1个Location标识只允许映射为1个虚拟远端Location标识。
- 不允许在包含vRSP\_R/RSP/RP任一分区的混合组网中配置虚拟远端Location信息。

## 参数说明

| 参数标识         | 参数名称           | 参数说明                                                                                                                                |
|:-------------|:---------------|:------------------------------------------------------------------------------------------------------------------------------------|
| VRLOCID      | 虚拟远端Location标识 | 可选必选说明：必选参数 参数含义：用于指定将要对接的远端SP分区的USCDB网元的虚拟的Location标识。 取值范围：1～512 默认值：无 配置原则：虚拟远端Location标识需全局唯一，虚拟远端Location标识和远端Location标识不允许重复。 |
| RPARTITIONID | 远端Partition标识  | 可选必选说明：必选参数 参数含义：用于指定待增加的远端Partition的Partition标识。操作员可以在远端分区使用LST PARTITION命令查询获得或者根据网络规划进行设置。 取值范围：1～250 默认值：无 配置原则：无               |
| RLOCID       | 远端Location标识   | 可选必选说明：必选参数 参数含义：用于指定待增加的远端Partition所在USCDB网元的Location标识。操作员可以在远端分区使用LST LOCATION命令查询获得。 取值范围：1～512 默认值：无 配置原则：无                    |

## 使用实例

配置一个虚拟远端Location映射。其中“虚拟远端Location标识”为“100”，“远端Partition标识”为“20”，“远端Location标识”为“81”。

```
ADD VRLOCATION: VRLOCID=100, RPARTITIONID=20, RLOCID=81;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                                 | 原因分析                                                                                                                                        | 处理建议                                                                                                  |
|-------:|:------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| 260521 | 配置的虚拟远端Location标识与其他的虚拟远端Location标识或远端Location标识存在冲突。 | 当前配置中的虚拟远端Location标识和远端Location标识不允许相同。当前配置中的虚拟远端Location标识和已配置的虚拟远端Location信息中的不允许相同。当前配置中的虚拟远端Location标识和远端Location信息中的远端Location标识不允许相同。 | 通过LST VRLOCATION和LST RLOCATION命令查看当前已经使用的Location标识。                                                  |
| 260522 | 配置的远端Partition标识和远端Location标识已经存在。                    | 远端Partition标识、远端Location标识不允许同时重复。                                                                                                          | 通过LST VRLOCATION命令查询远端Partition标识和远端Location标识，请重新执行本命令输入“远端Partition标识”和“远端Location标识”参数，确保与查询结果不重复。 |
| 260523 | 配置的虚拟远端Location标识或者远端Location标识与本地Location标识重复。       | 虚拟远端Location标识、远端Location标识不允许与本地Location标识重复。                                                                                              | 通过LST LOCATION命令查询本地Location标识，请重新执行本命令输入“虚拟远端Location标识”或“远端Location标识”参数，确保与查询结果不重复。                |
| 260524 | 本分区角色不是vRouting_Service或者vRouting。                    | 只允许在vRouting_Service或者vRouting分区上执行此命令。                                                                                                     | 执行LST PARTITION命令确认本局角色是否正确。                                                                          |
| 260525 | 远端Location标识已经配置。                                     | ADD VRLOCATION命令必须在ADD RLOCATION命令前执行。                                                                                                      | 通过RMV RLOCATION命令把已配置的远端Location删除，再重新执行ADD VRLOCATION设置。                                             |