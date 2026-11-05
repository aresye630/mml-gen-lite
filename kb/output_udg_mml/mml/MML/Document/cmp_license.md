# 比较License(CMP LICENSE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于比较系统运行的License与指定的License文件、或者任意两个License文件中的信息。

## 注意事项

当待比较的两个License相同，并且客户端上该命令的参数“显示相同记录”选择“NO（否）”时，显示成功。

## 参数说明

| 参数标识    | 参数名称           | 参数说明                                                                                                                                                                                                                                                                  |
|:--------|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMPTYPE | 比较类型           | 可选必选说明：必选参数。 参数含义：用于请求系统按照哪种比较类型来进行License比较。 取值范围： “RUNLIC(系统运行中的License和License文件)”：用于比较当前系统中运行的License和指定的License文件。“FILELIC(License文件之间)”：用于比较任意两个License文件。 默认值：无。 配置原则：无。                                                                                       |
| FN      | License文件名称    | 可选必选说明：该参数在“比较类型”配置为“RUNLIC(系统运行中的License和License文件)”时为条件必选参数。 参数含义：用于当比较类型选择“RUNLIC(系统运行中的License和License文件)”时，输入待比较的License文件名。 取值范围：长度为6~311的字符串。文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。 默认值：无。 配置原则：确认文件在License文件管理界面存在。 |
| SRCFN   | 第一个License文件名称 | 可选必选说明：该参数在“比较类型”配置为“FILELIC(License文件之间)”时为条件必选参数。 参数含义：用于当比较类型选择“FILELIC(License文件之间)”时，输入第一个待比较的License文件名称。 取值范围：长度为6~311的字符串。文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。 默认值：无。 配置原则：确认文件在License文件管理界面存在。                   |
| DESFN   | 第二个License文件名称 | 可选必选说明：该参数在“比较类型”配置为“FILELIC(License文件之间)”时为条件必选参数。 参数含义：用于当比较类型选择“FILELIC(License文件之间)”时，输入第二个待比较的License文件名称。 取值范围：长度为6~311的字符串。文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。 默认值：无。 配置原则：确认文件在License文件管理界面存在。                   |
| DSPTYPE | 显示相同记录         | 可选必选说明：该参数在“比较类型”配置为“RUNLIC(系统运行中的License和License文件)”或“FILELIC(License文件之间)”时为条件必选参数。 参数含义：用于请求系统按照哪种类型来显示比较结果。 取值范围： “YES（是）”：用于请求系统将相同的控制项和不同的控制项都显示。“NO（否）”：用于请求系统只显示不同的控制项。 默认值：“NO（否）”。 配置原则：无。                                                                  |

## 使用实例

比较2.0版本License文件“license\_20\_1205.dat”和“license\_19\_1205.dat”：

```
%%CMP LICENSE: CMPTYPE=FILELIC, SRCFN="license_20_1205.dat", DESFN="license_19_1205.dat", DSPTYPE=YES;%% 
RETCODE = 0  操作成功  

License名称 
----------- 
第一个License文件名称  =  license_20_1205.dat 
第二个License文件名称  =  license_19_1205.dat 
(结果个数 = 1)  

基本信息比较结果 
----------------
控制项描述     第一个License的值                                    第二个License的值  
                                   
国家           India                                                India                                                 
运营商         LTE                                                  LTE                                                   
局点           htipl                                                htipl                                                 
创建者         haier Technologies Co., Ltd                          haier Technologies Co., Ltd                           
License序列号  LIC201909290XXXXX                                    LIC2019082406XXXXX                                     
创建时间       2015-01-01 10:30:00                                  2015-01-01 10:30:00                                   
产品           iXXXX                                                ioXXXX                                                  
设备序列号     0123456789                                           0123456789                                            
版本           V200R0XXXXXXXXXXX                                    V200R018C00XXXXX                                     
属性           DEMO, NULL, NULL, NULL, NULL, NULL                   DEMO, NULL, NULL, NULL, NULL, NULL                    
注释           Order XXXXXXXXXXXXXXXXXXXXXXXXXXX                    Order XXXXXXXXXXXXXX   
(结果个数 = 11)  

特征项比较结果 
-------------- 
特征项      控制项      控制项描述  第一个License的值                       第二个License的值 
                        
basic01     NULL        截止日期    2020-12-05                              2019-12-05                               
basic01     NULL        属性        DEMO, 2020-12-05, 60, NULL, NULL, NULL  DEMO, 2019-12-05, 60, NULL, NULL, NULL   
basic01     basicfun1   基本软件1   1000                                    1000                                     
basic01     basicfun2   基本软件2   1                                       1                                        
basic01     basicfun3   基本软件3   1000                                    1000                                                           
basic02     NULL        截止日期    2020-12-05                              2019-12-05                               
basic02     NULL        属性        DEMO, 2020-12-05, 60, NULL, NULL, NULL  DEMO, 2019-12-05, 60, NULL, NULL, NULL   
basic02     basicfun4   基本软件4   1                                       1                                        
basic02     basicfun5   基本软件5   1                                       1                                        
basic02     basicfun6   基本软件6   1000                                    1000                                     
basic02     basicfun7   基本软件7   1000                                    1000                                     
(结果个数 = 14) 

 ---    END
```

比较3.0版本License：

```
%%CMP LICENSE: CMPTYPE=FILELIC, SRCFN="license_c20_share_20191130.xml", DESFN="license_c20_share_20190601.xml", DSPTYPE=YES;%% 
RETCODE = 0  操作成功  

License名称 
----------- 
第一个License文件名称  =  license_c20_share_20191130.xml 
第二个License文件名称  =  license_c20_share_20190601.xml 
(结果个数 = 1)  

基本信息比较结果 
---------------- 
控制项描述     第一个License的值              第二个License的值 
               
国家           Sweden                         Sweden                          
运营商         Net4Mobility HB                Net4Mobility HB                 
局点           FRSLUNDA                       FRSLUNDA                        
创建者         Huawei Technologies Co., Ltd.  Huawei Technologies Co., Ltd.   
License序列号  LIC201900000XXXXX              LIC2017111601XXXXX              
创建时间       2019-06-05 18:20:57            2012-01-17 18:20:57             
产品           iXXXXX                         iXXXXX                            
设备序列号     0298100810                     0123456789                      
版本           V200R018CXXXXX                 V200R018CXXXXX               
(结果个数 = 9)  

销售项比较结果 
-------------- 
销售项        控制项      控制项描述  第一个License的值  第二个License的值   
 
LT1SRANSAA11  NULL        截止日期    2019-09-30         2019-06-01          
LT1SRANSAA11  basicres1   NULL        1000               500                 
LT1SRANSAA11  basicres2   NULL        1000               1000                
LT1SRANSAA11  basicfun1   NULL        1                  1                   
LT1SRANSDC09  NULL        截止日期    2019-09-30         2019-06-01          
LT1SRANSDC09  basicfun1   NULL        1                  1                   
LT1SRANSDC09  basicfun2   NULL        1                  1                   
LT1SRANSDC10  NULL        截止日期    2019-09-30         2019-06-01          
LT1SRANSDC10  basicfun3   NULL        1                  1                   
LT1SRANSDC10  basicfun4   NULL        1                  1                            
(结果个数 = 10)  

---    END
```

与系统运行中的License比较：

```
%%CMP LICENSE: CMPTYPE=RUNLIC, FN="license_c20_share_20191130.xml", DSPTYPE=YES;%% 
RETCODE = 0  操作成功 
 
License名称 
----------- 
系统运行的License  =  license_c20_share_20191201_50.xml   
  待比较的License  =  license_c20_share_20191130.xml
(结果个数 = 1)
  
基本信息比较结果
---------------- 
控制项描述     系统运行的License的值          待比较的License的值   
           
国家           Sweden                         Sweden                          
运营商         Net4Mobility HB                Net4Mobility HB                 
局点           FRSLUNDA                       FRSLUNDA                        
创建者         Huawei Technologies Co., Ltd.  Huawei Technologies Co., Ltd.   
License序列号  LIC2019000000XXXXX             LIC2017111601XXXXX              
创建时间       2019-06-05 18:20:57            2012-01-17 18:20:57             
产品           iXXXXXXX                       iXXXXX                            
设备序列号     0298100810                     0123456789                      
版本           V200R018CXXXXX                 V200R018CXXXXX               
(结果个数 = 9)  

销售项比较结果 
-------------- 
销售项        控制项      控制项描述  系统运行的License的值  待比较的License的值  
  
KVBS034PVB01  NULL        截止日期    2019-12-05             2019-12-01            
KVBS034PVB01  basicres1   NUll        3000                   50000                 
KVBS034PVB01  basicres2   NUll        3000                   50000                                 
KVBS034PVB01  basicfun1   NUll        1                      1                     
KVBS034PVB01  basicfun2   NUll        1                      1                                    
KVBS034PVC01  NULL        截止日期    2019-12-05             2019-12-01            
KVBS034PVC01  basicres3   NUll        3000                   50000                 
KVBS034PVG01  NULL        截止日期    2019-12-05             2019-12-01            
KVBS034PVG01  basicres4   NUll        3000                   50000                 
KVBS034PVG01  basicres5   NUll        3000                   50000                 
KVBS034PVG01  basicfun3   NUll        1                      1   
(结果个数 = 11)  

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息，输出项说明如表1所示。

该命令执行异常，会返回对应的错误码及错误码解释信息。常见错误码列表如表2 错误码列表所示。

| 输出项名称       | 输出项解释                      |
|:------------|:---------------------------|
| License名称   | License文件的名称。              |
| 基本信息比较结果    | License的公共段和service段的比较结果。 |
| 特征性/销售项比较结果 | License的控制项的比较结果。          |

|    错误码 | 错误码解释                                                                                           | 原因分析                                                                                             | 处理建议                                  |
|-------:|:------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:--------------------------------------|
| 100801 | 系统内部异常                                                                                          | 安装过程中可能存在网络故障或者其他导致License服务不可用的异常因素。                                                            | 等待几分钟后，重新执行。如果重新执行返回失败，请联系华为技术支持处理。   |
| 100803 | 请求参数无效                                                                                          | 界面请求异常，参数缺失，或者不合法。                                                                               | 等待几分钟后，重新执行。如果重新执行返回失败，请联系华为技术支持处理。   |
| 100810 | License文件不存在，请先上传License文件                                                                      | License文件未上传。                                                                                    | 请先上传License文件。                        |
| 100831 | 比较License失败                                                                                     | 可能存在网络故障或者其他导致License服务不可用等异常因素，出现此种情况。                                                          | 等待几分钟后，重新执行。如果重新执行返回失败，请联系华为技术支持处理。   |
| 100839 | 当前没有激活的License文件，无法比较                                                                           | 应用未激活。                                                                                           | 应用尚未激活，无法按照系统运行中的License和License文件比较。 |
| 100840 | License文件版本号不一致，无法比较                                                                            | License文件版本号不一致。                                                                                 | 请使用相同版本的License文件。                    |
| 100841 | 第一个License文件不存在，请先上传License文件                                                                   | License文件未上传。                                                                                    | 请先上传License文件。                        |
| 100842 | 第二个License文件不存在，请先上传License文件                                                                   | License文件未上传。                                                                                    | 请先上传License文件。                        |
| 100843 | License文件名称无效，文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML    | License文件名称无效，文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。    | 重新上传正确格式的License文件。                   |
| 100844 | 第一个License文件名称无效，文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML | 第一个License文件名称无效，文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。 | 重新上传正确格式的License文件。                   |
| 100845 | 第二个License文件名称无效，文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML | 第二个License文件名称无效，文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。 | 重新上传正确格式的License文件。                   |