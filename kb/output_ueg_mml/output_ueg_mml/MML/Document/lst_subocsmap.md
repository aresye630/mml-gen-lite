# 查询OCS映射（LST SUBOCSMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UPCF配置数据库中用户扩展属性或消息属性OCS映射的配置信息。

- 如果需要查询全部的OCS映射记录，则不要输入任何参数。
- 如果需要查询指定的OCS映射记录，请输入“映射ID”或其它参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAPID        | 映射ID          | 用于指示UPCF需要按照哪个映射ID来查询OCS映射配置信息；若不输入，则表示查询所有的映射ID。 取值范围：0～1023 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| OCSRT        | OCS路由类型       | 用于标识OCS路由类型。 取值范围： SubscriberAttribute（Subscriber Attribute）MessageAttribute（Message Attribute） 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SUBATTR      | 用户属性          | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”时该参数有效，用于指示UPCF需要按照哪个用户属性来查询OCS映射配置信息；若不输入，则表示查询所有的用户属性。 取值范围： usrExAttr1（用户扩展属性1） usrExAttr2（用户扩展属性2） usrExAttr3（用户扩展属性3） usrExAttr4（用户扩展属性4） usrExAttr5（用户扩展属性5） usrExAttr6（用户扩展属性6） usrExAttr7（用户扩展属性7） usrExAttr8（用户扩展属性8） usrExAttr9（用户扩展属性9） usrExAttr10（用户扩展属性10） usrExAttr11（用户扩展属性14） usrExAttrStr1(用户扩展属性11) usrExAttrStr2(用户扩展属性12) usrExAttrStr3(用户扩展属性13) usrExAttrStr4(用户扩展属性15) usrExAttrStr5(用户扩展属性16) usrExAttrStr6(用户扩展属性17) usrExAttrStr7(用户扩展属性18) usrExAttrStr8(用户扩展属性19) usrExAttrStr9(用户扩展属性20) 缺省值：无。 |
| ATTRVALUE    | 用户属性值         | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”且“用户属性”参数取值为“usrExAttr1”～“usrExAttr11”时该参数有效，用于指示UPCF需要按照哪个用户属性值来查询OCS映射配置信息；若不输入，则表示查询所有的用户属性值。 取值范围：0～65535，4294967295usrExAttr1～usrExAttr10取值范围：0～255。其中，0～254为用户开户时的有效取值范围，即可以配置的用户属性值；255为用户开户时不填属性值时，系统设置的值。usrExAttr11取值范围：0～65535，4294967295。其中，0～65535为用户开户时的有效取值范围，即可以配置的用户属性值；4294967295为用户开户时不填属性值时，系统设置的值。 缺省值：无。  说明： 4294967295在LST SUBOCSMAP命令查询显示结果为“NULL”。                                                                                                                                                  |
| ATTRSTRVALUE | 用户字符串属性值      | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”且“用户属性”参数取值为“usrExAttrStr1”～“usrExAttrStr9”时该参数有效，用于标识映射用户扩展属性的值。 取值范围：长度不超过64的字符串。 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PEERTYPE     | 对端类型          | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”时该参数有效，用于指示UPCF需要按照哪个对端类型来查询用户属性OCS映射配置信息；若不输入，则表示查询所有的对端类型。 取值范围：OCS（OCS）DRA（DRA） 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| REALM        | OCS域名         | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”时该参数有效，用于指示UPCF需要按照哪个OCS域名来查询用户属性OCS映射配置信息；若不输入，则表示查询所有的OCS域名。 取值范围：长度不超过64的字符串。 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DESTREALM    | 目的OCS域名       | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”且“对端类型”参数为“DRA（DRA）”时该参数有效，用于标识映射目的OCS域名。 设置该参数前，需根据现网环境提前获取对应厂家OCS的域名。该参数设置后，不支持修改。 取值范围：长度不超过64的字符串。 默认值：无。  说明： 若Sy功能域路由不是默认路由，则该参数不生效。                                                                                                                                                                                                                                                                                                                                                                                    |
| MSGATRRT     | 消息属性类型        | 仅当本命令中的“OCS路由类型”参数为“MessageAttribute（Message Attribute）”时该参数有效，用于指示UPCF需要按照哪个消息属性类型来查询消息属性OCS映射配置信息；若不输入，则表示查询所有的消息属性类型。 取值范围： DefaultAPNMSISDNIMSIMSISDN_APNIMSI_APN 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                                |
| APNNAME      | APN名称         | 仅当本命令中的“OCS路由类型”参数为“MessageAttribute（Message Attribute）”，且“消息属性类型”参数为“APN”或“MSISDN_APN”或“IMSI_APN”时该参数有效，用于指示UPCF需要按照哪个APN名称来查询消息属性OCS映射配置信息；若不输入，则表示查询所有的APN名称。 取值范围：长度不超过32的字符串。 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                   |
| PREFIX       | IMSI/MSISDN前缀 | 仅当本命令中的“OCS路由类型”参数为“MessageAttribute（Message Attribute）”，且“消息属性类型”参数为“MSISDN”或“IMSI”或“MSISDN_APN”或“IMSI_APN”时该参数有效，用于指示UPCF需要按照哪个IMSI/MSISDN前缀来查询消息属性OCS映射配置信息；若不输入，则表示查询所有的IMSI/MSISDN前缀。 取值范围：长度不超过15的数字字符串。 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                       |
| OCSID        | OCS ID        | 仅当本命令中的“OCS路由类型”参数为“MessageAttribute（Message Attribute）”时该参数有效，用于指示UPCF需要按照哪个OCS ID来查询消息属性OCS映射配置信息；若不输入，则表示查询所有的OCS ID。 此参数必须先由ADD POCSCP命令定义OCS“接入点标识”，然后才能在此处索引。 取值范围：0～15 缺省值：无。                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRI          | Priority      | 仅当本命令中的“OCS路由类型”参数为“SubscriberAttribute（Subscriber Attribute）”并且“对端类型”为“OCS（OCS）”时该参数有效，用于表示用户扩展属性的优先级。 配置原则：设置的优先级值越小，则其优先级越高。如果同一个用户扩展属性的Priority取值相同则优先级相同。 取值范围：0～255 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                            |

## 使用实例

1. 查询所有的用户属性OCS映射的配置信息。

   ```
   LST SUBOCSMAP:;
   ```

   ```
   %%LST SUBOCSMAP:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   ---------------
    映射ID    OCS路由类型              用户属性            用户属性值    对端类型    OCS域名

    2         Subscriber Attribute     用户第一扩展属性    0             DRA         huawei.com
    1         Subscriber Attribute     用户第一扩展属性    255           OCS         huawei.com
   （结果个数 = 2）

   ---    END
   ```
2. 查询指定的用户属性OCS映射的配置信息，“映射ID”为“1”。

   ```
   LST SUBOCSMAP: MAPID=1;
   ```

   ```
   %%LST SUBOCSMAP: MAPID=1;%%
   RETCODE = 0  操作成功

   操作结果如下:
   ---------------
        映射ID  =  1
   OCS路由类型  =  Subscriber Attribute
      用户属性  =  用户第一扩展属性
    用户属性值  =  255
      对端类型  =  OCS
       OCS域名  =  huawei.com
   （结果个数 = 1）

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD SUBOCSMAP**命令的参数说明。