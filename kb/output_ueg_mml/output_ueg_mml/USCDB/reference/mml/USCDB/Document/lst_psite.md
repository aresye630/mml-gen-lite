# 查询远端营帐配置(LST PSITE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询远端业务发放站点的配置信息。

- 若需要查询全部远端业务发放站点的概要信息，请不要输入任何参数。
- 若需要查询某个远端业务发放站点数据记录的详细信息，请输入“Site ID”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                 |
|:------------|:--------------|:---------------------------------------------------------------------|
| SITEID      | Site ID       | 用于指示系统需要按照哪个站点ID来查询远端业务发放站点数据；若不输入，则表示查询所有的远端业务发放站点的数据。              |
| SRVSCENARIO | 业务场景          | 用于指示系统需要按照哪种业务场景来查询远端业务发放站点数据；若不输入，则表示查询所有的业务场景。                     |
| INTERFACE   | 接口类型          | 用于指示系统需要按照哪种接口类型来查询远端业务发放站点数据；若不输入，则表示查询所有的接口类型。                     |
| SITEAPPTYPE | 远端provision类型 | 用于指示系统需要按照哪个远端业务发放站点类型来查询远端业务发放站点数据；若不输入，则表示查询所有的远端业务发放类型的数据。        |
| HTTPS       | 是否使用HTTPS     | 用于指示系统需要按照“使用HTTPS”还是“不使用HTTPS”来查询远端业务发放站点数据；若不输入，则表示查询所有远端业务发放站点数据。 |

## 使用实例

1. 查询全部远端业务发放站点的概要信息：

   ```
   LST PSITE:;
   ```

   ```
   %%LST PSITE:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    Site ID  业务场景     接口类型     IP类型    远端provision IPV4       远端provision IPV6  本端IPV4       本端IPV6      远端provision端口      本端provision端口    远端provision类型      连接数系统     远端Partition ID  远端站点优先级  远端站点Location ID HLR序列号   HLR序列号     操作员     密码      是否使用HTTPS   描述         

    1        本地维护     MML接口      IPV4      10.53.6.78               NULL                10.53.6.79     NULL          7776                   0                    SUP-FE                 1              1                 1               NULL                8           0             admin      *****     NO              NULL         
    2        业务发放     SOAP接口     IPV4      192.168.9.10             NULL                192.168.9.11   NULL          8001                   0                    SUP-FE                 1              1                 2               NULL                1           1             admin      *****     NO              Huawei HLR1  
   (结果个数 = 2)
   ---    END
   ```
2. 查询“Site ID”为“2”的远端业务站点的详细信息：

   ```
   LST PSITE: SITEID=2;
   ```

   ```
   %%LST PSITE: SITEID=2;%%
   RETCODE = 0  操作成功

   操作结果如下
   --------------
                  Site ID  =  2
                 业务场景  =  业务发放
                 接口类型  =  SOAP接口
                   IP类型  =  IPV4
       远端provision IPV4  =  192.168.9.10
       远端provision IPV6  =  MULL
                 本端IPV4  =  192.168.9.11
                 本端IPV6  =  MULL
        远端provision端口  =  8001
        本端provision端口  =  0
        远端provision类型  =  SUP-FE
                   连接数  =  1
         远端Partition ID  =  1
           远端站点优先级  =  2
      远端站点Location ID  =  NULL
            系统HLR序列号  =  1
                HLR序列号  =  1
                   操作员  =  admin
                     密码  =  *****
            是否使用HTTPS  =  NO
                     描述  =  Huawei HLR1
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD PSITE**命令的参数说明。