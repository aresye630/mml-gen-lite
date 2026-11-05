# 设置CMPCC调试命令（SET CMPCCDBGDATA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置SMF网元上计费策略组件的调试信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令需要慎重使用，必须在华为技术支持人员的指导下操作。
- 不同的CS类型有不同的调试信息，不同的调试信息也有不同的参数，如果参数输入不准确，不会出现错误提示。
- 当前可执行的调试信息与CS类型的对应关系如下：
- 当CSTYPE为SM4GCM时，软调名称只能为"cmcore cnt excpcnt"，"cmcore cnt smccnt"，"cmcc perfproxy ggsn"，"cmcc perfproxy sgw"，"cmcc perfproxy pgw"，"cmcc perfproxy spgw"，"cmcc perfproxy ocsc"，"cmcc perfproxy gaag"，"cmcc perfproxy diam"其中一个。
- 当CSTYPE为RADIUSACCT时，软调名称只能为"cmacct cnt excpcnt"，"cmcc perfproxy acct"其中一个。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                               |
|:----------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CSTYPE    | 指定CS类型 | 可选必选说明：必选参数  参数含义：该参数用于指定CS的类型。  数据来源：本端规划 取值范围： SM4GCM（会话管理4G计费cell服务）RADIUSACCT（会话管理AAA计费cell服务）SM4GPOLICY（会话管理4G策略cell服务）GA（会话管理Ga链路cell服务）GY（会话管理Ga链路cell服务）GX（会话管理Gx链路cell服务）  默认值：无。  配置原则：无 |
| DEBUGNAME | 调试信息   | 可选必选说明：必选参数  参数含义：该参数用于表示调试信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无。  配置原则：无                                                                                                                |
| DEBUGPARA | 调试信息参数 | 可选必选说明：可选参数  参数含义：该参数用于指定软件调试命令下发的参数。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CMPCCDBGDATA查询当前参数配置值。  配置原则：无                                                |

## 使用实例

设置指定CsType为SM4GCM，调试信息为清除异常内统计数：

```
%%SET CMPCCDBGDATA: CSTYPE=SM4GCM, DEBUGNAME="cmcore cnt excpcnt", DEBUGPARA="clean";%%
RETCODE = 0    操作成功

---    END
```