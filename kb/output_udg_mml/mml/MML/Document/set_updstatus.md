# 设置升级状态（SET UPDSTATUS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**须知** 

该命令属于高危命令，执行该命令会设置升级状态，某些服务的状态会受到影响。若错误设置某些服务的升级状态，可能会导致该服务升级失败。请谨慎使用。

该命令用于设置RU升级开始和结束。

#### 注意事项

- 该命令执行后立即生效。
- 如果主主控没有设置升级开始，其他单板不能设置升级开始。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                                                                                                                              |
|:----------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUNAME          | RU名称   | 可选必选说明：可选参数 参数含义：该参数用于表示资源单元名称。 数据来源：本端规划 取值范围：1-63位字符串，区分大小写，不支持空格。 默认值：无                                                                                                                                                                                                        |
| SETSTATUS       | 设置状态   | 可选必选说明：必选参数 参数含义：该参数用于设置升级状态。 数据来源：本端规划 取值范围：枚举类型。 On(打开)：开始升级。Off(关闭)：结束升级。RollBackStart(回退开始)：无损回退开始。RollBackEnd(回退结束)：无损回退结束。 默认值：无  说明： 当“SERVINCEINSTANCE”参数为“0”时（“0”表示VNFP），该参数仅可配置 “RollBackStart”、“RollBackEnd”参数值。当“SERVINCEINSTANCE”参数为“0”之外的其他值时，该参数仅可配置“On”、“Off”参数值。 |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                                                                                                                      |

#### 使用实例

设置RU升级状态：

```
SET UPDSTATUS:SETSTATUS=On,SERVICEINSTANCE="vnfc";
SET UPDSTATUS:SETSTATUS=Off,SERVICEINSTANCE="vnfc";
SET UPDSTATUS:RUNAME="VNODE_UGW_VNFC_OMU_0001",SETSTATUS=On,SERVICEINSTANCE="vnfc";
SET UPDSTATUS:RUNAME="VNODE_UGW_VNFC_SPU_0065",SETSTATUS=Off,SERVICEINSTANCE="vnfc";
SET UPDSTATUS:SETSTATUS=RollBackStart,SERVICEINSTANCE="0";
SET UPDSTATUS:RUNAME="OMU1",SETSTATUS=RollBackEnd,SERVICEINSTANCE="0";
```