# 查询号段组(LST NUMGROUP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询号段组的配置信息：

- 若需要查询所有号段组的配置信息，无需输入参数。
- 若需要查询某个号段组的配置信息，请输入“号段组ID”。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                          |
|:--------|:-------|:----------------------------------------------|
| GROUPID | 号段组ID  | 用于指示系统按照哪个号段组ID来查询号段组前缀信息数据；若不输入，则表示所有的号段组ID。 |

## 使用实例

1. 查询号段组信息。

   ```
   LST NUMGROUP:;
   ```

   ```
   %%LST NUMGROUP:;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  GROUPID      GROUPNAME
                  1            numgroup1
                  2            numgroup2

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询号段组信息，“号段组ID”为“1”：

   ```
   LST NUMGROUP: GROUPID=1;
   ```

   ```
   %%LST NUMGROUP: GROUPID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

   "IMSI"
                  PREFIX          LENGTH
                  410             11

   "MSISDN"
                  PREFIX          LENGTH
                  139             0

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NUMGROUP**命令的参数说明。