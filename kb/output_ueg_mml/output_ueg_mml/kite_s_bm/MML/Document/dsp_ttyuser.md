# 显示用户信息（DSP TTYUSER）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示用户信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                       |
|:----------|:-------|:---------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE | 查询类型   | 可选必选说明：必选参数 参数含义：该参数用于表示查询用户信息的类型 USERINTF:用户界面 ONLINEUSER:在线用户。 数据来源：本端规划 取值范围：枚举类型。 USERINTF：用户界面。ONLINEUSER：在线用户。 默认值：无 |

#### 使用实例

- 查询用户界面的用户信息：

  ```
  DSP TTYUSER:QUERYTYPE=USERINTF;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  激活状态      接口编号    接口类型    速率    MODEM类型    认证模式    物理编号

  未激活状态    0           CON 0       9600    NULL         密码认证    1
  未激活状态    1           CON 0       9600    NULL         密码认证    2
  未激活状态    34          VTY 0       NULL    NULL         AAA认证     NULL
  未激活状态    35          VTY 1       NULL    NULL         AAA认证     NULL
  未激活状态    36          VTY 2       NULL    NULL         AAA认证     NULL
  未激活状态    37          VTY 3       NULL    NULL         AAA认证     NULL
  未激活状态    38          VTY 4       NULL    NULL         AAA认证     NULL
  未激活状态    39          VTY 5       NULL    NULL         AAA认证     NULL
  未激活状态    40          VTY 6       NULL    NULL         AAA认证     NULL
  未激活状态    41          VTY 7       NULL    NULL         AAA认证     NULL
  未激活状态    42          VTY 8       NULL    NULL         AAA认证     NULL
  未激活状态    43          VTY 9       NULL    NULL         AAA认证     NULL
  未激活状态    44          VTY 10      NULL    NULL         AAA认证     NULL
  未激活状态    45          VTY 11      NULL    NULL         AAA认证     NULL
  未激活状态    46          VTY 12      NULL    NULL         AAA认证     NULL
  未激活状态    47          VTY 13      NULL    NULL         AAA认证     NULL
  未激活状态    48          VTY 14      NULL    NULL         AAA认证     NULL
  未激活状态    49          VTY 15      NULL    NULL         AAA认证     NULL
  未激活状态    50          VTY 16      NULL    NULL         AAA认证     NULL
  未激活状态    51          VTY 17      NULL    NULL         AAA认证     NULL
  未激活状态    52          VTY 18      NULL    NULL         AAA认证     NULL
  未激活状态    53          VTY 19      NULL    NULL         AAA认证     NULL
  未激活状态    54          VTY 20      NULL    NULL         AAA认证     NULL
  未激活状态    100         NCA 0       NULL    NULL         AAA认证     NULL
  未激活状态    101         NCA 1       NULL    NULL         AAA认证     NULL
  未激活状态    102         NCA 2       NULL    NULL         AAA认证     NULL
  未激活状态    103         NCA 3       NULL    NULL         AAA认证     NULL
  未激活状态    104         NCA 4       NULL    NULL         AAA认证     NULL
  未激活状态    105         NCA 5       NULL    NULL         AAA认证     NULL
  未激活状态    106         NCA 6       NULL    NULL         AAA认证     NULL
  未激活状态    107         NCA 7       NULL    NULL         AAA认证     NULL
  未激活状态    108         NCA 8       NULL    NULL         AAA认证     NULL
  未激活状态    109         NCA 9       NULL    NULL         AAA认证     NULL
  未激活状态    110         NCA 10      NULL    NULL         AAA认证     NULL
  未激活状态    111         NCA 11      NULL    NULL         AAA认证     NULL
  未激活状态    112         NCA 12      NULL    NULL         AAA认证     NULL
  未激活状态    113         NCA 13      NULL    NULL         AAA认证     NULL
  未激活状态    114         NCA 14      NULL    NULL         AAA认证     NULL
  未激活状态    115         NCA 15      NULL    NULL         AAA认证     NULL
  未激活状态    116         NCA 16      NULL    NULL         AAA认证     NULL
  未激活状态    117         NCA 17      NULL    NULL         AAA认证     NULL
  未激活状态    118         NCA 18      NULL    NULL         AAA认证     NULL
  未激活状态    119         NCA 19      NULL    NULL         AAA认证     NULL
  激活状态      200         MML 0       NULL    NULL         AAA认证     NULL
  未激活状态    201         MML 1       NULL    NULL         AAA认证     NULL
  未激活状态    202         MML 2       NULL    NULL         AAA认证     NULL
  未激活状态    203         MML 3       NULL    NULL         AAA认证     NULL
  未激活状态    204         MML 4       NULL    NULL         AAA认证     NULL
  未激活状态    205         MML 5       NULL    NULL         AAA认证     NULL
  未激活状态    206         MML 6       NULL    NULL         AAA认证     NULL
  未激活状态    207         MML 7       NULL    NULL         AAA认证     NULL
  未激活状态    208         MML 8       NULL    NULL         AAA认证     NULL
  未激活状态    209         MML 9       NULL    NULL         AAA认证     NULL
  未激活状态    210         MML 10      NULL    NULL         AAA认证     NULL
  未激活状态    211         MML 11      NULL    NULL         AAA认证     NULL
  未激活状态    212         MML 12      NULL    NULL         AAA认证     NULL
  未激活状态    213         MML 13      NULL    NULL         AAA认证     NULL
  未激活状态    214         MML 14      NULL    NULL         AAA认证     NULL
  未激活状态    215         MML 15      NULL    NULL         AAA认证     NULL
  未激活状态    216         MML 16      NULL    NULL         AAA认证     NULL
  未激活状态    217         MML 17      NULL    NULL         AAA认证     NULL
  未激活状态    218         MML 18      NULL    NULL         AAA认证     NULL
  未激活状态    219         MML 19      NULL    NULL         AAA认证     NULL
  未激活状态    220         MML 20      NULL    NULL         AAA认证     NULL
  未激活状态    221         MML 21      NULL    NULL         AAA认证     NULL
  未激活状态    222         MML 22      NULL    NULL         AAA认证     NULL
  未激活状态    223         MML 23      NULL    NULL         AAA认证     NULL
  未激活状态    224         MML 24      NULL    NULL         AAA认证     NULL
  未激活状态    225         MML 25      NULL    NULL         AAA认证     NULL
  未激活状态    226         MML 26      NULL    NULL         AAA认证     NULL
  未激活状态    227         MML 27      NULL    NULL         AAA认证     NULL
  未激活状态    228         MML 28      NULL    NULL         AAA认证     NULL
  未激活状态    229         MML 29      NULL    NULL         AAA认证     NULL
  (结果个数 = 73)
  ---    END
  ```
- 查询当前在线的用户信息：

  ```
  DSP TTYUSER:QUERYTYPE= ONLINEUSER;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  当前使用    接口编号    接口类型    空闲时间    连接类型    网络地址      认证状态    命令行授权标志    用户名

  否          34          VTY 0       00:02:44    SSH         172.17.0.1    认证成功    是                omuser
  否          100         NCA 0       00:00:01    SSH         172.17.0.1    认证成功    是                VNFP_SYSTEM
  否          101         NCA 1       00:00:09    SSH         172.17.0.1    认证成功    是                VNFP_SYSTEM
  是          200         MML 0       00:00:00    SSH         172.17.0.1    认证成功    是                omuser
  (结果个数 = 4)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                                                     |
|:--------|:------------------------------------------------------------------------------------------|
| 激活状态    | 表示用户界面当前的激活状态：未激活状态、激活状态、激活并工作在异步模式。                                                      |
| 接口编号    | 用于表示用户界面的接口编号。接口编号0到1为Console使用，接口编号34到54为VTY使用，接口编号100到119为SNetconf使用，接口编号200到229为MML使用。 |
| 接口类型    | 用于表示接口类型。                                                                                 |
| 速率      | 用于表示速率。                                                                                   |
| MODEM类型 | 用于表示MODEM类型。                                                                              |
| 认证模式    | 表示认证模式： Password：密码认证 AAA：AAA认证 NONE：无认证。                                                 |
| 物理编号    | 用于表示物理编号。                                                                                 |
| 当前使用    | 表示用户界面当前是否在使用： Yes:在使用 No:未使用。                                                            |
| 空闲时间    | 用于表示空闲时间。                                                                                 |
| 连接类型    | 用于表示服务类型。                                                                                 |
| 网络地址    | 用于表示网络地址。                                                                                 |
| 认证状态    | 用于表示认证状态。                                                                                 |
| 命令行授权标志 | 用于表示命令行授权标志。                                                                              |
| 用户名     | 用于表示用户名。                                                                                  |