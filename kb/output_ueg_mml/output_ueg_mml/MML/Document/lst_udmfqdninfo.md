# 查询FQDN信息（LST UDMFQDNINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询FQDN信息：

- 当需要查询某一FQDN域名对应的所有IP地址对应关系时，请输入“FQDN名称”参数进行查询。
- 当需要查询所有FQDN域名及其对应IP地址关系时，请不需要输入任何参数，直接查询即可。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                  |
|:-------|:-------|:------------------------------------------------------------------------------------------------------|
| NAME   | FQDN名称 | 可选必选说明：可选参数。 参数含义：用于指示系统按照哪个FQDN名称来查询FQDN信息数据；若不输入，则表示查询所有的FQDN名称。 取值范围：长度不超过255位的字符串。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询“FQDN名称”为“udm1.huawei.com”的所有对应IP地址。

   ```
   LST UDMFQDNINFO: NAME="udm1.huawei.com";
   ```

   ```
   %%LST UDMFQDNINFO: NAME="udm1.huawei.com";%% 
   操作结果如下: 
   ------------- 
   FQDN名称                IP地址                   备注  
   udm1.huawei.com         192.168.13.67            huawei
   udm1.huawei.com         192.168.14.67            huawei

   (结果个数 = 2)  
   ---    END
   ```
2. 查询所有FQDN信息。

   ```
   LST UDMFQDNINFO:;
   ```

   ```
   %%LST UDMFQDNINFO:;%% 
   RETCODE = 0 操作成功
   操作结果如下: 
   ------------- 
   FQDN名称                IP地址                    备注  
   udm1.huawei.com         192.168.13.67             huawei
   udm1.huawei.com         192.168.14.67             huawei
   udm2.huawei.com         192.168.15.67             huawei

   (结果个数 = 3)   
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD UDMFQDNINFO**命令的参数说明。