# 查询NRF公钥（LST NRFKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已配置的NRF公钥信息。

- 若需要查询所有配置的NRF公钥配置信息，请不要输入任何参数。
- 若需要查询某个NRF公钥配置信息，请输入“公钥ID”或“NRF实例ID”。

## 注意事项

无。

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                            |
|:--------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| NRFKEYID      | 公钥ID    | 可选必选说明：可选参数。 参数含义：用于指定公钥在系统内的唯一标识。用于指定系统按照哪个公钥ID查询NRF公钥信息；若不输入，则表示查询所有公钥ID的NRF公钥配置信息。 取值范围：1～32 默认值：无。 配置原则：无。                                  |
| NRFINSTANCEID | NRF实例ID | 可选必选说明：可选参数。 参数含义：用于指定系统按照哪个NRF实例ID查询NRF公钥信息；若不输入，则表示查询所有NRF实例ID的NRF公钥配置信息。 取值范围：长度不超过127位的字符串 默认值：无。 配置原则：无。                                   |
| SNDKEYID      | NRF密钥ID | 可选必选说明：可选参数 参数含义：该参数表示NRF上配置的密钥ID，用于在TOKEN管理中标识当前生效的密钥。 数据来源：对端规划 取值范围：长度不超过128位的字符串，区分大小写。 默认值：无 配置原则：当需要在TOKEN校验时检查接收报文中当前生效的NRF密钥ID信息时配置此字段。 |

## 使用实例

1. 查询所有配置的NRF公钥配置信息。

   ```
   LST NRFKEY:;
   ```

   ```
   %%LST NRFKEY:;%%
   RETCODE = 0  操作成功

   操作结果如下;
   -------------------------
                     公钥ID  =  1
                NRF实例标识  =  8a6bd00f-c9af-4ebe-9184-0221f24ed040
                   NRF密钥ID = xxxxxxx
                       公钥  =  -----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ==-----END PUBLIC KEY-----
   (结果个数 = 1)
   ---    END
   ```
2. 查询“公钥ID”为“11”的公钥配置信息。

   ```
   LST NRFKEY: NRFKEYID=11;
   ```

   ```
   %%LST NRFKEY: NRFKEYID=11;%% 
   RETCODE = 0  操作成功

   操作结果如下;
   -------------------------
                公钥ID  =  11
           NRF实例标识  =  0221f24ed04
              NRF密钥ID = xxxxxxx
                  公钥  =  -----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ-----END PUBLIC KEY----- 
   (结果个数 = 1)  
   ---    END
   ```
3. 查询“NRF实例ID”为“0221f24ed04”的公钥配置信息。

   ```
   LST NRFKEY: NRFINSTANCEID="0221f24ed04";
   ```

   ```
   %%LST NRFKEY: NRFINSTANCEID="0221f24ed04";%% 
   RETCODE = 0  操作成功

   操作结果如下;
   -------------------------
                公钥ID  =  11
           NRF实例标识  =  0221f24ed04
              NRF密钥ID = xxxxxxx
                  公钥  =  -----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqLN3xmUoBeozpev3cF+sMtealu22AukFrLIjatB9TQV+ZIXN1/8hzCJXcvvOerBghzci7E/ZIHgpG595CiN8XwwyaFBJpBNLPMFK1xpkjvt/mAnRLrRGwcs5S7911Egsgi8JKsAHpXbMC6Ji5qAsIRhLvV7hr7j0ptd3l6g7Kpp4m0Ypp9K4bSnIQjVhMe160BZ7Iy4E4xVPzYc3lXLE2atCc1acAi3inOKt+Vi8Uaw5NqcpiCl4BiAwjJVkzBIjQw/Py1yFLrPWBZmXvQ1u8Ry520AM7pbUB03xisUdSpfGJtj7UATRmS5HLcVVkH+w4dwmcR9ZS13rSdg4VlDUURvkQEDD98y5TNgpr9sTNXKb4mgb9eEymkrSb/erHCsbnUDmDrwWIO5LF3hY/OjWDkns8fId2pmWYyXSOv9Nb7I6h/rkvSxt1zEuYmP7GKusJqcMiQqTUUYLZuQMJDpCdO2BCtPNoWlhX4MUNBpMsq5IB0KuA27NwKtSrOsafJs4/L/+IDl0sCbHg49uYKXVP2z3o9RSY3luPJcfR9VNF9lmmK0lqSxAB1eNvSlzoDHzgx2H/NjuIkP8WUh+/qxvWIgoR+nmL86c7PjF5kDNf5XgnKCxuDVa3yb4ZkAooEVwceQkxz2+GZssOsHEu48L4jFGctwCBmapPb666h0CAwEAAQ-----END PUBLIC KEY----- 
   (结果个数 = 1)  
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NRFKEY**命令的参数说明。