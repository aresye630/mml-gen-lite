# 显示资源池列表的资源占用情况（DSP FEI\_FRM\_CST\_POOL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示资源池列表的资源占用情况。

#### 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                     |
|:------------|:-------|:-------------------------------------------------------------------------------------------------------------------------|
| RUNAME      | RU名称   | 可选必选说明：可选参数 参数含义：该参数用于指定资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则： 区分大小写，不支持空格。RU名称为空时查询OMU记录。使用DSP RU查看RU名称。 |
| COMMANDFLAG | 命令行标志  | 可选必选说明：必选参数 参数含义：该参数用于表示命令行标志。 数据来源：本端规划 取值范围：枚举类型。 DSP_FRM_POOL：查询转发资源池。DSP_CST_POOL：查询存储资源池。 默认值：无                     |
| ID          | 编号     | 可选必选说明：可选参数 参数含义：该参数用于表示编号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967294。 默认值：无 配置原则：要求输入ID必须存在资源池。                             |

#### 使用实例

- 查看资源池列表的资源占用信息：

  ```
  DSP FEI_FRM_CST_POOL:RUNAME="VNODE_VNRS_VNFC_IPU_0064",COMMANDFLAG=DSP_FRM_POOL;
  ```

  ```
  RETCODE = 0  操作成功。

  转发池信息如下
  --------------
  资源池ID 转发资源名称          共享资源池名称        资源分配方式 开始地址      结束地址    转发资源最小值    转发资源最大值    资源总数    已分配资源数    剩余资源数                                                                                                                                                                                                   

  0        PHYGID                PHYGID                0            1             524287      0                 524287            524287      0               524287   
  1        RULE_INSTAT           RULE_INSTAT           0            1             200192      0                 24576             200192      0               24576    
  2        RULE_OUTSTAT          RULE_OUTSTAT          0            1             200192      0                 24576             200192      0               24576    
  3        QINQ_STAT_IN          QINQ_STAT_IN          0            0             65534       0                 65535             65535       0               65535    
  4        QINQ_STAT_OUT         QINQ_STAT_OUT         0            0             65534       0                 65535             65535       0               65535    
  5        FIM_IQVCTEXT          FIM_IQVCTEXT          0            0             65535       0                 65536             65536       0               65536    
  6        FIM_QINQ_ECID         FIM_QINQ_ECID         0            0             65535       0                 65536             65536       0               65536    
  7        RE_CGN                FE_RE4                0            0             122879      0                 64                122880      0               64       
  13       NST_CGN               NST_IID               0            0             65535       0                 64                65536       0               64       
  14       VXLAN_VNI_STAT_IN     VXLAN_VNI_STAT_IN     0            0             32767       0                 32768             32768       0               32768    
  15       VXLAN_VNI_STAT_OUT    VXLAN_VNI_STAT_OUT    0            0             32767       0                 32768             32768       0               32768    
  16       BD_TMGID_RES          BD_TMGID_RES          0            1             32768       0                 32768             32768       0               32768    
  17       MACLMT_RES            MACLMT_RES            0            1             32768       0                 32768             32768       0               32768    
  18       ELB_MLID_RES          ELB_MLID_RES          0            1             131072      0                 131072            131072      0               131072   
  19       FE_RE4                FE_RE4                0            0             122879      0                 122880            122880      8               122872   
  20       NHP_IID               NHP_IID               1            0             262143      0                 262144            262144      0               262144   
  21       NHP_XC                NHP_IID               1            0             262143      0                 262144            262144      0               262144   
  22       NHP_IIDG              NHP_IID               1            0             262143      0                 262144            262144      0               262144   
  23       NHP_IIDGFRR           NHP_IID               1            0             262143      0                 262144            262144      0               262144   
  24       NHP_IIDGIID           NHP_IID               1            0             262143      0                 262144            262144      0               262144   
  31       NST_IID               NST_IID               0            0             65535       0                 65536             65536       5               65531    
  33       NST_IIDG              NST_IID               0            0             65535       0                 65536             65536       0               65531    
  34       NST_IIDGFRR           NST_IID               0            0             65535       0                 65536             65536       0               65531    
  35       NST_IIDGIID           NST_IID               0            0             65535       0                 65536             65536       0               65531    
  36       NST_XC                NST_IID               0            0             65535       0                 65536             65536       0               65531    
  42       MPLSARP               MPLSARP               0            0             65535       0                 65536             65536       0               65536    
  44       44                    NST_IID               0            0             65535       0                 65536             65536       0               65531    
  (Number of results = 27)
  ---    END
  ```
- 查看存储资源池列表的资源占用信息：

  ```
  DSP FEI_FRM_CST_POOL:RUNAME="VNODE_VNRS_VNFC_IPU_0064",COMMANDFLAG=DSP_CST_POOL;
  ```

  ```
  RETCODE = 0  操作成功。

  存储池信息如下
  --------------
  存储池ID 存储池名称                   算法类型     资源池可以存储的总数 当前存储的资源数    老化池是否存在  老化池计数    当前遍历该资源池的遍历句柄数    RU名称   

  0        ACTION                       1            0                    1                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  1        POLICYNODEPRI                4            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  2        NONSUPPORT_BEHAVIOR_LOGGED   2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  3        PHYGID                       1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  4        PHYGID_REF                   1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  5        PHYGID_IN                    2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  6        PHYGID_OUT                   2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  7        POLICYNODE                   2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  8        ACLRULE                      2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  9        RULE_INSTATATTR              1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  10       RULE_OUTSTATATTR             1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  11       RULE_INSTAT                  1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  12       RULE_OUTSTAT                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  13       RULE_IN                      1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  14       RULE_OUT                     1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  15       CAR_IN                       1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  16       CAR_OUT                      1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  17       QoS                          1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  18       RULE_INSTAT_KEY_REF          1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  19       RULE_OUTSTAT_KEY_REF         1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  20       ACTIONID                     2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  21       ACTION_REDIRECT              1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  22       QINQ_IN                      1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  23       QINQ_OUT                     1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  24       INSUBIF_STAT_RESOURCE        1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  25       OUTSUBIF_STAT_RESOURCE       1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  26       QINQ                         2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  27       FIM_IFSTAT_INFO              1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  28       SUBIF_BD_STAT_MEMBER         2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  29       FIM_IQVCTEXT                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  30       FIM_QINQ_ECID                1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  31       POLICY_STAT_LASTRST          1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  32       TBTP_REF_RDRMHPI             2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  33       REDIRECT_RES                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  34       CGN_INSTANCE                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  36       CGN_NST                      1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  37       CGN_RE                       1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  38       CGN_INSTANCEARRAY            1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  39       CGN_INSTINFO                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  40       CGN_EXCLUDE_PORT             1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  41       CGN_EXCLUDE_PORT_CONFLICT    1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  46       CGNACL_NATOUTIF              1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  47       VSMHA_GLOBAL                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  48       VSMHA_SGBIND                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  50       CGN_VRID_MAP                 0            16                   0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  51       ID_CFG_ASYNMSG               1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  52       VXLAN_STAT                   1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  53       VXLAN_VNI_STAT_IN_RES        1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  54       VXLAN_VNI_STAT_OUT_RES       1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  57       BD_TMGID_RES                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  58       MACLMT_RES                   1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  59       BD_LEAF_RES                  1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  60       FID_INSTANCE_INFO            1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  61       L2_INSTANCE_INFO             1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  62       L2_PORT_STATE                1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  63       LICENSE_ASSIGN               1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  65       SPEC_CFGINFO                 1            0                    545                 0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  66       CLASSIFIER_MATCHTYPE         1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  67       CLASSIFIER_ACLRULE           2            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  68       IPSEC_RESOURCE               1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  69       ACL_DOWN_LOAD                1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  70       IPSEC_ACL_NODE               1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  71       STORE_FOR_TS                 1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  72       L2MAC_QUERY                  1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  73       VXLAN_TUNNEL_INFO            1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  74       CGNACL_PRIORITY              1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  75       CGNACL_TOTALCOUNT            1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  76       PROFILE_INCAR                1            0                    0                   0               0             0                               VNODE_VNRS_VNFC_IPU_0064
  To be continued..
  ---    END

  DSP FEI_FRM_CST_POOL:RUNAME="VNODE_VNRS_VNFC_IPU_0064",COMMANDFLAG=DSP_CST_POOL;
  RETCODE = 0  操作成功。

  存储池信息如下
  --------------
  存储池ID 存储池名称                   算法类型     资源池可以存储的总数 当前存储的资源数    老化池是否存在  老化池计数     当前遍历该资源池的遍历句柄数   RU名称   

  77       PROFILE_OUTCAR               1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  78       RE4                          1            0                    8                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  79       NHP                          1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  80       RE6                          1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  81       BFD_PROXY                    1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  82       BFD_GP                       1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  83       GRE                          1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  84       GLOBAL_RESPORT               1            0                    4                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  85       FE_RE4_REFCOUNT              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  86       FE_RE4                       6            0                    8                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  87       NHP_IID4                     1            0                    5                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  88       NHP_IIDG4                    1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  89       NHP_IIDGFRR4                 1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  90       NHP_IIDGIID4                 1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  91       NHP_XC                       1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  92       NHP_FE_IID4                  1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  93       NHP_FE_IIDG4                 1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  94       NHP_FE_IIDGFRR4              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  95       NHP_FE_IIDGIID4              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  96       NHP_FE_XC                    1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  102      FIB4_NHPINDEX2IID            1            0                    5                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  103      NST_FE_IID4                  1            0                    5                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  105      NST_FE_IIDG4                 1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  106      NST_FE_IIDGFRR4              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  107      NST_FE_IIDGIID4              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  108      NST_FE_XC                    1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  111      IID_TO_RE_INDEX              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  112      MPLS_ARPMISS_INDEX_TO_KEY    1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  113      MPLS_ARP_DATA                1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  114      MPLS_ARP_DATA_USER           1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  115      MPLS_NHLFE_LIST              1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  116      MPLS_ARP_FAKE_DATA           2            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  118      DYE_RDRCFG                   0            32                   0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  119      VPNLABEL                     1            0                    2                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  120      120                          1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  121      121                          1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  122      FLOWMODE_IF                  1            0                    0                   0               0              0                              VNODE_VNRS_VNFC_IPU_0064
  (Number of results = 105)
  2 reports in total
  ---    END
  ```

#### 输出结果说明

| 输出项名称             | 输出项解释                  |
|:------------------|:-----------------------|
| 转发资源池ID           | 该参数为转发资源池ID。           |
| 转发资源池名称           | 该参数为资源池名称。             |
| 共享资源池名称           | 该参数为共享资源池名称。           |
| 资源分配方式            | 该参数为资源分配方式。            |
| 开始地址              | 该参数为开始地址。              |
| 结束地址              | 该参数为结束地址。              |
| 转发资源最小值           | 该参数为转发资源最小值。           |
| 转发资源池ID           | 该参数为转发资源池ID。           |
| 转发资源池名称           | 该参数为资源池名称。             |
| 共享资源池名称           | 该参数为共享资源池名称。           |
| 资源分配方式            | 该参数为资源分配方式。            |
| 开始地址              | 该参数为开始地址。              |
| 结束地址              | 该参数为结束地址。              |
| 转发资源最小值           | 该参数为转发资源最小值。           |
| 转发资源最大值           | 该参数为转发资源最大值。           |
| 资源总数              | 该参数为资源总数。              |
| 已分配资源总数           | 该参数为已分配资源总数。           |
| 剩余资源数             | 该参数为剩余资源数。             |
| 存储池ID             | 该参数为存储池ID。             |
| 存储池名称             | 该参数为存储池名称。             |
| 算法类型              | 该参数为算法类型。              |
| 资源池可以存储的总数        | 该参数为资源池可以存储的总数。        |
| 当前存储的资源数          | 该参数为当前存储的资源数。          |
| 老化池是否存在           | 该参数为老化池是否存在。           |
| 老化池计数             | 该参数为老化池计数。             |
| 当前有多少个遍历句柄在遍历该资源池 | 该参数为当前有多少个遍历句柄在遍历该资源池。 |
| RU名称              | 该参数为资源单元名称。            |