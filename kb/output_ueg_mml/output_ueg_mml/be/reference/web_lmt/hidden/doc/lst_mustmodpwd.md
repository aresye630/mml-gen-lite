# 查询是否必须修改密码的状态信息(LST MUSTMODPWD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询PGW操作员是否必须修改密码。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                            |
|:-------|:-------|:--------------------------------------------------------------------------------|
| OP     | 操作员标识  | 用于指定当前登录的操作员标识，判断其是否需要在修改密码后才能登录。 取值范围：不超过32位的数字、字母或下划线组成的字符串，且首字符必须为字母。 默认值：无。 |

## 使用实例

1. 查询是否必须修改密码的状态信息。

   ```
   %%LST MUSTMODPWD:OP="huawei";%%
   ```

   ```
   %%LST MUSTMODPWD:OP="huawei";%%
   RETCODE = 0 操作成功

                                status of modifying password  =  OFF
                           expiry number of days of password  =  2
                threshold of prompting expiry number of days  =  1

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。