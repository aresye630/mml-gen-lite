# 查询默认协议组（LST DFTPROTGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询默认协议组。当运营商希望检索默认协议组设置，以便灵活配置自定义协议和规则等配置项，则执行该命令。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                      |
|:--------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------|
| PROTQRYOPTYPE | 协议查询操作类型 | 可选必选说明：必选参数 参数含义：该参数用于指定协议查询操作类型。 数据来源：本端规划 取值范围：枚举类型。 SPECIFIC：查询指定默认协议组。ALL：查询所有默认协议组。NAME：查询所有默认协议组名称。 默认值：无 配置原则：无                    |
| PROTGROUPNAME | 协议组名称    | 可选必选说明：条件必选参数 前提条件：该参数在“PROTQRYOPTYPE”配置为“SPECIFIC”时为必选参数。 参数含义：该参数用于指定协议组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 假如运营商需要查询默认协议组“database”的详细设置：

  ```
  LST DFTPROTGRP:PROTQRYOPTYPE=SPECIFIC,PROTGROUPNAME="database";
  ```

  ```
  RETCODE = 0  操作成功。

  默认协议组信息
  --------------
  协议组名称    协议名称       子协议名称 

  database      cddb           cddb       
  database      ldap           ldap       
  database      mysql          mysql      
  database      postgresql     postgresql 
  database      sparebackup    sparebackup
  database      sql_server     sql_server 
  database      tds            tds        
  database      tns            tns        
  (结果个数 = 8)
  ---    END
  ```
- 假如运营商需要查看所有默认协议组：

  ```
  LST DFTPROTGRP:PROTQRYOPTYPE=NAME;
  ```

  ```
  RETCODE = 0  操作成功。

  默认协议组信息
  --------------
  协议组名称            

  database              
  email                 
  file_access           
  game                  
  im                    
  mobile                
  network_administration
  network_storage       
  others                
  p2p                   
  remote_connectivity   
  stock                 
  streaming             
  tunneling             
  voip                  
  web_browsing          
  (结果个数 = 16)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释         |
|:--------|:--------------|
| 子协议名称   | 协议组包含的子协议的名字。 |

其余输出项请参见ADD PROTOCOLGROUP的参数说明。