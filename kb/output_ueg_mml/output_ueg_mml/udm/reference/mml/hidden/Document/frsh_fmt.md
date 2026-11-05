# 刷新内存中的缓存的数据字典(FRSH FMT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于将刷新当前工作区的数据字典。

该命令的操作场景一般为在开发的过程中，如果新增或修改表时，不用重启CM模块即可将最新的表数据刷新到内存。如果不怕麻烦的话重启CM也是可以的。

数据字典是OMU系统基础数据结构的一个虚拟称呼，简单来讲就是具体包含7张表：TBL\_BAMTABLEDEF、TBL\_BAMFIELDDEF、TBL\_BAMORDERDEF、TBL\_FAMTABLEDEF、TBL\_FAMFIELDDEF、TBL\_FAMINDEXDEF、TBL\_FAMINDEXFIELDDEF。它们基本包含的表ID定义、字段定义、最大元组数等这些系统基础信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

刷新当前工作区的数据字典:

`FRSH FMT:;`

```
%%FRSH FMT:;%%
RETCODE = 0  操作成功

---    END
```