# 显示指定VM上转发使用的所有或指定队列的详细信息（DSP SFE\_QUEUE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示指定资源单元上的所有或指定队列的详细信息。

#### 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                 |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------|
| QID    | 队列ID   | 可选必选说明：可选参数 参数含义：指定队列ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                |
| RUNAME | RU名称   | 可选必选说明：必选参数 参数含义：指定资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |

#### 使用实例

查看指定资源单元中所有队列的详细信息：

```
DSP SFE_QUEUE:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```
RETCODE = 0  操作成功。

结果如下
--------
队列ID        队列状态    队列算法    队列共享属性    用户输入参数    队列单元总个数    单元当前使用个数    单元空闲个数    读取队列成功个数    读取队列失败个数    写入队列成功个数    写入队列失败个数    队列名称                 是否过载         RU名称                  
                                                                                                                                                                                                                                
2147483653    normal      MPSC        pbuffer share   0               32767             0                   32767           93                  0                   93                  0                   sfe-pae-fab_send_11_0    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483654    normal      MPSC        pbuffer share   0               32767             0                   32767           4391                0                   4391                0                   sfe-pae-fab_recv_11_0    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483655    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-fab_send_11_1    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483656    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-fab_recv_11_1    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483657    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-fab_send_11_2    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483658    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-fab_recv_11_2    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483659    normal      MPSC        pbuffer share   0               32767             0                   32767           12026               0                   12026               0                   sfe-pae-fab_send_11_3    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483660    normal      MPSC        pbuffer share   0               32767             0                   32767           7731                0                   7731                0                   sfe-pae-fab_recv_11_3    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483661    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_send_11_0     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483662    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_recv_11_0     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483663    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_send_11_1     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483664    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_recv_11_1     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483665    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_send_11_2     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483666    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_recv_11_2     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483667    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_send_11_3     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483668    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext0_recv_11_3     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483669    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_send_11_0    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483670    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_recv_11_0    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483671    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_send_11_1    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483672    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_recv_11_1    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483673    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_send_11_2    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483674    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_recv_11_2    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483675    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_send_11_3    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483676    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfe-pae-tnl_recv_11_3    FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483677    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_send_11_0     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483678    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_recv_11_0     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483679    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_send_11_1     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483680    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_recv_11_1     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483681    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_send_11_2     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483682    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_recv_11_2     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483683    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_send_11_3     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483684    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext1_recv_11_3     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483685    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_send_11_0     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483686    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_recv_11_0     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483687    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_send_11_1     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483688    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_recv_11_1     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483689    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_send_11_2     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483690    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_recv_11_2     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483691    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_send_11_3     FALSE            VNODE_VNRS_VNFC_IPU_0064
2147483692    normal      MPSC        pbuffer share   0               32767             0                   32767           0                   0                   0                   0                   sfepaeext2_recv_11_3     FALSE            VNODE_VNRS_VNFC_IPU_0064
1             normal      MPSC        private         0               1023              0                   1023            0                   0                   0                   0                   SFE_FEI_QUEUE            FALSE            VNODE_VNRS_VNFC_IPU_0064
2             normal      MPSC        private         0               32767             0                   32767           0                   0                   0                   0                   SFE_MC_QUEUE             FALSE            VNODE_VNRS_VNFC_IPU_0064
3             normal      MPSC        private         0               1023              0                   1023            0                   0                   0                   0                   FEI_SFE_QUEUE            FALSE            VNODE_VNRS_VNFC_IPU_0064
12            normal      MPSC        private         0               1023              0                   1023            0                   0                   0                   0                   SFE_CP_CAR_QUEUE0        FALSE            VNODE_VNRS_VNFC_IPU_0064
13            normal      MPSC        private         0               1023              0                   1023            12119               0                   12119               0                   SFE_CP_CAR_QUEUE1        FALSE            VNODE_VNRS_VNFC_IPU_0064
14            normal      MPSC        private         0               1023              0                   1023            0                   0                   0                   0                   SFE_CP_CAR_QUEUE2        FALSE            VNODE_VNRS_VNFC_IPU_0064
15            normal      MPSC        private         0               1023              0                   1023            0                   0                   0                   0                   SFE_CP_CAR_QUEUE3        FALSE            VNODE_VNRS_VNFC_IPU_0064
(结果个数 = 47)                                                                                                                                                                                                                   
---    END
```

#### 输出结果说明

| 输出项名称    | 输出项解释                   |
|:---------|:------------------------|
| 队列ID     | 指定队列ID。                 |
| 队列状态     | 队列状态。                   |
| 队列算法     | 队列算法。                   |
| 队列共享属性   | 队列共享属性。                 |
| 用户输入参数   | 用户输入参数。                 |
| 队列单元总个数  | 队列单元总个数。                |
| 单元当前使用个数 | 单元当前使用个数。               |
| 单元空闲个数   | 单元空闲个数。                 |
| 读取队列成功个数 | 读取队列成功个数。               |
| 读取队列失败个数 | 读取队列失败个数。               |
| 写入队列成功个数 | 写入队列成功个数。               |
| 写入队列失败个数 | 写入队列失败个数。               |
| 队列名称     | 队列名称。                   |
| 是否过载     | 队列是否过载： TRUE：是。FALSE：否。 |
| RU名称     | 指定资源单元名称。               |