# 增加Diameter数据字典变更信息(ADD DMDICTCHG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

本命令属于高危命令，执行不当会造成系统运行异常从而影响业务运行，因此执行该命令前，需要与华为技术支持确认后才可以实施。

本命令用于增加Diameter数据字典变更信息。

## 注意事项

- Diameter数据字典变更信息对所有Diameter对端生效。
- 该命令不允许进行批操作。

## 参数说明

| 参数ID       | 参数名称          | 参数描述                                                                                                                                                                               |
|:-----------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DICTCHGIDX | 索引            | 用于指定一条Diameter数据字典变更信息在数据库中的索引。 取值范围： 0～255 默认值：无。                                                                                                                                 |
| DICTNAME   | 字典名字          | 用于指定字典名字（消息接口类型）。 取值范围： “Cx/Dx(Cx/Dx)”“Sh(Sh)”“S13(S13/S13')”“S6A/S6D(S6a/S6d)”“SWX(SWx)”“SLh(SLh)”“Zh(Zh)”“Ml(Ml)”“S6b(S6b)”“SWm(SWm)”“STa/Swa(STa/Swa)”“Zn(Zn)” 默认值：无。           |
| AVPNAME    | AVP名称         | 用于指定AVP名称。 取值范围： 0～65535 默认值：无。                                                                                                                                                    |
| AVPCODE    | AVP编码         | 用于指定AVP编码。 取值范围：1~2147483647 默认值：无。 说明： 执行该命令并且不输入该参数时，系统会设置初始值0。当“AVP编码”在数据库中值为“0”时， 该参数的取值不生效；当“AVP编码”在数据库中值不为“0”时，UDM取该参数配置的值。                                                  |
| AVPFLAG    | 设置为True的AVP标记 | 用于指定设置为True的AVP标记。 取值范围：全部选中全部清空全部灰化P_PRESENT(P标志位)： P-bit用于标识是否需要做端到端加密。该取值在当前版本暂不生效。M_PRESENT(M标志位)： M-bit用于标识本AVP是否必须的。V_PRESENT(V标志位)： V-bit用于指定Vendor-ID是否在AVP头中出现。 默认值：全部灰化。 |

## 使用实例

为了支持低版本diameter协议，请执行如下命令：

```
ADD DMDICTCHG: DICTCHGIDX=0, DICTNAME=S6A/S6D, AVPNAME=129, AVPFLAG=M_PRESENT-1&V_PRESENT-1;
```

```
ADD DMDICTCHG: DICTCHGIDX=1, DICTNAME=S6A/S6D, AVPNAME=83, AVPFLAG=M_PRESENT-1&V_PRESENT-1;
```

```
ADD DMDICTCHG: DICTCHGIDX=2, DICTNAME=S6A/S6D, AVPNAME=155, AVPFLAG=M_PRESENT-1&V_PRESENT-1;
```

```
ADD DMDICTCHG: DICTCHGIDX=3, DICTNAME=S6A/S6D, AVPNAME=156, AVPFLAG=M_PRESENT-1&V_PRESENT-1;
```

```
ADD DMDICTCHG: DICTCHGIDX=4, DICTNAME=S6A/S6D, AVPNAME=157, AVPFLAG=M_PRESENT-1&V_PRESENT-1;
```

```
ADD DMDICTCHG: DICTCHGIDX=5, DICTNAME=S6A/S6D, AVPNAME=169, AVPCODE=156, AVPFLAG=M_PRESENT-1&V_PRESENT-1;
```