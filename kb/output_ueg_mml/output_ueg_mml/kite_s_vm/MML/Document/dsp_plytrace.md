# 查询策略跟踪（DSP PLYTRACE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

此命令用于运维人员判断在CSLB转发路径上是否有完整的转发策略。转发路径分为上行和下行，其中上行指数据流从VNRS发往CSLB方向，下行指数据流从服务侧发往CSLB方向。

#### 注意事项

- 该命令执行后立即生效。
- 该命令批量下发可能导致执行超时。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称      | 参数说明                                                                                                              |
|:----------|:----------|:------------------------------------------------------------------------------------------------------------------|
| APPVNFCID | 服务VNFC ID | 可选必选说明：必选参数 参数含义：CSLB服务的VNFC ID，可通过DSP SRVIP查询。 取值范围：0~4294967294 默认值：无                                           |
| APPINSTID | 服务实例ID    | 可选必选说明：必选参数 参数含义：服务实例ID，通过DSP SRVIP：查询Instance ID。 取值范围：0~4294967294 默认值：无                                        |
| DIRECTION | 报文方向      | 可选必选说明：必选参数 参数含义：数据报文发送的方向。 取值范围：“E_FLOW_FRIP(从VNRS发往CSLB) ”“E_FLOW_FRAPP(从服务侧发往CSLB) ” 默认值：无                     |
| IPTYPE    | IP类型      | 可选必选说明：可选参数 参数含义：IP地址类型 取值范围：“IPV4(IPV4) ”“IPV6(IPV6) ” 默认值：无                                                     |
| SRCIPV4   | 源IPv4     | 可选必选说明：可选参数 参数含义：源IPv4地址 取值范围：0.0.0.0~255.255.255.255 默认值：无                                                       |
| SRCIPV6   | 源IPv6     | 可选必选说明：可选参数 参数含义：源IPv6地址 取值范围：0:0:0:0:0:0:0:0~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无                       |
| SRCPORT   | 源端口       | 可选必选说明：可选参数 参数含义：源端口 默认值：无                                                                                        |
| DSTIPV4   | 目的IPv4    | 可选必选说明：可选参数 参数含义：目的IPv4地址 取值范围：0.0.0.0~255.255.255.255 默认值：无                                                      |
| DSTIPV6   | 目的IPv6    | 可选必选说明：可选参数 参数含义：目的IPv6地址 取值范围：0~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无                                    |
| DSTPORT   | 目的端口      | 可选必选说明：可选参数 参数含义：目的端口 默认值：无                                                                                       |
| PROTTYPE  | 协议类型      | 可选必选说明：可选参数 参数含义：协议类型 取值范围：“PE_PROT_ICMP(Icmp) ”“PE_PROT_TCP(Tcp) ”“PE_PROT_UDP(Udp) ”“PE_PROT_SCTP(Sctp) ” 默认值：无 |
| VPNNAME   | VPN名称     | 可选必选说明：可选参数 参数含义：VPN名称 取值范围：0~31 默认值：无                                                                            |
| LBINDEX   | LB索引      | 可选必选说明：可选参数 参数含义：CSLB的索引号。 默认值：无                                                                                  |

#### 使用实例

- 查询VNRS发往CSLB的转发策略。

  `DSP PLYTRACE:APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRIP,DSTIPV4="10.255.255.255",DSTPORT=12033,PROTTYPE=PE_PROT_UDP,VPNNAME="test1",LBINDEX=2;`

  ```
  %%DSP PLYTRACE: APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRIP,DSTIPV4="10.255.255.255",DSTPORT=12033,PROTTYPE=PE_PROT_UDP,VPNNAME="test1",LBINDEX=2;%%
  RETCODE = 0  操作成功。
  结果如下:
  -------------------------
  服务VNFC ID  =  4
   服务实例ID  =  91
     报文方向  =  从VNRS发往CSLB
       IP类型  =  IPV4
       源IPv4  =  10.0.0.0
       源IPv6  =  2001:0db8::
       源端口  =  0
     目的IPv4  =  10.255.255.255
     目的IPv6  =  2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   目的端口号  =  12033
     协议类型  =  Udp
      VPN名称  =  test1
       LB索引  =  2
   结果字符串  =  
  LBSRV:
  Match = Success;usInstIdx = 4;FPlyID = 8192;FIdentID = 4096;
  VPNEXCH:
  Match = Success;udwMpfVpnIdx = 0;
  LBSRV:
  Match = Success;FPlyID = 8192;FIdentID = 4096;CoDeploy = True
  IT'S NOT RESERVED BY CSDB
  LBSRV:
  Match = Success;VpnFlag = 0;FPlyID = 8192;FIdentID = 4096
  POLICY:
  Match= Success;Type = 4;ID = 8192;Key1 = 1426846570;Key2 = 17;Key3 = 12033;Key4 = 0;ActionID = 4;NextHopID = 1;NextHopIndex = 16553
  NEXTHOP:
  Match= Success;ID= 1;Idx = 16553;Tp = 2416521521;Tb = 2;Qos = 1
  RESULT:
  Success
  (结果个数 = 1)
  ---    END
  ```
- 查询服务侧发往CSLB的转发策略。

  `DSP PLYTRACE:APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRAPP,SRCIPV4="10.0.0.0",SRCPORT=12033,VPNNAME="SADF",LBINDEX=1;`

  ```
  %%DSP PLYTRACE: APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRAPP,SRCIPV4="10.0.0.0",SRCPORT=12033,VPNNAME="SADF",LBINDEX=1;%%
  RETCODE = 0  操作成功。
  结果如下:
  -------------------------
   服务VNFC ID  =  4
    服务实例ID  =  91
      报文方向  =  从服务VNFC发往CSLB
        IP类型  =  IPV4
        源IPv4  =  10.0.0.0
        源IPv6  =  2001:0db8::
        源端口  =  12033
      目的IPv4  =  10.255.255.255
      目的IPv6  =  2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
    目的端口号  =  0
      协议类型  =  Icmp
       VPN名称  =  SADF
        LB索引  =  1
    结果字符串  =  
  VPNCFG:
  Match = Success;AppIdx = 0;LocalIdx = 0
  LBSRV:
  Match = Success; FPlyID = 8192; FIdentID = 4096;CoDeploy=True
  VPNRT:
  Match = Success;VpnIdx = 4;Tp = 0;Tb = 0
  RESULT:
  Success
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称     | 输出项解释                                                             |
|:----------|:------------------------------------------------------------------|
| 服务VNFC ID | CSLB服务的VNFC ID 取值范围：0~4294967296                                  |
| 服务实例ID    | 服务实例ID 取值范围：0~4294967296                                          |
| 报文方向      | 报文发送的方向 取值范围：“from Server to CSLB_VNFC ”“from VNRS to CSLB_VNFC ” |
| IP类型      | IP地址类型 取值范围：“IPV4(IPV4) ”“IPV6(IPV6) ”                            |
| 源IPv4     | 源IPv4的地址                                                          |
| 源IPv6     | 源IPv6的地址                                                          |
| 源端口       | 源端口 取值范围：0~65536                                                  |
| 目的IPv4    | 目的IPv4地址                                                          |
| 目的IPv6    | 目的IPv6地址                                                          |
| 目的端口号     | 目的端口 取值范围：0~65536                                                 |
| 协议类型      | 协议类型                                                              |
| VPN名称     | VPN名称                                                             |
| LB索引      | CSLB的索引号                                                          |
| 结果字符串     | 返回的查询结果                                                           |