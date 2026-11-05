# 配置到SGSN的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增SGSN时，在配置完成到SGSN的路由数据后，可通过配置Gn接口数据建立SGSN到SGSN的逻辑连接。

**说明** 

S16 接口支持GTP-U协议栈，如果需要将S16 接口和其他接口分离部署，可以通过****ADD GTPULE****配置S16接口GTP-U IP，并通过****ADD GTPUINTFATTR****配置GTPU逻辑IP隔离。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
- 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别              | 参数名称                          | 取值样例                               | 取值样例.1                             | 获取方法            | 说明               |
|:----------------|:------------------------------|:-----------------------------------|:-----------------------------------|:----------------|:-----------------|
| ADD SERVICEIP   | IP版本（IPVERSION）               | IPv4                               | IPv4                               | 参见“水平网设LLD文档 ”。 | 配置Gn接口业务IP。      |
| ADD SERVICEIP   | 业务IPv4地址（SERVICEIPV4）         | 192.168.0.1                        | 192.168.0.1                        | 参见“水平网设LLD文档 ”。 | 配置Gn接口业务IP。      |
| ADD SERVICEIP   | VPN实例名称（VPNINSTNAME）          | VPN_CN                             | VPN_CN                             | 参见“水平网设LLD文档 ”。 | 配置Gn接口业务IP。      |
| ADD GTPCLE      | 组号（GROUPID）                   | 0                                  | 0                                  | 参见“水平网设LLD文档 ”。 | 配置GTPC IP。       |
| ADD GTPCLE      | IP地址类型（IPTYPE）                | TPTADDR_TYPE_IPV4                  | TPTADDR_TYPE_IPV4                  | 参见“水平网设LLD文档 ”。 | 配置GTPC IP。       |
| ADD GTPCLE      | IPv4地址（LEIPV4）                | 192.168.0.1                        | 192.168.0.1                        | 参见“水平网设LLD文档 ”。 | 配置GTPC IP。       |
| ADD GTPCLE      | VPN名称（VPNNAME）                | VPN_CN                             | VPN_CN                             | 参见“水平网设LLD文档 ”。 | 配置GTPC IP。       |
| ADD GTPULE      | 组号（GROUPID）                   | 0                                  | 0                                  | 参见“水平网设LLD文档 ”。 | 配置GTPU IP。       |
| ADD GTPULE      | IP地址类型（IPTYPE）                | TPTADDR_TYPE_IPV4                  | TPTADDR_TYPE_IPV4                  | 参见“水平网设LLD文档 ”。 | 配置GTPU IP。       |
| ADD GTPULE      | IPv4地址（LEIPV4）                | 192.168.0.1                        | 192.168.0.1                        | 参见“水平网设LLD文档 ”。 | 配置GTPU IP。       |
| ADD GTPULE      | VPN名称（VPNNAME）                | VPN_CN                             | VPN_CN                             | 参见“水平网设LLD文档 ”。 | 配置GTPU IP。       |
| SET UGTP        | 空闲计数器扫描间隔（秒）（ICI）             | 180                                | 180                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET UGTP        | SM信令路径空闲计数器（SSI）              | 60                                 | 60                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET UGTP        | MM信令路径空闲计数器（MSI）              | 60                                 | 60                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET UGTP        | GTPMAP路径空闲计数器（GMSI）           | 60                                 | 60                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET UGTP        | 路径版本探测扫描周期（分钟）（PATHVERCHKINT） | 60                                 | 60                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 发送ECHO Request的路径（ECHOSIG）    | ALL                                | ALL                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 发送GTPv2 Echo请求间隔（s）（V2EI）     | 239                                | 239                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 乱序信元（OTSIE）                   | DENY                               | DENY                               | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 路径数过载门限（%）（POTHD）             | 85                                 | 85                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 路径数过载恢复（%）（PNTHD）             | 80                                 | 80                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 路径数拥塞门限（%）（PCTHD）             | 95                                 | 95                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 路径数拥塞恢复（%）（PRTHD）             | 90                                 | 90                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 检查GTP扩展头类型个数上限（GTPEXT）        | 10                                 | 10                                 | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 检查GTP扩展头类型长度上限（GTPEXLEN）      | 100                                | 100                                | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| SET GTPPUB      | 本端可处理的请求消息的最高GTP版本（GTPVER）    | GTPv2                              | GTPv2                              | 参见“水平网设LLD文档 ”。 | 配置GTP路径管理参数。     |
| ADD IPV4DNSH    | 主机名索引（HSINDEX）                | 1、2                                | 1、2                                | 参见“水平网设LLD文档 ”。 | 配置RAI解析数据。       |
| ADD IPV4DNSH    | 主机名（HOSTNAME）                 | RAC0001.LAC5321.MNC000.MCC460.GPRS | RAC0001.LAC5321.MNC000.MCC460.GPRS | 参见“水平网设LLD文档 ”。 | 配置RAI解析数据。       |
| ADD IPV4DNSH    | 地址区间号（ADDRSECTION）            | SECTION1                           | SECTION1                           | 参见“水平网设LLD文档 ”。 | 配置RAI解析数据。       |
| ADD IPV4DNSH    | IPv4地址1（IPV4ADDR1）            | 192.168.0.33                       | 192.168.0.33                       | 参见“水平网设LLD文档 ”。 | 配置RAI解析数据。       |
| ADD IPV4DNSH    | IPv4地址1（IPV4ADDR2）            | 192.168.0.34                       | 192.168.0.34                       | 参见“水平网设LLD文档 ”。 | 配置RAI解析数据。       |
| ADD SGSNCHARACT | 对端设备范围（RANGE）                 | SPECIAL_SGSN                       | SPECIAL_SGSN                       | 参见“水平网设LLD文档 ”。 | 配置对端SGSN支持的协议版本。 |
| ADD SGSNCHARACT | IP地址类型（IPT）                   | IPV4                               | IPV4                               | 参见“水平网设LLD文档 ”。 | 配置对端SGSN支持的协议版本。 |
| ADD SGSNCHARACT | SGSN IPv4信令面地址（IPV4）          | 192.168.0.33、192.168.0.34          | 192.168.0.33、192.168.0.34          | 参见“水平网设LLD文档 ”。 | 配置对端SGSN支持的协议版本。 |
| ADD SGSNCHARACT | 掩码（MASKV4）                    | 255.255.255.255                    | 255.255.255.255                    | 参见“水平网设LLD文档 ”。 | 配置对端SGSN支持的协议版本。 |
| ADD SGSNCHARACT | SGSN支持的QoS版本（QOSVER）          | R5QOS                              | R5QOS                              | 参见“水平网设LLD文档 ”。 | 配置对端SGSN支持的协议版本。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置Gn接口业务IP

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.0.1", VPNINSTNAME="VPN_CN";
   ```
3. 配置GTP数据。

   1. 配置GTPC IP。

      ```
      ADD GTPCLE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.0.1",VPNNAME="VPN_CN";
      ```
   2. 配置GTPU IP。

      ```
      ADD GTPULE: GROUPID=0, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.0.1",VPNNAME="VPN_CN";
      ```
   3. 配置GTP路径管理参数。

      ```
      SET UGTP: ICI=180, SSI=60, MSI=60, GMSI=60, PATHVERCHKINT=60;
      SET GTPPUB: ECHOSIG=ALL, V2EI=239, OTSIE=DENY, POTHD=85, PNTHD=80, PCTHD=95, PRTHD=90, GTPEXT=10, GTPEXLEN=100, GTPVER=GTPv2;
      ```
4. 配置SGSN上的数据。

   1. 配置RAI解析数据。

      ```
      ADD IPV4DNSH: HSINDEX=1, HOSTNAME="RAC0001.LAC5321.MNC000.MCC460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.0.33", IPV4ADDR2="192.168.0.34";
      ADD IPV4DNSH: HSINDEX=2, HOSTNAME="RAC0002.LAC5321.MNC000.MCC460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.0.33", IPV4ADDR2="192.168.0.34";
      ```
   2. 配置对端SGSN支持的协议版本。

      ```
      ADD SGSNCHARACT: RANGE=SPECIAL_SGSN, IPT=IPV4, IPV4="192.168.0.33", MASKV4="255.255.255.255", QOSVER=R5QOS;
      ADD SGSNCHARACT: RANGE=SPECIAL_SGSN, IPT=IPV4, IPV4="192.168.0.34", MASKV4="255.255.255.255", QOSVER=R5QOS;
      ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查GTPC GTP路径对端是否可达。

   **TST GTPCPATH**

   **说明** 

   IP地址为SGSN信令面IP。

   - **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.0.1", PEERIPV4ADDR="192.168.0.33";%%
     RETCODE = 0  操作成功

     操作结果如下:
     -------------------------
     本端IPv4地址  =  192.168.0.1
     对端IPv4地址  =  192.168.0.33
        GTP版本  =  GTPv1
     (结果数目 = 1)

     ---    END
     ```
   - **异常结果：**对端不可达。

     异常处理过程参见ALM-80610 GTPC路径故障。
3. 检查GTPU GTP路径对端是否可达。

   **TST GTPUPATH**

   **说明** 

   IP地址为SGSN用户面IP。

   - **预期结果：**对端可达，此处以IPv4为例。

     ```
     %%TST GTPUPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="10.2.9.20", PEERIPV4ADDR="10.2.14.20";%%
     RETCODE = 0  操作成功

     操作结果如下:
     -------------------------
     本端IP地址  =  10.2.9.20
     对端IP地址  =  10.2.14.20
        GTP版本  =  GTPv1
     (结果数目 = 1)

     ---    END
     ```
   - **异常结果：**对端不可达。

     异常处理过程参见ALM-80661 GTPU路径故障。