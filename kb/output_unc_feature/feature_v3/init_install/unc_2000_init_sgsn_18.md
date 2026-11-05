# 配置Hostfile的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增SGSN时，可通过配置Hostfile数据，用于SGSN在以下流程中进行域名解析：

* 在PDP激活时根据APN解析GGSN IP地址。
* Inter RAU时根据RAI解析对端SGSN IP地址。
* Relocation时根据目的RNC ID解析对端SGSN IP地址。
* SGSN Pool寻址时通过Default SGSN或者NRI+RAI解析SGSN IP地址。

进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：

* DNS服务器是网络中专门提供域名解析服务的服务器。
* DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。
* 本地主机信息表Hostfile则保存在本地SGSN中，包含的记录比较少。

SGSN进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 1 | 参见“水平网设LLD文档 ”。 | 配置Hostfile解析记录。 |
|  | 主机名（HOSTNAME） | CMNET.MNC000.MCC460.GPRS |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |
|  | IPV4ADDR1（IPv4地址1） | 192.168.31.2 |  |  |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 2 |  |  |
|  | 主机名（HOSTNAME） | CMWAP.MNC000.MCC460.GPRS |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |
|  | IPV4ADDR1（IPv4地址1） | 192.168.32.4、192.168.32.5 |  |  |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 3 |  |  |
|  | 主机名（HOSTNAME） | RAC0001.LAC5320.MNC0000.MCC0460.GPRS |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |
|  | IPV4ADDR1（IPv4地址1） | 10.137.196.81 |  |  |
| ****ADD IPV4DNSH**** | 主机名索引（HSINDEX） | 4 |  |  |
|  | 主机名（HOSTNAME） | RNC0450.MNC0000.MCC0460.GPRS |  |  |
|  | 地址区间号（ADDRSECTION） | SECTION1 |  |  |
|  | IPV4ADDR1（IPv4地址1） | 172.25.6.53、172.25.6.54 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. **可选：**配置PDP激活上下文时GGSN的DNS记录。

   ```
   ADD IPV4DNSH: HSINDEX=1, HOSTNAME="CMNET.MNC000.MCC460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.31.2";
   ADD IPV4DNSH: HSINDEX=2, HOSTNAME ="CMWAP.MNC000.MCC460.GPRS", ADDRSECTION =SECTION1, IPV4ADDR1="192.168.32.4", IPV4ADDR2="192.168.32.5";
   ```
3. **可选：**配置RAU时SGSN的DNS记录。

   ```
   ADD IPV4DNSH: HSINDEX=1, HOSTNAME="CMNET.MNC000.MCC460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.31.2";
   ```
4. **可选：**配置RELOCATION时GGSN的DNS记录。

   ```
   ADD IPV4DNSH: HSINDEX=4, HOSTNAME="RNC0450.MNC0000.MCC0460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="172.25.6.53", IPV4ADDR2="172.25.6.54";
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 执行以下命令，查询具体配置是否与数据规划表中的值一致。

   LST IPV4DNSH

版权所有 © 华为技术有限公司
