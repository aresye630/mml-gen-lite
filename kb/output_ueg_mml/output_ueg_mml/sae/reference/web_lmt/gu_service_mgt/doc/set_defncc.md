# 设置缺省的NCC模板(SET DEFNCC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会造成在某些VLR/SGSN下业务呼损，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于设置VLR/SGSN/MME/S4SGSN/NGS缺省的网络能力配置NCC（Network Capability Configuration）模板。

在开局配置本局数据时需要根据运营商要求配置VLR/SGSN/MME/S4SGSN/NGS缺省的NCC模板。操作员通过如下方式可配置缺省NCC模板：

- 设置VLR和SGSN缺省的NCC模板

  该NCC模板可用于指定VLR或SGSN所支持的业务和MAP操作（即MAP版本支持能力）的能力集合。通过执行**ADD NCCTPL**命令预先设置VLR/SGSN的能力集合，然后通过执行**ADD VLRTYP**或**ADD SGSNTYP**命令在配置VLR类型或SGSN类型的同时指定其NCC能力。在进行业务和MAP流程的处理时，HLR使用VLR号码或SGSN号码查询**VLR类型表**/**SGSN类型表**获取到NCC模板，然后根据NCC模板中配置的相应业务的处理方法进行处理。

  由于**VLR类型表**/**SGSN类型表**中可能没有配置所有的VLR号码或SGSN号码，所以会出现使用VLR号码或SGSN号码查询**VLR类型表**/**SGSN类型表**时匹配不上的情况，这样就不能进行网络兼容处理。因此，HLR需要设置VLR或SGSN的缺省NCC模板。当出现VLR号码或SGSN号码与**VLR类型表**/**SGSN类型表**不能匹配而无法获取NCC模板时，则HLR按照缺省NCC模板进行业务和MAP流程的处理。
- 设置MME和S4SGSN缺省的NCC模板

  该NCC模板用于指定MME或S4SGSN所支持的业务的能力集合。通过执行**ADD NCCTPL**命令预先设置MME/S4SGSN的能力集合，然后通过执行**ADD DPETYPE**命令在配置Diameter对端类型的同时指定其NCC能力。在进行业务的处理时，HSS使用对端身份标识查询**Diameter对端类型表**获取到NCC模板，然后根据NCC模板中配置的相应业务的处理方法进行处理。

  由于**Diameter对端类型表**中可能没有配置所有的对端身份标识，所以会出现使用对端身份标识查询**Diameter对端类型表**时匹配不上的情况，这样就不能进行网络兼容处理。因此，HSS需要设置MME或S4SGSN的缺省NCC模板。当出现对端身份标识与**Diameter对端类型表**不能匹配而无法获取NCC模板时，则HSS按照缺省NCC模板进行业务的处理。
- 设置NGS缺省的NCC模板

  该NCC模板用于指定NGS所支持的业务的能力集合。通过执行**ADD NGSNCCTPL**命令预先设置NGS的能力集合，然后通过**ADD NGSPETYPE**命令在配置NGS对端类型的同时指定其NCC能力。在进行业务处理时，UDM使用AMF身份类型查询对应的NCC模板，然后根据NCC模板中配置的相应业务的处理方法进行处理。

  由于NGS对端类型表中可能没有配置所有的AMF身份类型标识，所以会出现使用AMF身份类型标识查询NGS对端类型表时匹配不上的情况，这样就不能进行网络兼容处理。如果UDM设置NGS缺省NCC模板，当出现AMF身份类型与NGS对端类型表不能匹配而无法获取NCC模板时，则UDM按照缺省NCC模板进行业务的处理。

## 注意事项

该命令不允许进行批操作。

## 参数说明

| 参数标识             | 参数名称              | 参数说明                                                                                                                                                 |
|:-----------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN            | HLR序列号            | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。 取值范围：1～255 默认值：无。                                                                                       |
| NCCPROVFORVLR    | 是否提供VLR缺省NCC模板    | 用于标识是否设置VLR缺省NCC模板。 取值范围：TRUE：设置FALSE：不设置 默认值：无。                                                                                                     |
| VLRNCCTPL        | VLR缺省NCC模板ID      | 仅当本命令中的“是否提供VLR缺省NCC模板”参数为“TRUE”时该参数有效。用于标识VLR缺省NCC模板号。该参数必须先由ADD NCCTPL命令定义，然后才能在此处引用。 取值范围：0～99998 默认值：无。                                          |
| NCCPROVFORSGSN   | 是否提供SGSN缺省NCC模板   | 用于标识是否设置SGSN缺省NCC模板。 取值范围：TRUE：设置FALSE：不设置 默认值：无。                                                                                                    |
| SGSNNCCTPL       | SGSN缺省NCC模板ID     | 仅当本命令中的“是否提供SGSN缺省NCC模板”参数为“TRUE”时该参数有效。用于标识SGSN缺省NCC模板号。该参数必须先由ADD NCCTPL命令定义，然后才能在此处引用。 取值范围：0～99998 默认值：无。 配置原则：该参数取值可以与“VLR缺省NCC模板ID”参数相同，也可以不同。 |
| NCCPROVFORMME    | 是否提供MME缺省NCC模板    | 用于标识是否设置MME缺省NCC模板。 取值范围： TRUE: 设置FALSE: 不设置 默认值：无。                                                                                                  |
| MMENCCTPL        | MME缺省NCC模板ID      | 仅当本命令中的“是否提供MME缺省NCC模板”参数为“TRUE”时该参数有效。用于标识MME缺省NCC模板号。该参数必须先由ADD NCCTPL命令定义，然后才能在此处引用。 取值范围：0～99998 默认值：无。                                          |
| NCCPROVFORS4SGSN | 是否提供S4SGSN缺省NCC模板 | 用于标识是否设置S4SGSN缺省NCC模板。 取值范围： TRUE: 设置FALSE: 不设置 默认值：无。                                                                                               |
| S4SGSNNCCTPL     | S4SGSN缺省NCC模板ID   | 仅当本命令中的“是否提供S4SGSN缺省NCC模板”参数为“TRUE”时该参数有效。用于标识S4SGSN缺省NCC模板号。该参数必须先由ADD NCCTPL命令定义，然后才能在此处引用。 取值范围：0～99998 默认值：无。                                    |
| NCCPROVFORNGS    | 是否提供NGS缺省NCC模板    | 用于标识是否设置NGS缺省NCC模板。 取值范围：TRUE：设置FALSE：不设置 说明：取值为“FALSE”时表示去签约NGS缺省NCC模板。 默认值：无                                                                       |
| NGSNCCTPL        | NGS缺省NCC模板ID      | 当本命令中的“是否提供NGS缺省NCC模板”参数取值为“TRUE”时该参数必选。用于标识NGS缺省NCC模板ID。该参数必须先由ADD NGSNCCTPL命令定义，然后才能在此处引用。 取值范围：0～99998 默认值：无。                                     |

## 使用实例

1. 增加VLR/SGSN/MME/S4SGSN/NGS缺省的NCC模板数据记录，设置相应的NCC模板ID。其中，“HLR序列号”为“1”，“是否提供VLR缺省NCC模板”为“TRUE”，“VLR缺省NCC模板ID”为“1”，“是否提供SGSN缺省NCC模板”为“TRUE”，“SGSN缺省NCC模板ID”为“1”，“是否提供MME缺省NCC模板”为“TRUE”，“MME缺省NCC模板ID”为“1”，“是否提供S4SGSN缺省NCC模板”为“TRUE”，“S4SGSN缺省NCC模板”ID为“1”，“是否提供NGS缺省NCC模板”为“TRUE”，“NGS缺省NCC模板ID”为“1”：

   ```
   SET DEFNCC: HLRSN=1, NCCPROVFORVLR=TRUE, VLRNCCTPL=1, NCCPROVFORSGSN=TRUE, SGSNNCCTPL=1, NCCPROVFORMME=TRUE, MMENCCTPL=1, NCCPROVFORS4SGSN=TRUE, S4SGSNNCCTPL=1, NCCPROVFORNGS=TRUE, NGSNCCTPL=1;
   ```
2. 增加VLR/SGSN/MME/S4SGSN/NGS缺省的NCC模板数据记录，取消设置相应的NCC模板ID。其中，“HLR序列号”为“1”，“是否提供VLR缺省NCC模板”为“FALSE”，“是否提供SGSN缺省NCC模板”为“FALSE”，“是否提供MME缺省NCC模板”为“FALSE”，“是否提供S4SGSN缺省NCC模板”为“FALSE”，“是否提供NGS缺省NCC模板”为“FALSE”：

   ```
   SET DEFNCC: HLRSN=1, NCCPROVFORVLR=FALSE, NCCPROVFORSGSN=FALSE, NCCPROVFORMME=FALSE, NCCPROVFORS4SGSN=FALSE, NCCPROVFORNGS=FALSE;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                                                                                                                                                                                                                                                                    | 处理建议                                                                                                                                                                                                                                                                                                                                                                                            |
|:--------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义。                                                                                                                                                                                                                                                                                                                                                            | 根据实际情况，重新输入已定义的“HLR序列号”，可通过LST HLRSN命令查询已定义的“HLR序列号”。                                                                                                                                                                                                                                                                                                                                           |
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”参数不在相应的参数取值范围内。                                                                                                                                                                                                                                                                                                                                           | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                                                                                                                                                                                                                                                                                |
| ERR1009 | 参数丢失    | 可能原因为如下之一：“是否提供VLR缺省NCC模板”、“是否提供SGSN缺省NCC模板”、“是否提供MME缺省NCC模板”、“是否提供S4SGSN缺省NCC模板”或者“是否提供NGS缺省NCC模板”五个参数一个都没有输入。当“是否提供VLR缺省NCC模板”参数为“TRUE”时，“VLR缺省NCC模板ID”参数未输入。当“是否提供SGSN缺省NCC模板”参数为“TRUE”时，“SGSN缺省NCC模板ID”未输入。当“是否提供MME缺省NCC模板”参数为“TRUE”时，“MME缺省NCC模板ID”参数未输入。当“是否提供S4SGSN缺省NCC模板”参数为“TRUE”时，“S4SGSN缺省NCC模板ID”参数未输入。当“是否提供NGS缺省NCC模板”参数取值为“TRUE”时，“NGS缺省NCC模板ID”参数未输入。 | 根据实际情况，重新输入参数，确保满足以下条件：“是否提供VLR缺省NCC模板”、“是否提供SGSN缺省NCC模板”、“是否提供MME缺省NCC模板”、“是否提供S4SGSN缺省NCC模板”或“是否提供NGS缺省NCC模板”参数至少输入一个。当“是否提供VLR缺省NCC模板”参数为“TRUE”时，必须同时输入“VLR缺省NCC模板ID”参数。当“是否提供SGSN缺省NCC模板”参数为“TRUE”时，必须同时输入“SGSN缺省NCC模板ID”参数。当“是否提供MME缺省NCC模板”参数为“TRUE”时，必须同时输入“MME缺省NCC模板ID”参数。当“是否提供S4SGSN缺省NCC模板”参数为“TRUE”时，必须同时输入“S4SGSN缺省NCC模板ID”参数。当“是否提供NGS缺省NCC模板”参数为“TRUE”时，必须同时输入“NGS缺省NCC模板ID”参数。 |
| ERR3003 | 模板未定义   | 可能原因为如下之一：当“是否提供VLR缺省NCC模板”参数为“TRUE”时，“VLR缺省NCC模板ID”指示的NCC模板不存在。当“是否提供SGSN缺省NCC模板”参数为“TRUE”时，“SGSN缺省NCC模板ID”指示的NCC模板不存在。当“是否提供MME缺省NCC模板”参数为“TRUE”时，“MME缺省NCC模板ID”指示的NCC模板不存在。当“是否提供S4SGSN缺省NCC模板”参数为“TRUE”时，“S4SGSN缺省NCC模板ID”指示的NCC模板不存在。当“是否提供NGS缺省NCC模板”参数为“TRUE”时，“NGS缺省NCC模板ID”指示的NCC模板不存在。                                                                        | 根据实际情况，重新输入参数，确保满足以下条件：当“是否提供VLR缺省NCC模板”参数为“TRUE”时，同时输入的“VLR缺省NCC模板ID”参数指示的NCC模板在数据库中已存在。当“是否提供SGSN缺省NCC模板”参数为“TRUE”时，同时输入的“SGSN缺省NCC模板ID”参数指示的NCC模板在数据库中已存在。当“是否提供MME缺省NCC模板”参数为“TRUE”时，同时输入的“MME缺省NCC模板ID”参数指示的NCC模板在数据库中已存在。当“是否提供S4SGSN缺省NCC模板”参数为“TRUE”时，同时输入的“S4SGSN缺省NCC模板ID”参数指示的NCC模板在数据库中已存在。当“是否提供NGS缺省NCC模板”参数为“TRUE”时，同时输入的“NGS缺省NCC模板ID”参数指示的NCC模板在数据库中已存在。                       |