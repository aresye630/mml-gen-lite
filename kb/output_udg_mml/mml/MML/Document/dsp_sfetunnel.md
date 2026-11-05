# 显示Tunnel表项（DSP SFETUNNEL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于根据隧道类型、目的IP、源IP、VPN ID、KEY-USED、GRE-KEY、RUNAME显示Tunnel表项。

#### 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                           |
|:--------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------|
| GRETUNNELTYPE | GRE隧道类型  | 可选必选说明：必选参数 参数含义：GRE隧道类型。该参数用于控制输入参数中的目的IP、源IP地址的协议类型。 数据来源：本端规划 取值范围：枚举类型。 GRE4Tunnel：IPv4 GRE隧道。GRE6Tunnel：IPv6 GRE隧道。 默认值：无 |
| DESTINATION   | 目的IP地址   | 可选必选说明：条件必选参数 前提条件：该参数在“GRETUNNELTYPE”配置为“GRE4Tunnel”时为必选参数。 参数含义：该参数用于指定目的IP地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无                |
| SOURCE        | 源IP地址    | 可选必选说明：条件必选参数 前提条件：该参数在“GRETUNNELTYPE”配置为“GRE4Tunnel”时为必选参数。 参数含义：该参数用于指定源IP地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无                 |
| DESTINATION6  | 目的IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“GRETUNNELTYPE”配置为“GRE6Tunnel”时为必选参数。 参数含义：目的IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                     |
| SOURCE6       | 目的IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“GRETUNNELTYPE”配置为“GRE6Tunnel”时为必选参数。 参数含义：源IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                      |
| VPN           | VPN编号    | 可选必选说明：必选参数 参数含义：该参数用于指定VPN编号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～65535。 默认值：无                                                         |
| RUNAME        | RU名称     | 可选必选说明：必选参数 参数含义：该参数用于指定资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。区分大小写。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。                |
| KEYUSED       | Key标志    | 可选必选说明：必选参数 参数含义：该参数用于表示Key值配置标志。 数据来源：本端规划 取值范围：整数类型，取值范围为0～1。 默认值：无                                                          |
| GREKEY        | Key      | 可选必选说明：必选参数 参数含义：该参数用于表示配置的Key值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                                  |

#### 使用实例

显示指定资源单元的Tunnel表项：

```
DSP SFETUNNEL: GRETUNNELTYPE=GRE4Tunnel, DESTINATION="192.168.1.1", SOURCE="192.168.1.2", VPN=0, RUNAME="VNODE_VNRS_VNFC_IPU_0064", KEYUSED=1, GREKEY=10;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
 结果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
TableName    : IPV4 TUNNEL
TotalRecords : 1
(*):  Key of the table
---------------------------------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
           *TunnelId : 00000003                        TnlValid : 01                  
             KeyUsed : 01                              Checksum : 00                  
           TnlStatus : 01                           KeepAliveEn : 00                  
             IfCntEn : 00                              IfStatEn : 01                  
        RedundancyEn : 00                          ProtocolType : 00   
                McEn : 01                                IGMPEn : 00                
          ReasmBoard : 0041                              TnlMTU : 000005dc            
          TnlMTUIPv6 : 00000000                       SrcIPAddr : 192.168.1.2         
           DstIPAddr : 192.168.1.1                     VrfIndex : 0000                
        BindVrfIndex : 0000                      IfStatIndexIng : 00000014            
       IfStatIndexEg : 00000015                         IfIndex : 0000001b            

(结果个数 = 2)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 结果      | 查询结果。   |