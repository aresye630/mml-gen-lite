# 查询MEP HTTP服务端（LST MEPHTTPSERVER）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查询MEP HTTP服务端。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称          | 参数说明                                                                                                                   |
|:-----------|:--------------|:-----------------------------------------------------------------------------------------------------------------------|
| SERVERNAME | MEP HTTP服务端名称 | 可选必选说明：可选参数 参数含义：该参数用于指定MEP HTTP服务端名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：无 |

#### 使用实例

- 查询全部的MEPHTTPSERVER对象：

  ```
  LST MEPHTTPSERVER:;
  ```

  ```
  RETCODE = 0  操作成功

  MEP HTTP 服务端
  ---------------
  MEP HTTP服务端名称  MEP HTTP服务端组  MEP HTTP服务端类型          IPv4地址     IPv6地址  端口号  是否启用TLS  TLS参数名称  HTTP服务端通信参数名称  

  server              servergrp         对外部网元提供的服务        192.168.1.1  ::        8443    使能         tls          DefaultServerPara       
  server1             servergrp         转发内部策略下发请求的服务  0.0.0.0      ::        0       使能         tls          DefaultServerPara       
  (结果个数 = 2)

  ---    END
  ```
- 查询MEPHTTPSERVER对象，查询的MEPHTTPSERVER对象名称为"server"：

  ```
  LST MEPHTTPSERVER: SERVERNAME="server";
  ```

  ```
  RETCODE = 0  操作成功

  MEP HTTP 服务端
  ---------------
      MEP HTTP服务端名称  =  server
        MEP HTTP服务端组  =  servergrp
      MEP HTTP服务端类型  =  对外部网元提供的服务
                IPv4地址  =  192.168.1.1
                IPv6地址  =  ::
                  端口号  =  8443
             是否启用TLS  =  使能
             TLS参数名称  =  tls
  HTTP服务端通信参数名称  =  DefaultServerPara
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

参见ADD MEPHTTPSERVER的参数说明。