# 查询MEP HTTP客户端（LST MEPHTTPCLIENT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查询MEP HTTP客户端。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称          | 参数说明                                                                                                                   |
|:-----------|:--------------|:-----------------------------------------------------------------------------------------------------------------------|
| CLIENTNAME | MEP HTTP客户端名称 | 可选必选说明：可选参数 参数含义：该参数用于指定MEP HTTP客户端名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：无 |

#### 使用实例

- 查询全部的MEPHTTPCLIENT对象：

  ```
  LST MEPHTTPCLIENT:;
  ```

  ```
  RETCODE = 0  操作成功

  MEP HTTP客户端
  --------------
  MEP HTTP客户端名称  MEP HTTP客户端组  MEP HTTP客户端类型    IPv4地址     IPv6地址  是否启用TLS  TLS参数名称  HTTP客户端通信参数名称  对端服务标签  

  client              clientgrp         连接外部网元的客户端  192.168.1.1  ::        使能         tls          DefaultClientPara       MEP服务       
  client001           clientgrp         连接内部服务的客户端  0.0.0.0      ::        不使能       NULL         DefaultClientPara       MP1接口服务   
  (结果个数 = 2)

  ---    END
  ```
- 查询MEPHTTPCLIENT对象，查询的MEPHTTPCLIENT对象名称为"client"：

  ```
  LST MEPHTTPCLIENT: CLIENTNAME="client";
  ```

  ```
  RETCODE = 0  操作成功

  MEP HTTP客户端
  --------------
      MEP HTTP客户端名称  =  client
        MEP HTTP客户端组  =  clientgrp
      MEP HTTP客户端类型  =  连接外部网元的客户端
                IPv4地址  =  192.168.1.1
                IPv6地址  =  ::
             是否启用TLS  =  使能
             TLS参数名称  =  tls
  HTTP客户端通信参数名称  =  DefaultClientPara
            对端服务标签  =  MEP服务
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

参见ADD MEPHTTPCLIENT的参数说明。