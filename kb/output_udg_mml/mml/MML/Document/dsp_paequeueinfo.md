# 显示PAE队列信息（DSP PAEQUEUEINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示指定资源上队列的状态和统计信息，通过获取的信息，可了解通信是否正常，并进行故障诊断。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                    |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLTYPE     | 微服务类型  | 可选必选说明：必选参数 参数含义：该参数用于指定微服务类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务类型。    |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数 参数含义：该参数用于指定微服务实例号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务实例号。 |
| QUEUEID      | 队列ID   | 可选必选说明：可选参数 参数含义：队列ID。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～20。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无                                       |

#### 使用实例

- 显示微服务类型为“aa”微服务实例为“aa”中队列的状态和统计信息：

  ```
  DSP PAEQUEUEINFO:CELLTYPE="aa", CELLINSTANCE="aa";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  队列ID        队列名称                队列状态    算法ID    队列共享属性     用户输入参数    队列单元总个数    队列单元当前使用个数    队列单元空闲个数    读取队列成功的个数    读取队列失败的个数    写入队列成功的个数    写入队列失败的个数
   
  0x80000000    loop_vchannel_send_0    normal      MPSC      share            0               1023              0                       1023                0                     0                     0                     0                  
  0x80000001    loop_vchannel_recv_0    normal      MPSC      share            0               1023              0                       1023                8                     0                     8                     0                  
  0x80000002    loop_vchannel_send_1    normal      MPSC      share            0               1023              0                       1023                0                     0                     0                     0                  
  0x80000003    loop_vchannel_recv_1    normal      MPSC      share            0               1023              0                       1023                8                     0                     8                     0                  
  0x80000004    loop_vchannel_send_2    normal      MPSC      share            0               1023              0                       1023                0                     0                     0                     0                  
  0x80000005    loop_vchannel_recv_2    normal      MPSC      share            0               1023              0                       1023                0                     0                     0                     0                  
  0x80000006    loop_vchannel_send_3    normal      MPSC      share            0               1023              0                       1023                0                     0                     0                     0                  
  0x80000007    loop_vchannel_recv_3    normal      MPSC      share            0               1023              0                       1023                0                     0                     0                     0                  
  0x80000008    dp_to_dp_pkt            normal      MPSC      share            0               2047              0                       2047                10965                 0                     10965                 0                  
  0x80000009    fei_to_dp_pkt           normal      MPSC      share            0               2047              0                       2047                109                   0                     109                   0                  
  0x8000000A    fei_to_dp_msg           normal      MPSC      share            0               2047              0                       2047                0                     0                     0                     0                  
  0x8000000B    extport_0_send_0        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x8000000C    extport_0_recv_0        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x8000000D    extport_0_send_1        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x8000000E    extport_0_recv_1        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x8000000F    extport_0_send_2        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000010    extport_0_recv_2        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000011    extport_0_send_3        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000012    extport_0_recv_3        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000013    fabport_1_send_0        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000014    fabport_1_recv_0        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000015    fabport_1_send_1        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000016    fabport_1_recv_1        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000017    fabport_1_send_2        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000018    fabport_1_recv_2        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x80000019    fabport_1_send_3        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x8000001A    fabport_1_recv_3        normal      MPSC      pbuffer share    0               4095              0                       4095                0                     0                     0                     0                  
  0x8000001B    MSG_1001_Alert_Queue    normal      MPSC      share            0               2047              0                       2047                0                     0                     0                     0                  
  (结果个数 = 28)
  ---    END
  ```
- 显示微服务类型为“aa”微服务实例为“aa”中指定队列的状态和统计信息：

  ```
  DSP PAEQUEUEINFO: CELLTYPE="aa", CELLINSTANCE="aa", QUEUEID="0x80000000";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
                队列ID  =  0x80000000
              队列名称  =  loop_vchannel_send_0
              队列状态  =  normal
                算法ID  =  MPSC
          队列共享属性  =  share
          用户输入参数  =  0
        队列单元总个数  =  1023
  队列单元当前使用个数  =  0
      队列单元空闲个数  =  1023
    读取队列成功的个数  =  0
    读取队列失败的个数  =  0
    写入队列成功的个数  =  0
    写入队列失败的个数  =  0
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称      | 输出项解释                                                                                      |
|:-----------|:-------------------------------------------------------------------------------------------|
| 队列ID       | 队列ID。                                                                                      |
| 队列名称       | 队列名称。                                                                                      |
| 队列状态       | 队列状态，显示队列是否被破坏： global damage:队列全局控制块破坏。queue damage:队列体控制块破坏。normal:队列正常。                 |
| 算法ID       | 根据算法ID，可以确定单生产者还是多生产者，单消费者还是多消费者： SPSC:单生产者单消费者。SPMC:单生产者多消费者。MPSC:多生产者单消费者。MPMC:多生产者多消费者。 |
| 队列共享属性     | 表示是否是共享队列。 private:非共享。share:共享。pbuffer share:pbuf共享队列。                                    |
| 用户输入参数     | 用户参数，创建队列时初始化，设置时传入。                                                                       |
| 队列单元总个数    | 创建队列时单元总个数。                                                                                |
| 队列单元当前使用个数 | 队列单元当前使用个数。                                                                                |
| 队列单元空闲个数   | 队列单元中空闲的单元个数。                                                                              |
| 读取队列成功的个数  | 读取队列成功的个数。                                                                                 |
| 读取队列失败的个数  | 读取队列失败的个数。                                                                                 |
| 写入队列成功的个数  | 写入队列成功的个数。                                                                                 |
| 写入队列失败的个数  | 写入队列失败的个数。                                                                                 |