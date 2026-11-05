# 修改汇聚RU信息（MOD RUCONVERGENCE）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：NCG**

该命令用于修改汇聚RU信息。

#### 注意事项

此命令会影响汇聚RU与业务RU之间的分配关系，修改前请保证修改内容正确。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                                                                     |
|:-------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUID         | RU的ID    | 可选必选说明：必选参数 参数含义：该参数用来表示RU的ID。 数据来源：本端规划 取值范围：整数类型，取值范围为64～4294967294。 默认值：无 配置原则：该值需要执行LST SERVICERUSTATE命令，查询出存在的RU ID进行填写。                                                                            |
| RUROLE       | RU角色     | 可选必选说明：必选参数 参数含义：该参数用来表示当前RU角色。 数据来源：本端规划 取值范围：枚举类型。 CONVERGE：汇聚RU。SERVICE：业务RU。 默认值：无 配置原则：无。                                                                                                           |
| CURCONRUID   | 当前汇聚RUID | 可选必选说明：条件可选参数 前提条件：该参数在“RUROLE”配置为“SERVICE”时为条件可选参数。 参数含义：该参数用来表示当前汇聚RU的ID。 数据来源：本端规划 取值范围：整数类型，取值范围为64～4294967294。 默认值：无 配置原则：无。                                                                        |
| HISCONRUID   | 历史汇聚RUID | 可选必选说明：条件可选参数 前提条件：该参数在“RUROLE”配置为“SERVICE”时为条件可选参数。 参数含义：该参数用来表示历史汇聚RU的ID。 数据来源：本端规划 取值范围：整数类型，取值范围为64～4294967294。 默认值：无 配置原则：无。                                                                        |
| CONRUIDSTATE | 汇聚RUID状态 | 可选必选说明：条件可选参数 前提条件：该参数在“RUROLE”配置为“CONVERGE”时为条件可选参数。 参数含义：该参数用来表示汇聚RUID的状态。 数据来源：本端规划 取值范围：枚举类型。 NORMAL：正常。SUBHEALTH：亚健康。 默认值：无 配置原则：如果修改为亚健康状态，汇聚RU对应的业务RU不会迁移走，但是不会接受新的业务RU均衡；如果修改为正常状态，可以接受新的业务RU均衡。 |
| PROMODE      | 处理模式     | 可选必选说明：可选参数 参数含义：该参数用来表示当前RUID的处理模式。 数据来源：本端规划 取值范围：枚举类型。 SET：设置规则。CANCEL：取消规则。 默认值：无 配置原则：无。                                                                                                            |

#### 使用实例

1. “RU角色”参数为**CONVERGE（汇聚RU）**场景
   - “处理模式”参数为空，代表临时修改汇聚RU状态，不会修改数据表（LST RUCONVERGENCE命令查询不到设置记录），该汇聚RU会根据实际情况自动切换。示例：

     ```
     MOD RUCONVERGENCE: RUID=65, RUROLE=CONVERGE, CONRUIDSTATE=SUBHEALTH;
     ```
   - “处理模式”参数为SET，代表静态设置汇聚RU状态，LST RUCONVERGENCE命令可查询设置记录。示例：

     ```
     MOD RUCONVERGENCE: RUID=65, RUROLE=CONVERGE, CONRUIDSTATE=SUBHEALTH, PROMODE=SET;
     ```

     在此模式下，被设定的汇聚RU状态不会自动变化，如果想恢复RU自动调整功能，需要设置“处理模式”参数为CANCEL。示例：

     ```
     MOD RUCONVERGENCE: RUID=65, RUROLE=CONVERGE, CONRUIDSTATE=SUBHEALTH, PROMODE=CANCEL;
     ```
2. “RU角色”参数为**SERVICE（业务RU）**场景
   - “处理模式”参数为空，代表临时修改业务RU状态，不会修改数据表（LST RUCONVERGENCE命令查询不到设置记录），该业务的状态及对应的汇聚RU会根据实际情况自动切换。示例：

     ```
     MOD RUCONVERGENCE: RUID=71, RUROLE=SERVICE, CURCONRUID=64, HISCONRUID=65;
     ```
   - “处理模式”参数为SET，代表静态设置业务RU和汇聚RU的对应关系，LST RUCONVERGENCE命令可查询设置记录，静态设置以后，该业务RU不参与自动均衡计算，也不参与动态迁移，状态不会自动发生变化。示例：

     ```
     MOD RUCONVERGENCE: RUID=71, RUROLE=SERVICE, CURCONRUID=64, HISCONRUID=65, PROMODE=SET;
     ```

     **注意** 

     此命令中，**HISCONRUID**参数必须是实际存在的汇聚RU ID。因为在取消设置规则时，会将HISCONRUID和CURCONRUID对调，如果HISCONRUID不是实际存在的汇聚RU ID，会导致取消规则失败。

     如果想恢复此业务RU到原来状态，参与自动调整，需要设置“处理模式”参数为CANCEL。示例：

     ```
     MOD RUCONVERGENCE: RUID=66, RUROLE=SERVICE, PROMODE=CANCEL;
     ```

     **说明** 

     - 取消设置规则实际上就是将LST RUCONVERGENCE命令查询结果中的CURCONRUID和HISCONRUID对调，将业务RU的汇聚RU设置为原来的值。在取消设置规则时，会对HISCONRUID进行校验，判断此RU是否存在以及是否是汇聚RU，如果校验不通过（HISCONRUID不存在或者不是汇聚RU），则取消规则会失败。***失败后处理建议：执行“处理模式”参数为SET的MOD RUCONVERGENCE命令，给此业务RU设置一个可用的HISCONRUID。***
     - 建议在取消设置规则时不要输入CURCONRUID和HISCONRUID两个参数，因为取消设置规则是根据LST RUCONVERGENCE命令的查询结果进行设置的，人工输入的参数无效。