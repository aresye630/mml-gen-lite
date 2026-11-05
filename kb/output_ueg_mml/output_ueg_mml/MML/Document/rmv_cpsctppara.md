# 删除SCTP协议参数(RMV CPSCTPPARA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME、AMF**

该命令用于删除SCTP协议参数表中指定的记录。

#### 注意事项

- 该命令执行后立即生效。
- 删除SCTP协议参数表中指定的记录前，请执行**LST CPSCTPPARA**命令查询该记录是否存在。若存在且执行本命令失败，再执行**LST S1APLE**命令，**LST LCSAPLNK**命令，**LST SBCAPLE**命令，**LST SBCAPLNK**命令，**LST SGSLNK**命令，**LST CPDMLNK**命令，**LST CPM3LNK**命令，**LST M3APLE**命令，**LST SCTPLE**命令，**LST RCAPLNK**命令，**LST SGSRLNK**命令，依次确认S1APLE数据表、LCSAPLNK数据表、SBCAPLE数据表、SBCAPLNK数据表、SGSLNK数据表、CPDMLNK数据表、CPM3LNK数据表、M3APLE数据表、SCTPLE数据表、RCAPLNK数据表及SGSRLNK数据表中是否存在引用了此SCTP协议参数相关的记录，如果存在引用关系，则需要先删除该参数被引用的数据表中的相应记录后，再尝试删除该SCTP协议参数。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称       | 参数说明                                                                                                         |
|:--------------|:-----------|:-------------------------------------------------------------------------------------------------------------|
| SCTPPARAINDEX | SCTP协议参数索引 | 可选必选说明：必选参数 参数含义：该参数用于删除指定SCTP协议参数索引，在系统范围内部唯一标识一条SCTP协议参数。 前提条件：此参数已经在ADD CPSCTPPARA中设置。 取值范围：0~65534 默认值：无 |

#### 使用实例

删除SCTP协议参数索引号为0的SCTP协议参数表中指定的记录：

RMV CPSCTPPARA:SCTPPARAINDEX=0;