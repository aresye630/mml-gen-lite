# 显示当前安全CAR信息（DSP SECCARINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来显示防攻击策略中的CAR信息。

#### 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                               |
|:------------|:----------|:---------------------------------------------------------------------------------------------------|
| RUNAME      | RU名称      | 可选必选说明：必选参数 参数含义：资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |
| SECCARSYSID | 安全CAR系统ID | 可选必选说明：可选参数 参数含义：安全CAR系统ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～65535。 默认值：无                                |

#### 使用实例

查看当前生效的防攻击报文策略中的CAR信息：

```
DSP SECCARINFO:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```
RETCODE = 0  操作成功

结果如下
--------
RU名称                      安全CAR系统ID    安全策略编号    承诺信息速率（kbps）    承诺突发尺寸（bytes）    缺省承诺信息速率（kbps）    缺省承诺突发尺寸（bytes）    优先级    最小包补偿长度    缺省优先级    缺省最小包补偿长度    安全策略描述            

VNODE_VNRS_VNFC_IPU_0064    1                0               64                      10000                    64                          10000                        高        128               高            128                   SSH Server packet         
VNODE_VNRS_VNFC_IPU_0064    5                0               512                     9000000                  512                         9000000                      高        128               高            128                   BGP packet                
VNODE_VNRS_VNFC_IPU_0064    6                0               1000                    100000                   1000                        100000                       低        128               低            128                   LDP packet                
VNODE_VNRS_VNFC_IPU_0064    8                0               1000                    9000000                  1000                        9000000                      高        128               高            128                   OSPF packet               
VNODE_VNRS_VNFC_IPU_0064    12               0               512                     256000                   512                         256000                       高        128               高            128                   ICMP packet               
VNODE_VNRS_VNFC_IPU_0064    15               0               512                     60000                    512                         60000                        高        128               高            128                   IPV4 ARP packet           
VNODE_VNRS_VNFC_IPU_0064    17               0               1100                    9000000                  1100                        9000000                      中        350               中            350                   DHCP packet               
VNODE_VNRS_VNFC_IPU_0064    27               0               2000                    20000                    2000                        20000                        高        128               高            128                   BFD packet                
VNODE_VNRS_VNFC_IPU_0064    32               0               64                      10000                    64                          10000                        高        128               高            128                   SSH Client packet         
VNODE_VNRS_VNFC_IPU_0064    48               0               256                     9000000                  256                         9000000                      高        128               高            128                   TCPSYN packet             
VNODE_VNRS_VNFC_IPU_0064    50               0               256                     100000                   256                         100000                       低        128               低            128                   IPv4 ARP miss             
VNODE_VNRS_VNFC_IPU_0064    51               0               512                     20000                    512                         20000                        中        128               中            128                   IPV4 option packet        
VNODE_VNRS_VNFC_IPU_0064    52               0               1000                    9000000                  1000                        9000000                      高        128               高            128                   IPV4 GRE packet           
VNODE_VNRS_VNFC_IPU_0064    53               0               1000                    10000                    1000                        10000                        低        128               低            128                   Unknown packet            
VNODE_VNRS_VNFC_IPU_0064    54               0               256                     9000000                  256                         9000000                      中        128               中            128                   IPV4 TCP packet to CPU    
VNODE_VNRS_VNFC_IPU_0064    56               0               256                     9000000                  256                         9000000                      中        128               中            128                   IPV4 UDP packet to CPU    
VNODE_VNRS_VNFC_IPU_0064    58               0               512                     9000000                  512                         9000000                      中        128               中            128                   Fragment packet           
VNODE_VNRS_VNFC_IPU_0064    60               0               256                     2560                     256                         2560                         高        128               高            128                   Tcpsyn packets for SSH    
VNODE_VNRS_VNFC_IPU_0064    61               0               256                     2560                     256                         2560                         高        128               高            128                   Tcpsyn packets for TELNET 
VNODE_VNRS_VNFC_IPU_0064    62               0               512                     9000000                  512                         9000000                      高        128               高            128                   IPV6_BGP                  
VNODE_VNRS_VNFC_IPU_0064    63               0               256                     256000                   256                         256000                       高        128               高            128                   IPV6_ICMP                 
VNODE_VNRS_VNFC_IPU_0064    64               0               576                     209600                   576                         209600                       高        128               高            128                   IPV6_NA                   
VNODE_VNRS_VNFC_IPU_0064    65               0               576                     209600                   576                         209600                       高        128               高            128                   IPV6_NS                   
VNODE_VNRS_VNFC_IPU_0064    66               0               1000                    9000000                  1000                        9000000                      高        128               高            128                   IPV6_OSPF                 
VNODE_VNRS_VNFC_IPU_0064    67               0               576                     209600                   576                         209600                       高        128               高            128                   IPV6_RA                   
VNODE_VNRS_VNFC_IPU_0064    68               0               576                     209600                   576                         209600                       高        128               高            128                   IPV6_RS                   
VNODE_VNRS_VNFC_IPU_0064    69               0               400                     1000000                  400                         1000000                      高        128               高            128                   IPV6_MLD                  
VNODE_VNRS_VNFC_IPU_0064    70               0               512                     512000                   512                         512000                       低        128               低            128                   IPV4 default packet to CPU
VNODE_VNRS_VNFC_IPU_0064    71               0               1000                    100000                   1000                        100000                       高        128               高            128                   IPV6 default packet to CPU
VNODE_VNRS_VNFC_IPU_0064    89               0               512                     51200                    512                         51200                        中        128               中            128                   IPV6 DHCP packet          
VNODE_VNRS_VNFC_IPU_0064    125              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 1       
VNODE_VNRS_VNFC_IPU_0064    126              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 2       
VNODE_VNRS_VNFC_IPU_0064    127              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 3       
VNODE_VNRS_VNFC_IPU_0064    128              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 4       
VNODE_VNRS_VNFC_IPU_0064    129              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 5       
VNODE_VNRS_VNFC_IPU_0064    130              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 6       
VNODE_VNRS_VNFC_IPU_0064    131              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 7       
VNODE_VNRS_VNFC_IPU_0064    132              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 8       
VNODE_VNRS_VNFC_IPU_0064    133              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 9       
VNODE_VNRS_VNFC_IPU_0064    134              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 10      
VNODE_VNRS_VNFC_IPU_0064    135              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 11      
VNODE_VNRS_VNFC_IPU_0064    136              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 12      
VNODE_VNRS_VNFC_IPU_0064    137              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 13      
VNODE_VNRS_VNFC_IPU_0064    138              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 14      
VNODE_VNRS_VNFC_IPU_0064    139              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 15      
VNODE_VNRS_VNFC_IPU_0064    140              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 16      
VNODE_VNRS_VNFC_IPU_0064    141              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 17      
VNODE_VNRS_VNFC_IPU_0064    142              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 18      
VNODE_VNRS_VNFC_IPU_0064    143              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 19      
VNODE_VNRS_VNFC_IPU_0064    144              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 20      
VNODE_VNRS_VNFC_IPU_0064    145              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 21      
VNODE_VNRS_VNFC_IPU_0064    146              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 22      
VNODE_VNRS_VNFC_IPU_0064    147              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 23      
VNODE_VNRS_VNFC_IPU_0064    148              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 24      
VNODE_VNRS_VNFC_IPU_0064    149              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 25      
VNODE_VNRS_VNFC_IPU_0064    150              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 26      
VNODE_VNRS_VNFC_IPU_0064    151              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 27      
VNODE_VNRS_VNFC_IPU_0064    152              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 28      
VNODE_VNRS_VNFC_IPU_0064    153              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 29      
VNODE_VNRS_VNFC_IPU_0064    154              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 30      
VNODE_VNRS_VNFC_IPU_0064    155              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 31      
VNODE_VNRS_VNFC_IPU_0064    156              0               2000                    20000                    2000                        20000                        低        128               低            128                   User defined flow 32      
VNODE_VNRS_VNFC_IPU_0064    157              0               0                       0                        0                           0                            低        128               低            128                   Blacklist                 
VNODE_VNRS_VNFC_IPU_0064    158              0               4000                    9000000                  4000                        9000000                      高        128               高            128                   Whitelist                 
VNODE_VNRS_VNFC_IPU_0064    161              0               4000                    600000                   4000                        600000                       高        128               高            128                   WhiteListV6               
VNODE_VNRS_VNFC_IPU_0064    171              0               1000                    100000                   1000                        100000                       低        128               低            128                   LDP_UDP                   
VNODE_VNRS_VNFC_IPU_0064    241              0               256                     30000                    256                         30000                        低        128               低            128                   Tcpsyn packets for LDP    
VNODE_VNRS_VNFC_IPU_0064    242              0               45                      10000                    45                          10000                        低        128               低            128                   IP Msg trace              
(结果个数 = 68)
---    END
```

#### 输出结果说明

| 输出项名称     | 输出项解释               |
|:----------|:--------------------|
| RU名称      | 该参数表示资源单元。          |
| 安全CAR系统ID | 该参数表示安全CAR系统ID。     |
| 安全策略编号    | 该参数表示安全策略号。         |
| 承诺信息速率    | 该参数表示承诺信息速率。        |
| 承诺突发尺寸    | 该参数表示承诺突发尺寸。        |
| 缺省承诺信息速率  | 该参数表示默认承诺信息速率。      |
| 缺省承诺突发尺寸  | 该参数表示默认承诺突尺寸。       |
| 优先级       | 该参数表示优先级，可指定为高/中/低。 |
| 最小包补偿长度   | 该参数表示最小包补偿长度。       |
| 缺省优先级     | 该参数表示默认优先级。         |
| 缺省最小包补偿长度 | 该参数表示默认最小包长。        |
| 安全策略描述    | 该参数表示描述信息。          |