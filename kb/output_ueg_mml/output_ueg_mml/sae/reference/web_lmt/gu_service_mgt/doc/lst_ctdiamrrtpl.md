# 以格式2查询EPS漫游模板(LST CTDIAMRRTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用于查询EPS漫游模板数据。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                      |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪个HLR序列号来查询EPS漫游模板信息。 取值范围：1～255 默认值：无 配置原则：该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。     |
| TPLID  | 模板ID   | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪个模板ID来查询EPS漫游模板信息。 取值范围：0～65534 默认值：无 配置原则：该参数必须先由ADD DIAMRRTPL命令定义，然后才能在此处引用。 |

## 使用实例

查询“HLR序列号”为“23”，“模板ID”为“33”的EPS漫游模板信息，以特定的数据格式返回：

```
LST CTDIAMRRTPL: HLRSN=23, TPLID=33;
```

```
%%LST CTDIAMRRTPL: HLRSN=23, TPLID=33;%%
RETCODE = 0 SUCCESS0001:Operation is successful

                         TPLID = 33
                       TPLNAME = DIAM-NAME
                   DEFAULTRULE = PERMISSION
DIAMNODELIST
              DIAMIDENTITYTYPE = HOSTNAME
                  DIAMIDENTITY = test1.huawei.com
                     REALMNAME = huawei.com
                          RULE = RESTRICT

DIAMNODELIST
              DIAMIDENTITYTYPE = HOSTNAME
                  DIAMIDENTITY = test2.huawei.com
                          RULE = PERMISSION

Total count = 10

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD DIAMRRTPL**命令参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                           | 处理建议                                                                                          |
|:--------|:--------|:-----------------------------------------------|:----------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | 用户输入的“模板ID”对应的模板信息未添加。 “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“QoS模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST DIAMRRTPL命令查询已定义的“模板ID”。 |