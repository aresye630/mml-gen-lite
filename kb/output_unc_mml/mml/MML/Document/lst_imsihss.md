# 查询IMSI-HSS对应关系(LST IMSIHSS)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

此命令用于查看IMSI（International Mobile Subscriber Identity）与HSS（Home Subscriber Server）的映射关系表记录。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                             |
|:--------|:-------|:---------------------------------------------------------------------------------------------------------------------------------|
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数 参数含义：待查询的IMSI前缀。 数据来源：全网规划 取值范围：1～15位数字 默认值：无 配置原则：无  说明： IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

#### 使用实例

1. 查询系统内IMSI前缀为12301070001与HSS的映射关系表的最大匹配记录：

   LST IMSIHSS: IMSIPRE="12301070001";

   ```
   %%LST IMSIHSS: IMSIPRE="12301070001";%%
   RETCODE = 0  操作成功。

   IMSI和HSS映射表
   ---------------
             IMSI前缀  =  12301070001
              HSS域名  =  example.com
   Diameter路由组索引  =  0
         移动网络名称  =  noname
   (结果个数 = 1)

   ---    END
   ```
2. 查询系统内所有的IMSI与HSS的映射关系表记录：

   LST IMSIHSS:;

   ```
   %%LST IMSIHSS:;%%
   RETCODE = 0  操作成功。

   IMSI和HSS映射表
   ---------------
    IMSI前缀    HSS域名         　　　　　　          Diameter路由组索引    移动网络名称

    1230107000  example.com                           0                     noname      
    1230107     example01.com                         0                     noname      
   (结果个数 = 2)

   ---    END
   ```

#### 输出结果说明

参见**ADD IMSIHSS**的参数说明。