# 显示离线计费话单参数（LST OFCCDRPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询离线计费话单参数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示离线计费话单参数：

```
LST OFCCDRPARA:;
```

```
RETCODE = 0  操作成功

离线话单参数配置
----------------
                                    gsn-node-id字段前缀  =  NULL
                                  gsn-node-id字段分隔符  =  NULL
                                     SP合一网关话单控制  =  PGW-CDR
                      PGW-CDR携带List of Traffic Volume  =  使能
          PGW-CDR话单的List of Service Data携带RAT-Type  =  不使能
    PGW-CDR话单List of Service Data容器携带APN-AMBR开关  =  不使能
                                GCDR话单的sgsnAddress值  =  GTPC地址
    OCS故障导致用户离线后产生的话单pSFreeFormatData格式  =  十六进制
                                   CCFH强制产生话单开关  =  不使能
       CCFH强制产生话单填充的Charging Characteristics值  =  NULL
                           R6 eGCRD支持CCFH强制生成话单  =  不使能
                                  Last Activity功能开关  =  不使能
           PGW-CDR话单LoSD携带Serving PLMN Rate Control  =  不使能
SGW-CDR话单的LoTV携带CP CIoT EPS Optimisation Indicator  =  不使能
                     SGW-CDR流量容器携带扩展Qos参数开关  =  不使能
                  PGW-CDR话单的LoSD携带APN Rate Control  =  不使能
         SGW-CDR话单的LoTV携带Serving PLMN Rate Control  =  不使能
                     PGW-CDR业务容器携带扩展Qos参数开关  =  不使能
                     PGW-CDR流量容器携带扩展Qos参数开关  =  不使能
G-CDR/PGW-CDR中用户IPv6地址Interface Identifier填写方式  =  填写全0的Interface Identifier
      SGW-CDR中用户IPv6地址Interface Identifier填写方式  =  填写全0的Interface Identifier
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET OFCCDRPARA的参数说明。