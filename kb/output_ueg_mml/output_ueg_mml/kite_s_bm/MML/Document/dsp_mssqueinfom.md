# 显示队列总体信息（DSP MSSQUEINFOM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示MSS模块队列总体信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLTYPE     | 微服务类型  | 可选必选说明：必选参数 参数含义：该参数用于指定微服务类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看工作角色为数据转发对应的微服务类型。    |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数 参数含义：该参数用于指定微服务实例号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看工作角色为数据转发对应的微服务实例号。 |

#### 使用实例

显示微服务类型“aa”微服务类型实例 "bb"内队列总体信息：

```
DSP MSSQUEINFOM: CELLTYPE="aa", CELLINSTANCE="bb";
```

```
RETCODE = 0  操作成功。

结果如下
--------
队列编号      队列名称                队列属性         队列长度    队列深度    接管进程回收次数

0x0           ufpSchWorkQ0            private          4095        0           --            
0x1           DebugTimerCallback      private          4095        0           --            
0x2           ufpSchWorkQ1            private          4095        0           --            
0x3           ufpSchWorkQ2            private          4095        0           --            
0x4           ufpSchWorkQ3            private          4095        0           --            
0x5           ufpSchWorkQ4            private          4095        0           --            
0x80000000    loop_vchannel_send_0    pbuffer share    1023        0           0               
0x80000001    loop_vchannel_recv_0    pbuffer share    1023        0           0               
0x80000002    loop_vchannel_send_1    pbuffer share    1023        0           0               
0x80000003    loop_vchannel_recv_1    pbuffer share    1023        0           0               
0x80000004    loop_vchannel_send_2    pbuffer share    1023        0           0               
0x80000005    loop_vchannel_recv_2    pbuffer share    1023        0           0               
0x80000006    dp_to_dp_pkt            pbuffer share    2047        0           4               
0x80000007    fei_to_dp_pkt           pbuffer share    2047        0           4               
0x80000008    fei_to_dp_msg           pbuffer share    2047        0           0               
0x80000009    pae_pmtu_recv_Q         pbuffer share    4095        0           0               
0x8000000A    cp_car_que_0            pbuffer share    511         0           0               
0x8000000B    cp_car_que_1            pbuffer share    511         0           0               
0x8000000C    loop_vchannel_send_3    pbuffer share    1023        0           0               
0x8000000D    loop_vchannel_recv_3    pbuffer share    1023        0           0               
0x8000000E    sfe-pae-fab_send_0      pbuffer share    32767       0           1               
0x8000000F    sfe-pae-fab_recv_0      pbuffer share    32767       0           0               
0x80000010    sfe-pae-fab_send_1      pbuffer share    32767       0           1               
0x80000011    sfe-pae-fab_recv_1      pbuffer share    32767       0           0               
0x80000012    sfe-pae-fab_send_2      pbuffer share    32767       0           1               
0x80000013    sfe-pae-fab_recv_2      pbuffer share    32767       0           0               
0x80000014    sfe-pae-fab_send_3      pbuffer share    32767       0           1               
0x80000015    sfe-pae-fab_recv_3      pbuffer share    32767       0           0               
0x80000016    sfe-pae-ext_send_0      pbuffer share    32767       0           1               
0x80000017    sfe-pae-ext_recv_0      pbuffer share    32767       0           0               
0x80000018    sfe-pae-ext_send_1      pbuffer share    32767       0           1               
0x80000019    sfe-pae-ext_recv_1      pbuffer share    32767       0           0               
0x8000001A    sfe-pae-ext_send_2      pbuffer share    32767       0           1               
0x8000001B    sfe-pae-ext_recv_2      pbuffer share    32767       0           0               
0x8000001C    sfe-pae-ext_send_3      pbuffer share    32767       0           1               
0x8000001D    sfe-pae-ext_recv_3      pbuffer share    32767       0           0               
0x8000001E    sfe-pae-tnl_send_0      pbuffer share    32767       0           0               
0x8000001F    sfe-pae-tnl_recv_0      pbuffer share    32767       0           0               
0x80000020    sfe-pae-tnl_send_1      pbuffer share    32767       0           0               
0x80000021    sfe-pae-tnl_recv_1      pbuffer share    32767       0           0               
0x80000022    sfe-pae-tnl_send_2      pbuffer share    32767       0           0               
0x80000023    sfe-pae-tnl_recv_2      pbuffer share    32767       0           0               
0x80000024    sfe-pae-tnl_send_3      pbuffer share    32767       0           0               
0x80000025    sfe-pae-tnl_recv_3      pbuffer share    32767       0           0               
0x80000026    MSG_1001_Alert_Queue    pbuffer share    2047        0           4               
(结果个数 = 45)
---    END
```

#### 输出结果说明

| 输出项名称    | 输出项解释                                      |
|:---------|:-------------------------------------------|
| 队列编号     | 用于表示队列编号。                                  |
| 队列名称     | 用于表示队列名称。                                  |
| 队列属性     | 用于表示队列属性。                                  |
| 队列长度     | 用于表示队列长度。                                  |
| 队列深度     | 用于表示队列深度（免锁算法可能会导致查询到的队列深度出现翻转，重新再查询一次即可）。 |
| 接管进程回收次数 | 用于表示接管进程回收次数。                              |