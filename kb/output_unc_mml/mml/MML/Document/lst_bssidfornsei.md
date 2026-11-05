# 查询NSEI和BSSID值的对应关系(LST BSSIDFORNSEI)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

此命令用于查询NSEI和BSSID值的对应关系。只适用于Gb over IP自动配置的场景。

#### 注意事项

- 此命令执行后立即生效。
- 当一组NSE与BSSID值的对应关系“BSSIDRULE”不是“NSEI\_MAP\_SPECIFIC\_BSSID(指定BSSID)”时，“BSS标识”显示为NULL。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                            |
|:-------|:--------|:----------------------------------------------------------------------------------------------------------------|
| NSEI   | 起始NSE标识 | 可选必选说明：可选参数 参数含义：该参数用于指定待查询NSEI和BSSID值对应关系的网络服务实体起始标识。 取值范围：0～65535 默认值：无  说明： 本参数为ADD BSSIDFORNSEI中存在的起始NSE标识。 |

#### 使用实例

1. 查询所有NSEI和BSSID值的对应关系：

   LST BSSIDFORNSEI:;

   ```
   LST BSSIDFORNSEI:;%%
   RETCODE = 0  操作成功。

   操作结果如下
   --------------
   起始NSE标识  结束NSE标识   BSSID与NSEI的对应关系  BSS标识
   0            5             指定BSSID              2
   7            8             NSEI去掉前3位          NULL
   (结果个数 = 2)

   ---    END
   ```
2. 查询“ 起始NSE标识 ”为“0”的记录：

   LST BSSIDFORNSEI: NSEI=0;

   ```
   %%LST BSSIDFORNSEI: NSEI=0;%%
   RETCODE = 0  操作成功。

   操作结果如下
   --------------
             起始NSE标识  =  0
             结束NSE标识  =  5
   BSSID与NSEI的对应关系  =  指定BSSID
                 BSS标识  =  2
   (结果个数 = 1)

   ---    END
   ```

#### 输出结果说明

参见**ADD BSSIDFORNSEI**的参数说明。