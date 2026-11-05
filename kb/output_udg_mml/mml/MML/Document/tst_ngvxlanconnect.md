# 探测5G LAN Vxlan隧道连通性（TST NGVXLANCONNECT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

该命令控制用户面业务处理单元通过N6 Vxlan隧道向对端UPF发送ARP请求消息，根据是否收到ARP响应确定不同UPF间同一个5G LAN组的N6 Vxlan隧道是否互通。

#### 注意事项

- 该命令执行后立即生效。
- 该命令同一时刻只能执行一次。
- 该命令与NGSRVPING命令同一时刻只能执行一次。
- 该命令与NGVNVIFPING命令同一时刻只能执行一次。
- 该命令执行前需要执行ADD NGVNINSTANCE配置5G LAN组。
- 该命令执行前需要执行ADD NGVNVIF命令配置5G LAN组的虚拟接口，该虚拟接口的IPv4地址用于填充发送ARP报文的源IP地址。
- 该命令执行前需要SET UPETHSRVPARA命令配置用户面以太业务的MAC地址，该MAC地址用于填充发送ARP报文的源MAC地址。
- 该命令的目的IPv4地址不能与ADD NGVNVIF命令中的虚拟接口IP地址相同。
- 该命令最多发送10次ARP请求，单次ARP请求的超时时间为2s，期间没有收到ARP响应，探测结果为不互通。
- 该命令执行结果为互通时，设置NGVNINSTANCE命令的VXLANINTERWORK参数为“YES”；不互通时，设置NGVNINSTANCE命令的VXLANINTERWORK参数为“NO”。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                    | 参数说明                                                                                                                                                                                                                                                                                                                            |
|:---------------|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VNINSTANCE     | 5G LAN组名称               | 可选必选说明：必选参数 参数含义：该参数用于指定5G LAN组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。 默认值：无 配置原则：无 |
| PEERUPFVIFIPV4 | 对端UPF 5G LAN组虚拟接口IPv4地址 | 可选必选说明：必选参数 参数含义：该参数用于配置对端UPF 5G LAN组配置的虚拟接口IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                                                                                                                                                                                                                    |

#### 使用实例

- 探测5G LAN Vxlan隧道连通性，探测结果为互通：

  ```
  %%TST NGVXLANCONNECT: VNINSTANCE="a0000001-460-01-01", PEERUPFVIFIPV4="192.168.0.2";%%
  RETCODE = 99999  Real Time Report Success

  仍有后续报告输出
  ---    END

  %%TST NGVXLANCONNECT: VNINSTANCE="a0000001-460-01-01", PEERUPFVIFIPV4="192.168.0.2";%%
  RETCODE = 0  操作成功

  The inter-UPF VXLAN tunnel over the N6 interface is reachable and the number of times the ARP request is sent is 1.

  共有2个报告
  ---    END
  ```
- 探测5G LAN Vxlan隧道连通性，探测结果为不互通：

  ```
  %%TST NGVXLANCONNECT: VNINSTANCE="a0000001-460-01-01", PEERUPFVIFIPV4="192.168.0.2";%%
  RETCODE = 99999  Real Time Report Success

  仍有后续报告输出
  ---    END

  %%TST NGVXLANCONNECT: VNINSTANCE="a0000001-460-01-01", PEERUPFVIFIPV4="192.168.0.2";%%
  RETCODE = 0  操作成功

  The inter-UPF VXLAN tunnel over the N6 interface is unreachable.

  共有2个报告
  ---    END
  ```