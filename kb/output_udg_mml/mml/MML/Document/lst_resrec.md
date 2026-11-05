# 查询资源记录（LST RESREC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：CloudEPSN**

本命令实现查询A、AAAA、NS、SRV、NAPTR记录的功能。

#### 注意事项

- （CloudDNS无需执行此步骤）在依次执行SET DNSINFO、GEN DNSTASKID、EXC DNSCFGTASK初始化执行机后，可以开始使用增加LST RESREC命令。
- 完整域名，即参数“域名”以“.”结尾。添加资源记录的“域名”参数时，可以是完整域名，也可以是部分域名，会自动将部分域名和区域名一起拼接成完整域名。例如：当参数“域名”不是以“.”结尾，是部分域名时：“区域名”为“ln.mnc000.mcc460.gprs”，“域名”为“cmnet”，完整域名为“cmnet.ln.mnc000.mcc460.gprs.”。
- （CloudDNS不支持此功能）域名输入为“@”，设定为与当前区域名称同名的域名。
- 若没有输入“域名”参数，则输出当前“区域名称”下“记录类型”选中类型的从初始记录号开始的count个数的记录内容。
- 若输入“域名”参数，参数start、count不生效。
- 当增加记录时，“TTL”参数不填写时，显示为NULL，代表与当前“区域名称”有相同的TTL值。
- “START”和“COUNT”参数若没有填写，则默认返回“记录类型”的前100条记录，若记录数量少于100条，则返回“记录类型”已有的全部记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:---------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE     | 记录类型   | 可选必选说明：必选参数 参数含义：增加的记录类型。 数据来源：本端规划 取值范围：NA。 A：A记录。AAAA：AAAA记录。NAPTR：NAPTR记录。SRV：SRV记录。NS：NS记录。 默认值：无 配置原则： A记录：由域名解析出IPV4地址的记录。AAAA记录：由域名解析出IPV6地址的记录。NS记录：配置区域所属的授权域名服务器的记录。SRV记录：根据某项服务的域名解析出主机名的记录。NAPTR记录：根据域名解析出替换域名的记录。                                                                                                                                                                                           |
| VIEWNAME | 视图名称   | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。 参数含义：资源所属的域名解析视图名称。 数据来源：本端规划 取值范围：1、名称如果分段，每段不超过63个字符，并且视图名称（填入的视图名称）总长度不超过253个字符；如果不分段，填入的视图名称最长不超过63个字符。该字符数转化为符合DNS标准ASCII格式（Punycode编码）后的要求。 2、不支持连续的点、下划线、中横线（如“..”、“__”、“--”）。 3、视图名称的每段的内容支持以字母、数字、下划线、中横线的任意组合，但是不支持以中横线开头和不支持下划线结尾。 4、不允许输入仅一个“.”。 5、不支持以“.”开头和结尾。 默认值：default 配置原则： 视图名称需要在CMS WEB端配置。CloudDNS中视图默认值为"default"。大小写不敏感。 |
| ZONE     | 区域名称   | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为必选参数。 参数含义：资源记录的区域名。 数据来源：全网规划 取值范围：1、区名称的输入格式要正确（例：xxx.com），同视图内区名称唯一（同一视图下的权威区的区名称均唯一），“@”表示根区。如果分段，每段不超过63个字符，并且整个区名称（填入的权威区名称）总长度不超过189个字符；如果不分段，最长不超过63个字符。该字符数是转化为符合DNS标准ASCII格式（Punycode编码）后的要求。 2、不支持连续的点、下划线（如".."、"__"）。 3、不支持“*”。 4、不支持以“.”开头和结尾。 5、区名中每段的内容支持以字母、数字、下划线、中横线的任意组合，但是不支持以中横线开头。 默认值：无 配置原则：大小写不敏感。                            |
| DOMAIN   | 域名     | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。 参数含义：资源记录的域名。 数据来源：全网规划 取值范围：1、域名如果分段，每段不超过63个字符，并且整个域名名称总长度（填入的域名+自动填充的“.”+填入权威区名称+标准域名结尾自动填充的“.”）不超过254个字符；如果不分段，填入的域名最长不超过63个字符。该字符数转化为符合DNS标准ASCII格式（Punycode编码）后的要求。 2、不支持连续的点（如".."）。 3、支持以*开头，但是*后必须用点分割（如“*.xx”） 4、域名中每段的内容支持以字母、数字、下划线、中横线的任意组合，但是不支持以中横线开头。 5、不支持以"."开头。 默认值：无 配置原则： 大小写不敏感。只输入“@”字符表示用同名与区域名称的域名。（CloudDNS当前不支持此功能）。   |
| START    | 起始记录号  | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。 参数含义：资源记录起始记录号。 数据来源：本端规划 取值范围：NA。 默认值：0 配置原则： 若没有没配置domain参数，则输出当前zone下type类型选中的从初始记录号开始的count个数的记录内容。若设置了domain参数，参数start不生效。                                                                                                                                                                                                                   |
| COUNT    | 记录个数   | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。 参数含义：记录个数。 数据来源：本端规划 取值范围：NA。 默认值：100 配置原则： 若没有没配置domain参数，则输出当前zone下type类型选中的从初始记录号开始的count个数的记录内容。若设置了domain参数，参数count不生效。                                                                                                                                                                                                                      |

#### 使用实例

- 显示多条A记录，参数“记录类型”选择为“A”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，不填写查询范围：

  ```
  LST RESREC: TYPE=A, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org";
  ```

  ```
  %%LST RESREC: TYPE=A, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org";%%
  RETCODE = 0    操作执行成功

      绝对域名                                             IP地址                         TTL

      test.apn.epc.mncxxx.mccyyy.3gppnetwork.org        10.161.251.123                     800
      test1.apn.epc.mncxxx.mccyyy.3gppnetwork.org       10.161.251.124                     NULL
      test2.apn.epc.mncxxx.mccyyy.3gppnetwork.org       10.161.251.126，10.161.251.127     800
   (结果个数 = 3)
  共有1个报告
  ---    END
  ```
- 显示一条AAAA记录，参数“记录类型”选择为“AAAA”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：

  ```
  LST RESREC: TYPE=AAAA, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```

  ```
  %%LST RESREC: TYPE=AAAA, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test ";%%
  RETCODE = 0    操作执行成功

    绝对域名  =  test.apn.epc.mncxxx.mccyyy.3gppnetwork.org 
       IP地址 =  2001:db8:85a3:8da:131b:8b2e:2590:6354 
          TTL =  800
  (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 显示一条NAPTR记录，参数“记录类型”选择为“NAPTR”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：

  ```
  LST RESREC: TYPE=NAPTR, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```

  ```
  %%LST RESREC: TYPE=NAPTR, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";%%
  RETCODE = 0    操作执行成功

        绝对域名 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
            顺序 = 10
            偏好 = 10
            标志 = S
            服务 = x-3gpp-sgw:x-s5-gtp:x-s8-gtp:x-gn
      正则表达式 = NULL
        替换域名 = test1.cmnet.mnc000.mcc460.gprs.
  TTL  = 1
   (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 显示一条SRV记录，参数“记录类型”选择为“SRV”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：

  ```
  LST RESREC: TYPE=SRV, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```

  ```
  %%LST RESREC: TYPE=SRV, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";%%
  RETCODE = 0    操作执行成功

   绝对域名 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
     优先级 = 10
       权重 = 10
     端口号 = 8080
       目标 = test1.cmnet.mnc000.mcc460.gprs
       TTL  = 1
   (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 显示一条NS记录，参数“记录类型”选择为“NS”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：

  ```
  LST RESREC: TYPE=NS, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```

  ```
  %%LST RESREC: TYPE=NS, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";%%
  RETCODE = 0    操作执行成功

       区域名称 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
     域名服务器 = test1.apn.epc.mncxxx.mccyyy.3gppnetwork.org.
           TTL  = 1
   (结果个数 = 1)
  共有1个报告
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                          |
|:--------|:---------------------------------------------------------------|
| 绝对域名    | 资源记录的绝对域名。                                                     |
| IP地址    | IP地址。                                                          |
| 优先级     | SRV记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“权重”值选择一条记录。   |
| 权重      | SRV记录的权重。当几条记录的“优先级”值相同时，客户端根据此参数值选择一条记录。                      |
| 端口号     | 用于SRV记录，服务器上提供该种服务的端口号。                                        |
| 目标      | 用于SRV记录，提供该种服务的服务器域名。                                          |
| 顺序      | NAPTR记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“偏爱”值选择一条记录。 |
| 偏好      | NAPTR记录的优先级。当查询结果为多条记录时，客户端选择优先级高的记录。当优先级相同时，客户端根据“偏爱”值选择一条记录。 |
| 标志      | 用于NAPTR记录，表示下一次查询的类型。                                          |
| 服务      | 用于NAPTR记录，新目标上的服务，以及该服务交互使用的协议。                                |
| 正则表达式   | NAPTR记录的正则表达式。                                                 |
| 替换域名    | NAPTR记录的替换域名。                                                  |
| 域名服务器   | NS记录的域名服务器参数。                                                  |
| TTL     | 非本域DNS保留授权域资源记录的时间，即资源记录的生存周期。                                 |
| 区域名称    | 资源记录的区域名。                                                      |