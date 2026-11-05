# 查询补充业务SIP格式前转号码后缀(LST HCFFTNPOSTFIX)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令在用于IMS-HSS对接第三方AS网元时，查询Sh接口消息中呼叫前转类补充业务的前转号码为SIP格式时的号码后缀。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询呼叫前转类补充业务SIP格式前转号码后缀：

```
LST HCFFTNPOSTFIX:;
```

```
%%LST HCFFTNPOSTFIX:;%%
RETCODE = 0 SUCCESS0001:操作成功

SIPFORMATPOSTFIX
ims.mnc123.mcc732.3gppnetwork.org

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息，参数说明请参见**SET HCFFTNPOSTFIX**。