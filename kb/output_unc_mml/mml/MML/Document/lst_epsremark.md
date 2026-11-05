# 查询EPS QoS到TOS/DSCP的映射规则（LST EPSREMARK）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令用来显示UNC上在SAE架构下配置的QoS参数到IP报头中DSCP（区别服务编码点）/TOS（服务类型）的映射规则。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称          | 参数说明                                                                                                                                                                                    |
|:---------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：可选参数  参数含义：该参数指定QoS Profile的名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：  QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功，可以通过LST QOSPROFILE或LST QOSGLOBAL命令查询。 |

## 使用实例

指定QoS Profile名，显示EpsRemark配置信息：

```
%%LST EPSREMARK: QOSPROFILENAME="globalqos";%%
RETCODE = 0  操作成功

结果如下
--------
       QoS Profile名  =  globalqos
              AF级别  =  0
        AF丢弃优先级  =  0
                DSCP  =  对应的DSCP的值为101110
            标记类型  =  映射到Dscp
               TOS值  =  0
       ARP的优先级别  =  15
                 QCI  =  1
              DSCP值  =  0
   S1-U DSCP配置开关  =  使能
           S1-U DSCP  =  映射的DSCP值
         S1-U AF级别  =  0
   S1-U AF丢弃优先级  =  0
         S1-U DSCP值  =  22
 SGW S5 DSCP配置开关  =  使能
         SGW S5 DSCP  =  映射的DSCP值
       SGW S5 AF级别  =  0
 SGW S5 AF丢弃优先级  =  0
       SGW S5 DSCP值  =  23
 PGW S5 DSCP配置开关  =  使能
         PGW S5 DSCP  =  映射的DSCP值
       PGW S5 AF级别  =  0
 PGW S5 AF丢弃优先级  =  0
       PGW S5 DSCP值  =  24
 SGW S8 DSCP配置开关  =  使能
         SGW S8 DSCP  =  映射的DSCP值
       SGW S8 AF级别  =  0
 SGW S8 AF丢弃优先级  =  0
       SGW S8 DSCP值  =  25
 PGW S8 DSCP配置开关  =  使能
         PGW S8 DSCP  =  映射的DSCP值
       PGW S8 AF级别  =  0
 PGW S8 AF丢弃优先级  =  0
       PGW S8 DSCP值  =  26
PGW SGi DSCP配置开关  =  使能
        PGW SGi DSCP  =  映射的DSCP值
      PGW SGi AF级别  =  0
PGW SGi AF丢弃优先级  =  0
      PGW SGi DSCP值  =  27
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称            | 输出项解释                                              |
|:-----------------|:---------------------------------------------------|
| QoS Profile名称    | 该参数指定QoS Profile的名称。                               |
| AF级别             | 该参数用于表示AF队列序号。                                     |
| AF丢弃优先级          | 该参数表示AF丢弃优先级。                                      |
| DSCP             | 该参数用于表示DSCP。                                       |
| 标记类型             | 该参数用于表示映射到DSCP或者TOS。                               |
| TOS值             | 该参数表示映射到TOS的值，分别对应IP优先级的8个队列ID，优先值高的报文先于优先值低的报文发送。 |
| ARP的优先级别         | 该参数表示ARP的优先级别。                                     |
| QCI              | 该参数表示QoS流量级别。                                      |
| DSCP值            | 该参数用于表示映射的DSCP值。                                   |
| S1-U DSCP配置开关    | 该参数用于表示S1-U接口DSCP配置开关。                             |
| S1-U DSCP        | 该参数用于表示S1U DSCP。                                   |
| S1-U AF级别        | 该参数用于表示S1U接口AF队列序号。                                |
| S1-U AF丢弃优先级     | 该参数表示S1U接口AF丢弃优先级。                                 |
| S1-U DSCP值       | 该参数用于表示映射的S1U接口DSCP值。                              |
| SGW S5 DSCP配置开关  | 该参数用于表示SGW S5接口DSCP配置开关。                           |
| SGW S5 DSCP      | 该参数用于表示SGW S5 DSCP。                                |
| SGW S5 AF级别      | 该参数用于表示SGW S5接口AF队列序号。                             |
| SGW S5 AF丢弃优先级   | 该参数表示SGW S5接口AF丢弃优先级。                              |
| SGW S5 DSCP值     | 该参数用于表示映射的SGW S5接口DSCP值。                           |
| PGW S5 DSCP配置开关  | 该参数用于表示PGW S5接口DSCP配置开关。                           |
| PGW S5 DSCP      | 该参数用于表示PGW S5 DSCP。                                |
| PGW S5 AF级别      | 该参数用于表示PGW S5接口AF队列序号。                             |
| PGW S5 AF丢弃优先级   | 该参数表示PGW S5接口AF丢弃优先级。                              |
| PGW S5 DSCP值     | 该参数用于表示映射的PGW S5接口DSCP值。                           |
| SGW S8 DSCP配置开关  | 该参数用于表示SGW S8接口DSCP配置开关。                           |
| SGW S8 DSCP      | 该参数用于表示SGW S8 DSCP。                                |
| SGW S8 AF级别      | 该参数用于表示SGW S8接口AF队列序号。                             |
| SGW S8 AF丢弃优先级   | 该参数表示SGW S8接口AF丢弃优先级。                              |
| SGW S8 DSCP值     | 该参数用于表示映射的SGW S8接口DSCP值。                           |
| PGW S8 DSCP配置开关  | 该参数用于表示PGW S8接口DSCP配置开关。                           |
| PGW S8 DSCP      | 该参数用于表示PGW S8 DSCP。                                |
| PGW S8 AF级别      | 该参数用于表示PGW S8接口AF队列序号。                             |
| PGW S8 AF丢弃优先级   | 该参数表示PGW S8接口AF丢弃优先级。                              |
| PGW S8 DSCP值     | 该参数用于表示映射的PGW S8接口DSCP值。                           |
| PGW SGi DSCP配置开关 | 该参数用于表示PGW SGi接口DSCP配置开关。                          |
| PGW SGi DSCP     | 该参数用于表示PGW SGi DSCP。                               |
| PGW SGi AF级别     | 该参数用于表示PGW SGi接口AF队列序号。                            |
| PGW SGi AF丢弃优先级  | 该参数表示PGW SGi接口AF丢弃优先级。                             |
| PGW SGi DSCP值    | 该参数用于表示映射的PGW SGi接口DSCP值。                          |