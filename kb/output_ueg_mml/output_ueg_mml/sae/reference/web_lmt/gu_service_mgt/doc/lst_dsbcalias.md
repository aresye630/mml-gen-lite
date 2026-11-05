# 查询数据业务承载能力别名(LST DSBCALIAS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询指定数据业务的所有承载能力别名。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                     |
|:-------|:-------|:-----------------------------------------|
| HLRSN  | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。 |
| DSCODE | 数据业务码  | 基本业务的编码。各种数据业务的含义请参见“承载业务管理 ”。           |

## 使用实例

查询承载业务BS21的所有承载能力别名。

LST DSBCALIAS: HLRSN=1, DSCODE=BS21;

```
%%LST DSBCALIAS: HLRSN=1, DSCODE=BS21;%%
RETCODE = 0 SUCCESS0001:操作成功

                     ALIASNAME = BC21

Total count = 1

There is together 1 report

---    END
```