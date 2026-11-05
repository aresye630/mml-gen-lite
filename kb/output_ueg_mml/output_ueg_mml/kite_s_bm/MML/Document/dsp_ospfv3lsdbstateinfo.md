# 查询OSPFv3 LSDB的状态信息（DSP OSPFV3LSDBSTATEINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询OSPFv3 LSDB中各类LSA的详细信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:--------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROCID  | OSPFv3进程号 | 可选必选说明：可选参数 参数含义：OSPFv3进程号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无                                                                                                                                                                                                                                                                                                                                                                  |
| AREAID  | OSPFv3区域号 | 可选必选说明：可选参数 参数含义：OSPFv3区域号。 数据来源：全网规划 取值范围：IPv4地址类型。点分十进制格式。 默认值：无                                                                                                                                                                                                                                                                                                                                                                        |
| LSATYPE | LSA类型     | 可选必选说明：必选参数 参数含义：LSA类型。 数据来源：本端规划 取值范围：枚举类型。 Router-LSA：Router LSA。Network-LSA：Network LSA。Inter-Area-Prefix-LSA：Inter Area Router LSA。Inter-Area-Router-LSA：Inter Area Router LSA。AS-External-LSA：AS External LSA。Link-LSA：Link LSA。Intra-Area-Prefix-LSA：Intra Area Prefix LSA。Grace-LSA：Grace LSA。NSSA：NSSA。RI-Link-LSA：Router Information Link LSA。RI-Area-LSA：Router Information Area LSA。RI-AS-LSA：Router Information AS LSA。 默认值：无 |

#### 使用实例

- 查询OSPFv3全进程下LSDB中Router LSA的详细信息：

  ```
  DSP OSPFV3LSDBSTATEINFO:LSATYPE=Router-LSA;
  ```

  ```
  RETCODE = 0  操作成功。

  Router LSA Information
  ----------------------
                OSPFv3进程号  =  1
                  路由器标识  =  10.10.10.1
                OSPFv3区域号  =  0.0.0.0
                     LSA类型  =  Router LSA
               LSA的老化时间  =  74
       LSA报头中的链路状态ID  =  0.0.0.1
   发布或产生LSA的路由器标识  =  10.10.10.1
                   LSA序列号  =  0x80000004
                    重传次数  =  0
                   LSA校验和  =  0xa08c
                     LSA长度  =  36
                 LSA选项标志  =  -|-|-|-|-
                     LSA选项  =  -|-|-|-|E|V6
       （路由器LSA）链路类型  =  None
                服务类型度量  =  0
                  接口实例ID  =  0x0
                  邻居接口ID  =  0x0
              邻居路由器标识  =  10.10.10.2
  (结果个数 = 1)
  ---    END
  ```
- 查询OSPFv3全进程下LSDB中External LSA的详细信息：

  ```
  DSP OSPFV3LSDBSTATEINFO:LSATYPE=AS-External-LSA;
  ```

  ```
  RETCODE = 0  操作成功。

  External LSA Information
  ------------------------
                OSPFv3进程号  =  1
                  路由器标识  =  10.10.10.1
                     LSA类型  =  AS External LSA
               LSA的老化时间  =  74
       LSA报头中的链路状态ID  =  0.0.0.1
   发布或产生LSA的路由器标识  =  10.10.10.1
                   LSA序列号  =  0x80000004
                    重传次数  =  0
                   LSA校验和  =  0xa08c
                     LSA长度  =  36
                 LSA选项标志  =  E|-|T
                外部花费类型  =  Type 2
                服务类型度量  =  1
        IPv6前缀过滤策略名称  =  2001:db8::
                IPv6前缀长度  =  64
                IPv6前缀选项  =  -|-|-|-|-
          VPN引入路由的tag值  =  1
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称          | 输出项解释                                         |
|:---------------|:----------------------------------------------|
| OSPFv3进程号      | 该参数用于表示OSPFv3进程号。                             |
| 路由器标识          | 该参数用于表示OSPFv3路由器标识。                           |
| OSPFv3区域号      | 该参数表示区域号。                                     |
| LSA类型          | 该参数用于表示LSA类型。                                 |
| LSA的老化时间       | 该参数用于表示LSA的老化时间。                              |
| LSA报头中的链路状态ID  | 该参数用于表示LSA报头中的链路状态ID，与LSA类型一起描述路由域中唯一一个LSA。   |
| 发布或产生LSA的路由器标识 | 该参数用于表示发布或产生LSA的路由器标识。                        |
| LSA序列号         | 该参数用于表示LSA序列号，其他路由器根据这个值可以判断哪个LSA是最新的。        |
| 重传次数           | 该参数用于表示LSA的重传次数。                              |
| LSA校验和         | 该参数用于表示LSA校验和，除了LSA的老化时间外其它各域的校验和。            |
| LSA长度          | 该参数用于表示LSA的长度。                                |
| LSA选项标志        | 该参数用于表示LSA选项标志。                               |
| LSA选项          | 该参数用于表示LSA的选项域。                               |
| （路由器LSA）链路类型   | 该参数用于表示链路类型，分为P2P、TransNet、StubNet、Virtual四类。 |
| 服务类型度量         | 该参数用于表示服务类型度量。                                |
| 接口实例ID         | 该参数用于表示接口实例ID。                                |
| 邻居接口ID         | 该参数用于表示邻居接口实例ID。                              |
| 邻居路由器标识        | 该参数用于表示邻居路由器标识。                               |