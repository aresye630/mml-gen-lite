# 显示设备当前已加载的NETCONF数据模型（DSP NCSDATAMODEL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示设备当前已加载的NETCONF数据模型。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称    | 参数说明                                                                                                                                                                                        |
|:----------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOADFAILFLAG    | 加载失败标志位 | 可选必选说明：必选参数 参数含义：该参数用于表示加载失败标志位。 数据来源：本端规划 取值范围：枚举类型。 DATAMODEL：数据模型信息。LOADFAIL：加载失败的数据模型信息。 默认值：无                                                                                          |
| APPNAME         | 应用名称    | 可选必选说明：条件必选参数，该参数在“LOADFAILFLAG”配置为“DATAMODEL”时为必选参数。 参数含义：该参数用于表示应用名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无                                                                             |
| NAMESPACE       | 命名空间    | 可选必选说明：条件可选参数，该参数在“LOADFAILFLAG”配置为“DATAMODEL”时为可选参数。 参数含义：该参数用于表示命名空间。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无                                                                             |
| SCHEMATYPE      | 模式类型    | 可选必选说明：条件可选参数，该参数在“LOADFAILFLAG”配置为“DATAMODEL”时为可选参数。 参数含义：该参数用于表示对象类型。 数据来源：本端规划 取值范围：枚举类型。 CFG：配置数据模型。OPER：查询数据模型。ACTION：维护数据模型。TYPE：自定义数据类型模型。METHOD：方法数据模型。NOTIFICATION：通知类型数据模型。 默认值：无 |
| VERBOSEFLAG     | 详细信息标志位 | 可选必选说明：条件可选参数，该参数在“LOADFAILFLAG”配置为“DATAMODEL”时为可选参数。 参数含义：该参数用于表示详细信息标志位。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE                                                              |
| SERVICEINSTANCE | 服务实例    | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                                |

#### 使用实例

显示设备当前已加载的NETCONF数据模型：

```
DSP NCSDATAMODEL:LOADFAILFLAG=DATAMODEL,APPNAME="HTTPS",SCHEMATYPE=CFG,SERVICEINSTANCE="ACS";
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
数据模型XML字符串 = <?xml version="1.0" encoding="UTF-8"?>
<HTTPS xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0">
  <HttpClientCfgs>
    <HttpClientCfg>
      <vrId data-type="VRID" key="true"/>
      <serverType data-type="ENUM(type-name=httpsSERVTYPE)" key="true"/>
      <sslPolicyName data-type="STRING" length="23"/>
      <sslVerifyType data-type="BOOL"/>
    </HttpClientCfg>
  </HttpClientCfgs>
  <HttpServerCfgs>
    <HttpServerCfg>
      <vrId data-type="VRID" key="true"/>
      <serverType data-type="ENUM(type-name=httpsSERVTYPE)" key="true"/>
      <serverEnable data-type="BOOL"/>
      <secureEnable data-type="BOOL"/>
      <serverPort data-type="UINT32" min-val="80" max-val="65535"/>
      <securePort data-type="UINT32" min-val="443" max-val="65535"/>
      <aclName data-type="STRING" length="32"/>
      <aclNum data-type="UINT32" max-val="3999"/>
      <sslPolicyName data-type="STRING" length="23"/>
      <sslVerifyType data-type="BOOL"/>
      <idleTimeout data-type="UINT32" min-val="1" max-val="60"/>
      <secureOrNormal data-type="ENUM(type-name=httpsSERVER)"/>
      <selectACL data-type="ENUM(type-name=httpsACLTYPE)"/>
      <isSecureServer data-type="ENUM(type-name=httpsSECUREENABLE)"/>
      <IPv6secureOrNormal data-type="ENUM(type-name=httpsSERVER)"/>
      <serverIPv6Enable data-type="BOOL"/>
      <isSecureServerIPv6 data-type="ENUM(type-name=httpsSECUREENABLE)"/>
      <serverIPv6Port data-type="UINT32" min-val="80" max-val="65535"/>
      <secureIPv6Port data-type="UINT32" min-val="443" max-val="65535"/>
      <selectIPv6ACL data-type="ENUM(type-name=httpsACLTYPE)"/>
      <aclIPv6Name data-type="STRING" length="32"/>
      <aclIPv6Num data-type="UINT32" max-val="3999"/>
    </HttpServerCfg>
  </HttpServerCfgs>
  <HttpClientDnsDoms>
    <HttpClientDnsDom>
      <IPVersion data-type="ENUM(type-name=HTTPSTRANSIPADDR)"/>
      <peerHostV4 data-type="IPV4"/>
      <peerHostV6 data-type="IPV6"/>
      <DNSID data-type="STRING" length="255"/>
    </HttpClientDnsDom>
  </HttpClientDnsDoms>
</HTTPS>
(结果个数 = 1)  
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释              |
|:-----------|:-------------------|
| 数据模型XML字符串 | NETCONF加载的数据模型XML。 |