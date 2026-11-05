# 配置ACL防止UE之间的互访

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

对于企业APN用户，通常通过根据企业要求提供用户之间的互访功能；对于通用APN用户，为了防止用户之间的恶意攻击，一般情况下移动运营商禁止用户互访。为保证UE的安全，可以在UDG上设置包过滤策略UE之间互访的报文。UDG对报文的源地址和目的地址进行判断，如果都在用户的IP地址网段中，则禁止报文通过。

**说明** 

建议UE的IP地址网段与PDN侧服务器的IP地址网段隔离，否则配置了ACL防止UE之间的互访功能后，将导致UE无法访问PDN侧服务器。

**说明** 

适用于SGW-U、PGW-U、UPF。

## 必备事项

前提条件

无。

数据

| 类别         | 参数名称                       | 取值样例                                                                                                                                   | 获取方法      | 说明                                                  |
|:-----------|:---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|:----------|:----------------------------------------------------|
| 三四层的过滤规则   | 过滤器名字（FILTERNAME）          | protect_1 protect_2 protect_3 protect_4 protect_5 protect_6 protect_7 protect_8 protect_9                                              | 本端规划      | ADD FILTER                                          |
| 三四层的过滤规则   | 三四层IPv4协议输入类型（L34PROTTYPE） | STRING                                                                                                                                 | 本端规划      | ADD FILTER                                          |
| 三四层的过滤规则   | 三四层协议类型（L34PROTOCOL）       | ANY                                                                                                                                    | 本端规划      | ADD FILTER                                          |
| 三四层的过滤规则   | 手机IP地址配置模式（MSIPMODE）       | IP                                                                                                                                     | 全网规划      | 报文的源IP地址及反掩码。 ADD FILTER                            |
| 三四层的过滤规则   | 手机IP地址（MSIP）               | 10.40.0.0 10.42.0.0 10.45.0.0                                                                                                          | 全网规划      | 报文的源IP地址及反掩码。 ADD FILTER                            |
| 三四层的过滤规则   | 手机IP地址掩码类型（MSIPMASKTYPE）   | IPTYPE                                                                                                                                 | 全网规划      | 报文的源IP地址及反掩码。 ADD FILTER                            |
| 三四层的过滤规则   | 手机IP地址反掩码（MSIPMASK）        | 0.0.255.255 0.0.255.255 0.0.255.255                                                                                                    | 全网规划      | 报文的源IP地址及反掩码。 ADD FILTER                            |
| 三四层的过滤规则   | 服务器IP地址配置模式（SVRIPMODE）     | IP                                                                                                                                     | 全网规划      | 报文的目的IP地址及反掩码。 ADD FILTER                           |
| 三四层的过滤规则   | 服务器IP地址（SVRIP）             | 10.40.0.0 10.42.0.0 10.45.0.0                                                                                                          | 全网规划      | 报文的目的IP地址及反掩码。 ADD FILTER                           |
| 三四层的过滤规则   | 服务器IP地址掩码类型（SVRIPMASKTYPE） | IPTYPE                                                                                                                                 | 全网规划      | 报文的目的IP地址及反掩码。 ADD FILTER                           |
| 三四层的过滤规则   | 服务器IP地址反掩码（SVRIPMASK）      | 0.0.255.255 0.0.255.255 0.0.255.255                                                                                                    | 全网规划      | 报文的目的IP地址及反掩码。 ADD FILTER                           |
| ACL节点      | ACL节点名称（ACLNODENAME）       | node_protect_1 node_protect_2 node_protect_3 node_protect_4 node_protect_5 node_protect_6 node_protect_7 node_protect_8 node_protect_9 | 本端规划      | ADD ACLNODE                                         |
| ACL节点      | 过滤器名字（FILTERNAME）          | protect_1 protect_2 protect_3 protect_4 protect_5 protect_6 protect_7 protect_8 protect_9                                              | 从已配置数据中获取 | 已通过ADD FILTER命令配置完成，可以使用LST FILTER命令进行查询。           |
| ACL节点      | 动作类型（ACTIONTYPE）           | GATE                                                                                                                                   | 本端规划      | ADD ACLNODE                                         |
| ACL节点      | 门控动作（GATEACTION）           | DISCARD                                                                                                                                | 本端规划      | ADD ACLNODE                                         |
| ACL        | ACL名称（ACLNAME）             | acl-protect-ip                                                                                                                         | 本端规划      | ADD ACL                                             |
| ACL        | 匹配方式（MATCHORDER）           | AUTO                                                                                                                                   | 本端规划      | ADD ACL                                             |
| 绑定ACL-Node | ACL名称（ACLNAME）             | acl-protect-ip                                                                                                                         | 从已配置数据中获取 | 已通过ADD ACL命令配置完成，可以使用LST ACL命令进行查询。                 |
| 绑定ACL-Node | ACL节点名称（ACLNODENAME）       | node_protect_1 node_protect_2 node_protect_3 node_protect_4 node_protect_5 node_protect_6 node_protect_7 node_protect_8 node_protect_9 | 从已配置数据中获取 | 已通过ADD ACLNODE命令配置完成，可以使用LST ACLNODE命令进行查询。         |
| APN 绑定ACL  | APN名称（APN）                 | apn-test                                                                                                                               | 从已配置数据中获取 | 规划绑定ACL规则的APN实例，已通过ADD APN命令配置完成，可以使用LST APN命令进行查询。 |
| APN 绑定ACL  | 方向（DIRECTION）              | UPIN                                                                                                                                   | 本端规划      | ADD ACLBINDAPN                                      |
| APN 绑定ACL  | ACL名称（ACLNAME）             | acl-protect-ip                                                                                                                         | 从已配置数据中获取 | 已通过ADD ACL命令配置完成，可以使用LST ACL命令进行查询。                 |

## 操作步骤

1. 配置ACL节点使用的过滤规则。
   1. 配置三四层的过滤规则。

      **ADD FILTER**: FILTERNAME=过滤器名字,L34PROTTYPE=三四层IPv4协议输入类型,L34PROTOCOL=三四层协议类型;
   2. 将新配置的filter置为生效。

      **SET REFRESHSRV**: REFRESHTYPE=USERPROFILE;
2. 配置ACL节点，并绑定到ACL。
   1. 配置ACL节点，即配置三四层过滤规则对应的动作。

      **ADD ACLNODE**: ACLNODENAME=ACL节点名称,FILTERNAME=过滤器名字,ACTIONTYPE=动作类型;
   2. 配置ACL名称、排序方式。

      **ADD ACL**: ACLNAME=ACL名称,MATCHORDER=排序方式;
   3. 配置绑定ACL节点到ACL下。

      **ADD ACLNODEBINDACL**: ACLNAME=ACL名称,ACLNODENAME=ACL节点名称;
3. 配置ACL与APN的绑定关系。
   1. 指定APN名称。

      **ADD APN**: APN=APN名称;
   2. 配置ACL绑定到APN下。

      **ADD ACLBINDAPN**: APN=APN名称,DIRECTION=方向,ACLNAME=ACL名称;
   3. 将新配置的ACL和ACL节点置为生效。

      **SET REFRESHSRV**: REFRESHTYPE=ACL;

## 任务示例

任务描述

在UDG上配置ACL规则，防止UE之间的互访。UE的IP地址网段为：10.40.0.0/16、10.42.0.0/16、10.45.0.0/16。

脚本

1. 配置ACL节点使用的过滤规则。

   # 禁止10.40.0.0/16网段的UE访问10.40.0.0/16、10.42.0.0/16、10.45.0.0/16网段的UE。

   ```
   ADD FILTER:FILTERNAME="protect_1",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.40.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.40.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   ADD FILTER:FILTERNAME="protect_2",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.40.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.42.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   ADD FILTER:FILTERNAME="protect_3",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.40.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.45.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   # 禁止10.42.0.0/16网段的UE访问10.40.0.0/16、10.42.0.0/16、10.45.0.0/16网段的UE。

   ```
   ADD FILTER:FILTERNAME="protect_4",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.42.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.40.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   ADD FILTER:FILTERNAME="protect_5",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.42.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.42.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   ADD FILTER:FILTERNAME="protect_6",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.42.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.45.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   # 禁止10.45.0.0/16网段的UE访问10.40.0.0/16、10.42.0.0/16、10.45.0.0/16网段的UE。

   ```
   ADD FILTER:FILTERNAME="protect_7",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.45.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.40.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   ADD FILTER:FILTERNAME="protect_8",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.45.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.42.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   ADD FILTER:FILTERNAME="protect_9",L34PROTTYPE=STRING,L34PROTOCOL=ANY,MSIPMODE=IP,MSIP="10.45.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="0.0.255.255",SVRIPMODE=IP,SVRIP="10.45.0.0",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.255.255";
   ```

   ```
   SET REFRESHSRV:REFRESHTYPE=ALL;
   ```
2. 配置ACL节点，并绑定到ACL，将过滤规则和流动作关联。

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_1",FILTERNAME="protect_1",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_2",FILTERNAME="protect_2",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_3",FILTERNAME="protect_3",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_4",FILTERNAME="protect_4",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_5",FILTERNAME="protect_5",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_6",FILTERNAME="protect_6",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_7",FILTERNAME="protect_7",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_8",FILTERNAME="protect_8",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACLNODE:ACLNODENAME="node_protect_9",FILTERNAME="protect_9",ACTIONTYPE=GATE,GATEACTION=DISCARD;
   ```

   ```
   ADD ACL:ACLNAME="acl-protect-ip",MATCHORDER=AUTO;
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_1";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_2";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_3";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_4";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_5";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_6";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_7";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_8";
   ```

   ```
   ADD ACLNODEBINDACL:ACLNAME="acl-protect-ip",ACLNODENAME="node_protect_9";
   ```
3. 配置ACL与APN的绑定关系，将ACL应用到APN。

   ```
   ADD APN:APN="apn-test",HASVPN=DISABLE,HASVPNIPV6=DISABLE,RESTORPGWSWITCH=INHERIT;
   ```

   ```
   ADD ACLBINDAPN:APN="apn-test",DIRECTION=UPIN,ACLNAME="acl-protect-ip";
   ```

   ```
   SET REFRESHSRV:REFRESHTYPE=ACL;
   ```