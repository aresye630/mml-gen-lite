# 查询SOAP客户端IP地址(LST SOAPNAFIP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于查询系统中SOAP客户端IP地址的配置信息，使操作员了解当前UIM网元内配置的SOAP客户端IP地址配置信息：

- 若需要查询全部SOAP客户端的IP地址配置信息，请不要输入任何参数。
- 若需要查询某条SOAP客户端的IP地址配置信息，请输入参数“ID”。

  **说明** 

  该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                              |
|:-------|:-------|:--------------------------------------------------|
| ID     | ID     | 用于指示系统中需要按照哪个ID来查询IP地址配置信息；若不输入，则表示查询全部的IP地址配置信息。 |

## 使用实例

1. 查询一个具体ID对应的SOAPIP地址的配置信息，“ID”为“1”：

   ```
   LST SOAPNAFIP: ID=1;
   ```

   返回结果如下：

   ```
   %%LST SOAPNAFIP: ID=1;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
             ID  =  1
     IP地址类型  =  IPV6
       IPv4网段  =  NULL
   IPv4子网掩码  =  NULL
       IPv6网段  =  2001:DB8:1:0:0:0:0:0
   IPv6前缀长度  =  11
         IP描述  =  soap client ip1
   (结果个数 = 1)

   ---    END
   ```
2. 查询所有SOAPIP地址的配置信息：

   ```
   LST SOAPNAFIP:;
   ```

   返回结果如下：

   ```
   %%LST SOAPNAFIP:;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
    ID      IP地址类型  IPv4网段  IPv4子网掩码  IPv6网段              IPv6前缀长度  IP描述         

    1       IPV6        NULL      NULL          2001:DB8:1:0:0:0:0:0  11            soap client ip1
    2       IPV6        NULL      NULL          2001:DB8:1:0:0:0:0:0  12            soap client ip2
   (结果个数 = 2)

   ---    END
   ```