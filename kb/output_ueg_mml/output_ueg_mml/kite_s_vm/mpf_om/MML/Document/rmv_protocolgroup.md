# 删除自定义协议组（RMV PROTOCOLGROUP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：MPF**

该命令用来删除自定义协议组。

#### 注意事项

- 该命令执行后立即生效。
- 删除前，判断ProtocolGroup对象中的字段PROTGROUPNAME的值和BwmService对象中的字段PROTGROUPNAME的值是否相等，如果相等，则删除ProtocolGroup对象中的指定记录失败；判断ProtocolGroup对象中的字段PROTGROUPNAME的值和ProtGBindL7R对象中的字段PROTGROUPNAME的值是否相等，如果相等，则删除ProtocolGroup对象中的指定记录失败。
- 指定ProtGroupName但不指定ProtocolName，删除该ProtocolGroup的所有ProtocolName记录。
- 指定ProtGroupName和ProtocolName，删除指定ProtocolGroup的指定ProtocolName记录。
- 不指定ProtGroupName和ProtocolName，删除所有记录。
- 当删除指定ProtGroupName的最后一个ProtocolName时，删除该ProtocolGroup。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                       |
|:--------------|:-------|:-------------------------------------------------------------------------------------------|
| PROTGROUPNAME | 协议组名称  | 可选必选说明：可选参数 参数含义：该参数用于指定协议组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |
| PROTOCOLNAME  | 协议名称   | 可选必选说明：可选参数 参数含义：协议组包含的协议的名字。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无  |

#### 使用实例

如果想要删除一条自定义协议组“group1”，应该输入合法的数据，例如：

```
RMV PROTOCOLGROUP:PROTGROUPNAME="group1";
```