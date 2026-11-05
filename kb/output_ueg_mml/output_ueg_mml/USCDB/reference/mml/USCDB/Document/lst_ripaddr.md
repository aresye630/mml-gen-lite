# 查询远端网元IP地址(LST RIPADDR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询远端网元IP地址：

- 若需要查询全部远端网元IP地址的概要信息，请不要输入任何参数。
- 若需要查询某条远端网元IP地址的详细信息，请输入“远端Location标识”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称               | 参数说明                                                                                                                                                                                             |
|:--------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RLOCID  | 远端Location标识       | 用于指示系统需要按照哪个远端Location来查询远端网元IP地址信息；若不输入，则表示查询所有Location的远端网元IP地址信息。                                                                                                                             |
| ID      | 远端DPU模块号/远端业务IP索引  | 用于指示系统需要按照哪个远端DPU模块号/远端业务IP索引来查询远端网元IP地址信息；若不输入，则表示查询所有远端DPU模块号/远端业务IP索引对应的远端网元IP地址信息。                                                                                                           |
| IPVER   | IP类型               | 用于指示系统需要按照哪个IP类型来查询远端网元IP地址信息；若不输入，则表示查询所有IP类型所对应的远端网元IP地址信息。                                                                                                                                    |
| IPV4IP1 | 远端Location IPV4地址1 | 用于指示系统需要按照哪个远端Location IP地址来查询远端网元IP地址；若不输入，则表示查询所有远端Location IP地址对应的远端网元IP地址信息。                                                                                                                 |
| IPV6IP1 | 远端Location IPV6地址1 | 用于指示系统需要按照哪个远端Location IP地址来查询远端网元IP地址；若不输入，则表示查询所有远端Location IP地址对应的远端网元IP地址信息。 当参数“IP类型”设置为“IPV6(IPV6)”时，该参数有效，格式为“xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”，例如：2001:DB8:8432:4098:4782:5784::。 |
| IPV4IP2 | 远端Location IPV4地址2 | 用于指示系统需要按照哪个远端Location IP地址来查询远端网元IP地址；若不输入，则表示查询所有远端Location IP地址对应的远端网元IP地址信息。                                                                                                                 |
| IPV6IP2 | 远端Location IPV6地址2 | 用于指示系统需要按照哪个远端Location IP地址来查询远端网元IP地址；若不输入，则表示查询所有远端Location IP地址对应的远端网元IP地址信息。 当参数“IP类型”设置为“IPV6(IPV6)”时，该参数有效，格式为“xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”，例如：2001:DB8:8432:4098:4782:5784::。 |
| RDPUST  | 远端IP地址业务类型         | 用于指示系统需要按照哪个远端IP地址的业务类型来查询远端网元IP地址，此参数在USCDB下唯一，通过LOD FEPLUG命令加载FE插件后在此引用。                                                                                                                       |

## 使用实例

1. 查询所有远端网元IP地址：

   ```
   LST RIPADDR:;
   ```

   ```
   %%LST RIPADDR:;%%
   RETCODE = 0  操作成功

    远端Location标识  远端DPU模块号/远端业务IP索引   IP类型  远端Location IPV4地址1  远端Location IPV6地址1  远端Location IPV4地址2  远端Location IPV6地址2  远端IP地址业务类型

    10                11                             IPV4    192.168.21.150          NULL                    192.168.21.151          NULL                    SUP-FE         
    11                11                             IPV4    192.168.21.152          NULL                    192.168.21.153          NULL                    SUP-FE
   ```
2. 查询指定远端IP地址业务类型的远端网元IP地址，“远端IP地址业务类型”为“SUP-FE”：

   ```
   LST RIPADDR: RDPUST="SUP-FE";
   ```

   ```
   %%LST RIPADDR: RDPUST="SUP-FE";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
                远端Location标识  =  11
    远端DPU模块号/远端业务IP索引  =  11
                          IP类型  =  IPV4
          远端Location IPV4地址1  =  192.168.21.152
          远端Location IPV6地址1  =  NULL
          远端Location IPV4地址2  =  192.168.21.153
          远端Location IPV6地址2  =  NULL
              远端IP地址业务类型  =  SUP-FE
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD RIPADDR**命令的参数说明。