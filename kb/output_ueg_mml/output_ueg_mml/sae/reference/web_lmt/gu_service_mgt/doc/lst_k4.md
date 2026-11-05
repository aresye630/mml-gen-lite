# 查询K4(LST K4)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询所有K4的数据。

## 注意事项

- 如果K4为HSM类型，本命令查询结果中“K4序列号”、“K4名称”显示参数取值，“算法类型”参数显示为“NONE”。
- 如果“算法类型”为“SM4”，查询结果中显示“密钥生成时间”。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                     |
|:-------|:-------|:-------------------------|
| HLRSN  | HLR序列号 | 用于标识系统按照哪个HLR序列号来查询K4数据。 |

## 使用实例

- 查询K4数据，“HLR序列号”为“1”：

  ```
  LST K4: HLRSN=1;
  ```

  ```
  %%LST K4: HLRSN=1;%%
  RETCODE = 0 SUCCESS0001:操作成功

          "K4SNO" "ALGTYPE"     "K7SNO"   "KEYNAME"     "HSMKEYINDEX"

          1       AES128        NONE    
          2       AES256        NONE    

  Total count = 2

  There is together 1 report

  ---    END
  ```
- 存在“算法类型”为“SM4”的记录时，查询结果如下：

  ```
  LST K4: HLRSN=3;
  ```

  ```
  %%LST K4: HLRSN=3;%%
  RETCODE = 0 SUCCESS0001:操作成功

          "K4SNO" "ALGTYPE"     "K7SNO"   "KEYNAME"    "HSMKEYINDEX"     "CREATETIME"

          5       SM4            NONE                                     2024-10-01 14:00:00
          6       AES256         NONE    

  Total count = 2

  There is together 1 report

  ---    END
  ```