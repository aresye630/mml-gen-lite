# 删除网元PLMN信息（RMV UDMNFPLMN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会造成UDM在NRF上的注册信息中的PLMN信息发生错误，从而导致周边网元无法访问UDM提供的服务，造成业务失败，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于删除一个网元的PLMN信息。

- **命令作用**：该命令用于某条网元PLMN信息记录错误或不再需要时，支持删除已配置的网元PLMN信息。
- **命令索引关系**：该命令的参数索引关系如图1所示。

  **图1** 命令参数的索引关系图

## 注意事项

- 删除数据时，如果指定“索引”所在组的“组名称”被**ADD UDMNFSRV**命令的“PLMN组名称”、**ADD UDMNFCOMINFO**命令的“允许的PLMN”引用，且是所在组的最后一条记录，则不允许删除。

- 删除数据成功，如果指定“索引”所在组的“组名称”被**ADD UDMNFSRV**命令的“PLMN组名称”引用，且**ADD UDMNFSRV**命令中的“网元状态”为“REGISTERED”时，将按照**ADD UDMNFSRV**命令中“更新方式”参数指定的更新模式立即向NRF发送更新请求。
- 删除数据成功，如果指定“索引”所在组的“组名称”已在**ADD UDMNFCOMINFO**命令的“允许的PLMN组”中引用，且**ADD UDMNFCOMINFO**命令的“公共信息标识”在**ADD UDMNFSRV**命令的“网元公共信息标识”中引用，且**ADD UDMNFSRV**命令中的“网元状态”为“REGISTERED”时，将按照**ADD UDMNFSRV**命令中“更新方式”参数指定的更新模式立即向NRF发送更新请求。
- 删除数据成功，如果指定“索引”所在组的“组名称”已在**ADD UDMNFCOMINFO**命令的“允许的PLMN组”中引用，且**ADD UDMNFCOMINFO**命令的“公共信息标识”在**ADD UDMNFSERVICE**命令的“网元公共信息标识”中引用，且**ADD UDMNFSERVICE**命令的“组名称”在**ADD UDMNFSRV**命令的“网元服务组”中引用，且**ADD UDMNFSRV**命令中的“网元状态”为“REGISTERED”时，将按照**ADD UDMNFSRV**命令中“更新方式”参数指定的更新模式立即向NRF发送更新请求。
- 当凌晨自动校验或执行**VRY NRFDATA**命令手动校验NRFClient内存数据时，在校验该MML命令的过程中，无法执行该命令，若运行该命令，则提示“360155 该MML数据正在校验中，请稍后再试”。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                         |
|:--------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GRPNAME | 组名称    | 可选必选说明：必选参数 参数含义：标识一组网元PLMN信息的关键字段之一，用于指定需要删除哪个组名称对应的网元PLMN信息。 取值范围：长度不超过32的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 参数来源：该参数由本端UDM自行定义。操作员可以使用LST UDMNFPLMN命令查询获得。 默认值：无。 配置原则：该参数和“索引”参数组成全局唯一对象关键字段。 |
| INDEX   | 索引     | 可选必选说明：必选参数 参数含义：标识一组网元PLMN信息的关键字段之一，用于指定需要删除哪个索引对应的网元PLMN信息。 取值范围：1~1024 参数来源：该参数由本端UDM自行定义。操作员可以使用LST UDMNFPLMN命令查询获得。 默认值：无。 配置原则：该参数和“组名称”参数组成全局唯一对象关键字段。                                |

## 使用实例

当在测试场景下网元上不带业务时，需要删除某个配置错误的网元PLMN信息记录时，可以执行如下步骤进行操作：

1. 执行**RMV UDMNFPLMN**命令删除“组名称”为“nfplmn”，“索引”为“1”配置记录之前，须先使用**LST UDMNFSRV**命令和**LST UDMNFCOMINFO**命令查询该PLMN组是否被网元实例引用：

   ```
   LST UDMNFSRV: NFINSNAME="udm-application-001";
   ```

   ```
   %%LST UDMNFSRV: NFINSNAME="udm-application-001";%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
       网元实例名称  =  udm-application-001
       网元实例标识  =  f716585a-cb75-474c-9202-6e8ce59d3651
      NRF所属组信息  =  udm-nrfgroup-01
           网元类型  =  统一数据管理
           网元状态  =  正常工作状态
           配置方式  =  命令模式
         PLMN组名称  =  nfplmn
      S-NSSAI组名称  =  UDM
            NSI列表  =  NULL
               位置  =  NULL
   网元公共信息标识  =  cominfo-01
       网元信息标识  =  cominfo-01
     网元服务持续性  =  是
         网元服务组  =  UDM1
       上报网管标志  =  不上报网管
           更新方法  =  PUT更新
           心跳周期  =  0
           更新标识  =  触发更新
           恢复时间  =  2020-08-31 10:36:20
       网元实例信息  =  NULL
   (结果个数 = 1)

   ---    END
   ```

   ```
   LST UDMNFCOMINFO: NFCOMINFOID="cominfo-01";
   ```

   ```
   +++    UDM/*MEID:276 MENAME:udm276*/        2019-05-08 17:41:11+8:00 
   O&M    #3179 
   %%LST UDMNFCOMINFO: NFCOMINFOID="cominfo-01";%% 
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
       公共信息标识  =  cominfo-01
           网元类型  =  鉴权服务功能
           全量域名  =  huawei.com  
     PLMN间全量域名  =  NULL      
       允许的PLMN组  =  nfplmn
     允许的网元类型  =  UDM
           允许的域  =  NULL
    允许的S-Nssai组  =  NULL
             优先级  =  NULL
               能力  =  NULL
               负载  =  0
       IP地址和端口  =  NULL
    (结果个数 = 1) 

    ---    END
   ```
2. 根据查询结果判断该PLMN组是否被引用：
   - 若未被引用，请直接执行**RMV UDMNFPLMN**命令删除网元PLMN信息，“组名称”为“nfplmn”，“索引”为“1”。

     ```
     RMV UDMNFPLMN: GRPNAME="nfplmn", INDEX=1;
     ```
   - 若被引用，请执行a，b，c三步完成网元PLMN信息删除操作。
     1. 执行**RMV UDMNFCOMINFO**命令删除网元公共信息：

        ```
        RMV UDMNFCOMINFO: NFCOMINFOID="cominfo-01";
        ```
     2. 执行**RMV UDMNFSRV**命令删除网元实例：

        ```
        RMV UDMNFSRV: NFINSNAME="udm-application-001";
        ```
     3. 执行**RMV UDMNFPLMN**命令删除网元PLMN信息，“组名称”为“nfplmn”，“索引”为“1”。

        ```
        RMV UDMNFPLMN: GRPNAME="nfplmn", INDEX=1;
        ```
3. 删除配置错误的网元PLMN信息后，重新根据正确规划的信息完成网元PLMN信息添加。

   ```
   ADD UDMNFPLMN: GRPNAME="plmngroup-01", INDEX=1, MCC="123", MNC="00";
   ```
4. 再次执行**LST UDMNFPLMN**命令查询当前配置与其规划是否一致。

   ```
   %%LST UDMNFPLMN: GRPNAME="plmngroup-01", INDEX=1;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
       组名称  =  plmngroup-01
         索引  =  1
   移动国家码  =  123
   移动网络码  =  00
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释             | 原因分析                                                     | 处理建议                                                                                                                                                     |
|-------:|:------------------|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
|    505 | 当前操作的配置数据不存在      | 输入的索引值不存在或已被删除。                                          | 执行LST UDMNFPLMN命令，查询已添加的网元PLMN信息记录，选择需要删除的“索引”值，重新执行本命令进行删除。                                                                                             |
| 360044 | 当前记录在其他命令中引用，无法删除 | 该PLMN的“索引”所在组的“组名称”被ADD UDMNFSRV命令或ADD UDMNFCOMINFO命令引用。 | 如需继续执行本命令，请先执行LST UDMNFSRV命令和LST UDMNFCOMINFO命令查询当前记录的引用关系，执行RMV UDMNFSRV命令或RMV UDMNFCOMINFO命令删除ADD UDMNFSRV或ADD UDMNFCOMINFO命令对该PLMN所属组的引用，再执行本命令删除该记录。 |
| 360155 | 该MML数据正在校验中，请稍后再试 | NRFClient内存数据校验正在进行中，对该命令的校验结束后才可执行该命令。                  | 请稍后重试。                                                                                                                                                   |