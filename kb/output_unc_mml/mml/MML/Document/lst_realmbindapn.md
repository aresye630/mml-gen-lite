# 查询APN与Diameter Realm关联关系（LST REALMBINDAPN）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter域与APN的绑定关系。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                           |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------|
| APN    | APN名称  | 可选必选说明：必选参数 参数含义：该参数用于指定要与Diameter域绑定的APN实例名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：根据实际需要查询的APN实例输入对应参数。 |

#### 使用实例

- 查询APN isp与Diameter域的绑定关系：

  ```
  LST REALMBINDAPN: APN="isp";
  ```

  ```
  RETCODE = 0  操作成功

  APN与Diameter Realm关联关系
  ---------------------------
                         APN名称  =  isp
                    Diameter应用  =  Gx应用
     根据IMSI构造归属地Realm开关  =  使能
                         Realm名  =  NULL
  Supported-Features动态协商开关  =  不使能
                     Feature列表  =  3GPP Rel-8 Gx功能&3GPP Rel-9 Gx功能
   Supported-Feature AVP携带开关  =  使能
  (结果个数 = 1)

  ---    END
  ```
- 查询APN newisp与Diameter域的绑定关系：

  ```
  LST REALMBINDAPN: APN="newisp";
  ```

  ```
  RETCODE = 0 操作成功。

  APN与Diameter Realm关联关系
  ---------------------------
  APN名称 Diameter应用 根据IMSI构造归属地Realm开关 Realm名 Supported-Features动态协商开关 Feature列表

  newisp Gy应用 不使能 ocs.huawei.com 不使能 NULL
  newisp Gx应用 使能 NULL 使能 3GPP Rel-8 Gx功能 & 3GPP Rel-9 Gx功能
  (结果个数 = 2)
  --- END
  ```

#### 输出结果说明

参见ADD REALMBINDAPN的参数说明。