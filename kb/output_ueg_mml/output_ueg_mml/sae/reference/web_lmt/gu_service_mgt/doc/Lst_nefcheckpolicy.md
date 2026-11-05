# 查询NEF检查策略配置(LST NEFCHKPOLICY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统配置的NEF合法性检查策略数据记录。

- 若需要查询所有已配置的NEF合法性检查策略，则不输入任何参数。
- 若需要查询某个NEF的合法性检查策略，请输入“NEF名称”参数。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                   |
|:--------|:-------|:---------------------------------------------------------------------------------------|
| NEFNAME | NEF名称  | 可选必选说明：可选参数 参数含义：用于指定根据哪个NEF名称来查询系统配置的NEF合法性检查策略数据记录。 取值范围：长度不超过64的字符串。 默认值：无。 配置原则：无。 |

## 使用实例

- 查询所有NEF合法性检查策略记录。

  ```
  LST NEFCHKPOLICY:;
  ```

  ```
  %%LST NEFCHKPOLICY:;%%
  RETCODE = 0 SUCCESS0001:Operation is successful

                 NEFNAME                                                      TYPE
                 neffqdn                                                      FQDN
                 nefIPv4                                                      IPV4

  Total count = 2

  There is together 1 report

  ---    END
  ```
- 查询“NEF名称”为“nefIPv4”的NEF检查策略记录。

  ```
  LST NEFCHKPOLICY: NEFNAME="nefIPv4";
  ```

  ```
  %%LST NEFCHKPOLICY: NEFNAME="nefIPv4";%%
  RETCODE = 0 SUCCESS0001:Operation is successful

                         NEFNAME = nefIPv4
                            TYPE = IPV4
                         NEFIPV4 = 127.20.128.110

  Total count = 3

  There is together 1 report

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NEFCHKPOLICY**命令的参数说明。