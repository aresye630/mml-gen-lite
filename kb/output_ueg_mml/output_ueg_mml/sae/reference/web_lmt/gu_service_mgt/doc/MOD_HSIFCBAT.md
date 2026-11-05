# 批量修改共享iFC(MOD HSIFCBAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中批量修改指定IMPU相关的Service Profile所包含的某个共享iFC的信息。该命令的使用场景为：使用**ADD IMSSUB**或者**ADD HSIFC**命令为用户设置“共享iFC模板ID”时，命令中指定的“共享iFC模板ID”设置错误，可使用该命令为用户修改新的“共享iFC模板ID”。

## 注意事项

- 参数IMPU和IMPUFILE只能存在一个。
- BATTYPE参数等于DISCONTINUOUS参数IMPUFILE可见，IMPU不可见。
- BATTYPE参数等于CONTINUOUS参数IMPU可见，IMPUFILE不可见。
- 该命令涉及批量处理用户数据，请操作人员谨慎操作。

## 参数说明

| 参数标识     | 参数名称        | 参数说明                                                                                                                                                                                                                                                                            |
|:---------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSIFCID  | 共享iFC模板ID   | 用于指定需要修改的共享iFC模板的序号，操作员可以使用LST HTPLINF命令查询获得。                                                                                                                                                                                                                                   |
| NSIFCID  | 新的共享iFC模板ID | 用于指定新的共享iFC模板的索引，该参数必须先由ADD HSIFCTPL命令定义，然后才能在此处索引。 说明： 必选参数。当通过SET HSYSTEMPARA命令设置“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参为“TRUE(TRUE)”时，该参数需要引用用户签约的“HLR序列号”下的共享iFC模板。                                                                                                        |
| BATTYPE  | 批操作类型       | 指定批操作的类型，为枚举类型。 取值范围： DISCONTINUOUS(1)CONTINUOUS(5) 缺省值： 无                                                                                                                                                                                                                      |
| IMPU     | IMPU        | 仅当本命令中的参数“批操作类型”取值为“CONTINUOUS”时，该参数有效。用于指定一个需要修改共享iFC的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。IMPU支持正则表达式，正则表达式主要用于处理连续号段。正则表达式以“!”开始和结尾，正则表达式包含两个字段，第一个字段表示取值范围，此字段以“[”和“]”为开始和结尾；另一个是长度字段，表明要生成几位字段，范围是1~4。使用正则表达方式批操作时，IMPU参数中正则表达式外不能使用其它‘!’。 取值范围： 长度不超过133的字符串 缺省值： 无 |
| IMPUFILE | IMPU导入文件    | 仅当本命令中的参数“批操作类型”取值为“DISCONTINUOUS”时，该参数有效。用于指定一个需要修改共享iFC的IMPU导入文件名。导入文件中为需要批量修改的IMPU集合，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。导入文件主要用于非连续号段。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                          |

## 使用实例

修改共享iFC。共享iFC模板ID：1，新的共享iFC模板ID：2，批操作类型：CONTINUOUS，IMPU：sip:hello![0-9]{2}!@huawei.com。

```
MOD HSIFCBAT: OSIFCID=1, NSIFCID=2, BATTYPE=CONTINUOUS, IMPU="sip:hello![0-9]{2}!@huawei.com";
```

修改IMPU导入文件的共享IFC。共享iFC模板ID：1，新的共享iFC模板ID：2，批操作类型：DISCONTINUOUS，IMPU导入文件：IMPU\_SIFIDLIST.txt。IMPU导入文件中的内容如下：

tel:+2154140000

tel:+2154140033

...

tel:+2154149999

```
MOD HSIFCBAT: OSIFCID=1, NSIFCID=2, BATTYPE=DISCONTINUOUS, IMPUFILE="impu.txt";
```