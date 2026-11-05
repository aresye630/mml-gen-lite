# 查询用户模板（LST USERPROFILE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询用户模板。

#### 注意事项

如果不输入用户模板名称，表示查询系统中所有用户模板。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称     | 参数说明                                                                                                                                                                                                |
|:----------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERPROFILENAME | 用户模板名称   | 可选必选说明：可选参数 参数含义：该参数用于指定用户模板名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。 默认值：无 配置原则：无                                                                                        |
| UPSPECTYPE      | 用户模板规格类型 | 可选必选说明：可选参数 参数含义：该参数用于指定用户模板类型，当取值为SPECIFICATION_LIMITED时，表示规格受限用户模板，表示会话安装的该类型的USERPROFILE数和该类型的USERPROFILE绑定的规则数量均存在一定限制。 数据来源：本端规划 取值范围： DEFAULT：默认配置。SPECIFICATION_LIMITED：规格受限配置。 默认值：无 配置原则：无 |

#### 使用实例

- 假如运营商需要查询名称为testuserprofile1的用户模板：

  ```
  LST USERPROFILE: USERPROFILENAME="testuserprofile1";
  ```

  ```
  RETCODE = 0  操作成功。

  用户模板信息
  ------------
                             用户模板名称  =  testuserprofile1
                         用户模板规格类型  =  默认配置
                    Alias Marking使能标记  =  不使能
                           防DDOS攻击标记  =  不使能
                Captive模式时间阈值（分）  =  0
                   配额申请时报文处理动作  =  缓存
                         实时位置上报开关  =  继承
                                 锁定标记  =  不使能
                            缺省URR组名称  =  NULL
                        缺省信令URR组名称  =  NULL
                          重定向URR组名称  =  NULL
                          TCP重传计费标识  =  未配置
                         TCP重传URR组名称  =  NULL
                            URL白名单名称  =  NULL
                             扩展属性名称  =  NULL
                    CCR-Initia URR组名称1  =  NULL
                   CCR-Initial URR组名称2  =  NULL
                   CCR-Initial URR组名称3  =  NULL
                   CCR-Initial URR组名称4  =  NULL
                   CCR-Initial URR组名称5  =  NULL
                   CCR-Initial URR组名称6  =  NULL
                   CCR-Initial URR组名称7  =  NULL
                   CCR-Initial URR组名称8  =  NULL
                   CCR-Initial URR组名称9  =  NULL
                  CCR-Initial URR组名称10  =  NULL
                             用户模板别名  =  NULL
                 IPv6 TCP报文长度（字节）  =  0
                 IPv4 TCP报文长度（字节）  =  0
  Tethering用户下最多可接入后台终端的数量  =  0
                               配置域名称  =  NULL
                继承全局缺省URR组配置开关  =  使能
                继承全局缺省信令URR组开关  =  使能
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询所有的用户模板：

  ```
  LST USERPROFILE:;
  ```

  ```
  RETCODE = 0  操作成功。

  用户模板信息
  ------------
  用户模板名称        用户模板规格类型        Alias Marking使能标记    防DDOS攻击标记    Captive模式时间阈值（分）    配额申请时报文处理动作    实时位置上报开关    锁定标记    缺省URR组名称    缺省信令URR组名称    重定向URR组名称    TCP重传计费标识    TCP重传URR组名称    URL白名单名称    扩展属性名称    CCR-Initia URR组名称1    CCR-Initial URR组名称2    CCR-Initial URR组名称3    CCR-Initial URR组名称4    CCR-Initial URR组名称5    CCR-Initial URR组名称6    CCR-Initial URR组名称7    CCR-Initial URR组名称8    CCR-Initial URR组名称9    CCR-Initial URR组名称10    用户模板别名    IPv6 TCP报文长度（字节）    IPv4 TCP报文长度（字节）    Tethering用户下最多可接入后台终端的数量    配置域名称  继承全局缺省URR组配置开关  继承全局缺省信令URR组开关

  testuserprofile1    默认配置        不使能                   不使能            0                            缓存                      继承                不使能      NULL             NULL                 NULL               未配置             NULL                NULL             NULL            NULL                     NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                       NULL            0                           0                           0                                          NULL               使能               使能
  testuserprofile2    默认配置        不使能                   不使能            0                            缓存                      继承                不使能      NULL             NULL                 NULL               未配置             NULL                NULL             NULL            NULL                     NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                       NULL            0                           0                           0                                          NULL               使能               使能
  testuserprofile3    默认配置        不使能                   不使能            0                            缓存                      继承                不使能      NULL             NULL                 NULL               未配置             NULL                NULL             NULL            NULL                     NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                       NULL            0                           0                           0                                          NULL               使能               使能
  (结果个数 = 3)
  ---    END
  ```

#### 输出结果说明

| 输出项名称                | 输出项解释                   |
|:---------------------|:------------------------|
| 锁定标记                 | 指定锁定标记。                 |
| CCR-Initia URR组名称1   | 指定CCR-Initial URR组名称1。  |
| CCR-Initial URR组名称2  | 指定CCR-Initial URR组名称2。  |
| CCR-Initial URR组名称3  | 指定CCR-Initial URR组名称3。  |
| CCR-Initial URR组名称4  | 指定CCR-Initial URR组名称4。  |
| CCR-Initial URR组名称5  | 指定CCR-Initial URR组名称5。  |
| CCR-Initial URR组名称6  | 指定CCR-Initial URR组名称6。  |
| CCR-Initial URR组名称7  | 指定CCR-Initial URR组名称7。  |
| CCR-Initial URR组名称8  | 指定CCR-Initial URR组名称8。  |
| CCR-Initial URR组名称9  | 指定CCR-Initial URR组名称9。  |
| CCR-Initial URR组名称10 | 指定CCR-Initial URR组名称10。 |

其余输出项请参见ADD USERPROFILE、SET URRGRPBINDING、SET WHITEURLLISTBIND的参数说明。