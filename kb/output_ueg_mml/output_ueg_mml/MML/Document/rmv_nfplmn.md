# 删除网元PLMN信息（RMV NFPLMN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会导致系统异常，影响业务处理，需联系华为技术支持确认后再执行。

该命令用于删除一个网元的PLMN信息。

- **命令作用**：该命令用于某条网元PLMN信息记录错误或不再需要时，支持删除已配置的网元PLMN信息。
- **命令索引关系**：该命令的参数索引关系如图1所示。

  **图1** 命令参数的索引关系图

## 注意事项

- 删除数据时，如果指定“索引”所在组的“组名称”被**ADD NFSRV**命令的“PLMN组名称”、**ADD NFCOMINFO**命令的“允许的PLMN组”引用，且是所在组的最后一条记录，则不允许删除。

- 删除数据成功，如果指定“索引”所在组的“组名称”被**ADD NFSRV**命令的“PLMN组名称”引用，且**ADD NFSRV**命令中的“网元状态”为“REGISTERED”时，将按照**ADD NFSRV**命令中“更新方式”参数指定的更新模式60秒内向NRF发送Nnrf\_NFManagement\_NFUpdate Request消息请求更新。
- 删除数据成功，如果指定“索引”所在组的“组名称”已在**ADD NFCOMINFO**命令的“允许的PLMN组”中引用，且**ADD NFCOMINFO**命令的“公共信息标识”在**ADD NFSRV**命令的“网元公共信息标识”中引用，且**ADD NFSRV**命令中的“网元状态”为“REGISTERED”时，将按照**ADD NFSRV**命令中“更新方式”参数指定的更新模式60秒内向NRF发送Nnrf\_NFManagement\_NFUpdate Request消息请求更新。
- 删除数据成功，如果指定“索引”所在组的“组名称”已在**ADD NFCOMINFO**命令的“允许的PLMN组”中引用，且**ADD NFCOMINFO**命令的“公共信息标识”在**ADD NFSERVICE**命令的“网元公共信息标识”中引用，且**ADD NFSERVICE**命令的“组名称”在**ADD NFSRV**命令的“网元服务组”中引用，且**ADD NFSRV**命令中的“网元状态”为“REGISTERED”时，将按照**ADD NFSRV**命令中“更新方式”参数指定的更新模式60秒内向NRF发送Nnrf\_NFManagement\_NFUpdate Request消息请求更新。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                      |
|:--------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GRPNAME | 组名称    | 可选必选说明：必选参数 参数含义：标识一组网元PLMN信息的关键字段之一，用于指定需要删除哪个组名称对应的网元PLMN信息，操作员可以使用LST NFPLMN命令查询获得。 取值范围：长度不超过32的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 参数来源：该参数由本端PCF自行定义。 默认值：无。 配置原则：该参数和“索引”参数组成全局唯一对象关键字段。 |
| INDEX   | 索引     | 可选必选说明：必选参数 参数含义：标识一组网元PLMN信息的关键字段之一，用于指定需要删除哪个索引对应的网元PLMN信息，操作员可以使用LST NFPLMN命令查询获得。 取值范围：1~1024 参数来源：该参数由本端PCF自行定义。 默认值：无。 配置原则：该参数和“组名称”参数组成全局唯一对象关键字段。                                |

## 使用实例

当在测试场景下网元上不带业务时，需要删除某个配置错误的网元PLMN信息记录时，可以执行如下步骤进行操作：

1. 执行**RMV NFPLMN**命令删除“组名称”为“nfplmn”，“索引”为“1”配置记录之前，须先使用**LST NFSRV**命令和**LST NFCOMINFO**命令查询该PLMN组是否被网元实例引用：

   ```
   LST NFSRV: NFINSNAME="pcf-application-001";
   ```

   ```
   %%LST NFSRV: NFINSNAME="pcf-application-001";%%
   RETCODE = 0  操作成功 

         网元实例名称  =  pcf-application-001  
         网元实例标识  =  c89aabf9-2ee9-11eb-8717-0255c2cb00a7
                 节点  =  NULL
        NRF所属组信息  =  nrfgroup-01           
             网元类型  =  策略控制功能           
             网元状态  =  正常工作状态           
             配置方式  =  命令模式         
           PLMN组名称  =  nfplmn      
        S-NSSAI组名称  =  snssai-group-01            
              NSI列表  =  NULL               
                 位置  =  NULL  
     网元公共信息标识  =  cominfo_01      
         网元信息标识  =  pcfinfo_01     
       网元服务持续性  =  NULL         
           网元服务组  =  NULL 
   网元服务范围组名称  =  nfserscope       
         上报网管标志  =  不上报网管  
             更新开关  =  更新开关打开     
             更新方法  =  PUT更新    
             心跳周期  =  10      
         网元实例信息  =  NULL 

   (结果个数 = 1)

   ---    END
   ```

   ```
   LST NFCOMINFO: NFCOMINFOID="cominfo-01";
   ```

   ```
   %%LST NFCOMINFO: NFCOMINFOID="cominfo_01";%% 
   RETCODE = 0  操作成功

       公共信息标识  =  cominfo_01
           网元类型  =  策略控制功能
           全量域名  =  huawei.com  
     PLMN间全量域名  =  NULL      
       允许的PLMN组  =  nfplmn
     允许的网元类型  =  PCF
           允许的域  =  NULL
    允许的S-Nssai组  =  NULL
             优先级  =  NULL
               容量  =  NULL
               负载  =  0
       IP地址和端口  =  NULL
     IP地址校验开关  =  YES
    (结果个数 = 1) 

    ---    END
   ```
2. 根据查询结果判断该PLMN组是否被引用：
   - 若未被引用，请直接执行**RMV NFPLMN**命令删除网元PLMN信息，“组名称”为“nfplmn”，“索引”为“1”。

     ```
     RMV NFPLMN: GRPNAME="nfplmn", INDEX=1;
     ```
   - 若被引用，请执行a，b，c三步完成网元PLMN信息删除操作。
     1. 执行**RMV NFCOMINFO**命令删除网元公共信息：

        ```
        RMV NFCOMINFO: NFCOMINFOID="cominfo-01";
        ```
     2. 执行**RMV NFSRV**命令删除网元实例：

        ```
        RMV NFSRV: NFINSNAME="pcf-application-001";
        ```
     3. **执行RMV NFPLMN**命令删除网元PLMN信息，“组名称”为“nfplmn”，“索引”为“1”。

        ```
        RMV NFPLMN: GRPNAME="nfplmn", INDEX=1;
        ```
3. 删除配置错误的网元PLMN信息后，重新根据正确规划的信息完成网元PLMN信息添加。

   ```
   ADD NFPLMN: GRPNAME="plmngroup-01", INDEX=1, MCC="123", MNC="00";
   ```
4. 再次执行**LST NFPLMN**命令查询当前配置与其规划是否一致。

   ```
   %%LST NFPLMN: GRPNAME="plmngroup-01", INDEX=1;%%
   RETCODE = 0  操作成功

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

|    错误码 | 错误码解释             | 原因分析                                               | 处理建议                                                                                                                                   |
|-------:|:------------------|:---------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
|    505 | 当前操作的配置数据不存在      | 输入的索引值不存在或已被删除。                                    | 执行LST NFPLMN命令，查询已添加的网元PLMN信息记录，选择需要删除的“索引”值，重新执行本命令进行删除。                                                                              |
| 360044 | 当前记录在其他命令中引用，无法删除 | 该PLMN的“索引”所在组的“组名称”被ADD NFSRV命令或ADD NFCOMINFO命令引用。 | 如需继续执行本命令，请先执行LST NFSRV命令和LST NFCOMINFO命令查询当前记录的引用关系，执行RMV NFSRV命令或RMV NFCOMINFO命令删除ADD NFSRV或ADD NFCOMINFO命令对该PLMN所属组的引用，再执行本命令删除该记录。 |