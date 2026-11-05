# 查询指定IMPU的ONEKEY数据(LST HONEKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于从HSS的业务数据库中查询指定IMPU相关One Key信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                     |
|:-------|:-------|:-----------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要查询One Key的IMPU ，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无 |

## 使用实例

查询One Key数据。IMPU：sip:impuinfo@huawei.com。

```
LST HONEKEY: IMPU="sip:impuinfo@huawei.com";
```

## 输出结果说明

| 参数标识      | 参数说明                     |
|:----------|:-------------------------|
| WUSERNAME | 显示IMPU相关的web username信息。 |
| HTOKEN    | 显示IMPU相关的Http token信息。   |
| AP        | 显示IMPU相关的接入点信息。          |