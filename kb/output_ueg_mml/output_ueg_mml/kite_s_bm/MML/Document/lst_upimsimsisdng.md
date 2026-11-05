# 查询IMSI和MSISDN号段组（LST UPIMSIMSISDNG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来显示本地所有已配置的IMSI/MSISDN号码段组信息，或者根据号码段组的名称来显示指定IMSI/MSISDN号码段组的配置信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称             | 参数说明                                                                                                   |
|:-------------|:-----------------|:-------------------------------------------------------------------------------------------------------|
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI/MSISDN号码段组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 查询IMSI/MSISDN号码段组信息，其中IMSI/MSISDN号段组名称为huawei：

  ```
  LST UPIMSIMSISDNG: SEGGROUPNAME="huawei";
  ```

  ```
  RETCODE = 0  操作成功。

  IMSI或MSISDN号段组信息
  ----------------------
  IMSI/MSISDN号段组名称  =  huawei
    IMSI/MSISDN号段名称  =  imsi
             配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有IMSI/MSISDN号码段组信息：

  ```
  LST UPIMSIMSISDNG:;
  ```

  ```
  RETCODE = 0  操作成功。

  IMSI或MSISDN号段组信息
  ----------------------
  IMSI/MSISDN号段组名称    IMSI/MSISDN号段名称    配置域名称

  huawei                   imsi                   NULL
  huawei                   imsi01                 NULL
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD UPIMSIMSISDNG的参数说明。