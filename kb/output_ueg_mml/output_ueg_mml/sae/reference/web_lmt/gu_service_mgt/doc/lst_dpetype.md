# 查询Diameter对端类型(LST DPETYPE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询Diameter对端类型的记录：

- 若需要查询某个HLR序列号下全部Diameter对端类型的概要配置信息，请只输入“HLR序列号”。
- 若需要查询某个HLR序列号下某个Diameter对端类型的详细配置信息，请输入“HLR序列号”和“对端身份标识”。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                       |
|:-----------|:-------|:-----------------------------------------------------------|
| HLRSN      | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询Diameter对端类型数据。                         |
| PEERENTITY | 对端身份标识 | 用于指示系统按照哪个对端身份标识来查询Diameter对端类型数据；若不输入，则表示所有的Diameter对端类型。 |

## 使用实例

1. 查询一个Diameter对端类型，“HLR序列号”为“1”，“对端身份标识”为“test.huawei.com”：

   ```
   LST DPETYPE: HLRSN=1, PEERENTITY="test.huawei.com";
   ```

   ```
   %%LST DPETYPE: HLRSN=1, PEERENTITY="test.huawei.com";%%
   RETCODE = 0 SUCCESS0001:操作成功

           "Peer Entity Type"  "Peer Entity"           "Peer Entity Name"            "Type"              "Net Type"         "MMENCCTPL"       "S4SGSNNCCTPL"
           Host Name           test.huawei.com          test                          LOCALDOMESTIC       NON_VoLTE           NOTPROV           NOTPROV

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的所有Diameter对端类型：

   ```
   LST DPETYPE: HLRSN=1;
   ```

   ```
   %%LST DPETYPE: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "Peer Entity Type"  "Peer Entity"          "Peer Entity Name"           "Type"              "Net Type"          "MMENCCTPL"              "S4SGSNNCCTPL"
           Host Name           test.huawei.com          test                      LOCALDOMESTIC        NON_VoLTE            1                     1
           Realm Name          test1.huawei.com          test1                    CROSSDOMESTIC         VoLTE                1                       1

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析               | 处理建议                                                 |
|:--------|:--------|:-------------------|:-----------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数的取值中含有不符合要求的字符串。 | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合取值范围。                   |
| ERR3007 | 记录不存在   | HLR序列号未定义。         | 使用LST HLRSN命令查询后，重新确认要查询哪个“HLR序列号”对应的Diameter对端数据记录。 |