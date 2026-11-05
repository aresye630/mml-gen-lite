# 查询密码强度检查策略(LST HSECPOLICY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已配置的密码强度检查策略信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询已配置的密码强度检查策略信息，命令如下：

```
LST HSECPOLICY:;
```

```
%%LST HSECPOLICY:;%%
RETCODE = 0 SUCCESS0001:操作成功

SECURITY            MINLEN              PWD_CHARTYPE        PWD_NO_OPR_ID       PWD_NO_ORDER        PWD_UPPER           PWD_LOWER           PWD_NUMBER          PWD_SPECIAL         CONTSAMECHARNUM
TRUE                6                   TRUE                TRUE                TRUE                TRUE                TRUE                TRUE                TRUE                2

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

请参见**SET HSECPOLICY**命令的参数说明。