# 设置绑定配置(SET BINDCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会影响会话绑定，修改绑定配置需要重启UPCF后才能生效，需联系华为技术支持确认后再执行。

若配置绑定参数的“类型”为“Data”且对应“IPv4Addr”或“IPv6Prefix”为“support”时，数据Gx或N7会话的绑定参数只读取Data类型配置，不使用Default的设置。

该命令为配置类命令，用于在5G场景下，设置Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定配置。绑定配置有两种方式如表1所示：

| 绑定方式      | UPCF当前支持的绑定类型/功能   | 场景说明                                                         |
|:----------|:-------------------|:-------------------------------------------------------------|
| 基于会话类型的绑定 | 语音会话绑定             | Rx语音会话+Gx语音会话绑定即VoLTE场景。Rx语音会话+N7语音会话绑定即VoNR或EPS FallBack场景。 |
| 基于会话类型的绑定 | 数据会话绑定             | Rx数据会话+Gx数据会话绑定即4G能力开放场景。N5数据会话+N7数据会话绑定即5G能力开放或者业务分流场景。     |
| 基于会话类型的绑定 | IP冲突解决             | 支持基于数据Gx接口和数据N7接口所有用户会话IP冲突问题解决。                             |
| 基于IP地址的绑定 | -                  | 支持基于IPv4的绑定配置和IPv6的绑定配置。                                     |

Rx进行会话绑定场景下，如果Gx和N7会话同时存在，系统需要设置绑定配置，否则，N7会话不参与IP分发和会话绑定。

## 注意事项

**命令生效方式**：

修改绑定配置信息后，需要执行重启HLB、DLB、PES和DUS服务及清理Session备份数据才能生效。

**相关约束**（仅针对当“类型”取值为“Default”即不区分语音会话绑定和数据会话绑定场景）：

1. 配置“IPv4IMSI”、“IPv4MSISDN”、“IPv6IMSI”或“IPv6MSISDN”进行会话绑定时，需要和软参“VRM\_SUBSRCIPTIONIDTYPE”设置的用户类型保持一致。
2. 多PCEF组网下，配置“IPv4IMSI”、“IPv4MSISDN”、“IPv6IMSI”或“IPv6MSISDN”进行会话绑定时，多PCEF必须携带用户ID（SUPI或GPSI）。
3. 多PCEF组网下，仅支持不同的PCEF对端携带相同IP的场景进行数据Gx会话绑定。
4. 当参数“类型”类型配置为“Data”后，选择任何一个参数并将其参数配置为“support”，数据Gx或N7会话下的IP冲突检测及绑定方式仅使用“Data”类型的设置，不再使用“Default”类型的设置。
5. 在缺省的情况下，系统在初始化时已经在配置数据库中预置了绑定配置信息，其中“类型”取值为“Default”时，
   - “IPv4Addr”和“IPv6Prefix”参数取值为“支持”。
   - “IPv4IMSI”、“IPv4MSISDN”、“IPv4IPDomain”、“IPv4Dnn”、“IPv4PcefGroup”、“IPv6IMSI”、“IPv6MSISDN”、“IPv6IPDomain”及“IPv6Dnn”取值为“不支持”。
6. Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话进行绑定时，需遵循如下绑定原则：
   - 不支持N5会话与Gx会话绑定。
   - Rx会话绑定时，优先与Gx会话进行绑定，当Gx会话绑定失败后再与N7会话进行绑定。
   - 同一个Rx会话，不支持同时绑定Gx和N7会话。
   - 同一个N7会话，支持同时绑定Rx会话和N5会话，但绑定的Rx会话和N5会话总数不能超过8个。
   - 优先根据系统IPv4的配置进行绑定，当IPv4绑定失败后再根据IPv6的配置进行绑定。
   - 根据IPv6的配置进行绑定时，优先绑定IPv6前缀最长（软参“VRM\_IPV6HASHLENGTH”与“VRM\_NRIPV6HASHLENGTH”中较大值）匹配的。
   - 如果Gx、N7、Rx或N5会话未携带配置的某个属性，则按照该属性为空，系统通过配置的其他属性进行绑定。
7. 在参数“ID”配置为“Data”，其他参数配置全为“Unsupport”时，配置的记录不生效，系统会使用系统默认配置的“Default”类型记录，“Default”类型配置的会话绑定方式可能非预期。

## 参数说明

| 参数标识          | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID            | 类型            | 可选必选说明：必选参数 参数含义：用于设置当前绑定配置适用的会话类型。 取值范围： Default(Default)：所有会话类型即不区分语音会话绑定和数据会话绑定时可采用此种类型进行绑定设置。Data(Data)：数据Gx会话或数据N7会话即提供了专门的数据会话绑定方式，此参数用于数据会话和语音会话需要单独做区分场景时使用。 默认值：无。 配置原则： 对于升级场景，“类型”取值为“Default”的配置兼容低版本中“ID”取值为“1”的配置，因此升级前后绑定配置不变。对于20.6.2及其后续版本，可通过选择“类型”取值为“Data”，单独对数据会话进行绑定配置，从而实现数据和语音在绑定配置上的隔离。如果启用了“类型”取值为“Data”的配置，则必须通过ADD APN命令添加语音APN，进而用于区分会话绑定类型属于语音场景的绑定还是数据场景的绑定。N5接口暂只支持与数据N7会话进行绑定，因此配置了“类型”为“Data”的绑定方式后，N5会话下的所有绑定方式仅使用“Data”类型，不再使用“Default”类型的设置，且N5会话的绑定方式与数据N7会话绑定方式保持一致。  说明： 当本命令为“Data”类型下的参数全选为“Unsupport”时，会默认使用“Default”类型的配置查询绑定会话。                                                                                            |
| IPV4ADDR      | IPv4Addr      | 当“类型”取值为“Default”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下配置不区分数据会话绑定和语音会话绑定，该参数用于表示是否支持通过IPv4地址进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：无。 当“类型”取值为“Data”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下仅用于数据会话绑定的配置，该参数用于表示是否支持通过IPv4地址进行数据GX会话或数据N7会话参与的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则： 此场景下若同时配置了“IPv4Addr”和“IPv4PcefGroup”参数，由于“IPv4PcefGroup”只对数据Gx会话生效，所以对于数据Gx会话系统内部会使用“IPv4Addr”+“IPv4PcefGroup”的参数配置参与绑定；而数据N7会话仅使用“IPv4Addr”参数配置参与绑定。此场景下若同时配置了“IPv4Addr”和“IPv4IPDomain”参数，由于“IPv4IPDomain”只对数据N7会话生效，所以对于数据N7会话系统内部会使用“IPv4Addr”+ “IPv4IPDomain”的参数配置参与绑定；而数据Gx会话仅使用“IPv4Addr”参数配置参与绑定。                                         |
| IPV4IMSI      | IPv4IMSI      | 当“类型”取值为“Default”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下配置不区分数据会话绑定和语音会话绑定，该参数用于表示是否支持通过IPv4+IMSI进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。 当“类型”取值为“Data”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下仅用于数据会话绑定的配置，该参数用于表示是否支持通过IPv4+IMSI进行数据Gx会话或数据N7会话参与的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。                                                                                                                                                                                                                                                                                  |
| IPV4MSISDN    | IPv4MSISDN    | 当“类型”取值为“Default”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下配置不区分数据会话绑定和语音会话绑定，该参数用于表示是否支持通过IPv4+MSISDN进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。 当“类型”取值为“Data”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下仅用于数据会话绑定的配置，该参数用于表示是否支持通过IPv4+MSISDN进行数据Gx会话或数据N7会话参与的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。                                                                                                                                                                                                                                                                              |
| IPV4IPDOMAIN  | IPv4IPDomain  | 当“类型”取值为“Default”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下配置不区分数据会话绑定和语音会话绑定，该参数用于表示是否支持通过IPv4+IP地址域进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。 当“类型”取值为“Data”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下仅用于数据会话绑定的配置，该参数用于表示是否支持通过IPv4+IP地址域进行数据N7会话参与的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下若同时配置了“IPv4Addr”和“IPv4IPDomain”参数，由于“IPv4IPDomain”只对数据N7会话生效，所以对于数据N7会话系统内部会使用“IPv4Addr”+ “IPv4IPDomain”的参数配置参与绑定；而数据Gx会话仅使用“IPv4Addr”参数配置参与绑定。  说明： 本参数设置为“Support(支持)”时：语音Gx会话中的IPDomain取值来源由软参“VRM_IPDOMAINSRCFORGX”来决定。数据Gx会话中的IPDomain取值不受软参“VRM_IPDOMAINSRCFORGX”控制。                                       |
| IPV4DNN       | IPv4Dnn       | 当“类型”取值为“Default”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下配置不区分数据会话绑定和语音会话绑定，该参数用于表示是否支持通过IPv4+Dnn进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。 当“类型”取值为“Data”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下仅用于数据会话绑定的配置，该参数用于表示是否支持通过IPv4+Dnn进行数据Gx会话或数据N7会话参与的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。                                                                                                                                                                                                                                                                                    |
| IPV4PCEFGROUP | IPv4PcefGroup | “类型”取值为“Default”或“类型”取值为“Data”场景下时该参数均用于数据Gx间的会话绑定，参数描述如下： 可选必选说明：可选参数 参数含义：用于表示是否支持通过IPv4+PcefGroup进行数据Gx会话间的绑定。 取值范围： Support(支持)Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv4Addr”为“Support”。 配置原则：配置该参数为支持时，需通过ADD PPCEF或ADD PDHOSTCFG配置“PPCEFGROUP”。若UPCF一个FE同时提供语音和数据业务时，需使用ADD APN命令配置“VoLTE-APN(VoLTE-APN)”区分数据和语音Gx会话。 应用场景：在给语音Gx分配独立的IP段，但给数据Gx分配的IP段在PCEF间存在IP段重叠的场景下配置，同时需要保证组网内未开启Rx会话与数据Gx绑定的业务。  说明： 当配置该参数为“Support(支持)”，数据Gx携带IPv4进行绑定处理时将忽略参数“IPv4IPDomain”，但IPv4的其他绑定参数仍能生效。例如，当配置“IPv4Addr”和“IPv4Dnn”为“Support(支持)”，数据Gx携带IPv4使用IPv4+Dnn参与绑定；修改“IPv4Addr”、 “IPv4IPDomain”、“IPv4PcefGroup”、“IPv4Dnn”为“Support(支持)”后，数据Gx携带IPv4使用IPv4+Dnn+PcefGroup参与绑定。 |
| IPV6PREFIX    | IPv6Prefix    | 当“类型”取值为“Default”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下配置不区分数据会话绑定和语音会话绑定，该参数用于表示是否支持通过IPv6地址前缀进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：用于N5会话与N7会话绑定时，仅支持IPv6地址前缀长度为48位、64位或128位。 当“类型”取值为“Data”时，参数说明如下：可选必选说明：可选参数 参数含义：此场景下仅用于数据会话绑定的配置，该参数用于表示是否支持通过IPv6Prefix进行数据Gx会话或数据N7参与的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：用于N5会话与数据N7会话绑定时，仅支持IPv6地址前缀长度为48位、64位或128位。                                                                                                                                                                                                                                                          |
| IPV6IMSI      | IPv6IMSI      | 可选必选说明：该参数仅在“类型”取值为“Default”时生效，且为可选参数。 参数含义：用于表示是否支持通过IPv6+IMSI进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv6Prefix”为“Support”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IPV6MSISDN    | IPv6MSISDN    | 可选必选说明：该参数仅在“类型”取值为“Default”时生效，且为可选参数。 参数含义：用于表示是否支持通过IPv6+MSISDN进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv6Prefix”为“Support”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| IPV6IPDOMAIN  | IPv6IPDomain  | 可选必选说明：该参数仅在“类型”取值为“Default”时生效，且为可选参数。 参数含义：用于表示是否支持通过IPv6+IP地址域进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv6Prefix”为“Support”。  说明： 本参数设置为“Support(支持)”时：语音Gx会话中的IPDomain取值来源由软参“VRM_IPDOMAINSRCFORGX”来决定。数据Gx会话中的IPDomain取值不受软参“VRM_IPDOMAINSRCFORGX”控制。                                                                                                                                                                                                                                                                                                                                                            |
| IPV6DNN       | IPv6Dnn       | 可选必选说明：该参数仅在“类型”取值为“Default”时生效，且为可选参数。 参数含义：用于表示是否支持通过IPv6+Dnn进行Rx会话与Gx会话、Rx会话与N7会话和N5会话与N7会话的绑定。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：此场景下需同时配置“IPv6Prefix”为“Support”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 使用实例

- 不区分语音/数据会话场景下的配置示例。

  场景描述：当前局点无需通过单独设置语音会话绑定和数据会话绑定关系即可区分语音会话和数据会话，则可以直接执行如下配置，统一对UPCF所有接口会话进行处理。

  1. 执行**SET BINDCFG**命令配置Rx会话与Gx会话、Rx会话与N7会话、N5会话与N7会话的绑定配置信息。
     - “类型”为“Default”
     - “IPv4Addr”为“支持”
     - “IPv4IMSI”为“支持”
     - “IPv4IPDomain”为“支持”
     - “IPv4Dnn”为“支持”

     ```
     SET BINDCFG: ID=Default, IPV4ADDR=Support, IPV4IMSI=Support, IPV4IPDOMAIN=Support, IPV4DNN=Support;
     ```
  2. 在CSP网元下，执行**DSP POD**命令，查询pcf中的所有Pod类型。命令示例如下：

     ```
     DSP POD: TYPE=byType, PODTYPE="pcf";
     ```
  3. 执行**RST POD**命令，重启HLB、DLB、PES和DUS服务。

     **须知** 

     重启各服务时，输入的Pod类型需与2中查询结果保持一致。

     重启虚拟机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvl1-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvl2-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvr1-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvra-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvrb-pod231", FORCEFLAG=true, MEID="231";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="231";
     ```

     重启裸机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-dus-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-link-pod231", FORCEFLAG=true, MEID="231";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="231";
     ```
  4. 在USCDB网元下，执行**CLR CLUSTER**命令，清除Session备份数据。

     命令示例如下：

     ```
     CLR CLUSTER: SERVICETYPE="UPCF-SESSION";
     ```

     **说明** 

     由于特殊原因无法清除Session备份数据的局点，需要联系华为技术支持。
  5. 在对端网元强制用户下线再重新上线。

- **数据**场景下，数据Gx会话、数据N7会话参与绑定配置信息。

  场景描述：该场景用于处理必须区分语音会话和数据会话绑定关系。

  1. 执行**ADD APN**命令，添加语音APN，此步骤为必选。
     - “PCRF标识”为“1”，标识PCRF实体，该参数必须先由**ADD PCRF**命令定义，然后才能在此处索引。
     - “APN标识”为“0”。
     - “APN名称”为“ims”。
     - “APN类型”为“VoLTE-APN”，表示该APN用来处理VoLTE场景。
     - “APN匹配类型”为“FullMatching”。

     ```
     ADD APN: PCRFID=1, APNID=0, APNNAME="ims", APNTYPE=VoLTE-APN, APNMATCHTYPE=FullMatching;
     ```
  2. 执行**SET BINDCFG**命令配置Rx会话与Gx会话、Rx会话与N7会话数据场景下的绑定配置信息。
     - “类型”为“Data”
     - “IPv4Addr”为“支持”
     - “IPv4IMSI”为“支持”

     ```
     SET BINDCFG: ID=Data, IPV4ADDR=Support, IPV4IMSI=Support;
     ```
  3. 执行**SET BINDCFG**命令配置Rx会话与Gx会话、Rx会话与N7会话、N5会话与N7会话即所有接口的绑定配置信息。

     **说明** 

     此配置是针对UPCF所有接口即不区分语音会话和数据会话生效，但步骤2已经单独针对数据场景做了配置，系统关于数据会话绑定会优先采用步骤2的配置作为数据会话绑定的最终配置。而当前步骤的配置仅针对语音会话绑定场景生效，进而实现数据会话和语音会话绑定关系的区分。

     - “类型”为“Default”
     - “IPv4Addr”为“支持”
     - “IPv4IMSI”为“支持”
     - “IPv4IPDomain”为“支持”
     - “IPv4Dnn”为“支持”

     ```
     SET BINDCFG: ID=Default, IPV4ADDR=Support, IPV4IMSI=Support, IPV4IPDOMAIN=Support, IPV4DNN=Support;
     ```
  4. 在CSP网元下，执行**DSP POD**命令，查询pcf中的所有Pod类型。命令示例如下：

     ```
     DSP POD: TYPE=byType, PODTYPE="pcf";
     ```
  5. 执行**RST POD**命令，重启HLB、DLB、PES和DUS服务。

     **须知** 

     重启各服务时，输入的Pod类型需与4中查询结果保持一致。

     重启虚拟机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvl1-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvl2-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvr1-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvra-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvrb-pod231", FORCEFLAG=true, MEID="231";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="231";
     ```

     重启裸机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-dus-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-link-pod231", FORCEFLAG=true, MEID="231";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="231";
     ```
  6. 在USCDB网元下，执行**CLR CLUSTER**命令，清除Session备份数据。

     命令示例如下：

     ```
     CLR CLUSTER: SERVICETYPE="UPCF-SESSION";
     ```

     **说明** 

     由于特殊原因无法清除Session备份数据的局点，需要联系华为技术支持。
  7. 在对端网元强制用户下线再重新上线。

- Gx/N7数据会话场景下解决**IP冲突**的配置。

  IP冲突场景描述：当IP资源有限时，从Gx接口上线的所有用户的数据会话中存在个别会话的IP地址一样即产生了IP冲突，此时UPCF支持设置数据Gx会话与会话之间的判断关系进而解决IP冲突场景造成的会话异常问题。详细配置示例如下：

  1. 假设当前未配置任何会话绑定信息，但当前存在用户Gx会话与会话之间IP冲突，可执行**LST BINDCFG**查询当前的绑定设置。

     ```
     %%LST BINDCFG: ID=Default;%%
     RETCODE = 0  操作成功

     操作结果如下:
     -------------
              类型  =  Default
          IPv4Addr  =  支持
          IPv4IMSI  =  不支持
        IPv4MSISDN  =  不支持
      IPv4IPDomain  =  不支持
           IPv4Dnn  =  不支持
     IPv4PcefGroup  =  不支持
        IPv6Prefix  =  支持
          IPv6IMSI  =  不支持
        IPv6MSISDN  =  不支持
      IPv6IPDomain  =  不支持
           IPv6Dnn  =  不支持
     (操作结果数 = 1)

     ---    END
     ```

     **说明** 

     在缺省的情况下，系统在初始化时已经在配置数据库中预置了上述绑定配置信息。
  2. 根据1查询结果可知，当前未手动配置任何绑定信息，查询结果显示为系统默认的配置信息。根据当前的冲突现状，仅根据IPv4地址已经无法解决会话的唯一性即会话冲突，需手动增加绑定信息即在IPv4基础上“与”上其他字段，以此确保会话唯一性，进而解决因冲突导致的会话异常。

     ```
     SET BINDCFG: ID=Default, IPV4ADDR=Support, IPV4IMSI=Support;
     ```
  3. 修改绑定设置后，须重启微服务并清库才能生效。

     在CSP网元下，执行**DSP POD**命令，查询pcf中的所有Pod类型。命令示例如下：

     ```
     DSP POD: TYPE=byType, PODTYPE="pcf";
     ```
  4. 执行**RST POD**命令，重启HLB、DLB、PES和DUS服务。

     **须知** 

     重启各服务时，输入的Pod类型需与3中查询结果保持一致。

     重启虚拟机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvl1-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvl2-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvr1-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvra-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-srvrb-pod231", FORCEFLAG=true, MEID="231";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="231";
     ```

     重启裸机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-dus-pod231", FORCEFLAG=true, MEID="231";
     RST POD: TYPE=byType, PODTYPE="pcf-link-pod231", FORCEFLAG=true, MEID="231";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="231";
     ```
  5. 在USCDB网元下，执行**CLR CLUSTER**命令，清除Session备份数据。

     命令示例如下：

     ```
     CLR CLUSTER: SERVICETYPE="UPCF-SESSION";
     ```

     **说明** 

     由于特殊原因无法清除Session备份数据的局点，需要联系华为技术支持。
  6. 在对端网元强制用户下线再重新上线。

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释                          | 原因分析                                                                                                                                                               | 处理建议                                                                                                                                               |
|------:|:-------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| 57891 | 不选择IP地址时不支持选择其它绑定属性。           | 仅当“IPv4Addr”配置为“支持”时，才可以配置“IPv4IMSI”、“IPv4MSISDN”、“IPv4IPDomain”或“IPv4Dnn”为“支持”。仅当“IPv6Prefix”配置为“支持”时，才可以配置“IPv6IMSI”、“IPv6MSISDN”、“IPv6IPDomain”或“IPv6Dnn”为“支持”。 | 通过执行LST BINDCFG命令查询系统所有参数的配置信息。根据查询信息配置，确保配置其他IPv4类型的绑定信息为“支持”时，“IPv4Addr”已配置为“支持”，配置其他IPv6类型的绑定信息为“支持”时，“IPv6Prefix”已配置为“支持”。                     |
| 57917 | 不能同时配置IMSI与MSISDN属性。           | 系统不支持参数“IPv4IMSI”与“IPv4MSISDN”或“IPv6IMSI”与“IPv6MSISDN”同时设置为“支持”。                                                                                                   | 通过执行LST BINDCFG命令查询系统参数“IPv4IMSI”、“IPv4MSISDN”、“IPv6IMSI”和“IPv6MSISDN”的配置信息。根据查询信息配置，确保配置的“IPv4IMSI”与“IPv4MSISDN”、“IPv6IMSI”与“IPv6MSISDN”不同时为“支持”。 |
| 57938 | IPv4Addr和IPv6Prefix至少需要选择支持一个。 | 系统不支持参数“IPv4Addr”和“IPv6Prefix”同时设置为“不支持”。                                                                                                                          | 通过执行LST BINDCFG命令查询系统参数“IPv4Addr”和“IPv6Prefix”的配置信息。根据查询信息配置，确保配置的“IPv4Addr”和“IPv6Prefix”不同时为“不支持”。                                                |