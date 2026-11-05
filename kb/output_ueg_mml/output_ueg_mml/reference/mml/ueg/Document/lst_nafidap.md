# 查询网络应用功能AP列表数据(LST NAFIDAP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询BSF上配置的AP的FQDN与AP域名或AP IP地址的映射关系信息：

- 若需要查询某个AP的FQDN与AP域名或AP IP地址的映射关系数据，请输入“FQDN”参数。
- 若需要查询全部AP的FQDN与AP域名或AP IP地址的映射关系数据，请不要输入任何参数。

  **说明** 

  该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                         |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------|
| FQDN   | FQDN   | 用于指示系统需要按照哪个全量域名来查询AP的FQDN与AP域名或AP IP地址的映射关系信息。 需要指出的是，该参数不区分大小写，在执行本命令查询出的报文中为全小写形式。 取值范围：长度不超过127的字符串。 默认值：无。 注意：该参数为可选参数。 |

## 使用实例

1. 查询全部AP的FQDN与AP IP地址的映射关系数据：

   ```
   LST NAFIDAP:;
   ```

   返回结果如下：

   ```
   %%LST NAFIDAP:;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
    FQDN             域名         IP地址类型  NAF IPv4地址   NAF IPv6地址

    bsf.huawei.com   huawei1.com  NULL        NULL           NULL        
    bsf1.huawei.com  NULL         IPV4        192.168.10.11  NULL        
   (结果个数 = 2)

   ---    END
   ```
2. 查询某个AP的FQDN与AP域名的映射关系数据，“FQDN”为“bsf.huawei.com”：

   ```
   LST NAFIDAP: FQDN="bsf.huawei.com";
   ```

   返回结果如下：

   ```
   %%LST NAFIDAP: FQDN="bsf.huawei.com";%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
           FQDN  =  bsf.huawei.com
           域名  =  huawei1.com
     IP地址类型  =  NULL
   NAF IPv4地址  =  NULL
   NAF IPv6地址  =  NULL
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

请参见**ADD NAFIDAP**命令的参数说明。