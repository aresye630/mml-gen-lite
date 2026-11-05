# 查询用户小区信息（LST PSUBLOCFLITER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户已签约业务记录的小区信息。查询时如果有多条小区信息，则返回多条记录。

## 注意事项

无。

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                         |
|:--------------|:-------|:---------------------------------------------|
| USRIDENTIFIER | 用户标识   | 用于指定需要查询哪个用户的小区信息。 取值范围：长度不超过255的字符串。 默认值：无。 |

## 使用实例

查询用户的小区信息，“USRIDENTIFIER”为“46010381012\*\*\*\*”。

```
LST PSUBLOC: USRIDENTIFIER="46010381012****";
```

```
%%LST PSUBLOCFLITER: USRIDENTIFIER="46010381012****";%% 
RETCODE = 0 Operation succeeded  
Service Name                      UsrLocationType   SAC1    SAC2   SAC3   SAC4   SAC5   SAC6   SAC7   SAC8   SAC9   SAC10   SAC11   SAC12   SAC13   SAC14   SAC15   SAC16   SAC17   SAC18   SAC19   SAC20   SAC21   SAC22   SAC23   SAC24   SAC25   SAC26   SAC27   SAC28   SAC29   SAC30   SAC31   SAC32   ECI1        ECI2   ECI3   ECI4   ECI5   ECI6   ECI7   ECI8   ECI9   ECI10   ECI11   ECI12   ECI13   ECI14   ECI15   ECI16   ECI17   ECI18   ECI19   ECI20   ECI21   ECI22   ECI23   ECI24   ECI25   ECI26   ECI27   ECI28   ECI29   ECI30   ECI31   ECI32 
5GFUP_Service                     1                 69877   NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL        NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL 
5GFUP_Service                     0                 NULL    NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    123456789   NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL   NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL    NULL   
Total count = 2  
There is together 1 report  
---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。查询结果中各参数的含义如表1所示。

| 输出项名称           | 输出项解释                                              |
|:----------------|:---------------------------------------------------|
| Service Name    | 用于表示业务名称。 取值范围：长度不超过64的字符串。                        |
| UsrLocationType | 用于表示用户已签约业务记录的位置信息类型。 取值范围： 0：表示4G位置信息。1：表示3G位置信息。 |
| SAC1-SAC32      | 用于表示用户已签约业务记录的3G小区信息。 取值范围：长度为1～5的十进制数字。           |
| ECI1-ECI32      | 用于表示用户已签约业务记录的4G小区信息。 取值范围：长度为1～9的十进制数字。           |