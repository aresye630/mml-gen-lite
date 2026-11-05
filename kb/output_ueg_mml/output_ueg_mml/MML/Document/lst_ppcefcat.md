# 查询PCRF对端PCEF类别的配置信息(LST PPCEFCAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

用于在配置数据库中查询对端PCEF类别的数据记录。

- 如果需要查询所有PCRF对端PCEF类别数据记录，请不要输入任何参数。
- 如果需要查询指定PCRF对端PCEF类别标识的数据记录，请依据参数说明输入指定查询条件。

## 注意事项

执行该命令，如果显示“触发器能力集1”或“触发器能力集2”参数结果为“NULL”，则需要进一步判断触发器能力支持情况：通过在CSP网元上执行“EXP MML”命令导出MML配置，查看**ADD/MOD PPCEFCAT**命令的“触发器能力集1”或“触发器能力集2”参数。

- 如果该参数不存在，则表示参数支持所有触发器能力。
- 如果该参数存在，则表示支持的触发器能力为参数所显示的配置值，需要根据现网情况设置预期的参数值。

## 参数说明

| 参数标识            | 参数名称          | 参数说明                                                                                                                                                                                                               |
|:----------------|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCRFID          | PCRF标识        | 用于标识PCRF实体，该参数必须先由ADD PCRF命令定义，然后才能在此处索引。 取值范围： 1 默认值： 无。                                                                                                                                                          |
| PCEFCATID       | 对端PCEF类别标识    | 用于唯一识别对端PCEF、BBERF或TDF类别的标识，不允许重复。 取值范围： 1～16 默认值： 无。  说明： 当前UPCF不支持配置BBERF对端，该参数配置BBERF类别的标识后不生效。                                                                                                                 |
| PCEFCAT         | 对端PCEF类别      | 用于标识对端PCEF、BBERF或TDF类别，Gxx接口对端必须配置为BBERF类别。 取值范围：长度不超过16字节的字符串 默认值： 无。  说明： 当前UPCF不支持配置BBERF对端，该参数配置BBERF对端的类别后不生效。                                                                                                |
| TIMEOUTPROCESS  | 会话超时后处理方式     | 会话超时后的处理方式，当PCRF向PCEF或TDF下发RAR，而PCEF或TDF返回响应超时。此时，系统根据该参数的值分别采取不同的超时处理方式。 取值范围：ReleaseSingleSession：表示释放自身单个会话，系统只向当前处理会话的PCEF或TDF发送ASR（RAR）。ReleaseAllSession：表示释放所有绑定会话，系统会向所有绑定会话的PCEF或TDF发送ASR（RAR）。 默认值： 无。   |
| TERMINALPROCESS | CCR_T会话释放处理方式 | 对端下线的处理方式，当PCEF或TDF发起CCR下线请求时，系统根据该参数的值分别采取不同的处理方式。 取值范围：ReleaseSingleSession：表示释放该PCEF或TDF对应的会话的同时，系统会按照配置释放其他会话。ReleaseAllSession：表示释放该PCEF或TDF绑定的会话的同时，系统会向所有绑定会话的PCEF或TDF发送ASR（RAR），通知其他PCEF或TDF也释放会话。 默认值： 无。 |
| TSAFAILDPROCESS | TSA返回失败后处理方式  | 用于指定系统根据哪个TSA返回失败后处理方式查询PCEF的能力配置记录，如果不填写则表示该参数不作为查询条件。 取值范围： ReleaseSingleSession：表示释放自身会话。ReleaseAllSession：表示既释放自身会话，也释放绑定的Gx会话。 默认值：无。                                                                         |
| ISAPN           | 设置APN         | 是否设置APN。 取值说明：YES（是）NO（否） 默认值： 无。                                                                                                                                                                                  |
| APNID           | APN标识         | 该对端PCEF类别对应的APNID。当“ISAPN”取值为“YES”时，此参数有效。 取值说明：由ADD APN命令定义，且“APNTYPE”为“Multi-PCEF-APN”的APN。 取值范围：0～319 默认值：无。                                                                                                    |

## 使用实例

1. 查询所有PCRF对端PCEF类别数据记录，不输入任何参数。

   ```
   LST PPCEFCAT:;
   ```

   ```
   %%LST PPCEFCAT:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------------------
   PCRF标识  对端PCEF类别标识  对端PCEF类别  会话超时后的处理方式  CCR_T会话释放处理方式   TSA返回失败后处理方式    触发器能力集1                         触发器能力集2          设置APN     APN标识

   1         1                 GGSN          释放自身单个会话      释放自身单个会话        释放所有绑定会话         SGSN_CHANGE, QOS_CHANGE               DEFAULT_QOS_CHANGE     NO          NULL 
   1         2                 DPI           释放所有绑定会话      释放所有绑定会话        释放所有绑定会话         SGSN_CHANGE, QOS_CHANGE, RAT_CHANGE   REDIRECTION	      NO          NULL
   (结果个数 ＝ 2)

   ---END
   ```
2. 查询指定PCRF对端PCEF类别标识的数据记录，PCRF实体标识为1，对应PCEF类别标识为1。

   ```
   LST PPCEFCAT: PCRFID=1, PCEFCATID=1;
   ```

   ```
   %%LST PPCEFCAT: PCRFID=1, PCEFCATID=1;%%
   RETCODE = 0 操作成功

   操作结果如下;
   -------------------------
               PCRF标识  = 1
        对端PCEF类别标识 = 1
            对端PCEF类别 = GGSN
    会话超时后的处理方式 = 释放自身单个会话
   CCR_T会话释放处理方式 = 释放自身单个会话
   TSA返回失败后处理方式 = 释放所有绑定会话
           触发器能力集1 = SGSN_CHANGE
           触发器能力集2 = DEFAULT_QOS_CHANGE
                 设置APN = NO
                 APN标识 = NULL
   (结果个数 ＝ 1)
   ---END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见本命令的参数说明。