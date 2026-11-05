# 查询全局Diameter域（LST GLBDIAMREALM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询已配置的全局Diameter域与IMSI/MSISDN号段和应用类型的绑定关系。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                                                       |
|:------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| APPLICATION | Diameter应用      | 可选必选说明：可选参数 参数含义：该参数用于指定全局Diameter域所属的Diameter应用。 数据来源：全网规划 取值范围：枚举类型。 GY：Gy接口应用。GX：Gx接口应用。S6B：S6b接口应用。 默认值：无 配置原则：根据实际需要查询的应用类型选择对应的应用参数。 |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数 参数含义：该参数用于指定要与Diameter域绑定的IMSI/MSISDN号段的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                        |

#### 使用实例

- 查询全局Diameter域与Gx应用的绑定关系：

  ```
  LST GLBDIAMREALM: APPLICATION=GX;
  ```

  ```
  RETCODE = 0  操作成功

  全局Diameter域名
  ----------------
                    Diameter应用  =  Gx
             IMSI/MSISDN号段名称  =  imsi_msisdn_segment_1
                          优先级  =  101
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  pcrf.huawei.com
  Supported-Features动态协商开关  =  不使能
   Supported-Feature AVP携带开关  =  使能
                     Feature列表  =  3GPP Rel-8 Gx功能&3GPP Rel-9 Gx功能
  (结果个数 = 1)

  ---    END
  ```
- 查询所有全局Diameter域的绑定关系：

  ```
  LST GLBDIAMREALM:;
  ```

  ```
  RETCODE = 0  操作成功

  全局Diameter域名
  ----------------
                    Diameter应用  =  Gx
             IMSI/MSISDN号段名称  =  imsi_msisdn_segment_1
                          优先级  =  101
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  pcrf.huawei.com
  Supported-Features动态协商开关  =  不使能
   Supported-Feature AVP携带开关  =  使能
                     Feature列表  =  3GPP Rel-8 Gx功能&3GPP Rel-9 Gx功能
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

参见ADD GLBDIAMREALM的参数说明。