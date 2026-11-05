# 查询通配符值(LST WILDCARD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询数据表中的通配字段及通配值：

- 若需要查询全部表的使用情况的概要信息，请不要输入任何参数。
- 若需要查询某个表的使用情况的详细信息，请输入“表ID”和“模块号”参数。

## 注意事项

在不同的网元下，参数表ID和模块类型会有所不同。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                      |
|:-------|:-------|:--------------------------------------------------------------------------|
| TID    | 表ID    | 用于指示系统需要按照表ID来查询通配符；若不输入，则表示所有的表。 取值范围：下拉列表中给出的所有表。 默认值：无。 配置原则：无。        |
| MT     | 模块类型   | 用于指示系统需要按照模块类型来查询通配符；若不输入，则表示所有的模块类型。 取值范围：下拉列表中给出的所有模块类型。 默认值：无。 配置原则：无。 |

## 使用实例

查询数据表中的通配字段及通配值:

`LST WILDCARD:;`

```
%%LST WILDCARD:;%%
RETCODE = 0  操作成功

表的通配符值
------------
 模块类型  表ID    表名称                 字段名称          通配符值

 WCDB      452     tbl_NMOutTkDest        iOutTrkNMSrcCode  65534   
 WCDB      454     tbl_NMCircuitReject    iTkGrpNo          65534   
 WCDB      457     tbl_NMTempRoute        iCallerCAT        254     
 WCDB      457     tbl_NMTempRoute        sCallerDN         eeeeeeee
 WCDB      457     tbl_NMTempRoute        iInTrkNMSrcCode   65534   
 WCDB      458     tbl_NMCancelDeRoute    iSubrouteno       65534   
 WCDB      460     tbl_NMSkipSubRoute     iSubrouteno       65534   
 WCDB      461     tbl_NMLimDirectRoute   iCallerCAT        254     
 WCDB      461     tbl_NMLimDirectRoute   iInTrkNMSrcCode   65534   
 WCDB      462     tbl_NMCircuitReserved  iSubRouteType     254     
 WCDB      462     tbl_NMCircuitReserved  iInTrkNMSrcCode   65534   
 WCDB      844     tbl_GrpLimit           iDesGrpNum        65534   
 WCDB      844     tbl_GrpLimit           iSrcGrpNum        65534   
(结果个数 = 13)

---    END
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1所示。

命令执行异常，请联系华为技术支持处理。

| 输出项名称   | 输出项解释                       |
|:--------|:----------------------------|
| 表名称     | 用于表示当前查询通配符信息中表的描述信息。       |
| 字段名称    | 用于表示当前查询通配符信息中通配符对应表中的字段信息。 |
| 通配符值    | 用于表示当前查询通配符信息中通配符描述信息。      |