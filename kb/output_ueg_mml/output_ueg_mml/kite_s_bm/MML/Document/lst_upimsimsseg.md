# 查询IMSI和MSISDN号段（LST UPIMSIMSSEG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询IMSI/MSISDN号码段。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                 |
|:------------|:----------------|:-----------------------------------------------------------------------------------------------------|
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI/MSISDN号段名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 查询IMSI和MSISDN号段：

  ```
  LST UPIMSIMSSEG:;
  ```

  ```
  RETCODE = 0  操作成功。

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称  =  imsi
  IMSI/MSISDN号段类型  =  IMSI
       号段起始字符串  =  1
       号段结束字符串  =  2
           配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有IMSI和MSISDN号段：

  ```
  LST UPIMSIMSSEG:;
  ```

  ```
  RETCODE = 0  操作成功。

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称    IMSI/MSISDN号段类型    号段起始字符串    号段结束字符串    配置域名称

  huawei                 IMSI                   130               139               NULL      
  huawei1                IMSI                   130               139               NULL      
  imsi                   IMSI                   1                 2                 NULL           
  (结果个数 = 3)
  ---    END
  ```

#### 输出结果说明

参见ADD UPIMSIMSSEG的参数说明。