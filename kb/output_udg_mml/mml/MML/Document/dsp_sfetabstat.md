# 显示SFE表项简要信息（DSP SFETABSTAT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示指定资源单元上SFE表项的简要信息。

简要信息包括表的记录数量以及容量。

#### 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                            |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------|
| RUNAME | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于指定资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。区分大小写。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |

#### 使用实例

显示指定资源单元的SFE表的简要信息：

```
DSP SFETABSTAT:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
信息描述   
   
AIB Table Template Type: Small template
AIB Table ID: 2
AIB Table Capacity: 786432
AIB Table Count: 0
                                   
ARP Table Template Type: Small template
ARP Table ID: 36
ARP Table Capacity: 131072
ARP Table Count: 1
                                  
ARP-REPLY Table Template Type: Small template
ARP-REPLY Table ID: 37
ARP-REPLY Table Capacity: 2048
ARP-REPLY Table Count: 2
                  
AT Table Template Type: Small template
AT Table ID: 18
AT Table Capacity: 65536
AT Table Count: 0
                                      
BA Table Template Type: Small template
BA Table ID: 8
BA Table Capacity: 2048
BA Table Count: 160
                                      
BFD-ERECV Table Template Type: Small template
BFD-ERECV Table ID: 32
BFD-ERECV Table Capacity: 1024
BFD-ERECV Table Count: 1
                  
BFD-IRECV Table Template Type: Small template
BFD-IRECV Table ID: 39
BFD-IRECV Table Capacity: 1024
BFD-IRECV Table Count: 2
                  
BFD-ISEND Table Template Type: Small template
BFD-ISEND Table ID: 33
BFD-ISEND Table Capacity: 1024
BFD-ISEND Table Count: 2
                 
BFD-PKT Table Template Type: Small template
BFD-PKT Table ID: 11
BFD-PKT Table Capacity: 1024
BFD-PKT Table Count: 2
                       
CTRLVID Table Template Type: Small template
CTRLVID Table ID: 16
CTRLVID Table Capacity: 65536
CTRLVID Table Count: 0
                      
DHCP Table Template Type: Small template
DHCP BIND Table ID: 46
DHCP BIND Table Capacity: 4096
DHCP BIND Table Count: 0
                  
ECIB Table Template Type: Small template
ECIB Table ID: 6
ECIB Table Capacity: 262144
ECIB Table Count: 1
                                
EPAT Table Template Type: Small template
EPAT Table ID: 5
EPAT Table Capacity: 64
EPAT Table Count: 2
                                  
FIB4 Table Template Type: Small template
FIB4 Table ID: 57
FIB4 Table Capacity: 122880
FIB4 Table Count: 21
                             
ICIB Table Template Type: Small template
ICIB Table ID: 4
ICIB Table Capacity: 262144
ICIB Table Count: 1
                               
IPAT Table Template Type: Small template
IPAT Table ID: 3
IPAT Table Capacity: 64
IPAT Table Count: 2
                                   
IPSEC-TUNNEL Table Template Type: Small template
IPSEC-TUNNEL Table ID: 56
IPSEC-TUNNEL Table Capacity: 10240
IPSEC-TUNNEL Table Count: 0
        
IQVCT Table Template Type: Small template
IQVCT Table ID: 42
IQVCT Table Capacity: 8192
IQVCT Table Count: 0
                              
NHP Table Template Type: Small template
NHP Table ID: 1
NHP Table Capacity: 262144
NHP Table Count: 0
                                  
NST Table Template Type: Small template
NST Table ID: 9
NST Table Capacity: 262144
NST Table Count: 13
                                  
NST6 Table Template Type: Small template
NST6 Table ID: 26
NST6 Table Capacity: 262144
NST6 Table Count: 0
                              
PHB Table Template Type: Small template
PHB Table ID: 7
PHB Table Capacity: 1024
PHB Table Count: 144
                                   
PORT Table Template Type: Small template
PORT Table ID: 14
PORT Table Capacity: 16
PORT Table Count: 0
                                   
RE Table Template Type: Small template
RE Table ID: 0
RE Table Capacity: 122880
RE Table Count: 21
                                   
TUNNEL Table Template Type: Small template
TUNNEL Table ID: 12
TUNNEL Table Capacity: 4096
TUNNEL Table Count: 0
                          
VPN Table Template Type: Small template
VPN Table ID: 10
VPN Table Capacity: 4096
VPN Table Count: 5
                                  
ND Table Template Type: Small template
ND Table ID: 24
ND Table Capacity: 65536
ND Table Count: 0
                                     
RE6 Table Template Type: Small template
RE6 Table ID: 25
RE6 Table Capacity: 122880
RE6 Table Count: 0
                                 
MPLSARP Table Template Type: Small template
MPLSARP Table ID: 28
MPLSARP Table Capacity: 65536
MPLSARP Table Count: 1
                      
NHLFE Table Template Type: Small template
NHLFE Table ID: 27
NHLFE Table Capacity: 331776
NHLFE Table Count: 0
                           
NHP6 Table Template Type: Small template
NHP6 Table ID: 29
NHP6 Table Capacity: 262144
NHP6 Table Count: 0
                              
NDH Table Template Type: Small template
NDH Table ID: 55
NDH Table Capacity: 131072
NDH Table Count: 0
                                 
FIB6 Table Template Type: Small template
FIB6 Table ID: 58
FIB6 Table Capacity: 122880
FIB6 Table Count: 0
                               
VLANIF Table Template Type: Small template
VLANIF BD Table ID: 20
VLANIF BD Table Capacity: 32768
VLANIF BD Table Count: 0
                 
BE Table Template Type: Small template
BE Table ID: 38
BE Table Capacity: 65536
BE Table Count: 0
                                      
FEI-BFD-ERECV Table Template Type: Small template
FEI-BFD-ERECV Table ID: 13
FEI-BFD-ERECV Table Capacity: 1024
FEI-BFD-ERECV Table Count: 1
      
FEI-SEC-CAR Table Template Type: Small template
FEI-SEC-CAR Table ID: 15
FEI-SEC-CAR Table Capacity: 512
FEI-SEC-CAR Table Count: 1
            
FEI-SEC-SWITCH Table Template Type: Small template
FEI-SEC-SWITCH Table ID: 17
FEI-SEC-SWITCH Table Capacity: 5
FEI-SEC-SWITCH Table Count: 1
      
BFD-ERECV-HASH Table Template Type: Small template
BFD-ERECV-HASH Table ID: 40
BFD-ERECV-HASH Table Capacity: 1024
BFD-ERECV-HASH Table Count: 1
   
GREIDX Table Template Type: Small template
GREIDX Table ID: 41
GREIDX Table Capacity: 4096
GREIDX Table Count: 0
                          
ARPSFG Table Template Type: Small template
ARPSFG Table ID: 54
ARPSFG Table Capacity: 4096
ARPSFG Table Count: 0
                           
MEB Table Template Type: Small template
MEB Table ID: 43
MEB Table Capacity: 2048
MEB Table Count: 0
                                    
MFIB Table Template Type: Small template
MFIB Table ID: 44
MFIB Table Capacity: 1
MFIB Table Count: 0
                                    
ND-FAST-REPLY Table Template Type: Small template
ND-FAST-REPLY Table ID: 65
ND-FAST-REPLY Table Capacity: 1024
ND-FAST-REPLY Table Count: 0

DLP Table Template Type: Small template
DLP Table ID: 53
DLP Table Capacity: 2048
DLP Table Count: 0
                                    
GPHB Table Template Type: Small template
GPHB Table ID: 30
GPHB Table Capacity: 64
GPHB Table Count: 0
                                   
Fabric-Tunnel Table Template Type: Small template
Fabric-Tunnel Table ID: 31
Fabric-Tunnel Table Capacity: 1024
Fabric-Tunnel Table Count: 0
      
Trunk Table Template Type: Small template
Trunk Table ID: 34
Trunk Table Capacity: 1024
Trunk Table Count: 0 
               
(结果个数 = 48)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 信息描述    | 查询到的简要信息描述。 |