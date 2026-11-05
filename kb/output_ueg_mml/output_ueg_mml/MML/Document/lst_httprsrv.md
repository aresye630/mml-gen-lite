# 查询远端服务器配置(LST HTTPRSRV)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询远端服务器配置。

- 若需要查询所有远端服务器配置，请不输入任何参数。
- 若需要查询某个远端服务器配置，请输入“远端服务器名称”。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                     |
|:------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| RSERVERNAME | 远端服务器名称 | 可选必选说明：可选参数 参数含义：用于指示系统按照远端服务器名称标识来查询远端服务器配置信息；若不输入，则表示查询所有远端服务器配置信息。 取值范围：长度不超过128的由数字和字母组成的字符串，只允许输入0～9，a～z，A～Z，“-”和“_” 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有的远端服务器配置：

   ```
   LST HTTPRSRV:;
   ```

   ```
   %%LST HTTPRSRV:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   远端服务器名称  链路类型  远端服务器组名  本端IP名称  对端IP地址类型  对端IPv4地址  对端IPv6地址  对端端口号  开启HTTPS  证书应用场景     TLS配置ID  链路集参数ID  PING帧发送周期  动态链路开启HTTPS  是否在URI中使用FQDN  远端服务器域名       URI前缀

   aa              动态      NULL            HLB         NULL            NULL          NULL          NULL        NULL       NULL             NULL       1             NULL            BYURI              NULL                 test.huawei.com      a111
   aaa             静态      NULL            HLB         IPV4            10.0.0.2      NULL          80          TRUE       HLB证书应用场景  1          1             0               NULL               NULL                 test01.huawei.com    a222
   abc             动态      NULL            HLB         NULL            NULL          NULL          NULL        NULL       NULL             NULL       1             NULL            BYURI              NULL                 test02.huawei.com    a123

   (结果个数 = 3)

   ---    END
   ```
2. 查询指定远端服务器名称的远端服务器配置：

   ```
   LST HTTPRSRV:RSERVERNAME="abc";
   ```

   ```
   %%LST HTTPRSRV:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
        远端服务器名称  =  abc
              链路类型  =  动态
        远端服务器组名  =  NULL
            本端IP名称  =  HLB
        对端IP地址类型  =  NULL
          对端IPv4地址  =  NULL
          对端IPv6地址  =  NULL
            对端端口号  =  NULL
             开启HTTPS  =  NULL
          证书应用场景  =  NULL
             TLS配置ID  =  NULL
          链路集参数ID  =  1
        PING帧发送周期  =  NULL
     动态链路开启HTTPS  =  BYURI
   是否在URI中使用FQDN  =  NULL
        远端服务器域名  =  test02.huawei.com
               URI前缀  =  a123
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD HTTPRSRV**命令的参数说明。