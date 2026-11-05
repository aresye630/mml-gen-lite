# 查询SMF选择策略（LST SMFSELPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询SMF的选择策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                         |
|:---------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE | 用户范围   | 可选必选说明：可选参数  参数含义：该参数用于指定应用SMF选择策略的用户范围。  数据来源：全网规划 取值范围： “ALL_USER（所有用户）”：所有用户“HOME_USER（本网用户）”：本网用户“FOREIGN_USER（外网用户）”：外网用户“IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀  默认值：无  配置原则：  对于指定的用户（群），SMF选择策略的匹配优先级从高到低依次为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE  | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。  参数含义：该参数用于指定应用SMF选择策略的用户的IMSI前缀。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。  默认值：无  配置原则：无                                                                                                                                          |

## 使用实例

- 查询当前配置的SMF选择策略，执行如下命令：

  ```
  %%LST SMFSELPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                           用户范围  =  所有用户
                                           IMSI前缀  =  NULL
                                        DNN群组标识  =  NULL
                              是否携带Serving Scope  =  No
                                           服务范围  =  NULL
                                  是否支持I-SMF选择  =  否
                                        是否使用TAI  =  否
                                   是否使用用户IMSI  =  否
                                     是否使用MSISDN  =  否
                              融合SMF/PGW-C选择条件  =  NULL
                                        是否重选SMF  =  是
                                    优选同一SMF开关  =  否
                                            DNN格式  =  默认方式
                            签约信息中的SMF选择策略  =  默认
                     EPS与5GS互操作专用切片选择策略  =  签约方式
                     EPS与5GS互操作专用切片业务类型  =  0
                     EPS与5GS互操作专用切片细分标识  =  FFFFFF
                                          I-SMF重选  =  默认模式
                                  4到5切换I-SMF重选  =  默认模式
                            签约信息中的相同SMF指示  =  否			 
                                ISMF场景相同SMF开关  =  是			 
                                VSMF场景相同SMF开关  =  是
                                         V-SMF重选   =  默认模式
                                  4到5切换V-SMF重选  =  默认模式
                              Preferred TAI功能开关  =  否  
                                漫游用户是否使用TAI  =  是
                                漫游用户DNN群组标识  =  1
                             是否携带IsmfSupportInd  =  否
  Home Routed国际漫游选择H-SMF是否携带Serving Scope  =  否
           Home Routed国际漫游场景下H-SMF的服务范围  =  NULL
                 Home Routed国际漫游用户DNN群组标识  =  NULL
                                           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询当前配置“用户范围”为“本网用户”的SMF选择策略，执行如下命令：

  ```
  %%LST SMFSELPLCY: SUBRANGE=HOME_USER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                           用户范围  =  本网用户
                                           IMSI前缀  =  NULL
                                        DNN群组标识  =  NULL
                              是否携带Serving Scope  =  No
                                           服务范围  =  NULL
                                  是否支持I-SMF选择  =  否
                                        是否使用TAI  =  否
                                   是否使用用户IMSI  =  否
                                     是否使用MSISDN  =  否
                              融合SMF/PGW-C选择条件  =  NULL
                                        是否重选SMF  =  是
                                    优选同一SMF开关  =  否
                                            DNN格式  =  默认方式
                            签约信息中的SMF选择策略  =  默认
                     EPS与5GS互操作专用切片选择策略  =  签约方式
                     EPS与5GS互操作专用切片业务类型  =  0
                     EPS与5GS互操作专用切片细分标识  =  FFFFFF
                                          I-SMF重选  =  默认模式
                                  4到5切换I-SMF重选  =  默认模式
                            签约信息中的相同SMF指示  =  否			 
                                ISMF场景相同SMF开关  =  是			 
                                VSMF场景相同SMF开关  =  是
                                         V-SMF重选   =  默认模式
                                  4到5切换V-SMF重选  =  默认模式
                              Preferred TAI功能开关  =  否
                                漫游用户是否使用TAI  =  否
                                漫游用户DNN群组标识  =  NULL
                             是否携带IsmfSupportInd  =  否
  Home Routed国际漫游选择H-SMF是否携带Serving Scope  =  否
           Home Routed国际漫游场景下H-SMF的服务范围  =  NULL
                 Home Routed国际漫游用户DNN群组标识  =  NULL
                                           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 输出结果说明

| 输出项名称                                   | 输出项解释                                                                                                                                                    |
|:----------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 用户范围                                    | 该参数用于指定应用SMF选择策略的用户范围。                                                                                                                                   |
| IMSI前缀                                  | 该参数用于指定应用SMF选择策略的用户的IMSI前缀。                                                                                                                              |
| DNN群组标识                                 | 该参数用于标识使用ServingScope选择目标SMF的PDU会话的DNN。如果使用不同DNN的不同PDU会话在选择目标SMF时都有使用ServingScope的要求，则可以将这些DNN配置到同一个DNN群组，以简化配置。                                         |
| 是否携带Serving Scope                       | 该参数用于标识AMF在选择目标SMF时是否携带服务范围（Serving Scope）信息。                                                                                                            |
| 服务范围                                    | 该参数用于描述目标SMF的服务范围。                                                                                                                                       |
| 是否支持I-SMF选择                             | 该参数用于指定是否支持I-SMF选择。I-SMF主要是插入在SMF和AMF之间，负责控制SMF无法直接控制的I-UPF。                                                                                             |
| 是否使用TAI                                 | 该参数用于指定是否将UE当前所驻留的TAI作为目标SMF的选择条件。此外，当配置支持I-SMF选择时，该配置项无效。                                                                                               |
| 是否使用用户IMSI                              | 该参数用于指定是否将用户的IMSI作为目标SMF的选择条件。                                                                                                                           |
| 是否使用MSISDN                              | 该参数用于指定是否将用户的MSISDN作为目标SMF的选择条件。                                                                                                                         |
| 融合SMF/PGW-C选择条件                         | 该参数用于表示AMF在选择融合了PGW-C功能的SMF时使用的判断条件，如UE的无线能力、UE的签约数据等，其中签约数据包括：核心网类型限制（coreNetworkTypeRestrictions）以及选择的DNN是否支持EPS互操作（Interworking with EPS Indication）。 |
| 是否重选SMF                                 | 该参数用于指定当AMF首次选择某个SMF并且发起PDU会话流程，如果对端返回5xx原因值时，是否重新选择新的SMF再次重试业务请求。                                                                                       |
| 优选同一SMF开关                               | 该参数用于控制同一用户使用相同的DNN和不同的网络切片建立多个PDU会话时，AMF是否优选选择同一SMF。如果当前SMF不支持新建PDU会话的网络切片，此时AMF必须选择符合条件的SMF。 若用户匹配ADD SMFPRESELBYIMSI配置记录，本功能失效。                       |
| DNN格式                                   | 该参数用于AMF选择目标SMF时，服务发现消息中携带的DNN的格式。                                                                                                                       |
| 签约信息中的SMF选择策略                           | 该参数用于控制AMF选择用户签约信息中指定SMF列表中SMF的策略。                                                                                                                       |
| EPS与5GS互操作专用切片选择策略                      | 该参数用于EPS与5GS互操作流程中，控制AMF发现I-SMF/V-SMF时使用的切片来源。                                                                                                           |
| EPS与5GS互操作专用切片业务类型                      | 该参数用于设置EPS与5GS互操作专用切片业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。                                                                             |
| EPS与5GS互操作专用切片细分标识                      | 该参数用于设置EPS与5GS互操作专用切片细分标识，运营商根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。                                                                                      |
| I-SMF重选                                 | 该参数表示4到5移动注册更新流程中，互操作专用切片与会话关联切片不一致时，是否重选I-SMF。                                                                                                          |
| 4到5切换I-SMF重选                            | 该参数表示4到5切换流程中，互操作专用切片与会话关联切片不一致时，是否重选I-SMF。                                                                                                              |
| 签约信息中的相同SMF指示                           | 该参数用于控制同一用户多个PDU会话使用相同的DNN和S-NSSAI时，AMF是否根据签约信息中的sameSmfInd指示选择SMF。 若用户匹配ADD SMFPRESELBYIMSI配置记录，本功能失效。                                                  |
| ISMF场景相同SMF开关                           | 该参数用于控制当SAMESMFIND打开时，同一用户之前创建的拥有相同DNN和NSSAI的PDU会话插入了I-SMF，新创建的PDU会话是否仍然选择相同的I-SMF和锚点SMF。                                                                |
| VSMF场景相同SMF开关                           | 该参数用于控制当SAMESMFIND打开时，同一用户之前创建的拥有相同DNN和NSSAI的PDU会话插入了V-SMF，新创建的PDU会话是否仍然选择相同的V-SMF。                                                                      |
| V-SMF重选                                 | 该参数表示漫游用户的4到5移动注册更新流程中，互操作专用切片与会话关联切片不一致时，是否重选V-SMF。                                                                                                     |
| 4到5切换V-SMF重选                            | 该参数表示漫游用户的4到5切换流程中，互操作专用切片与会话关联切片不一致时，是否重选V-SMF。                                                                                                         |
| Preferred TAI功能开关                       | 该参数用于控制AMF选择锚点SMF时，是否开启携带Preferred TAI向NRF做服务发现的功能。 漫游用户Home Routed会话发现H-SMF不携带Preferred TAI，不受该参数控制。                                                    |
| 漫游用户是否使用TAI                             | 该参数用于指定对于异网漫游用户HomeRouted模式的PDU会话，是否将UE当前所驻留的TAI作为选择H-SMF的条件。 漫游用户的类型（国际漫游/异网漫游），使用ADD NGCONNECTPLMN的ROAMTYPE参数来指定。                                      |
| 漫游用户DNN群组标识                             | 该参数用于标识异网漫游用户使用TAI选择H-SMF的PDU会话的DNN。如果使用不同DNN的不同PDU会话在选择目标SMF时都有使用TAI的要求，则可以将这些DNN配置到同一个DNN群组，以简化配置。                                                     |
| 是否携带IsmfSupportInd                      | 该参数用于设置AMF在服务发现I-SMF时是否携带IsmfSupportInd信息。 漫游场景该功能不生效。                                                                                                   |
| Home Routed国际漫游选择H-SMF是否携带Serving Scope | 该参数用于控制在Home Routed国际漫游场景下AMF在选择H-SMF时是否携带服务范围（Serving Scope）信息。                                                                                         |
| Home Routed国际漫游场景下H-SMF的服务范围            | 该参数用于配置Home Routed国际漫游场景下目标H-SMF的服务范围。                                                                                                                   |
| Home Routed国际漫游用户DNN群组标识                | 该参数用于标识Home Routed国际漫游场景下使用ServingScope选择目标H-SMF的PDU会话的DNN。如果使用不同DNN的不同PDU会话在选择目标SMF时都有使用ServingScope的要求，则可以将这些DNN配置到同一个DNN群组，以简化配置。                     |
| 描述信息                                    | 该参数用于描述SMF选择策略，在运维中起助记作用。                                                                                                                                |