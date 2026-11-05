# 查询VPN信息配置(LST VPNINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询数据库中VPNINFO数据记录。

- 若需要查询所有VPN信息配置，请不输入任何参数。
- 若需要查询某个VPN信息配置，请输入“VPNINFO名称”。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                          |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| VPNINFONAME | VPNINFO名称 | 可选必选说明：可选参数。 参数含义：用于指示系统按照哪个VPNINFO名称来查询VPN信息配置数据；若不输入，则表示查询所有的VPNINFO名称。 取值范围：长度不超过128的由数字和字母组成的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有VPN信息：

   ```
   LST VPNINFO:;
   ```

   ```
   %%LST VPNINFO:;%%
   RETCODE = 0  操作成功

   VPNINFO名称  VPN名称          VPN ID  VPN属性

   vpn1         VRF_T_Signaling  2       MobileNetwork
   vpn2         VRF_T_Name       3       MobileNetwork
   (结果个数 = 2)

   ---    END
   ```
2. 查询“VPNINFO名称”为“vpn1”的信息：

   ```
   LST VPNINFO: VPNINFONAME="vpn1";
   ```

   ```
   %%LST VPNINFO: VPNINFONAME="vpn1";%%
   RETCODE = 0  操作成功

   VPNINFO名称  =  vpn1
       VPN名称  =  VRF_T_Signaling
        VPN ID  =  2
       VPN属性  =  MobileNetwork
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD VPNINFO**命令的参数说明。