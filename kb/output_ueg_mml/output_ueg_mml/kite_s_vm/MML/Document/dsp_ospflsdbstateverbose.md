# 查询OSPF LSDB详细信息（DSP OSPFLSDBSTATEVERBOSE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示OSPF LSDB详细信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                                                                                                                                                                                           |
|:------------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROCESSID   | OSPF进程号       | 可选必选说明：可选参数 参数含义：该参数表示OSPF进程号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无                                                                                                                                                                                    |
| LSATYPE     | LSA类型         | 可选必选说明：必选参数 参数含义：该参数表示LSA类型。 数据来源：本端规划 取值范围：枚举类型。 Router：Router LSA。Network：Network LSA。Sum_Net：ABR Summary LSA。Sum_Asbr：ASBR Summary LSA。External：AS-External LSA。NSSA：NSSA LSA。Opq_Link：Opaque Link LSA。Opq_Area：Opaque Area LSA。Opq_As：Opaque AS LSA。 默认值：无 |
| LINKSTATEID | LSA报文中的链路状态ID | 可选必选说明：可选参数 参数含义：该参数表示LSA报文中的链路状态ID。 数据来源：本端规划 取值范围：IPv4地址类型。点分十进制格式。 默认值：无                                                                                                                                                                                    |

#### 使用实例

- 查询OSPF全进程下LSDB中Router LSA的详细信息：

  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=Router;
  ```

  ```
  RETCODE = 0  操作成功。

  Router LSA信息
  ------------------------
                 OSPF进程号  =  1
                     区域号  =  0.0.0.0
                 路由器标识  =  192.168.3.111
                    LSA类型  =  Router LSA
      LSA报文中的链路状态ID  =  192.168.3.111
  发布或产生LSA的路由器标识  =  192.168.3.111
         LSA的老化时间（s）  =  701
                    LSA长度  =  36
                  LSA序列号  =  0x80000002
                  LSA校验和  =  0xa02e
                    LSA选项  =  E
                LSA选项标志  =  ASBR ABR
                     链路ID  =  192.168.14.0
                   链路数据  =  255.255.255.0
                   链路类型  =  Stub Network
               服务类型度量  =  1
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPF全进程下LSDB中Network LSA的详细信息：

  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=Network;
  ```

  ```
  RETCODE = 0  操作成功。

  Network LSA信息
  -----------------------
                       OSPF进程号  =  1
                           区域号  =  0.0.0.0
                       路由器标识  =  192.168.3.111
                          LSA类型  =  Network LSA
            LSA报文中的链路状态ID  =  192.168.3.111
        发布或产生LSA的路由器标识  =  192.168.3.111
                LSA的老化时间（s） =  266
                          LSA长度  =  32
                        LSA序列号  =  0x80000001
                        LSA校验和  =  0x66c4
                          LSA选项  =  E
                         网络掩码  =  255.255.255.0
               与网络连接的路由器  =  192.168.3.112
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPF全进程下LSDB中External LSA的详细信息：

  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=External;
  ```

  ```
  RETCODE = 0  操作成功。

  As-external-LSA信息
  ---------------------------
                 OSPF进程号  =  1
                     区域号  =  0.0.0.0
                 路由器标识  =  192.168.3.111
                    LSA类型  =  AS-External LSA
      LSA报文中的链路状态ID  =  192.168.3.100
  发布或产生LSA的路由器标识  =  192.168.3.112
         LSA的老化时间（s）  =  666
                    LSA长度  =  36
                  LSA序列号  =  0x80000001
                  LSA校验和  =  0x6dd8
                    LSA选项  =  E
                   网络掩码  =  255.255.255.255
                 服务类型ID  =  0
               服务类型度量  =  1
                      E类型  =  2
                 转发IP地址  =  0.0.0.0
                   路由标识  =  1
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPF全进程下LSDB中Opq\_Area LSA的详细信息：

  ```
  DSP OSPFLSDBSTATEVERBOSE:LSATYPE=Opq_Area;
  ```

  ```
  RETCODE = 0  操作成功。

  Opaque-area LSA信息
  ---------------------------
                 OSPF进程号  =  1
                     区域号  =  0.0.0.0
                 路由器标识  =  192.168.3.111
                    LSA类型  =  Opaque Area LSA
      LSA报文中的链路状态ID  =  10.10.10.0
  发布或产生LSA的路由器标识  =  192.168.3.111
          LSA的老化时间（s） =  1305
                    LSA长度  =  28
                  LSA序列号  =  0x80000001
                  LSA校验和  =  0x31e3
                    LSA选项  =  E
                 Opaque类型  =  4
                  Opaque ID  =  0
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称          | 输出项解释                                                       |
|:---------------|:------------------------------------------------------------|
| OSPF进程号        | 表示OSPF进程号。                                                  |
| 区域号            | 表示区域号。                                                      |
| 路由器标识          | 表示路由器标识。                                                    |
| LSA类型          | 表示LSA类型。                                                    |
| LSA报文中的链路状态ID  | 表示LSA报文中的链路状态ID。                                            |
| 发布或产生LSA的路由器标识 | 表示发布或产生LSA的路由器标识。                                           |
| LSA的老化时间（s）    | 表示LSA的老化时间。                                                 |
| LSA长度          | 表示LSA长度。                                                    |
| LSA序列号         | 表示LSA序列号。                                                   |
| LSA校验和         | 表示LSA校验和。                                                   |
| LSA选项          | 表示LSA选项。                                                    |
| LSA选项标志        | 表示LSA选项标志。                                                  |
| 链路ID           | 表示（路由器LSA）链路ID（按链路类型分类）。                                    |
| 链路数据           | 表示（路由器LSA）链路数据。                                             |
| 链路类型           | 表示（路由器LSA）链路类型。                                             |
| 服务类型度量         | 表示服务类型度量。                                                   |
| 网络掩码           | 表示（网络LSA）网络掩码。                                              |
| 与网络连接的路由器      | 表示（网络LSA）与网络连接的路由器。                                         |
| 服务类型ID         | 表示服务类型ID。                                                   |
| E类型            | 表示外部路由开销计算类型。                                               |
| 转发IP地址         | 表示转发IP地址。                                                   |
| 路由标识           | 表示路由标识。32位字段，防止路由环路，用于在Type-5/Type-7 LSA上。                  |
| Opaque类型       | 表示Opaque类型。                                                 |
| Opaque ID      | 表示（Opaque LSA）Opaque ID号，Opaque类型+Opaque ID号=LSA报头中的链路状态ID。 |