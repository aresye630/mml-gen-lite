# 查询APN L2TP配置（LST APNL2TPATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询APN的L2TP相关信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                           |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------|
| APN    | APN名称  | 可选必选说明：可选参数 参数含义：指定APN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 假设用户要查询所有APN下配置的L2TP相关信息：

  ```
  LST APNL2TPATTR:;
  ```

  ```
  APN的L2TP配置信息
  -----------------
  APN名称        APN支持L2TP功能    L2TP组号    RADIUS服务器返回多LNS的工作模式    ICRQ携带Calling-number AVP值    ICCN携带鉴权信元开关    发起IPCP协商开关    ICCN携带PrivateGroupId AVP开关    ICCN携带TxConnectSpeed值    ICRQ携带Bearer Type AVP开关    MSISND作为ICCN代理认证用户名    域名位置      增加或剥离域名    ICCN 携带LCP CONFREQ信元开关ICCN    l2tp支持ipv6功能开关

  apnname1       不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  apntest        不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  huawei.com     不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  huawei.com1    不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  huawei.com2        不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  example           不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  example.com       不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  example.sww       不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  example.sww2      不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  example.sww3      不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  example.sww5      不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  exampleapn        不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  exampleapn1       不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能    使能                              不使能
  ysdf           不使能             NULL        主备                               MSISDN                          不使能                  不使能              使能                              不使能                      使能                           不使能                          NULL    不支持增加或剥离域名功能       使能                              不使能
  (结果个数 = 14)
  ---    END
  ```
- 假设用户要查询APN “huawei.com”下配置的L2TP相关信息：

  ```
  LST APNL2TPATTR:APN="huawei.com";
  ```

  ```
  RETCODE = 0  操作成功。

  APN的L2TP配置信息
  -----------------
                          APN名称  =  huawei.com
                  APN支持L2TP功能  =  不使能
                         L2TP组号  =  NULL
  RADIUS服务器返回多LNS的工作模式  =  主备
     ICRQ携带Calling-number AVP值  =  MSISDN
             ICCN携带鉴权信元开关  =  不使能
                 发起IPCP协商开关  =  不使能
   ICCN携带PrivateGroupId AVP开关  =  使能
         ICCN携带TxConnectSpeed值  =  不使能
      ICRQ携带Bearer Type AVP开关  =  使能
     ICCN 携带LCP CONFREQ信元开关  =  使能
                         域名位置  =  NULL
                   增加或剥离域名  =  不支持增加或剥离域名功能
     ICCN 携带LCP CONFREQ信元开关  =  使能
             l2tp支持ipv6功能开关  =  不使能
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

参见SET APNL2TPATTR的参数说明。