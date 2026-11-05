# 修改PSA UPF和ATSSS UPF绑定关系中的ATSSS-UPF（MOD PSAUPFBINDATSSS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于修改PSA UPF和ATSSS UPF绑定关系中的ATSSS UPF。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称          | 参数说明                                                                                                                                                                         |
|:---------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSAUPFINSTNAME | PSA UPF实例名称   | 可选必选说明：必选参数  参数含义：该参数用于指定PSA UPF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：  该参数需要在ADD UPNODE中事先配置，可执行LST UPNODE进行查看。注意查询结果是“UPF功能”为None的“UPF实例名称”。      |
| ATSSSINSTNAME  | ATSSS UPF实例名称 | 可选必选说明：必选参数  参数含义：该参数用于指定ATSSS UPF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：  该参数需要在ADD UPNODE中事先配置，可执行LST UPNODE进行查看。注意查询结果是“UPF功能”取值为ATSSS的“UPF实例名称”。 |

## 使用实例

假设执行此命令前已经使用ADD PSAUPFBINDATSSS添加了一条记录：PSA UPF实例名称为upf\_none，ATSSS UPF实例名称为upf\_atsss。现修改绑定关系中的ATSSS UPF实例名称为upf\_atsss\_1：

```
MOD PSAUPFBINDATSSS: PSAUPFINSTNAME="upf_none", ATSSSINSTNAME="upf_atsss_1";
%%MOD PSAUPFBINDATSSS: PSAUPFINSTNAME="upf_none", ATSSSINSTNAME="upf_atsss_1";%%
RETCODE = 0  操作成功

---    END
```