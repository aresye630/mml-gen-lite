# 查询HLB链路话统对象实例(LST UDMHTTPLNKMOI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UdmHttpService和UdmTcpService服务链路负荷统计对象实例。

- 若要查询所有UdmHttpService和UdmTcpService服务链路负荷统计对象实例，请不要输入任何参数。
- 若要查询UdmHttpService或者UdmTcpService服务链路负荷统计对象实例，请输入“服务名称”参数。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                  |
|:-----------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------|
| SERVERNAME | 服务名称   | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个服务名称查询对应服务链路负荷统计对象实例；若不输入，则表示查询所有UdmHttpService和UdmTcpService服务链路负荷统计对象实例。 取值范围：长度不超过36位的字符串。 默认值：无 配置原则：无 |

## 使用实例

1. 查询所有UdmHttpService和UdmTcpService服务链路负荷统计对象实例：

   ```
   LST UDMHTTPLNKMOI:;
   ```

   ```
   %%LST UDMHTTPLNKMOI:;%%
   RETCODE = 0  操作成功

   服务实例ID            服务名称        

   13337016847928967364  UdmTcpService   
   13338691880879434137  UdmHttpService  
   13338691880879441936  UdmHttpService  
   (结果个数 = 3)

   ---    END
   ```
2. 查询所有UdmHttpService服务链路负荷统计对象实例：

   ```
   LST UDMHTTPLNKMOI: SERVERNAME="UdmTcpService";
   ```

   ```
   %%LST UDMHTTPLNKMOI: SERVERNAME="UdmTcpService";%%
   RETCODE = 0  操作成功

   服务实例ID  =  13337016847928967364
     服务名称  =  UdmTcpService
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**RMV UDMHTTPLNKMOI**命令的参数说明。