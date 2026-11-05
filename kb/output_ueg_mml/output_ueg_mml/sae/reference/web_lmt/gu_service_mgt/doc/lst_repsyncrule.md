# 查询透明数据同步规则(LST REPSYNCRULE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询透明数据同步规则数据记录。

## 注意事项

该命令用只允许通过以下几种方式查询透明数据同步规则数据：

- 不输入参数，查询所有记录。
- 仅输入“记录索引”。
- 仅输入“规则类型”。
- 仅输入“透明数据同步规则ID”
- 仅输入“透明数据同步规则ID”和“服务标识”

## 参数说明

| 参数标识   | 参数名称       | 参数说明                                                                                                                      |
|:-------|:-----------|:--------------------------------------------------------------------------------------------------------------------------|
| INDEX  | 记录索引       | 可选必选说明：可选参数 参数含义：用于指定根据哪个索引来查询透明数据同步规则。 取值范围：1～65534 默认值：无。 配置原则：无。                                                       |
| RULEID | 透明数据同步规则ID | 可选必选说明：可选参数 参数含义：用于标识查询透明数据同步规则ID的同步规则。 取值范围：1～65534 默认值：无。 配置原则：无。                                                       |
| TYPE   | 规则类型       | 可选必选说明：可选参数 参数含义：用于标识查询哪种类型的透明数据同步规则。 取值范围： Global：全局规则SubBasis：用户级同步规则 默认值：无。 配置原则：无。                                    |
| SRVIND | 服务标识       | 可选必选说明：可选参数 参数含义：用于标识查询哪个服务标识对应的透明数据同步规则。如果存在字符“=”、“;”、“\”、“,”、“"”和“'”，需要在该字符前添加转义字符“\”。 取值范围：长度不超过127的字符串 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有透明数据同步规则：

   ```
   LST REPSYNCRULE:;
   ```

   ```
   LST REPSYNCRULE:;  
   RETCODE = 0  操作成功。
   结果如下:
   -------------------------
   INDEX   RULEID   TYPE         SRVIND  PROV
   1       1        Global       glb     TRUE
   2       2        SubBasis     456     FALSE
   3       3        SubBasis     abc     FALSE
   4       3        SubBasis     def     FALSE
   5       3        SubBasis     ghi     FALSE

   (结果个数 = 5)
   ---    END
   ```
2. 查询“记录索引”为“1”的透明数据同步规则：

   ```
   RMV REPSYNCRULE:INDEX=1;
   ```

   ```
   LST REPSYNCRULE:INDEX=1;
   RETCODE = 0  操作成功。 
   结果如下:
   -------------------------
   INDEX   RULEID   TYPE         SRVIND   PROV
   1       3        SubBasis     abc      FALSE
   (结果个数 = 1)
   ---    END
   ```
3. 查询“规则类型”为“SubBasis”的透明数据同步规则：

   ```
   LST REPSYNCRULE: TYPE = SubBasis;
   ```

   ```
   LST REPSYNCRULE: TYPE = SubBasis; 
   RETCODE = 0  操作成功。
   结果如下:
   -------------------------
   INDEX   RULEID   TYPE         SRVIND  PROV
   2       2        SubBasis     456     FALSE
   3       3        SubBasis     abc     FALSE
   4       3        SubBasis     def     FALSE
   5       3        SubBasis     ghi     FALSE

   (结果个数 = 4)
   ---    END
   ```
4. 查询“透明数据同步规则ID”为“3”的透明数据同步规则：

   ```
   LST REPSYNCRULE:RULEID=3;
   ```

   ```
   LST REPSYNCRULE:RULEID=3; 
   RETCODE = 0  操作成功。
   结果如下:
   -------------------------
   INDEX  RULEID   TYPE         SRVIND  PROV
   3      3        SubBasis     abc     FALSE
   4      3        SubBasis     def     FALSE
   5      3        SubBasis     ghi     FALSE

   (结果个数 = 3)
   ---    END
   ```
5. 查询“透明数据同步规则ID”为“3”、“服务标识”为“abc”的透明数据同步规则：

   ```
   LST REPSYNCRULE: RULEID=3, SRVIND="abc";
   ```

   ```
   LST REPSYNCRULE: RULEID=3, SRVIND="abc"; 
   RETCODE = 0  操作成功。 
   结果如下:
   -------------------------
   INDEX  RULEID   TYPE         SRVIND   PROV
   3      3        SubBasis     abc      FALSE
   (结果个数 = 1)
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见****ADD REPSYNCRULE****命令的参数说明。