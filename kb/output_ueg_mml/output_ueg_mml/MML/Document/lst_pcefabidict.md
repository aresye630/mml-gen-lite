# 查询PCRF对端PCEF能力字典配置信息(LST PCEFABIDICT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于在配置数据库中查询对端PCEF实体能力字典的配置信息。如果需要查询全部PCEF能力字典的配置信息，请不要输入任何参数；如果需要查询某个PCEF能力字典的配置信息，请依据参数说明输入查询条件。

## 注意事项

无。

## 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                               |
|:----------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| ABILITYDICTID   | 能力字典ID | 用于标识PCEF能力字典的编号。 取值范围： 0~127 取值说明：63~127为预置数据，其中63为TDF，64为HuaweiGGSN，65为HuaweiSymaSIG，66为AllotPCEF，67为HuaweiGGSNR9，68为HuaweiPDNGW，69~127预留。 默认值： 无 |
| ABILITYDICTNAME | 能力字典名  | 用于具体描述一个PCEF能力字典的名称，以便于识别。其值域类型为字符串，不区分大小写。 取值范围： 长度不超过32的字符串 默认值： 无                                                                               |

## 使用实例

1. 查询所有PCEF能力字典的配置信息。

   ```
   LST PCEFABIDICT:;
   ```

   ```
   %%LST PCEFABIDICT:;%% 
   RETCODE = 0 操作成功

   操作结果如下:
   ------------------------
    能力字典ID              能力字典名称

    64                     HUAWEIGGSN             
    65                     HUAWEISYMASIG          
    66                     ALLOTPCEF              
    67                     HUAWEIGGSNR9           
    68                     HUAWEIPDNGW            
    69                     ABILITYDICTIONARY69    
    70                     ABILITYDICTIONARY70    
    71                     ABILITYDICTIONARY71    
    72                     ABILITYDICTIONARY72    
    73                     ABILITYDICTIONARY73    
    74                     ABILITYDICTIONARY74    
    75                     ABILITYDICTIONARY75    
    76                     ABILITYDICTIONARY76    
    77                     ABILITYDICTIONARY77    
    78                     ABILITYDICTIONARY78    
    79                     ABILITYDICTIONARY79    
    80                     ABILITYDICTIONARY80    
    81                     ABILITYDICTIONARY81    
    82                     ABILITYDICTIONARY82    
    83                     ABILITYDICTIONARY83    
    84                     ABILITYDICTIONARY84    
    85                     ABILITYDICTIONARY85    
    86                     ABILITYDICTIONARY86    
    87                     ABILITYDICTIONARY87    
    88                     ABILITYDICTIONARY88    
    89                     ABILITYDICTIONARY89    
    90                     ABILITYDICTIONARY90    
    91                     ABILITYDICTIONARY91    
    92                     ABILITYDICTIONARY92    
    93                     ABILITYDICTIONARY93    
    94                     ABILITYDICTIONARY94    
    95                     ABILITYDICTIONARY95    
    96                     ABILITYDICTIONARY96    
    97                     ABILITYDICTIONARY97    
    98                     ABILITYDICTIONARY98    
    99                     ABILITYDICTIONARY99    
    100                    ABILITYDICTIONARY100   
    101                    ABILITYDICTIONARY101   
    102                    ABILITYDICTIONARY102   
    103                    ABILITYDICTIONARY103   
    104                    ABILITYDICTIONARY104   
    105                    ABILITYDICTIONARY105   
    106                    ABILITYDICTIONARY106   
    107                    ABILITYDICTIONARY107   
    108                    ABILITYDICTIONARY108   
    109                    ABILITYDICTIONARY109   
    110                    ABILITYDICTIONARY110   
    111                    ABILITYDICTIONARY111   
    112                    ABILITYDICTIONARY112   
    113                    ABILITYDICTIONARY113   
    114                    ABILITYDICTIONARY114   
    115                    ABILITYDICTIONARY115   
    116                    ABILITYDICTIONARY116   
    117                    ABILITYDICTIONARY117   
    118                    ABILITYDICTIONARY118   
    119                    ABILITYDICTIONARY119   
    120                    ABILITYDICTIONARY120   
    121                    ABILITYDICTIONARY121   
    122                    ABILITYDICTIONARY122   
    123                    ABILITYDICTIONARY123   
    124                    ABILITYDICTIONARY124   
    125                    ABILITYDICTIONARY125   
    126                    ABILITYDICTIONARY126   
    127                    ABILITYDICTIONARY127   
   (Number of results = 64)

   ---    END
   ```
2. 查询一条PCEF能力字典的配置信息。“能力字典ID”为“64”。

   ```
   LST PCEFABIDICT: ABILITYDICTID=64;
   ```

   ```
   %%LST PCEFABIDICT: ABILITYDICTID=64;%% 
   RETCODE = 0 操作成功 

   操作结果如下:
   ------------------------ 
   能力字典ID  = 64
   能力字典名称 = HuaweiGgsn 
   (Number of results = 1) 
   --- END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见本命令的参数说明。