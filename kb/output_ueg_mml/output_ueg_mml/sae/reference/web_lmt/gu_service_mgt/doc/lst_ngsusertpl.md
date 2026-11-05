# 查询5GS用户模板(LST NGSUSERTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询5GS用户模板数据。

- 若需要查询某个HLR序列号下全部的5GS用户模板数据，请根据模板记录数进行操作：
  - 模板记录数小于或等于5000条时，请输入“HLR序列号”参数或“HLR序列号”参数与“保存文件名”参数的组合，其他参数不输入。
  - 模板记录数大于5000条时，请输入“HLR序列号”参数及“保存文件名”参数，其他参数不输入。

- 若需要查询某条5GS用户模板数据且不返回详细信息，请同时输入“HLR序列号”和“模板ID”参数，“是否显示详细信息”参数设置为“FALSE”。
- 若需要查询某条5GS用户模板数据且返回详细信息，请同时输入“HLR序列号”和“模板ID”参数，“是否显示详细信息”参数设置为“TRUE”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                             |
|:-------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号   | 可选必选说明：必选参数 参数含义：用于指示系统按照哪个HLR序列号来查询5GS用户模板信息数据。 取值范围：1～255 默认值：无。 配置原则：无。                                                                                                                                                                                                                                       |
| TPLID  | 模板ID     | 可选必选说明：必选参数 参数含义：用于指示系统按照哪个模板ID来查询5GS用户模板信息数据；若不输入，则表示查询所有的5GS用户模板数据。 取值范围：1～2147483646 默认值：无。 配置原则：无。                                                                                                                                                                                                           |
| DETAIL | 是否显示详细信息 | 可选必选说明：必选参数 参数含义：用于指示系统是否显示5GS用户模板中会话信息模板配置的详细信息。 取值范围： TRUE：以Json字符串格式显示5GS用户模板中会话信息模板配置的详细信息。FALSE：查询结果仅显示会话信息模板ID。 默认值：无。 配置原则：无。                                                                                                                                                                             |
| SAVEAS | 保存文件名    | 可选必选说明：可选参数 参数含义：用于指示保存查询结果的文件名称。当模板记录数超过5000条时必须输入该参数，将查询结果保存在PGW模块所在容器上，否则会报错“ERR4153：报文数量超过上限，需要指定保存文件名进行查询”。 取值范围：1~20位字符串，可由字母、数字或字符“_”、“.”组成。 默认值：无 配置原则： 该参数与“模板ID”参数只能输入一个。保存文件名参数指定的文件，可以通过“PGW Web LMT”界面的“文件管理器”下载。“保存文件名”使用不支持的字符会导致文件无法下载、下载文件内容异常、文件无法删除的情况，请修改保存文件名并重新执行命令获取文件。删除异常文件请联系华为技术支持处理。 |

## 使用实例

1. 查询“HLR序列号”为“1”的5GS用户模板信息：

   ```
   LST NGSUSERTPL: HLRSN=1;
   ```

   ```
   %%LST NGSUSERTPL: HLRSN=1;%% 
   RETCODE = 0 SUCCESS0001:操作成功      
              
                    TPLID        TPLNAME                
                       1            1                
                       2            11                
                       3            11           
        
   Total count = 3  

   There is together 1 report  

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“模板ID”为“1”的5GS用户模板信息，且不显示详细信息：

   ```
   LST NGSUSERTPL: HLRSN=1, TPLID=1, DETAIL=FALSE;
   ```

   ```
   %%LST NGSUSERTPL: HLRSN=1, TPLID=1, DETAIL=FALSE;%% 
   RETCODE = 0 SUCCESS0001:操作成功       
                       
                       HLRSN = 1                          
                       TPLID = 1                        
                     TPLNAME = prepaid                         
                      AMBRUP = 1                         
                      UPUNIT = Gbps                         
                      AMBRDW = 200                         
                      DWUNIT = Mbps                    
                 FORBIDTPLID = 1                   
                SERAREATPLID = 1                            
                         MPS = FALSE                            
                         MCS = FALSE                       
                    DLBUFFER = 100                       
                    AUTHTYPE = 5G-AKA                    
                 MICOALLOWED = FALSE                    
                 SMDATATPLID = 100   
               SMSSUBSCRIBED = TRUE
                       MTSMS = FALSE
                     MTSMSBA = FALSE
                     MTSMSBR = FALSE
                       MOSMS = FALSE
                     MOSMSBA = FALSE
                     MOSMSBR = FALSE
       NSSAIINCLUSIONALLOWED = TRUE
                    CHARGING = 0000
                 NREDRXVALUE = 1
           NRREDCAPEDRXVALUE = 1
              NRN1EXPTWVALUE = 1
          NRREDCAPEXPTWVALUE = 1

   Total count = 28

   There is together 1 report  

   ---    END
   ```
3. 查询“HLR序列号”为“1”，“模板ID”为“1”的5GS用户模板信息，且显示详细信息：

   ```
   LST NGSUSERTPL: HLRSN=1, TPLID=1, DETAIL=TRUE;
   ```

   ```
   %%LST NGSUSERTPL: HLRSN=1, TPLID=1, DETAIL=TRUE;%% 
   RETCODE = 0 SUCCESS0001:操作成功       
                       
                       HLRSN = 1           
                       TPLID = 1                        
                     TPLNAME = prepaid                         
                      AMBRUP = 1                         
                      UPUNIT = Gbps                         
                      AMBRDW = 200                         
                      DWUNIT = Mbps                    
                 FORBIDTPLID = 1                   
                SERAREATPLID = 1                            
                         MPS = FALSE                            
                         MCS = FALSE                       
                    DLBUFFER = 100                       
                    AUTHTYPE = 5G-AKA                    
                        MICO = FALSE                    
                  SMDATALIST = [{"SNSSAI":"123","ISDEFAULTSNSSAI":true,"DNNDATALIST":[{"DNN":"123","ISDEFAULTDNN":true,"DNNQOSTPLID":11},{"DNN":"123456","ISDEFAULTDNN":false,"DNNQOSTPLID":11}]},{"SNSSAI":"111","ISDEFAULTSNSSAI":false,"DNNDATALIST":[{"DNN":"111111","ISDEFAULTDNN":true,"DNNQOSTPLID":11}]},{"SNSSAI":"000-abcdef","ISDEFAULTSNSSAI":true}]
                    CHARGING = 0000
                 NREDRXVALUE = 1
           NRREDCAPEDRXVALUE = 1
              NRN1EXPTWVALUE = 1
          NRREDCAPEXPTWVALUE = 1

   Total count = 20

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NGSUSERTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                   | 原因分析                          | 处理建议                                                                                                                        |
|:--------|:------------------------|:------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义                   | “HLR序列号”和“模板ID”标识的5GS用户模板不存在。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”的组合，可通过LST HLRSN命令查询已定义的“HLR序列号”，使用本命令输入已定义“HLR序列号”参数，其他参数不输入，查询已定义“HLR序列号”和“模板ID”标识的5GS用户模板。 |
| ERR3097 | HLR序列号未定义               | 输入的“HLR序列号”未定义。               | 根据实际情况，重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN命令查询。                                                            |
| ERR4153 | 报文数量超过上限，需要指定保存文件名进行查询。 | 5GS用户模板信息的数量超过了5000个。         | 输入参数“保存文件名”，将查询结果保存在文件中。                                                                                                    |