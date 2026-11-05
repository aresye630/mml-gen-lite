# 配置到CG的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增CG或SGSN时，在配置完成SGSN到CG的路由数据后，可通过配置Ga接口数据建立SGSN到CG的逻辑连接。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- UNC软件安装已完成。

- 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
- 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
- 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

| 类别              | 参数名称                  | 取值样例                                       | 取值样例.1                                     | 获取方法            | 说明                           |
|:----------------|:----------------------|:-------------------------------------------|:-------------------------------------------|:----------------|:-----------------------------|
| ADD SERVICEIP   | IP版本（IPVERSION）       | IPv4、IPv6                                  | IPv4、IPv6                                  | 参见“水平网设LLD文档 ”。 | 配置Ga接口业务IP。                  |
| ADD SERVICEIP   | 业务IPv4地址（SERVICEIPV4） | 10.10.11.145                               | 10.10.11.145                               | 参见“水平网设LLD文档 ”。 | 配置Ga接口业务IP。                  |
| ADD SERVICEIP   | 业务IPv6地址（SERVICEIPV6） | 2001:db8:2001:145                          | 2001:db8:2001:145                          | 参见“水平网设LLD文档 ”。 | 配置Ga接口业务IP。                  |
| ADD SERVICEIP   | VPN实例名称（VPNINSTNAME）  | VPN_Billing                                | VPN_Billing                                | 参见“水平网设LLD文档 ”。 | 配置Ga接口业务IP。                  |
| ADD CHGCDPIP    | IP地址类型（IPT）           | IPv4、IPv6                                  | IPv4、IPv6                                  | 参见“水平网设LLD文档 ”。 | 增加CDP进程的IP地址。                |
| ADD CHGCDPIP    | IPv4地址（IPV4ADDR）      | 10.10.11.145                               | 10.10.11.145                               | 参见“水平网设LLD文档 ”。 | 增加CDP进程的IP地址。                |
| ADD CHGCDPIP    | IPv6地址（IPV6ADDR）      | 2001:db8:2001:145                          | 2001:db8:2001:145                          | 参见“水平网设LLD文档 ”。 | 增加CDP进程的IP地址。                |
| ADD CHGCDPIP    | 起始端口号（PORTBGN）        | 3699                                       | 3699                                       | 参见“水平网设LLD文档 ”。 | 增加CDP进程的IP地址。                |
| ADD CHGCDPIP    | 结束端口号（PORTEND）        | 3700                                       | 3700                                       | 参见“水平网设LLD文档 ”。 | 增加CDP进程的IP地址。                |
| ADD CHGCDPIP    | VPN名称（VPNNAME）        | VPN_Billing                                | VPN_Billing                                | 参见“水平网设LLD文档 ”。 | 增加CDP进程的IP地址。                |
| ADD CHGCG       | IP地址类型（IP）            | 10.100.3.17、10.100.3.16                    | 10.100.3.17、10.100.3.16                    | 参见“水平网设LLD文档 ”。 | 配置CG的基本信息。                   |
| ADD CHGCG       | 优先级（GRD）              | 1、0                                        | 1、0                                        | 参见“水平网设LLD文档 ”。 | 配置CG的基本信息。                   |
| ADD CHGCG       | GTP承载协议（PRO）          | UDP                                        | UDP                                        | 参见“水平网设LLD文档 ”。 | 配置CG的基本信息。                   |
| ADD CHGCG       | CG协议版本（CGR）           | R6                                         | R6                                         | 参见“水平网设LLD文档 ”。 | 配置CG的基本信息。                   |
| ADD CHGCG       | CG接收端口号（SPN）          | 3380                                       | 3380                                       | 参见“水平网设LLD文档 ”。 | 配置CG的基本信息。                   |
| ADD CHGCG       | 缺省CG（DEFAULTCG）       | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 配置CG的基本信息。                   |
| SET CHGGA       | GPRS CDR协议版本（GCR）     | R6                                         | R6                                         | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | UMTS CDR协议版本（UCR）     | R6                                         | R6                                         | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R98 CDR版本（CHGVER98）   | CMCCV130                                   | CMCCV130                                   | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R99 CDR版本（CHGVER99）   | GPP32015V360                               | GPP32015V360                               | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R4 CDR版本（CHGVER4）     | GPP32215V440                               | GPP32215V440                               | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R5 CDR版本（CHGVER5）     | GPP32215V560                               | GPP32215V560                               | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R6 CDR版本（CHGVER6）     | GPP32251V660                               | GPP32251V660                               | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R7 CDR版本（CHGVER7）     | GPP32251V740                               | GPP32251V740                               | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | R9 CDR版本（CHGVER9）     | GPP32251V940                               | GPP32251V940                               | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | CDR重发间隔（s）（ITVRES）    | 3                                          | 3                                          | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | CDR重发次数（RSNUM）        | 3                                          | 3                                          | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | 硬盘操作失败告警次数门限（HDDETH）  | 5                                          | 5                                          | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| SET CHGGA       | 硬盘空间不足门限（%）（HDDFSL）   | 70                                         | 70                                         | 参见“水平网设LLD文档 ”。 | 配置SGSN支持的计费协议版本。             |
| ADD CHGBEHA     | 计费行为（CB）              | B1                                         | B1                                         | 参见“水平网设LLD文档 ”。 | 增加计费行为参数。                    |
| ADD CHGBEHA     | 行为属性（BA）              | NOROAMING                                  | NOROAMING                                  | 参见“水平网设LLD文档 ”。 | 增加计费行为参数。                    |
| ADD CHGBEHA     | 支持的计费属性（ACC）          | HOTBILLING-1&FLATRATE-1&PREPAID-1&NORMAL-1 | HOTBILLING-1&FLATRATE-1&PREPAID-1&NORMAL-1 | 参见“水平网设LLD文档 ”。 | 增加计费行为参数。                    |
| SET CHGCHAR     | 计费属性（CC）              | HOTBILLING、FLATRATE、PREPAID、NORMAL         | HOTBILLING、FLATRATE、PREPAID、NORMAL         | 参见“水平网设LLD文档 ”。 | 配置计费属性参数                     |
| SET CHGCHAR     | 生成S-CDR（SP）           | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 配置计费属性参数                     |
| SET CHGPLMNCHAR | PLMN 类型（PLMN）         | VPLMN、HPLMN                                | VPLMN、HPLMN                                | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成M-CDR（MP）           | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成S-CDR（SP）           | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成S-SMO-CDR（SMOP）     | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成S-SMT-CDR（SMTP）     | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成LCS-MO-CDR（LCSMOP）  | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成LCS-MT-CDR（LCSMTP）  | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGPLMNCHAR | 生成LCS-NI-CDR（LCSNIP）  | YES                                        | YES                                        | 参见“水平网设LLD文档 ”。 | 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。 |
| SET CHGWKDY     | 星期序号（WKDAY）           | SUN、SAT、FRI、THURS、WED、TUES、MON             | SUN、SAT、FRI、THURS、WED、TUES、MON             | 参见“水平网设LLD文档 ”。 | 配置计费星期。                      |
| SET CHGWKDY     | 计费属性（CC）              | HOTBILLING、FLATRATE、PREPAID、NORMAL         | HOTBILLING、FLATRATE、PREPAID、NORMAL         | 参见“水平网设LLD文档 ”。 | 配置计费星期。                      |
| SET CHGWKDY     | 费率类型（TT）              | WEEKEND、WORK                               | WEEKEND、WORK                               | 参见“水平网设LLD文档 ”。 | 配置计费星期。                      |
| ADD CHGTARI     | 费率类型（TT）              | WORK                                       | WORK                                       | 参见“水平网设LLD文档 ”。 | 配置工作日的四种计费属性用户的费率时段。         |
| ADD CHGTARI     | 起始时间（ST）              | 00&00&00                                   | 00&00&00                                   | 参见“水平网设LLD文档 ”。 | 配置工作日的四种计费属性用户的费率时段。         |
| ADD CHGTARI     | 结束时间（ET）              | 00&00&00                                   | 00&00&00                                   | 参见“水平网设LLD文档 ”。 | 配置工作日的四种计费属性用户的费率时段。         |
| ADD CHGTARI     | 计费属性（CC）              | HOTBILLING、FLATRATE、PREPAID、NORMAL         | HOTBILLING、FLATRATE、PREPAID、NORMAL         | 参见“水平网设LLD文档 ”。 | 配置工作日的四种计费属性用户的费率时段。         |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置Ga接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.11.145", VPNINSTNAME="VPN_Billing";
   ADD SERVICEIP: IPVERSION=IPv6, SERVICEIPV6="2001:db8:2001:145", VPNINSTNAME="VPN_Billing";
   ```
3. 配置CG数据。

   1. 增加CDP进程的IP地址。

      ```
      ADD CHGCDPIP: IPT=IPv4, IPV4ADDR="10.10.11.145",PORTBGN=3699, PORTEND=3700, VPNNAME="VPN_Billing"; 
      ADD CHGCDPIP: IPT=IPv6, IPV6ADDR="2001:db8:2001:145",PORTBGN=3699, PORTEND=3700, VPNNAME="VPN_Billing";
      ```
   2. 配置CG的基本信息。

      ```
      ADD CHGCG: IP="10.100.3.17", GRD=1, PRO=UDP, CGR=R6, SPN=3380, DEFAULTCG=YES;
      ADD CHGCG: IP="10.100.3.16", GRD=0, PRO=UDP, CGR=R6, SPN=3380, DEFAULTCG=YES;
      ```
   3. 配置SGSN支持的计费协议版本。

      ```
      SET CHGGA: GCR=R6, UCR=R6, CHGVER98=CMCCV130, CHGVER99=GPP32015V360, CHGVER4=GPP32215V440, CHGVER5=GPP32215V560, CHGVER6=GPP32251V660, CHGVER7=GPP32251V740, CHGVER9=GPP32251V940, ITVRES=3, RSNUM=3, HDDETH=5, HDDFSL=70;
      ```
   4. 增加计费行为参数。

      ```
      ADD CHGBEHA: CB=B1, BA=NOROAMING, ACC=HOTBILLING-1&FLATRATE-1&PREPAID-1&NORMAL-1;
      ```
   5. 配置计费属性参数

      ```
      SET CHGCHAR: CC=HOTBILLING, SP=YES;
      SET CHGCHAR: CC=FLATRATE, SP=YES;
      SET CHGCHAR: CC=PREPAID, SP=YES;
      SET CHGCHAR: CC=NORMAL, SP=YES;
      ```
   6. 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。

      ```
      SET CHGPLMNCHAR: PLMN=VPLMN, MP=YES, SP=YES, SMOP=YES, SMTP=YES, LCSMOP=YES, LCSMTP=YES, LCSNIP=YES;
      SET CHGPLMNCHAR: PLMN=HPLMN, MP=YES, SP=YES, SMOP=YES, SMTP=YES, LCSMOP=YES, LCSMTP=YES, LCSNIP=YES;
      ```
4. 配置费率数据。

   1. 配置计费星期。

      ```
      SET CHGWKDY: WKDAY=SUN, CC=HOTBILLING, TT=WEEKEND;
      SET CHGWKDY: WKDAY=SAT, CC=HOTBILLING, TT=WEEKEND;
      SET CHGWKDY: WKDAY=FRI, CC=HOTBILLING, TT=WORK;
      SET CHGWKDY: WKDAY=THURS, CC=HOTBILLING, TT=WORK;
      SET CHGWKDY: WKDAY=WED, CC=HOTBILLING, TT=WORK;
      SET CHGWKDY: WKDAY=TUES, CC=HOTBILLING, TT=WORK;
      SET CHGWKDY: WKDAY=MON, CC=HOTBILLING, TT=WORK;
      SET CHGWKDY: WKDAY=SUN, CC=FLATRATE, TT=WEEKEND;
      SET CHGWKDY: WKDAY=SAT, CC=FLATRATE, TT=WEEKEND;
      SET CHGWKDY: WKDAY=FRI, CC=FLATRATE, TT=WORK;
      SET CHGWKDY: WKDAY=THURS, CC=FLATRATE, TT=WORK;
      SET CHGWKDY: WKDAY=WED, CC=FLATRATE, TT=WORK;
      SET CHGWKDY: WKDAY=TUES, CC=FLATRATE, TT=WORK;
      SET CHGWKDY: WKDAY=MON, CC=FLATRATE, TT=WORK;
      SET CHGWKDY: WKDAY=SUN, CC=PREPAID, TT=WEEKEND;
      SET CHGWKDY: WKDAY=SAT, CC=PREPAID, TT=WEEKEND;
      SET CHGWKDY: WKDAY=FRI, CC=PREPAID, TT=WORK;
      SET CHGWKDY: WKDAY=THURS, CC=PREPAID, TT=WORK;
      SET CHGWKDY: WKDAY=WED, CC=PREPAID, TT=WORK;
      SET CHGWKDY: WKDAY=TUES, CC=PREPAID, TT=WORK;
      SET CHGWKDY: WKDAY=MON, CC=PREPAID, TT=WORK;
      SET CHGWKDY: WKDAY=SUN, CC=NORMAL, TT=WEEKEND;
      SET CHGWKDY: WKDAY=SAT, CC=NORMAL, TT=WEEKEND;
      SET CHGWKDY: WKDAY=FRI, CC=NORMAL, TT=WORK;
      SET CHGWKDY: WKDAY=THURS, CC=NORMAL, TT=WORK;
      SET CHGWKDY: WKDAY=WED, CC=NORMAL, TT=WORK;
      SET CHGWKDY: WKDAY=TUES, CC=NORMAL, TT=WORK;
      SET CHGWKDY: WKDAY=MON, CC=NORMAL, TT=WORK;
      ```
   2. 配置工作日的四种计费属性用户的费率时段。

      ```
      ADD CHGTARI: TT=WORK, ST=00&00&00, ET=00&00&00, CC=HOTBILLING;
      ADD CHGTARI: TT=WORK, ST=00&00&00, ET=00&00&00, CC=FLATRATE;
      ADD CHGTARI: TT=WORK, ST=00&00&00, ET=00&00&00, CC=PREPAID;
      ADD CHGTARI: TT=WORK, ST=00&00&00, ET=00&00&00, CC=NORMAL;
      ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 检查Ga接口通信状态。

   **DSP CHGCG**

   - **预期结果：**“CG状态”应为“通信正常”。

     ```
     %%DSP CHGCG:;%%
     RETCODE = 0  操作成功。

     输出结果如下
     ------------
     RU名称            进程号    CG的IP地址    CG状态      GTP承载协议    CG接收端口号

     USN_SP_RU_0064    0         10.1.1.1       通信正常    UDP            3386        
     USN_SP_RU_0064    0         10.1.1.2       通信正常    UDP            3386        
     (结果个数 = 2)
     ---    END
     ```
   - **异常结果：**“CG状态”应为“通信中断”。

     异常处理过程参见ALM-80663 SGSN和CG通讯中断。
3. 验证话单传递功能。
   1. 创建Ga接口跟踪。

      **说明** 

      参数选择：

      - Ru名称：资源单元的名称。
      - CGF的IP地址：要跟踪的CG地址。
      - 其它参数：选择默认值。
   2. 执行话单测试命令。
      - 2G

        **TST CHGCDR**: CDRTYPE=SCDR, SYSTYPE=GPRS;
      - 3G

        **TST CHGCDR**: CDRTYPE=SCDR, SYSTYPE=UMTS;
   3. 检查话单测试命令结果。
      - **预期结果：**命令执行成功。
      - **异常结果：**命令测试失败，有10810号告警产生。

        异常处理过程参见ALM-10810 CG未配置。
   4. 检查Ga接口跟踪结果。
      - **预期结果：**Ga接口可以跟踪到Echo Request和Echo Response消息，参见图1。

        **图1** Ga接口跟踪（样例）
      - **异常结果：**Ga接口跟踪无话单消息，有10810号告警产生。

        异常处理过程参见ALM-10810 CG未配置。

        **说明** 

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。