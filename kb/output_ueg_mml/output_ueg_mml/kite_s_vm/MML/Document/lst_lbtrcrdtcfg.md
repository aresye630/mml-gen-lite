# 查询跟踪重定向（LST LBTRCRDTCFG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询跟踪重定向参数配置。

#### 注意事项

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                            |
|:-------|:-------|:----------------------------------------------------------------|
| INDEX  | 重定向索引  | 可选必选说明：可选参数 参数含义：该参数用于指定跟踪重定向参数配置的索引。 数据来源：本端规划 取值范围：1~32 默认值：无 |

#### 使用实例

1. 查询所有已添加跟踪重定向配置。

   LST LBTRCRDTCFG:;

   ```
   %%LST LBTRCRDTCFG:;%%
   RETCODE = 0  操作成功。

   操作结果如下：
   --------------
   重定向索引  VPN      IP地址类型  源IPv4地址  源IPv6地址   源端口号    目的IPv4地址    目的IPv6地址   
   目的端口号    描述       

   1          trcrdt     IPv4       10.0.0.0    2001:0db8::   32676      10.255.255.255   2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   32768         Redirection
   2          trcrdt1    IPv4       10.0.0.0    2001:0db8::   10000      10.255.255.255   2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   10000         DyeTrace1  
   3          trcrdt2    IPv4       10.0.0.0    2001:0db8::   10000      10.255.255.255   2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   10000         DyeTrace2  
   4          trcrdt3    IPv4       10.0.0.0    2001:0db8::   10000      10.255.255.255   2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   10000         DyeTrace3  
   5          trcrdt4    IPv6       10.0.0.0    2001:0db8::   10000      10.255.255.255   2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   10000         DyeTrace4  
   (结果个数 = 5)
   ---    END
   ```
2. 查询INDEX为2的跟踪重定向参数配置。

   LST LBTRCRDTCFG: INDEX=2;

   ```
   %%LST LBTRCRDTCFG: INDEX=2;%%
   RETCODE = 0  操作成功。

   操作结果如下：
   --------------
     重定向索引  =  2
            VPN  =  trcrdt1
     IP地址类型  =  IPv4
   源IPv4地址    =  10.0.0.0
     源IPv6地址  =  2001:0db8::
       源端口号  =  10000
   目的IPv4地址  =  10.255.255.255
   目的IPv6地址  =  2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
     目的端口号  =  10000
           描述  =  DyeTrace1
   (结果个数 = 1)
   ---    END
   ```

#### 输出结果说明

参见**ADD LBTRCRDTCFG**的参数说明。