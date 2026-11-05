# 显示本端Recovery值及系统重启时间（DSP LOCALRECOVERY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于查询本端Recovery值及系统重启时间。

## 注意事项

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP RECOVERY / MOD RECOVERY配置。
- 本端Recovery值仅在公共软参DWORD4 BIT16设置为1时增加。
- 系统重启时间是否刷新由DWORD4 BIT15软参控制。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询本端Recovery值及系统重启时间：DSP LOCALRECOVERY:;

```
%%DSP LOCALRECOVERY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  本端Recovery值  =  0
      系统重启时间  =  2021-03-04 00:00:00
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称       | 输出项解释                                                 |
|:------------|:------------------------------------------------------|
| 本端Recovery值 | 该参数用于表示本端Recovery值，系统重启后本值加1。                         |
| 系统重启时间      | 该参数用于表示系统重启时间。如果值为1970-01-01 00:00:00，则说明系统没有重启，可以忽略。 |