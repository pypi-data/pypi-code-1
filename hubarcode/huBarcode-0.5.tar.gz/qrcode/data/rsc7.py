import cPickle

rs_cal_table = cPickle.loads("""(lp1
(lp2
I127
aI122
aI154
aI164
aI11
aI68
aI117
aa(lp3
I127
aI122
aI154
aI164
aI11
aI68
aI117
aa(lp4
I254
aI244
aI41
aI85
aI22
aI136
aI234
aa(lp5
I129
aI142
aI179
aI241
aI29
aI204
aI159
aa(lp6
I225
aI245
aI82
aI170
aI44
aI13
aI201
aa(lp7
I158
aI143
aI200
aI14
aI39
aI73
aI188
aa(lp8
I31
aI1
aI123
aI255
aI58
aI133
aI35
aa(lp9
I96
aI123
aI225
aI91
aI49
aI193
aI86
aa(lp10
I223
aI247
aI164
aI73
aI88
aI26
aI143
aa(lp11
I160
aI141
aI62
aI237
aI83
aI94
aI250
aa(lp12
I33
aI3
aI141
aI28
aI78
aI146
aI101
aa(lp13
I94
aI121
aI23
aI184
aI69
aI214
aI16
aa(lp14
I62
aI2
aI246
aI227
aI116
aI23
aI70
aa(lp15
I65
aI120
aI108
aI71
aI127
aI83
aI51
aa(lp16
I192
aI246
aI223
aI182
aI98
aI159
aI172
aa(lp17
I191
aI140
aI69
aI18
aI105
aI219
aI217
aa(lp18
I163
aI243
aI85
aI146
aI176
aI52
aI3
aa(lp19
I220
aI137
aI207
aI54
aI187
aI112
aI118
aa(lp20
I93
aI7
aI124
aI199
aI166
aI188
aI233
aa(lp21
I34
aI125
aI230
aI99
aI173
aI248
aI156
aa(lp22
I66
aI6
aI7
aI56
aI156
aI57
aI202
aa(lp23
I61
aI124
aI157
aI156
aI151
aI125
aI191
aa(lp24
I188
aI242
aI46
aI109
aI138
aI177
aI32
aa(lp25
I195
aI136
aI180
aI201
aI129
aI245
aI85
aa(lp26
I124
aI4
aI241
aI219
aI232
aI46
aI140
aa(lp27
I3
aI126
aI107
aI127
aI227
aI106
aI249
aa(lp28
I130
aI240
aI216
aI142
aI254
aI166
aI102
aa(lp29
I253
aI138
aI66
aI42
aI245
aI226
aI19
aa(lp30
I157
aI241
aI163
aI113
aI196
aI35
aI69
aa(lp31
I226
aI139
aI57
aI213
aI207
aI103
aI48
aa(lp32
I99
aI5
aI138
aI36
aI210
aI171
aI175
aa(lp33
I28
aI127
aI16
aI128
aI217
aI239
aI218
aa(lp34
I91
aI251
aI170
aI57
aI125
aI104
aI6
aa(lp35
I36
aI129
aI48
aI157
aI118
aI44
aI115
aa(lp36
I165
aI15
aI131
aI108
aI107
aI224
aI236
aa(lp37
I218
aI117
aI25
aI200
aI96
aI164
aI153
aa(lp38
I186
aI14
aI248
aI147
aI81
aI101
aI207
aa(lp39
I197
aI116
aI98
aI55
aI90
aI33
aI186
aa(lp40
I68
aI250
aI209
aI198
aI71
aI237
aI37
aa(lp41
I59
aI128
aI75
aI98
aI76
aI169
aI80
aa(lp42
I132
aI12
aI14
aI112
aI37
aI114
aI137
aa(lp43
I251
aI118
aI148
aI212
aI46
aI54
aI252
aa(lp44
I122
aI248
aI39
aI37
aI51
aI250
aI99
aa(lp45
I5
aI130
aI189
aI129
aI56
aI190
aI22
aa(lp46
I101
aI249
aI92
aI218
aI9
aI127
aI64
aa(lp47
I26
aI131
aI198
aI126
aI2
aI59
aI53
aa(lp48
I155
aI13
aI117
aI143
aI31
aI247
aI170
aa(lp49
I228
aI119
aI239
aI43
aI20
aI179
aI223
aa(lp50
I248
aI8
aI255
aI171
aI205
aI92
aI5
aa(lp51
I135
aI114
aI101
aI15
aI198
aI24
aI112
aa(lp52
I6
aI252
aI214
aI254
aI219
aI212
aI239
aa(lp53
I121
aI134
aI76
aI90
aI208
aI144
aI154
aa(lp54
I25
aI253
aI173
aI1
aI225
aI81
aI204
aa(lp55
I102
aI135
aI55
aI165
aI234
aI21
aI185
aa(lp56
I231
aI9
aI132
aI84
aI247
aI217
aI38
aa(lp57
I152
aI115
aI30
aI240
aI252
aI157
aI83
aa(lp58
I39
aI255
aI91
aI226
aI149
aI70
aI138
aa(lp59
I88
aI133
aI193
aI70
aI158
aI2
aI255
aa(lp60
I217
aI11
aI114
aI183
aI131
aI206
aI96
aa(lp61
I166
aI113
aI232
aI19
aI136
aI138
aI21
aa(lp62
I198
aI10
aI9
aI72
aI185
aI75
aI67
aa(lp63
I185
aI112
aI147
aI236
aI178
aI15
aI54
aa(lp64
I56
aI254
aI32
aI29
aI175
aI195
aI169
aa(lp65
I71
aI132
aI186
aI185
aI164
aI135
aI220
aa(lp66
I182
aI235
aI73
aI114
aI250
aI208
aI12
aa(lp67
I201
aI145
aI211
aI214
aI241
aI148
aI121
aa(lp68
I72
aI31
aI96
aI39
aI236
aI88
aI230
aa(lp69
I55
aI101
aI250
aI131
aI231
aI28
aI147
aa(lp70
I87
aI30
aI27
aI216
aI214
aI221
aI197
aa(lp71
I40
aI100
aI129
aI124
aI221
aI153
aI176
aa(lp72
I169
aI234
aI50
aI141
aI192
aI85
aI47
aa(lp73
I214
aI144
aI168
aI41
aI203
aI17
aI90
aa(lp74
I105
aI28
aI237
aI59
aI162
aI202
aI131
aa(lp75
I22
aI102
aI119
aI159
aI169
aI142
aI246
aa(lp76
I151
aI232
aI196
aI110
aI180
aI66
aI105
aa(lp77
I232
aI146
aI94
aI202
aI191
aI6
aI28
aa(lp78
I136
aI233
aI191
aI145
aI142
aI199
aI74
aa(lp79
I247
aI147
aI37
aI53
aI133
aI131
aI63
aa(lp80
I118
aI29
aI150
aI196
aI152
aI79
aI160
aa(lp81
I9
aI103
aI12
aI96
aI147
aI11
aI213
aa(lp82
I21
aI24
aI28
aI224
aI74
aI228
aI15
aa(lp83
I106
aI98
aI134
aI68
aI65
aI160
aI122
aa(lp84
I235
aI236
aI53
aI181
aI92
aI108
aI229
aa(lp85
I148
aI150
aI175
aI17
aI87
aI40
aI144
aa(lp86
I244
aI237
aI78
aI74
aI102
aI233
aI198
aa(lp87
I139
aI151
aI212
aI238
aI109
aI173
aI179
aa(lp88
I10
aI25
aI103
aI31
aI112
aI97
aI44
aa(lp89
I117
aI99
aI253
aI187
aI123
aI37
aI89
aa(lp90
I202
aI239
aI184
aI169
aI18
aI254
aI128
aa(lp91
I181
aI149
aI34
aI13
aI25
aI186
aI245
aa(lp92
I52
aI27
aI145
aI252
aI4
aI118
aI106
aa(lp93
I75
aI97
aI11
aI88
aI15
aI50
aI31
aa(lp94
I43
aI26
aI234
aI3
aI62
aI243
aI73
aa(lp95
I84
aI96
aI112
aI167
aI53
aI183
aI60
aa(lp96
I213
aI238
aI195
aI86
aI40
aI123
aI163
aa(lp97
I170
aI148
aI89
aI242
aI35
aI63
aI214
aa(lp98
I237
aI16
aI227
aI75
aI135
aI184
aI10
aa(lp99
I146
aI106
aI121
aI239
aI140
aI252
aI127
aa(lp100
I19
aI228
aI202
aI30
aI145
aI48
aI224
aa(lp101
I108
aI158
aI80
aI186
aI154
aI116
aI149
aa(lp102
I12
aI229
aI177
aI225
aI171
aI181
aI195
aa(lp103
I115
aI159
aI43
aI69
aI160
aI241
aI182
aa(lp104
I242
aI17
aI152
aI180
aI189
aI61
aI41
aa(lp105
I141
aI107
aI2
aI16
aI182
aI121
aI92
aa(lp106
I50
aI231
aI71
aI2
aI223
aI162
aI133
aa(lp107
I77
aI157
aI221
aI166
aI212
aI230
aI240
aa(lp108
I204
aI19
aI110
aI87
aI201
aI42
aI111
aa(lp109
I179
aI105
aI244
aI243
aI194
aI110
aI26
aa(lp110
I211
aI18
aI21
aI168
aI243
aI175
aI76
aa(lp111
I172
aI104
aI143
aI12
aI248
aI235
aI57
aa(lp112
I45
aI230
aI60
aI253
aI229
aI39
aI166
aa(lp113
I82
aI156
aI166
aI89
aI238
aI99
aI211
aa(lp114
I78
aI227
aI182
aI217
aI55
aI140
aI9
aa(lp115
I49
aI153
aI44
aI125
aI60
aI200
aI124
aa(lp116
I176
aI23
aI159
aI140
aI33
aI4
aI227
aa(lp117
I207
aI109
aI5
aI40
aI42
aI64
aI150
aa(lp118
I175
aI22
aI228
aI115
aI27
aI129
aI192
aa(lp119
I208
aI108
aI126
aI215
aI16
aI197
aI181
aa(lp120
I81
aI226
aI205
aI38
aI13
aI9
aI42
aa(lp121
I46
aI152
aI87
aI130
aI6
aI77
aI95
aa(lp122
I145
aI20
aI18
aI144
aI111
aI150
aI134
aa(lp123
I238
aI110
aI136
aI52
aI100
aI210
aI243
aa(lp124
I111
aI224
aI59
aI197
aI121
aI30
aI108
aa(lp125
I16
aI154
aI161
aI97
aI114
aI90
aI25
aa(lp126
I112
aI225
aI64
aI58
aI67
aI155
aI79
aa(lp127
I15
aI155
aI218
aI158
aI72
aI223
aI58
aa(lp128
I142
aI21
aI105
aI111
aI85
aI19
aI165
aa(lp129
I241
aI111
aI243
aI203
aI94
aI87
aI208
aa(lp130
I113
aI203
aI146
aI228
aI233
aI189
aI24
aa(lp131
I14
aI177
aI8
aI64
aI226
aI249
aI109
aa(lp132
I143
aI63
aI187
aI177
aI255
aI53
aI242
aa(lp133
I240
aI69
aI33
aI21
aI244
aI113
aI135
aa(lp134
I144
aI62
aI192
aI78
aI197
aI176
aI209
aa(lp135
I239
aI68
aI90
aI234
aI206
aI244
aI164
aa(lp136
I110
aI202
aI233
aI27
aI211
aI56
aI59
aa(lp137
I17
aI176
aI115
aI191
aI216
aI124
aI78
aa(lp138
I174
aI60
aI54
aI173
aI177
aI167
aI151
aa(lp139
I209
aI70
aI172
aI9
aI186
aI227
aI226
aa(lp140
I80
aI200
aI31
aI248
aI167
aI47
aI125
aa(lp141
I47
aI178
aI133
aI92
aI172
aI107
aI8
aa(lp142
I79
aI201
aI100
aI7
aI157
aI170
aI94
aa(lp143
I48
aI179
aI254
aI163
aI150
aI238
aI43
aa(lp144
I177
aI61
aI77
aI82
aI139
aI34
aI180
aa(lp145
I206
aI71
aI215
aI246
aI128
aI102
aI193
aa(lp146
I210
aI56
aI199
aI118
aI89
aI137
aI27
aa(lp147
I173
aI66
aI93
aI210
aI82
aI205
aI110
aa(lp148
I44
aI204
aI238
aI35
aI79
aI1
aI241
aa(lp149
I83
aI182
aI116
aI135
aI68
aI69
aI132
aa(lp150
I51
aI205
aI149
aI220
aI117
aI132
aI210
aa(lp151
I76
aI183
aI15
aI120
aI126
aI192
aI167
aa(lp152
I205
aI57
aI188
aI137
aI99
aI12
aI56
aa(lp153
I178
aI67
aI38
aI45
aI104
aI72
aI77
aa(lp154
I13
aI207
aI99
aI63
aI1
aI147
aI148
aa(lp155
I114
aI181
aI249
aI155
aI10
aI215
aI225
aa(lp156
I243
aI59
aI74
aI106
aI23
aI27
aI126
aa(lp157
I140
aI65
aI208
aI206
aI28
aI95
aI11
aa(lp158
I236
aI58
aI49
aI149
aI45
aI158
aI93
aa(lp159
I147
aI64
aI171
aI49
aI38
aI218
aI40
aa(lp160
I18
aI206
aI24
aI192
aI59
aI22
aI183
aa(lp161
I109
aI180
aI130
aI100
aI48
aI82
aI194
aa(lp162
I42
aI48
aI56
aI221
aI148
aI213
aI30
aa(lp163
I85
aI74
aI162
aI121
aI159
aI145
aI107
aa(lp164
I212
aI196
aI17
aI136
aI130
aI93
aI244
aa(lp165
I171
aI190
aI139
aI44
aI137
aI25
aI129
aa(lp166
I203
aI197
aI106
aI119
aI184
aI216
aI215
aa(lp167
I180
aI191
aI240
aI211
aI179
aI156
aI162
aa(lp168
I53
aI49
aI67
aI34
aI174
aI80
aI61
aa(lp169
I74
aI75
aI217
aI134
aI165
aI20
aI72
aa(lp170
I245
aI199
aI156
aI148
aI204
aI207
aI145
aa(lp171
I138
aI189
aI6
aI48
aI199
aI139
aI228
aa(lp172
I11
aI51
aI181
aI193
aI218
aI71
aI123
aa(lp173
I116
aI73
aI47
aI101
aI209
aI3
aI14
aa(lp174
I20
aI50
aI206
aI62
aI224
aI194
aI88
aa(lp175
I107
aI72
aI84
aI154
aI235
aI134
aI45
aa(lp176
I234
aI198
aI231
aI107
aI246
aI74
aI178
aa(lp177
I149
aI188
aI125
aI207
aI253
aI14
aI199
aa(lp178
I137
aI195
aI109
aI79
aI36
aI225
aI29
aa(lp179
I246
aI185
aI247
aI235
aI47
aI165
aI104
aa(lp180
I119
aI55
aI68
aI26
aI50
aI105
aI247
aa(lp181
I8
aI77
aI222
aI190
aI57
aI45
aI130
aa(lp182
I104
aI54
aI63
aI229
aI8
aI236
aI212
aa(lp183
I23
aI76
aI165
aI65
aI3
aI168
aI161
aa(lp184
I150
aI194
aI22
aI176
aI30
aI100
aI62
aa(lp185
I233
aI184
aI140
aI20
aI21
aI32
aI75
aa(lp186
I86
aI52
aI201
aI6
aI124
aI251
aI146
aa(lp187
I41
aI78
aI83
aI162
aI119
aI191
aI231
aa(lp188
I168
aI192
aI224
aI83
aI106
aI115
aI120
aa(lp189
I215
aI186
aI122
aI247
aI97
aI55
aI13
aa(lp190
I183
aI193
aI155
aI172
aI80
aI246
aI91
aa(lp191
I200
aI187
aI1
aI8
aI91
aI178
aI46
aa(lp192
I73
aI53
aI178
aI249
aI70
aI126
aI177
aa(lp193
I54
aI79
aI40
aI93
aI77
aI58
aI196
aa(lp194
I199
aI32
aI219
aI150
aI19
aI109
aI20
aa(lp195
I184
aI90
aI65
aI50
aI24
aI41
aI97
aa(lp196
I57
aI212
aI242
aI195
aI5
aI229
aI254
aa(lp197
I70
aI174
aI104
aI103
aI14
aI161
aI139
aa(lp198
I38
aI213
aI137
aI60
aI63
aI96
aI221
aa(lp199
I89
aI175
aI19
aI152
aI52
aI36
aI168
aa(lp200
I216
aI33
aI160
aI105
aI41
aI232
aI55
aa(lp201
I167
aI91
aI58
aI205
aI34
aI172
aI66
aa(lp202
I24
aI215
aI127
aI223
aI75
aI119
aI155
aa(lp203
I103
aI173
aI229
aI123
aI64
aI51
aI238
aa(lp204
I230
aI35
aI86
aI138
aI93
aI255
aI113
aa(lp205
I153
aI89
aI204
aI46
aI86
aI187
aI4
aa(lp206
I249
aI34
aI45
aI117
aI103
aI122
aI82
aa(lp207
I134
aI88
aI183
aI209
aI108
aI62
aI39
aa(lp208
I7
aI214
aI4
aI32
aI113
aI242
aI184
aa(lp209
I120
aI172
aI158
aI132
aI122
aI182
aI205
aa(lp210
I100
aI211
aI142
aI4
aI163
aI89
aI23
aa(lp211
I27
aI169
aI20
aI160
aI168
aI29
aI98
aa(lp212
I154
aI39
aI167
aI81
aI181
aI209
aI253
aa(lp213
I229
aI93
aI61
aI245
aI190
aI149
aI136
aa(lp214
I133
aI38
aI220
aI174
aI143
aI84
aI222
aa(lp215
I250
aI92
aI70
aI10
aI132
aI16
aI171
aa(lp216
I123
aI210
aI245
aI251
aI153
aI220
aI52
aa(lp217
I4
aI168
aI111
aI95
aI146
aI152
aI65
aa(lp218
I187
aI36
aI42
aI77
aI251
aI67
aI152
aa(lp219
I196
aI94
aI176
aI233
aI240
aI7
aI237
aa(lp220
I69
aI208
aI3
aI24
aI237
aI203
aI114
aa(lp221
I58
aI170
aI153
aI188
aI230
aI143
aI7
aa(lp222
I90
aI209
aI120
aI231
aI215
aI78
aI81
aa(lp223
I37
aI171
aI226
aI67
aI220
aI10
aI36
aa(lp224
I164
aI37
aI81
aI178
aI193
aI198
aI187
aa(lp225
I219
aI95
aI203
aI22
aI202
aI130
aI206
aa(lp226
I156
aI219
aI113
aI175
aI110
aI5
aI18
aa(lp227
I227
aI161
aI235
aI11
aI101
aI65
aI103
aa(lp228
I98
aI47
aI88
aI250
aI120
aI141
aI248
aa(lp229
I29
aI85
aI194
aI94
aI115
aI201
aI141
aa(lp230
I125
aI46
aI35
aI5
aI66
aI8
aI219
aa(lp231
I2
aI84
aI185
aI161
aI73
aI76
aI174
aa(lp232
I131
aI218
aI10
aI80
aI84
aI128
aI49
aa(lp233
I252
aI160
aI144
aI244
aI95
aI196
aI68
aa(lp234
I67
aI44
aI213
aI230
aI54
aI31
aI157
aa(lp235
I60
aI86
aI79
aI66
aI61
aI91
aI232
aa(lp236
I189
aI216
aI252
aI179
aI32
aI151
aI119
aa(lp237
I194
aI162
aI102
aI23
aI43
aI211
aI2
aa(lp238
I162
aI217
aI135
aI76
aI26
aI18
aI84
aa(lp239
I221
aI163
aI29
aI232
aI17
aI86
aI33
aa(lp240
I92
aI45
aI174
aI25
aI12
aI154
aI190
aa(lp241
I35
aI87
aI52
aI189
aI7
aI222
aI203
aa(lp242
I63
aI40
aI36
aI61
aI222
aI49
aI17
aa(lp243
I64
aI82
aI190
aI153
aI213
aI117
aI100
aa(lp244
I193
aI220
aI13
aI104
aI200
aI185
aI251
aa(lp245
I190
aI166
aI151
aI204
aI195
aI253
aI142
aa(lp246
I222
aI221
aI118
aI151
aI242
aI60
aI216
aa(lp247
I161
aI167
aI236
aI51
aI249
aI120
aI173
aa(lp248
I32
aI41
aI95
aI194
aI228
aI180
aI50
aa(lp249
I95
aI83
aI197
aI102
aI239
aI240
aI71
aa(lp250
I224
aI223
aI128
aI116
aI134
aI43
aI158
aa(lp251
I159
aI165
aI26
aI208
aI141
aI111
aI235
aa(lp252
I30
aI43
aI169
aI33
aI144
aI163
aI116
aa(lp253
I97
aI81
aI51
aI133
aI155
aI231
aI1
aa(lp254
I1
aI42
aI210
aI222
aI170
aI38
aI87
aa(lp255
I126
aI80
aI72
aI122
aI161
aI98
aI34
aa(lp256
I255
aI222
aI251
aI139
aI188
aI174
aI189
aa(lp257
I128
aI164
aI97
aI47
aI183
aI234
aI200
aa.""")
