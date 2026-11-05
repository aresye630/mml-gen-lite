# 查询系统HLR（LST SYSHLRSN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已经添加的系统HLR。

- 若需要查询全部系统HLR的概要信息，请不要任何输入参数。
- 若需要查询某条系统HLR的详细信息，请输入“系统HLR序列号”。

## 注意事项

ADMINISTRATOR级别的操作员或被赋给该命令权限的操作员具有本命令的操作权限。

## 参数说明

| 参数标识     | 参数名称     | 参数说明                                     |
|:---------|:---------|:-----------------------------------------|
| SYSHLRSN | 系统HLR序列号 | 用于指示系统需要按照哪个系统HLR来查询信息；若不输入，则表示所有的系统HLR。 |

## 使用实例

1. 查询所有的系统HLR：

   ```
   LST SYSHLRSN:;
   ```

   ```
   %%LST SYSHLRSN:;%%
   RETCODE = 0 操作成功

           "System HLRSN"    "HLR Status"    "HLR Name"                                   
           1                 MASTER          syshlrsn1  
           2                 ACTIVE          syshlrsn2
           3                 INACTIVE        syshlrsn3

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询HLR序列号为1的系统：

   ```
   LST SYSHLRSN: SYSHLRSN=1;
   ```

   ```
   %%LST SYSHLRSN: SYSHLRSN=1;%%
   RETCODE = 0 操作成功

                          SYSHLRSN = 1
                            STATUS = MASTER
                           HLRNAME = syshlrsn1

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**ADD SYSHLRSN**命令的参数说明。