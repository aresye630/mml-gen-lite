# 查询虚拟HLR（LST VHLRSN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询虚拟HLR。

- 若需要查询全部虚拟HLR的概要信息，请不要任何输入参数。
- 若需要查询某个虚拟HLR的详细信息，请输入“系统HLR序列号”或“虚拟HLR序列号”或这两个参数的组合。

## 注意事项

ADMINISTRATOR级别的操作员或被赋给该命令权限的操作员具有本命令的操作权限。

## 参数说明

| 参数标识     | 参数名称     | 参数说明                                                 |
|:---------|:---------|:-----------------------------------------------------|
| SYSHLRSN | 系统HLR序列号 | 用于指示系统需要按照哪个系统HLR序列号来查询虚拟HLR的信息；若不输入，则表示所有的系统HLR序列号。 |
| HLRSN    | 虚拟HLR序列号 | 用于指示系统需要按照哪个虚拟HLR序列号来查询虚拟HLR的信息；若不输入，则表示所有的虚拟HLR序列号。 |

## 使用实例

1. 查询所有虚拟运营商信息：

   ```
   LST VHLRSN:;
   ```

   ```
   %%LST VHLRSN:;%%
   RETCODE = 0 操作成功

          "System HLRSN"   "Virtual HLRSN"  "Virtual HLR Name"
           1                2                HLRSN1
           3                4                HLRSN3

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询被“系统HLR序列号”为“1”管理的虚拟HLR信息：

   ```
   LST VHLRSN: SYSHLRSN=1;
   ```

   ```
   %%LST VHLRSN: SYSHLRSN=1;%%
   RETCODE = 0 操作成功

           "System HLRSN"   "Virtual HLRSN"  "Virtual HLR Name"
           1                2                HLRSN1

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**ADD VHLRSN**命令的参数说明。