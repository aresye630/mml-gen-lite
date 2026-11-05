# 查询缺省EPS QoS模板替代配置(LST DEFREPEPSQOSID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在UDM中查询一条或多条缺省EPS QoS模板替代配置记录：

- 若需要查询一条指定的缺省EPS QoS模板替代配置记录，请输入参数“HLR序列号”和“用户签约的EPS QoS模板ID”。
- 若需要查询指定虚拟HLR下的全部缺省EPS QoS模板替代配置记录，请只输入参数“HLR序列号”，参数“用户签约的EPS QoS模板ID”不输入。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称             | 参数说明                                                                        |
|:------------|:-----------------|:----------------------------------------------------------------------------|
| HLRSN       | HLR序列号           | 用于指示系统按照哪个HLR序列号来查询缺省EPS QoS模板替代配置。                                         |
| USREPSQOSID | 用户签约的EPS QoS模板ID | 用于指示系统需要按照哪个用户签约的EPS QoS模板ID来查询缺省替代配置；若不输入，则表示查询指定虚拟HLR下的全部缺省EPS QoS模板替代配置。 |

## 使用实例

1. 查询“HLR序列号”为“1”，“用户签约的EPS QoS模板ID”为“1”的一条缺省EPS QoS模板替代配置记录：

   ```
   LST DEFREPEPSQOSID: HLRSN=1, USREPSQOSID=1;
   ```

   ```
   %%LST DEFREPEPSQOSID: HLRSN=1, USREPSQOSID=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "EPS QoS template ID"         "Replaced EPS QoS template ID"
           1                             3

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的虚拟HLR之下的所有缺省EPS QoS模板替代配置记录：

   ```
   LST DEFREPEPSQOSID: HLRSN=1;
   ```

   ```
   %%LST DEFREPEPSQOSID: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "EPS QoS template ID"         "Replaced EPS QoS template ID"
           1                             3
           5                             1

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                           | 处理建议                                                                                                                                                                                           |
|:--------|:--------|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | 可能原因为如下之一：输入的“HLR序列号”和“用户签约的EPS QoS模板ID”的组合对应的缺省EPS QoS模板替代配置记录未预先定义。输入的“HLR序列号”对应的虚拟HLR未预先定义。 | 根据实际情况，重新输入参数：若只输入了“HLR序列号”和“用户签约的EPS QoS模板ID”，请只输入“HLR序列号”，重新执行LST DEFREPEPSQOSID命令。若只输入了“HLR序列号”，请使用LST HLRSN命令，判断对应的虚拟HLR是否已定义：是，说明虚拟HLR之下不存在任何缺省EPS QoS模板替代配置记录。否，虚拟HLR未定义，请输入正确的“HLR序列号”。 |