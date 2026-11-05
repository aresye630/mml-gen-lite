# 查询模块(LST MODULE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询服务器Pod上的模块情况，使操作员了解当前UDM网元内模块的相关配置信息时。模块即Pod上运行的业务进程。

查询模块配置的相关方法如下：

- 若需要查询全部模块信息，请不要输入任何参数值。
- 若需要查询全部模块信息中符合某一参数条件的模块时，请在对应参数中输入对应的参数值。如：需要查询UDM30T\_HLR\_QHF的Pod上配置的所有模块信息时，请在参数“主用Pod名称”中输入对应的参数值“UDM30T\_HLR\_QHF”。
- 若需要查询全部模块信息中符合多个参数条件的模块时，请在对应的多个参数中输入对应的参数值。如：需要查询UDM30T\_HLR\_QHF的Pod上配置的所有DSG模块信息时，请在参数“主用Pod名称”中输入对应的参数值“UDM30T\_HLR\_QHF”，参数“模块类型”中输入对应值“DSG(DSG)”。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                  |
|:---------|:--------|:------------------------------------------------------|
| MID      | 模块号     | 用于指示系统需要按照哪个模块号来查询模块配置信息；若不输入，则表示所有的模块号。              |
| MT       | 模块类型    | 用于指示系统需要按照哪个模块类型来查询模块配置信息；若不输入，则表示所有的模块类型。            |
| APPTYPE  | 模块应用类型  | 仅当本命令中的“模块类型”参数为“CCU(CCU)”时该参数有效。用于指定一个模块的应用类型。       |
| PODNAME1 | 主用Pod名称 | 用于指示系统需要按照哪个主用进程所在Pod的名称来查询模块配置信息；若不输入，则表示所有的主用Pod名称。 |
| PODNAME2 | 备用Pod名称 | 用于指示系统需要按照哪个备用进程所在Pod的名称来查询模块配置信息；若不输入，则表示所有的备用Pod名称。 |
| MNAME    | 模块名称    | 用于指示系统需要按照哪个模块名称来查询模块配置信息；若不输入，则表示所有的模块名称。            |

## 使用实例

1. 查询所有模块的配置信息。

   ```
   LST MODULE:;
   ```

   ```
   %%LST MODULE:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    模块号  模块类型  模块应用类型  主用Pod名称                 备用Pod名称     模块名称

    
    41      DSG       NULL          UDM_VNF_10_UDMFEU_S_VDU_1_0  NULL            DSG41   
    42      DSG       NULL          UDM_VNF_10_UDMFEU_S_VDU_2_0  NULL            DSG42   
    61      CCU       ALL           UDM_VNF_10_UDMFEU_S_VDU_1_0  NULL            CCU61   
    62      CCU       ALL           UDM_VNF_10_UDMFEU_S_VDU_1_0  NULL            CCU62   
    63      CCU       ALL           UDM_VNF_10_UDMFEU_S_VDU_1_0  NULL            CCU63   
    67      HSF       NULL          UDM_VNF_10_UDMFEU_S_VDU_1_0  NULL            HSF67   
    71      CCU       ALL           UDM_VNF_10_UDMFEU_S_VDU_2_0  NULL            CCU71   
    72      CCU       ALL           UDM_VNF_10_UDMFEU_S_VDU_2_0  NULL            CCU72   
    73      CCU       ALL           UDM_VNF_10_UDMFEU_S_VDU_2_0  NULL            CCU73   
    77      HSF       NULL          UDM_VNF_10_UDMFEU_S_VDU_2_0  NULL            HSF77   
   (结果个数 = 10)

   ---    END
   ```
2. 以单一参数为条件进行查询。例如：查询“模块号”为“1”的模块的配置信息。

   ```
   LST MODULE: MID=1;
   ```

   ```
   %%LST MODULE: MID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
           模块号  =  41
         模块类型  =  DSG
     模块应用类型  =  NULL
      主用Pod名称  =  UDM_VNF_10_UDMFEU_S_VDU_1_0
      备用Pod名称  =  NULL
         模块名称  =  DSG41
   (结果个数 = 1)

   ---    END
   ```
3. 以多个参数为条件进行组合查询。例如：查询“模块类型”为“DSG(DSG)”且“主用Pod名称”为“UDM\_VNF\_10\_UDMFEU\_S\_VDU\_1\_0”的模块的配置信息。

   ```
   LST MODULE: MT=DSG, PODNAME1="UDM_VNF_10_UDMFEU_S_VDU_1_0";
   ```

   ```
   %%LST MODULE: MT=DSG, PODNAME1="UDM_VNF_10_UDMFEU_S_VDU_1_0";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    模块号  模块类型  模块应用类型  主用Pod名称                       备用Pod名称  模块名称

    41       DSG       NULL         UDM_VNF_10_UDMFEU_S_VDU_1_0       NULL          DSG41    
    
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD MODULE**命令的参数说明。