# 查询外置AUC错误码映射(LST AUCERRORCODE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询已配置的外置AUC错误码映射关系。

仅输入参数“域”时，查询结果显示对应域下的所有错误码映射关系；同时输入“域”和“原始错误码”时，查询结果显示对应域下指定的原始错误码记录。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                              |
|:----------|:-------|:----------------------------------------------------------------------------------|
| DOMAIN    | 域      | 可选必选说明：必选参数 参数含义：标识外置AUC错误码映射信息的关键字段，用于指定查询哪个域的错误码映射关系。 取值范围：4GIMS 默认值：无。 配置原则：无。 |
| ERRORCODE | 原始错误码  | 可选必选说明：可选参数 参数含义：用于指定查询外置AUC返回的哪个原始错误码对应的映射关系。 取值范围：0～65535 默认值：无。 配置原则：无。        |

## 使用实例

1. 查询4G域对应的错误码映射关系：

   ```
   LST AUCERRORCODE: DOMAIN=4G;
   ```

   ```
   %%LST AUCERRORCODE: DOMAIN=4G;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  DOMAIN       ERRORCODE           RETURNERRORCODE
                  4G           403                 DIAMETER_MULTI_ROUND_AUTH(1001)
                  4G           405                 DIAMETER_LIMITED_SUCCESS(2002)

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询IMS域“原始错误码”为“500”对应的返回错误码:

   ```
   LST AUCERRORCODE: DOMAIN=IMS, ERRORCODE=500;
   ```

   ```
   %%LST AUCERRORCODE: DOMAIN=IMS, ERRORCODE=500;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  DOMAIN       ERRORCODE           RETURNERRORCODE
                  IMS          500                 DIAMETER_FIRST_REGISTRATION(2001)

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。输出结果请参考**ADD AUCERRORCODE**命令参数含义。