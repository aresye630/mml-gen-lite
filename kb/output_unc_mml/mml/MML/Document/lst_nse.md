# 查询信令实体（LST NSE）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询信令实体参数（Network service Entity，NSE）。信令实体分别位于BSS侧和SGSN侧，用于提供GB接口操作所需的网络管理功能。请参考 3GPP TS 48.016。

#### 注意事项

- 系统最大支持8192个静态NSE，每个进程最大可配置1024个静态NSE。
- 查询方式包括：
  - 若未输入参数，表示查询所有记录。
  - 若输入OTHERNODE，未输入BNSEI，表示查询所有属于该OTHERNODE的NSE记录。
  - 若输入BNSEI，则查询对应NSEI记录，不允许与OTHERNODE同时输入。
- 若输入RU名称，则查询指定RU上所有NSE记录，不允许与OTHERNODE同时输入，也不允许与NSEI同时输入。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:----------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LNKRDTMP  | “NSE连接方向”匹配原则 | 可选必选说明：可选参数 参数含义：该参数用于指定以“NSE连接方向”为关键字查询时的匹配原则。当“NSE连接方向”参数输入时，本参数将控制“NSE连接方向”输入值的查询方式。当“NSE连接方向”参数未输入时，本参数不起作用。 取值范围：“EQUAL（等于）”：按以“NSE连接方向”输入值完全匹配进行筛选。“BEGIN（始于）”：按以特定字符开头的文本进行筛选。“INCLUDE（包含）”：按在文本中任意位置有特定字符的文本进行筛选。“EXCLUDE（不包含）”：按在文本中任意位置无特定字符的文本进行筛选。 默认值：“EQUAL（等于）”                                                                                                                                                                                                                                       |
| OTHERNODE | NSE连接方向       | 可选必选说明：可选参数 参数含义：该参数用于指定该NSE所连接的对端局点的名字或名字的一部分。 取值范围：1~29位字符串 默认值：无  说明： 任意一种匹配原则的情况下，关键字都不区分大小写。举例：假设系统中存在“SHBSC001”、“SHBSC002”、“SHBSC003”、“NJBSC001”、“NJBSC002”、“HZBSC001”6个NSE记录。 若要筛选与“SHBSC001”完全相同的记录，请选择“EQUAL（等于）”，并输入“SHBSC001”，输出结果为“SHBSC001”。若要筛选以字母“SH”开头的记录，请选择“BEGIN（始于）”，并输入“SH”，输出结果为“SHBSC001”、“SHBSC002”、“SHBSC003”。若要筛选在文本中任意位置有“001”的记录，请选择“INCLUDE（包含）”，并输入“001”，输出结果为“SHBSC001”、“NJBSC001”、“HZBSC001”。若要筛选在文本中任意位置不存在“SH”的记录，请选择“EXCLUDE（不包含）”，并输入“SH”，输出结果为“NJBSC001”、“NJBSC002”、“HZBSC001”。 |
| SGSNINDEX | SGSN索引        | 可选必选说明：可选参数 参数含义：该参数用于指定SGSN索引。 取值范围：0 默认值：0                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| NSEIFLTP  | “NSE标识”筛选方式   | 可选必选说明：可选参数 参数含义：该参数用于指定以“NSE标识”作为查询关键字的筛选方式。当“NSE标识”参数输入时，本参数将控制“NSE标识”输入值的查询方式。当“NSE标识”参数未输入时，本参数不起作用。 取值范围：“EQUAL（等于）”“NOT_EQ（不等于）”“NOT_LESS（不小于）”“NOT_LARGER（不大于）”“RANGE（范围）” 默认值：“EQUAL（等于）”  说明： 若要按上限数字和下限数字进行筛选，请选择“RANGE（范围）”。                                                                                                                                                                                                                                                                              |
| BNSEI     | NSE标识         | 可选必选说明：可选参数 参数含义：该参数用于指定网络服务实体标识。 取值范围：0~65535 默认值：无  说明： 当NSEIFLTP设置为“RANGE（范围）”时，本参数表示“起始NSE标识”。                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ENSEI     | 结束NSE标识       | 可选必选说明：条件可选参数 参数含义：该参数用于指定网络服务实体标识。 前提条件：该参数在NSEIFLTP参数设置为“RANGE（范围）”时，才需要配置。 取值范围：0~65535 默认值：无  说明： 当NSEIFLTP设置为“RANGE（范围）”时，本参数与“NSE标识”参数都必须输入，并且要求“结束NSE标识”的值必须大于或等于“NSE标识”的值。                                                                                                                                                                                                                                                                                                                                   |
| RUNAME    | RU名称          | 可选必选说明：可选参数 参数含义：该参数用于指定SPU资源单元名。该参数可以通过DSP RU命令查询。 取值范围：0~63位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                              |

#### 使用实例

查询系统所有NSE：

LST NSE: NSEIFLTP=EQUAL;

```
%%LST NSE: NSEIFLTP=EQUAL;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
NSE连接方向                 NSE标识   BVCI    RU名称     进程号         BSS编号    FLUSH监控定时器(ms)是否支持PFC                   是否支持CBL                   是否支持INR                   是否支持LCS                     是否支持RIM                     是否支持PFCFC                   是否携带ARP信元   是否携带RA Capability信元   是否支持Gb-Flex    是否支持特殊业务类型             BSS支持的Qos版本           是否支持MOCN                     是否支持SPID 
GB_IF_TEST_NS               13901     0       NULL       255            133        50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)     否           
S1                          180       0       NULL       255            180        50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)     否           
E2                          2000      0       USN_VSU1   1              2000       50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)     否           
(结果个数 = 3)

---    END
```

查询NSE连接方向名称为S1 （不区分大小写）的NSE：

LST NSE: OTHERNODE="s1", NSEIFLTP=EQUAL;

```
%%LST NSE: OTHERNODE="s1", NSEIFLTP=EQUAL;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
              NSE连接方向  =  S1
                  NSE标识  =  180
                     BVCI  =  0
                  RU名称   =  NULL
                   进程号  =  255
                  BSS编号  =  180
      FLUSH监控定时器(ms)  =  50
              是否支持PFC  =  否(BSS侧不支持,SGSN侧支持)
              是否支持CBL  =  否(BSS侧不支持,SGSN侧支持)
              是否支持INR  =  否(BSS侧不支持,SGSN侧支持)
              是否支持LCS  =  否(BSS侧不支持,SGSN侧不支持)
              是否支持RIM  =  否(BSS侧不支持,SGSN侧不支持)
            是否支持PFCFC  =  否(BSS侧不支持,SGSN侧不支持)
          是否携带ARP信元  =  否
是否携带RA Capability信元  =  否
          是否支持Gb-Flex  =  否
     是否支持特殊业务类型  =  否
         BSS支持的Qos版本  =  R99
             是否支持MOCN  =  否(BSS侧不支持,SGSN侧不支持)
             是否支持SPID  =  否
(结果个数 = 1)
---    END
```

查询NSE连接方向名称中包含s（不区分大小写）的NSE：

LST NSE: LNKRDTMP=INCLUDE, OTHERNODE="s", NSEIFLTP=EQUAL;

```
%%LST NSE: LNKRDTMP=INCLUDE, OTHERNODE="s", NSEIFLTP=EQUAL;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
NSE连接方向                 NSE标识   BVCI    RU名称     进程号         BSS编号    FLUSH监控定时器(ms)是否支持PFC                   是否支持CBL                   是否支持INR                   是否支持LCS                     是否支持RIM                     是否支持PFCFC                   是否携带ARP信元   是否携带RA Capability信元   是否支持Gb-Flex    是否支持特殊业务类型             BSS支持的Qos版本           是否支持MOCN                     是否支持SPID 
GB_IF_TEST_NS               13901     0       NULL       255            133        50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)     否           
S1                          180       0       NULL       255            180        50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)    否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)     否           
(结果个数 = 2)

---    END
```

查询NSE标识范围为100~2000的NSE：

LST NSE: NSEIFLTP=RANGE, BNSEI=100, ENSEI=2000;

```
%%LST NSE: NSEIFLTP=RANGE, BNSEI=100, ENSEI=2000;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
NSE连接方向                 NSE标识   BVCI    RU名称      进程号         BSS编号    FLUSH监控定时器(ms)是否支持PFC                   是否支持CBL                  是否支持INR                  是否支持LCS                     是否支持RIM                    是否支持PFCFC                  是否携带ARP信元   是否携带RA Capability信元   是否支持Gb-Flex    是否支持特殊业务类型             BSS支持的Qos版本           是否支持MOCN                   是否支持SPID 
S1                          180       0       NULL        255            180        50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)   否(BSS侧不支持,SGSN侧支持)   否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)   否(BSS侧不支持,SGSN侧不支持)   否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)   否           
E2                          2000      0       USN_VSU1    1              2000       50                 否(BSS侧不支持,SGSN侧支持)    否(BSS侧不支持,SGSN侧支持)   否(BSS侧不支持,SGSN侧支持)   否(BSS侧不支持,SGSN侧不支持)    否(BSS侧不支持,SGSN侧不支持)   否(BSS侧不支持,SGSN侧不支持)   否                否                          否                 否                               R99                        否(BSS侧不支持,SGSN侧不支持)   否           
(结果个数 = 2)

---    END
```

使用指定的RU查询NSE：

LST NSE: NSEIFLTP=EQUAL, RUNAME="USN\_VSU1";

```
%%LST NSE: NSEIFLTP=EQUAL, RUNAME="USN_VSU1";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
              NSE连接方向  =  E1
                  NSE标识  =  2000
                     BVCI  =  0
                  RU名称   =  USN_VSU1
                   进程号  =  0
                  BSS编号  =  2000
      FLUSH监控定时器(ms)  =  50
              是否支持PFC  =  否(BSS侧不支持,SGSN侧支持)
              是否支持CBL  =  否(BSS侧不支持,SGSN侧支持)
              是否支持INR  =  否(BSS侧不支持,SGSN侧支持)
              是否支持LCS  =  否(BSS侧不支持,SGSN侧不支持)
              是否支持RIM  =  否(BSS侧不支持,SGSN侧不支持)
            是否支持PFCFC  =  否(BSS侧不支持,SGSN侧不支持)
          是否携带ARP信元  =  否
是否携带RA Capability信元  =  否
          是否支持Gb-Flex  =  否
     是否支持特殊业务类型  =  否
         BSS支持的Qos版本  =  R99
             是否支持MOCN  =  否(BSS侧不支持,SGSN侧不支持)
             是否支持SPID  =  否
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见**ADD NSE**的参数说明。