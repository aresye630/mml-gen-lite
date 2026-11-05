# 设置 NE 类型（SET NETYPE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

本命令用于改变网元形态。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 网元形态初始值由系统生成,该命令参数初始值为NULL。
- SET NETYPE的ProxySGWU仅限于设备作为独立关口局设备，承接国际漫游语音业务的ProxySGW形态时配置。其他场景不能配置为ProxySGWU。
- SET NETYPE的PorxyUPF仅限于设备作为独立关口局设备，承接国际漫游语音业务的PorxyUPF形态时配置。其他场景不能配置为PorxyUPF。
- SET NETYPE目前支持的形态设置值如下表：

| 逻辑类型                    | 排查方法指导     | 配置结果确认                              |
|:------------------------|:-----------|:------------------------------------|
| UPF                     | DSP NEINFO | 网元配置类型值为UPF(纯5G)                    |
| ProxySGWU               | DSP NEINFO | 网元配置类型值为ProxySGWU                   |
| UPF;PGWU                | DSP NEINFO | 网元配置类型值为UPF;PGWU(45G融合)             |
| UPF;SGWU                | DSP NEINFO | 网元配置类型值为UPF;SGWU(45G融合)             |
| UPF;SGWU;PGWU           | DSP NEINFO | 网元配置类型值为UPF;SGWU;PGWU(45G融合)        |
| UPF;SGWU;PGWU;GGSNU     | DSP NEINFO | 网元配置类型值为UPF;SGWU;PGWU;GGSNU(245G融合) |
| UPF;PGWU;GGSNU          | DSP NEINFO | 网元配置类型值为UPF;PGWU;GGSNU(245G融合)      |
| ProxySGWU;ProxyUPF;PGWU | DSP NEINFO | 网元配置类型值为ProxySGWU;ProxyUPF;PGWU     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                     |
|:-----------|:-------|:-------------------------------------------------------------------------------------------------------------------------|
| NETYPEENUM | 网元形态   | 可选必选说明：必选参数 参数含义：网元形态枚举。 数据来源：本端规划 取值范围：位域类型。 SGWUPGWUUPFGGSNUProxySGWUProxyUPFUEGTypeLUEGTypeMAMFSMFUDMPCF 默认值：无 配置原则：无 |

#### 使用实例

将网元形态设置为UPF;PGWU：

```
SET NETYPE:NETYPEENUM=GGSNU-0&PGWU-1&ProxySGWU-0&SGWU-0&UPF-1&ProxyUPF-0;
```