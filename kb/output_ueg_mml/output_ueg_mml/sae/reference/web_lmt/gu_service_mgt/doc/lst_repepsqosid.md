# 查询EPS QoS模板替代配置(LST REPEPSQOSID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在UDM中查询一条或多条EPS QoS模板替代配置记录：

- 若需要查询一条指定的EPS QoS模板替代配置记录，请输入参数“HLR序列号”、“用户签约的EPS QoS模板ID”和“对端身份标识”。
- 若需要查询指定虚拟HLR下指定用户EPS QoS模板ID对应的全部替代配置记录，请输入参数“HLR序列号”和“用户签约的EPS QoS模板ID”，参数“对端身份标识”不输入。
- 若需要查询指定虚拟HLR下的全部EPS QoS模板替代配置记录，请只输入参数“HLR序列号”，参数“用户签约的EPS QoS模板ID”和“对端身份标识”不输入。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称             | 参数说明                                                                                        |
|:------------|:-----------------|:--------------------------------------------------------------------------------------------|
| HLRSN       | HLR序列号           | 用于指示系统按照哪个HLR序列号来查询EPS QoS模板替代配置。                                                           |
| USREPSQOSID | 用户签约的EPS QoS模板ID | 用于指示系统需要按照哪个用户签约的EPS QoS模板ID来查询EPS QoS模板替代配置；若不输入，则表示查询某个虚拟HLR下的全部EPS QoS模板替代配置。            |
| PEERENTITY  | 对端身份标识           | 用于指示系统需要按照哪个Diameter服务节点的身份标识来查询EPS QoS模板替代配置；若不输入，则表示查询某个虚拟HLR下某个用户EPS QoS模板ID对应的全部替代配置记录。 |

## 使用实例

1. 查询“HLR序列号”为“1”，“用户签约的EPS QoS模板ID”为“1”，“对端身份标识”为“test.huawei.com”的一条EPS QoS模板替换配置记录：

   ```
   LST REPEPSQOSID: HLRSN=1, USREPSQOSID=1, PEERENTITY="test.huawei.com";
   ```

   ```
   %%LST REPEPSQOSID: HLRSN=1, USREPSQOSID=1, PEERENTITY="test.huawei.com";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "EPS QoS template ID"           "Peer Entity Type"              "Peer Entity"                   "Replaced EPS QoS template ID"
           1                               Host Name                       test.huawei.com                 2

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“用户签约的EPS QoS模板ID”为“1”所对应的所有EPS QoS模板替换配置记录：

   ```
   LST REPEPSQOSID: HLRSN=1, USREPSQOSID=1;
   ```

   ```
   %%LST REPEPSQOSID: HLRSN=1, USREPSQOSID=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "EPS QoS template ID"           "Peer Entity Type"              "Peer Entity"                   "Replaced EPS QoS template ID"
           1                               Host Name                       a.com                           2
           1                               Host Name                       test.huawei.com                 2

   Total count = 2

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”的虚拟HLR之下的所有EPS QoS模板替换配置记录：

   ```
   LST REPEPSQOSID: HLRSN=1;
   ```

   ```
   %%LST REPEPSQOSID: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "EPS QoS template ID"           "Peer Entity Type"              "Peer Entity"                   "Replaced EPS QoS template ID"
           1                               Host Name                       a.com                           2
           1                               Host Name                       test.huawei.com                 2
           2                               Host Name                       a.huawei.com                    1
           2                               Realm Name                      b.com                           3
           2                               Host Name                       bbc.com                         1
           3                               Host Name                       c.com                           1

   Total count = 6

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                                                                                         | 处理建议                                                                                                                                                                                                                                                       |
|:--------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”参数不在相应的参数取值范围内。                                                                                                                                                                | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                                                                                                                                           |
| ERR1009 | 参数丢失    | 输入了参数“对端身份标识”，但未输入参数“用户签约的EPS QoS模板ID”。                                                                                                                                                      | 根据实际情况，重新输入参数，确保“用户签约的EPS QoS模板ID”和“对端身份标识”同时输入。                                                                                                                                                                                                           |
| ERR3007 | 记录不存在   | 可能原因为如下之一：输入的“HLR序列号”、“用户签约的EPS QoS模板ID”和“对端身份标识”的组合对应的EPS QoS模板替代配置记录未预先定义。输入的“HLR序列号”和“用户签约的EPS QoS模板ID”之下不存在任何EPS QoS模板替换配置记录。输入的“HLR序列号”对应的虚拟HLR未预先定义。输入的“HLR序列号”之下不存在任何EPS QoS模板替代配置记录。 | 根据实际情况，重新输入参数：若输入了“HLR序列号”、“用户签约的EPS QoS模板ID”和“对端身份标识”，请只输入“HLR序列号”和“用户签约的EPS QoS模板ID”，重新执行命令。若只输入了“HLR序列号”和“用户签约的EPS QoS模板ID”，请只输入“HLR序列号”，重新执行命令。若只输入了“HLR序列号”，请使用LST HLRSN命令，判断对应的虚拟HLR是否已定义：是，说明虚拟HLR之下不存在任何EPS QoS模板替代配置记录。否，虚拟HLR未定义，请输入正确的“HLR序列号”。 |