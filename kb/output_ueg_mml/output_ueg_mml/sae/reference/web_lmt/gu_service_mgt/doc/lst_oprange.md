# 查询操作员号段权限(LST OPRANGE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询操作员号段权限的配置信息：

- 若需要查询所有操作员号段权限的配置信息，无需输入参数。
- 若需要查询某个操作员号段权限的配置信息，请输入“操作员名称”。

## 注意事项

操作员的级别为ADMINISTRATOR或操作员被赋给该命令权限时，才具有查询号段的权限。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                         |
|:-------|:-------|:-----------------------------|
| OPNAME | 操作员名称  | 用于指示系统按照哪个操作员名称来查询号段组前缀信息数据。 |

## 使用实例

1. 查询操作员号段权限。

   ```
   LST OPRANGE:;
   ```

   ```
   %%LST OPRANGE:;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  OPNAME       GROUPTYPE
                  opr1         BOTH
                  opr2         MSISDN

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询操作员号段权限，“操作员名称”为“opr1”：

   ```
   LST OPRANGE: OPNAME="opr1";
   ```

   ```
   %%LST OPRANGE: OPNAME="opr1";%%
   RETCODE = 0 SUCCESS0001:操作成功

                           OPNAME = opr1
                        GROUPTYPE = BOTH
                          GROUPID = 1

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD OPRANGE**命令的参数说明。