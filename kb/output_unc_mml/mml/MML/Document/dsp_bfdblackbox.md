# 查询BFD黑匣子信息（DSP BFDBLACKBOX）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令行用于查询BFD的黑匣子信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                    |
|:-----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE       | 黑匣子类型  | 可选必选说明：必选参数 参数含义：黑匣子的类型。 数据来源：本端规划 取值范围：枚举类型。 SESSION：会话信息。SOCK：套接字。HA：高可靠性。SMOOTH_APP：应用平滑信息。RELIABILITY：可靠性。SMOOTH_FEI：FEI平滑。SMOOTH_FES：FES平滑。FES_TLV：FES的TLV。GFD_COMMON：GFD公共消息。GFD_NOTIFY：GFD消息通告。DISCRIMINATOR：会话标识符。DEVM_LIB：DEVM消息。VPN_LIB：VPN消息。EVENT：事件消息。IFM_LIB：IFM消息。 默认值：无 |
| LOCALDISCR | 本地标识符  | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“DISCRIMINATOR”时为必选参数。 参数含义：本地描述符。 数据来源：本端规划 取值范围：整数类型，取值范围为1～49152。 默认值：无                                                                                                                                                                              |

#### 使用实例

查询BFD高可靠性的黑匣子信息：

```
DSP BFDBLACKBOX:TYPE=HA;
```

```
RETCODE = 0  操作成功。

结果如下
----------------
   黑匣子信息  =  2016-12-23 0:38:3:55  Execute batch backup FSM.(input:0,state:0)
2016-12-23 0:38:4:950  Execute batch backup FSM.(input:1,state:1)
2016-12-23 0:38:5:955  Execute batch backup FSM.(input:3,state:2)
2016-12-23 0:38:6:950  Execute batch backup FSM.(input:4,state:3)
2016-12-23 0:38:7:955  Execute batch backup FSM.(input:5,state:4)
2016-12-23 0:38:8:959  Execute batch backup FSM.(input:7,state:6)
2016-12-23 0:38:9:965  Execute batch backup FSM.(input:8,state:7)
2016-12-23 0:38:10:964  Execute batch backup FSM.(input:10,state:8)
2016-12-23 1:30:19:798  Execute component FSM.(input:1,state:7)
(结果个数 = 1)
--- END
```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 黑匣子信息   | 查询黑匣子返回的信息。 |