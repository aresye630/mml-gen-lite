# 查询Diameter IP链路(LST DIAMIPLINK)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询Diameter IP链路记录。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询Diameter IP链路：

`LST DIAMIPLINK:;`

```
%%LST DIAMIPLINK:;%%
RETCODE = 0  操作成功

查询结果如下
------------
 链路索引   IP版本  本端IPV4地址  本端IPV6地址        IP版本     对端IPV4地址  对端IPV6地址

 2         IPV4      10.2.15.17     NULL          IPV4      10.2.141.180   NULL        
 1         IPV4      10.2.15.17     NULL          IPV4      10.2.141.160   NULL        
 0         IPV4      10.2.15.17     NULL          IPV4      10.2.141.170   NULL        
(结果个数 = 3)

---    END
```

## 输出结果说明

| 输出项名称    | 输出项解释                |
|:---------|:---------------------|
| 链路索引     | 用于返回Diameter IP链路索引。 |
| IP版本     | 用于返回本端IP版本。          |
| 本端IPV4地址 | 用于返回本端IPV4地址。        |
| 本端IPV6地址 | 用于返回本端IPV6地址。        |
| IP版本     | 用于返回对端IP版本。          |
| 对端IPV4地址 | 用于返回对端IPV4地址。        |
| 对端IPV6地址 | 用于返回对端IPV6地址。        |