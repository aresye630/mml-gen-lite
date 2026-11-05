# 显示PAE内联口亚健康统计信息（DSP FABRICSUBHEALTHYSTAT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示Fabric平面亚健康30个周期的统计信息，包括发包数、收包数、丢包数、错包数。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                 |
|:-------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLTYPE     | 微服务类型  | 可选必选说明：必选参数 参数含义：该参数用于指定微服务类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看工作角色为数据转发对应的微服务类型。                     |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数 参数含义：该参数用于指定微服务实例号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看工作角色为数据转发对应的微服务实例号。                  |
| SRCTB        | 本端节点TB | 可选必选说明：可选参数 参数含义：该参数用于指定本端节点的资源ID。 数据来源：本端规划 取值范围：整数类型，0~4294967295。 默认值：无 配置原则：使用DSP PAENODE查看资源ID。                                                                                                 |
| DSTTB        | 远端节点TB | 可选必选说明：可选参数 参数含义：该参数用于指定远端节点的资源ID。 数据来源：本端规划 取值范围：整数类型，0~4294967295。 默认值：无 配置原则：使用DSP PAENODE查看资源ID。                                                                                                 |
| SRCPORTNAME  | 本端端口名称 | 可选必选说明：可选参数 参数含义：该参数用于指定本端端口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～19。不支持空格，区分大小写。 默认值：无 配置原则：使用DSP PAEPORTINFO查看端口名称。                                                                                    |
| DSTPORTNAME  | 远端端口名称 | 可选必选说明：可选参数 参数含义：该参数用于指定远端端口名称。端口Bonding模式下，统计的是本端端口发送到远端资源总的报文信息，远端端口名字显示为“NULL”。可以使用DSP PAEPORTINFO查看是否是Bonding模式。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～19。不支持空格，区分大小写。 默认值：无 配置原则：Bonding模式下不支持指定远端端口名称。 |
| LATESTNUM    | 最近周期个数 | 可选必选说明：可选参数 参数含义：查询最近亚健康周期的个数。 数据来源：本端规划 取值范围：整数类型，取值范围为1~30。 默认值：无                                                                                                                                  |

#### 使用实例

- 显示微服务类型为“104”微服务实例为“isu-pod-1172-16-1-214\_\_103\_\_0”本端节点TB为 "1114" 本端端口为 "eth2" 的Fabric链路亚健康统计信息：

  ```
  %%DSP FABRICSUBHEALTHYSTAT: CELLTYPE="104", CELLINSTANCE="isu-pod-1172-16-1-214__103__0", SRCTB=1114, SRCPORTNAME="eth2";%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
  周期索引  本端节点TB  远端节点TB  本端端口名称  远端端口名称  报文类型     发送报文数目  远端接收报文数目  丢失报文数目  错误报文数目  

  0         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  1         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  2         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  3         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  4         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  5         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  6         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  7         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  8         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  9         1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  10        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  11        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  12        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  13        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  14        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  15        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  16        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  17        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  18        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  19        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  20        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  21        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  22        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  23        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  24        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  25        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  26        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  27        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  28        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  29        1114        1115        eth2          NULL          oam_packet   0             0                 0             0             
  0         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  1         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  2         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  3         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  4         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  5         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  6         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  7         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  8         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  9         1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  10        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  11        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  12        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  13        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  14        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  15        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  16        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  17        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  18        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  19        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  20        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  21        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  22        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  23        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  24        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  25        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  26        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  27        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  28        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  29        1114        1115        eth2          NULL          user_packet  0             0                 0             0             
  (结果个数 = 60)

  ---    END
  ```

#### 输出结果说明

| 输出项名称    | 输出项解释                  |
|:---------|:-----------------------|
| 周期索引     | 用于表示周期索引。              |
| 本端节点TB   | 用于表示本端节点的资源ID。         |
| 远端节点TB   | 用于表示远端节点的资源ID。         |
| 本端端口名称   | 用于表示本端端口名称。            |
| 远端端口名称   | 用于表示远端端口名称。            |
| 报文类型     | 用于表示报文类型，包括OAM报文和用户报文。 |
| 发送报文数目   | 用于表示发送报文数目。            |
| 远端接收报文数目 | 用于表示远端接收报文数目。          |
| 丢失报文数目   | 用于表示丢失报文数目。            |
| 错误报文数目   | 用于表示错误报文数目。            |