# 查询短消息转发平台地址(LST SMFWDPLT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用来查询SMS Forwarding业务的短消息转发平台地址列表。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称      | 参数说明                                            |
|:----------|:----------|:------------------------------------------------|
| HLRSN     | HLR序列号    | 用于指示系统按照哪个HLR序列号来查询SMS Forwarding业务的短消息转发平台地址。  |
| SMFWDPLAT | 短消息转发平台地址 | 用于指示系统需要查询哪个短消息转发平台地址；若不输入，则表示查询所有的短消息转发平台地址列表。 |

## 使用实例

1. 要查询短消息转发平台地址列表，“HLR序列号”为“1”，“短消息转发平台地址”为“1234567891”：

   ```
   LST SMFWDPLT: HLRSN=1, SMFWDPLAT="1234567891";
   ```

   ```
   %%LST SMFWDPLT: HLRSN=1, SMFWDPLAT="1234567891";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "SMFWDPLAT"         "ISDEFAULT"      "FWDPLATNAME"
           1234567891          FALSE            default

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 要查询全部短消息转发平台地址列表，“HLR序列号”为“1”：

   ```
   LST SMFWDPLT: HLRSN=1;
   ```

   ```
   %%LST SMFWDPLT: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "SMFWDPLAT"         "ISDEFAULT"      "FWDPLATNAME"
           1234567890          FALSE            <NULL>
           1234567891          TRUE             <NULL>
           1234567892          FALSE            <NULL>

   Total count = 3

   There is together 1 report

   ---    END
   ```