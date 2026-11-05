# 查询PCRF对端AF能力字典配置信息(LST AFABIDICT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于在配置数据库中查询对端AF实体能力字典的配置信息：

- 如果需要查询全部AF能力字典的配置信息，请不要输入任何参数。
- 如果需要查询某个AF能力字典的配置信息，请依据参数说明输入查询条件。

## 注意事项

无。

## 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                        |
|:----------------|:-------|:--------------------------------------------------------------------------------------------|
| ABILITYDICTID   | 能力字典ID | 用于指示系统需要按照哪个能力字典ID来查询AF能力字典配置信息；若不输入，则表示所有的能力字典ID。 取值范围： 0～127 默认值： 无                       |
| ABILITYDICTNAME | 能力字典名  | 用于指示系统需要按照哪个能力字典名来查询AF能力字典配置信息；若不输入，则表示所有的能力字典名。其值域类型为字符串，不区分大小写。 取值范围： 长度不超过32的字符串。 默认值： 无 |

## 使用实例

1. 查询所有AF能力字典的配置信息。

   ```
   LST AFABIDICT:;
   ```

   ```
   %%LST AFABIDICT:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
    能力字典ID  能力字典名 

    0           AF         
    1           RESTFULAF  
    2           AFABIDICT2 
    3           AFABIDICT3 
    4           AFABIDICT4 
    5           AFABIDICT5 
    6           AFABIDICT6 
    7           AFABIDICT7 
    8           AFABIDICT8 
    9           AFABIDICT9 
    10          AFABIDICT10
    11          AFABIDICT11
    12          AFABIDICT12
    13          AFABIDICT13
    14          AFABIDICT14
    15          AFABIDICT15
    16          AFABIDICT16
    17          AFABIDICT17
    18          AFABIDICT18
    19          AFABIDICT19
    20          AFABIDICT20
    21          AFABIDICT21
    22          AFABIDICT22
    23          AFABIDICT23
    24          AFABIDICT24
    25          AFABIDICT25
    26          AFABIDICT26
    27          AFABIDICT27
    28          AFABIDICT28
    29          AFABIDICT29
    30          AFABIDICT30
    31          AFABIDICT31
    67          TEST       
   (结果个数 = 33)

   ---    END
   ```
2. 查询一条AF能力字典的配置信息。“能力字典ID”为“30”。

   ```
   LST AFABIDICT: ABILITYDICTID=30;
   ```

   ```
   %%LST AFABIDICT: ABILITYDICTID=30;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   能力字典ID  =  30
   能力字典名  =  AFABIDICT30

   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

请参见**ADD AFABIDICT**命令的参数说明。