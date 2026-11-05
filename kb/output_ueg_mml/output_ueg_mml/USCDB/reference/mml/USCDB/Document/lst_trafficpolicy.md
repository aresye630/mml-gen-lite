# 查询流量策略(LST TRAFFICPOLICY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询流量策略。

- 若需要查询全部流量策略信息，请不要输入任何参数。
- 若需要查询某条流量策略信息，请输入“接入类型”或其它参数或这些参数的组合。

  **说明** 

  该命令在当前版本暂不支持。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                           |
|:-------------|:-------|:-----------------------------------------------|
| ACCESSTYPE   | 接入类型   | 用于指示系统按照哪个接入类型来查询流量策略数据；若不输入，则表示所有的接入类型。       |
| LDAPUSER     | LDAP用户 | 用于指示系统按照哪个LDAP用户名称来查询流量策略数据；若不输入，则表示所有的LDAP用户。 |
| FETYPENAME   | FE类型名称 | 用于指示系统按照哪个FE类型来查询流量策略数据；若不输入，则表示所有的FE类型。       |
| TRAFFICVALUE | 流量值    | 用于指示系统按照哪个流量配置值来查询流量策略数据；若不输入，则表示所有流量策略配置值。    |

## 使用实例

1. 查询所有流量策略。

   `LST TRAFFICPOLICY:;`

   ```
   %%LST TRAFFICPOLICY:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    接入类型  LDAP用户  FE类型名称  流量值

    LDAP      ldap_u1   NULL        100   
    DCI       NULL      SUP-FE      100   
   (结果个数 = 2)

   ---    END
   ```
2. 查询LDAP用户流量策略，“接入类型”为“LDAP”。

   `LST TRAFFICPOLICY: ACCESSTYPE=LDAP;`

   ```
   %%LST TRAFFICPOLICY: ACCESSTYPE=LDAP;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
     接入类型  =  LDAP
     LDAP用户  =  ldap_u1
   FE类型名称  =  NULL
       流量值  =  100
   (结果个数 = 1)

   ---    END
   ```
3. 查询DCI用户流量策略，“接入类型”为“DCI”。

   `LST TRAFFICPOLICY: ACCESSTYPE=DCI;`

   ```
   %%LST TRAFFICPOLICY: ACCESSTYPE=DCI;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
     接入类型  =  DCI
     LDAP用户  =  NULL
   FE类型名称  =  SUP-FE
       流量值  =  100
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**ADD TRAFFICPOLICY**命令的参数说明。