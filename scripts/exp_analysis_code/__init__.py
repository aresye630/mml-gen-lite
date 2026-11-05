#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""exp_analysis_code — S3 确定性代码管线包（P1）。

切片规划见 docs/S3分析代码化改造设计.md（T1~T9）。
本模块 = p1_parse：EXP 解析层 —— 注释/命令行切分、verb/命令类型统计、
元数据提取（ME Type/Version/PatchVersion/导出时间/网元名）、许可开关统计。

数据驱动红线：本包规则（rules/*.yaml）与代码禁止出现局点实例值；
命令名/参数名为产品级通用知识，可入 yaml。
"""
