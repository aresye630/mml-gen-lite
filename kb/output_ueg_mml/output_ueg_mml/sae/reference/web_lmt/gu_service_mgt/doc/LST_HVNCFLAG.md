# 查询指定IMPU的IMS漫游权限检查标志(LST HVNCFLAG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于从HSS的业务数据库中查询指定IMPU的IMS漫游权限检查标志，IMPU的漫游网络检查标志可以通过SET
HVNCFLAG操作设置。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                            |
|:-------|:-------|:------------------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于在业务数据库中指定一个需要查询漫游权限检查标识的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

查询指定IMPU的IMS漫游权限检查标志。IMPU：sip:impuinfo@huawei.com。

```
LST HVNCFLAG: IMPU="sip:impuinfo@huawei.com";
```

```
%%LST HVNCFLAG: IMPU="sip:impuinfo@huawei.com";%%
RETCODE = 0 SUCCESS0001:操作成功

VNCFLAG
1

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

| 参数标识    | 参数说明                                         |
|:--------|:---------------------------------------------|
| VNCFLAG | 显示IMPU的漫游权限检查标志。 0：表示不需要检查漫游权限。1：表示需要检查漫游权限。 |