# 查询5GC QoS到TOS/DSCP的映射规则（LST 5GCREMARK）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用来查询5G用户配置的QoS参数到IP报头中DSCP（区别服务编码点）/TOS（服务类型）的映射规则。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称          | 参数说明                                                                                                                                        |
|:---------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：可选参数  参数含义：该参数指定QoS Profile的名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：  该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |

## 使用实例

- 查询给定QoS Profile名称对应的5GC Remark配置：

  ```
  %%LST 5GCREMARK: QOSPROFILENAME="profile";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
    QoS Profile名  =  profile
              5QI  =  5
    ARP的优先级别  =  5
         标记类型  =  映射到Dscp
             DSCP  =  对应的DSCP的值为000000
           AF级别  =  0
     AF丢弃优先级  =  0
            TOS值  =  0
           DSCP值  =  0
  N3 DSCP配置开关  =  disable
          N3 DSCP  =  对应的DSCP的值为101110
        N3 AF级别  =  0
  N3 AF丢弃优先级  =  0
        N3 DSCP值  =  0
  N9 DSCP配置开关  =  disable
          N9 DSCP  =  对应的DSCP的值为101110
        N9 AF级别  =  0
  N9 AF丢弃优先级  =  0
        N9 DSCP值  =  0
  N6 DSCP配置开关  =  disable
          N6 DSCP  =  对应的DSCP的值为101110
        N6 AF级别  =  0
  N6 AF丢弃优先级  =  0
        N6 DSCP值  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询所有5GC Remark配置：

  ```
  %%LST 5GCREMARK:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  QoS Profile名  5QI  ARP的优先级别  标记类型    DSCP                    AF级别  AF丢弃优先级  TOS值  DSCP值  N3 DSCP配置开关  N3 DSCP                 N3 AF级别  N3 AF丢弃优先级  N3 DSCP值  N9 DSCP配置开关  N9 DSCP                 N9 AF级别  N9 AF丢弃优先级  N9 DSCP值  N6 DSCP配置开关  N6 DSCP                 N6 AF级别  N6 AF丢弃优先级  N6 DSCP值  

  globalqos      6    6              映射到Dscp  对应的DSCP的值为101110  0       0             0      0       disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          
  profile        5    5              映射到Dscp  对应的DSCP的值为000000  0       0             0      0       disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          
  (结果个数 = 2)

  ---    END
  ```

## 输出结果说明

| 输出项名称         | 输出项解释                                              |
|:--------------|:---------------------------------------------------|
| QoS Profile名称 | 该参数指定QoS Profile的名称。                               |
| 5QI           | 该参数表示5G QoS Identifier。                            |
| ARP的优先级别      | 该参数表示ARP的优先级别。                                     |
| 标记类型          | 该参数用于表示映射到DSCP或者TOS。                               |
| DSCP          | 该参数用于表示DSCP。                                       |
| AF级别          | 该参数用于表示AF队列序号。                                     |
| AF丢弃优先级       | 该参数表示AF丢弃优先级。                                      |
| TOS值          | 该参数表示映射到TOS的值，分别对应IP优先级的8个队列ID，优先值高的报文先于优先值低的报文发送。 |
| DSCP值         | 该参数用于表示映射的DSCP值。                                   |
| N3 DSCP配置开关   | 该参数用于表示N3接口DSCP配置开关。                               |
| N3 DSCP       | 该参数用于表示N3 DSCP。                                    |
| N3 AF级别       | 该参数用于表示N3接口AF队列序号。                                 |
| N3 AF丢弃优先级    | 该参数表示N3接口AF丢弃优先级。                                  |
| N3 DSCP值      | 该参数用于表示映射的N3接口DSCP值。                               |
| N9 DSCP配置开关   | 该参数用于表示N9接口DSCP配置开关。                               |
| N9 DSCP       | 该参数用于表示N9 DSCP。                                    |
| N9 AF级别       | N9 AF级别。                                           |
| N9 AF丢弃优先级    | N9 AF丢弃优先级。                                        |
| N9 DSCP值      | 该参数用于表示映射的N9接口DSCP值。                               |
| N6 DSCP配置开关   | 该参数用于表示N6接口DSCP配置开关。                               |
| N6 DSCP       | 该参数用于表示N6 DSCP。                                    |
| N6 AF级别       | N6 AF级别。                                           |
| N6 AF丢弃优先级    | N6 AF丢弃优先级。                                        |
| N6 DSCP值      | 该参数用于表示映射的N6接口DSCP值。                               |