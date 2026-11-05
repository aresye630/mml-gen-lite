# 查询PS的APN和EPS数据对应关系(LST PSAPNEPS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询PS的APN和EPS数据的对应关系。

- 若需要查询全部的PS的APN和EPS数据的对应关系，请输入“HLR序列号”参数，其他参数不输入。
- 若需要查询某条PS的APN和EPS数据的对应关系，请同时输入“HLR序列号”和“接入点名称”参数。

**说明** 

由于APN不区分大小写，所以填写时也不区分大小写，界面大写和小写都可以填写，但是存入数据库统一为小写，所以查询出来的也都是小写。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                  |
|:-------|:-------|:----------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询计费特性和EPS数据对应关系数据。                                  |
| APN    | 接入点名称  | 用于标识系统需要按照哪个接入点名称来查询PS的APN和EPS数据的对应关系数据；若不输入，则表示所有的PS的APN和EPS数据的对应关系。 |

## 使用实例

1. 查询“HLR序列号”为“1”的所有PS的APN和EPS数据的对应关系记录：

   ```
   LST PSAPNEPS: HLRSN=1;
   ```

   ```
   %%LST PSAPNEPS: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "APN"         "APNTPLID"   "DEFAULTCFGFLAG"     "EPSQOSTPLID"    "PDPTYPE"   "VPLMN"   "CHARGE"    "STDCHARGE"
   huawei.com    1            TRUE                 1                IPV4        FALSE     NORMAL      
   huawei1.com   2            FALSE                2                IPV6        FALSE                 1111

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“接入点名称”为“huawei.com”的PS的APN和EPS数据的对应关系记录：

   ```
   LST PSAPNEPS: HLRSN=1, APN="huawei.com";
   ```

   ```
   %%LST PSAPNEPS: HLRSN=1 , APN="huawei.com";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   "APN"        "APNTPLID"   "DEFAULTCFGFLAG"     "EPSQOSTPLID"    "PDPTYPE"   "VPLMN"   "CHARGE"  "STDCHARGE"
   huawei.com   1            TRUE                 1                IPV4        FALSE     NORMAL    

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD PSAPNEPS**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                               | 处理建议                                                          |
|:--------|:--------|:-------------------------------------------------------------------|:--------------------------------------------------------------|
| ERR3007 | 记录不存在   | 可能原因为如下之一：“HLR序列号”未定义。 “HLR序列号”和“接入点名称”的对应的PS的APN和EPS数据的对应关系记录不存在。 | 根据实际情况，重新输入已定义的“HLR序列号”或“接入点名称”，可通过LST HLRSN命令查询已定义的“HLR序列号”。 |