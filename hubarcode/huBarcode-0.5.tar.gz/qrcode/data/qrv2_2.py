import cPickle

byte_num = 359
matrix_d = cPickle.loads("""(lp1
(lp2
I24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI22
aI21
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI18
aI17
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI15
aI15
aI15
aI15
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI14
aI13
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI12
aI11
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI10
aI9
aI8
aI7
aI8
aI7
aI8
aI7
aI8
aI7
aI8
aI7
aI8
aI7
aI8
aI7
aI8
aI7
aI5
aI4
aI5
aI4
aI5
aI4
aI5
aI4
aI5
aI4
aI5
aI4
aI5
aI4
aI5
aI4
aI3
aI2
aI3
aI2
aI3
aI2
aI3
aI2
aI3
aI2
aI3
aI2
aI3
aI2
aI3
aI2
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aa(lp3
I24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI15
aI15
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI19
aI18
aI17
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aa(lp4
I255
aI98
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI100
aI81
aI231
aI90
aI124
aI129
aI96
aI141
aI19
aI118
aI88
aI149
aI227
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI243
aI126
aI144
aI149
aI203
aI102
aI96
aI141
aI19
aI118
aI88
aI149
aI227
aI110
aI243
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI96
aI129
aI3
aI74
aI88
aI81
aI243
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI137
aI231
aI146
aI108
aI145
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI227
aI110
aI88
aI149
aI19
aI118
aI96
aI141
aI102
aI149
aI126
aI133
aI102
aI112
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI88
aI149
aI19
aI118
aI96
aI141
aI203
aI102
aI144
aI149
aI72
aI133
aI3
aI102
aI112
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI243
aI114
aI88
aI81
aI3
aI74
aI96
aI129
aI219
aI146
aI144
aI153
aI72
aI65
aI19
aI90
aI112
aI145
aI203
aI130
aI128
aI137
aI243
aI114
aI88
aI81
aI3
aI74
aI96
aI129
aI219
aI146
aI144
aI153
aI227
aI98
aI72
aI65
aI19
aI90
aI112
aI145
aI203
aI130
aI128
aI137
aI243
aI114
aI255
aI98
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
aI100
aI153
aI116
aI65
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI227
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI144
aI149
aI203
aI102
aI96
aI141
aI19
aI118
aI88
aI149
aI227
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI243
aI126
aI144
aI149
aI203
aI102
aI96
aI141
aI19
aI118
aI88
aI149
aI227
aI110
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI243
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI129
aI96
aI90
aI19
aI81
aI88
aI98
aI227
aI137
aI128
aI146
aI219
aI145
aI112
aI74
aI3
aI102
aI219
aI157
aI96
aI118
aI3
aI133
aI88
aI110
aI243
aI149
aI128
aI118
aI203
aI141
aI112
aI145
aI124
aI130
aI231
aI137
aI100
aI114
aI255
aI81
aI116
aI74
aI231
aI129
aI108
aI146
aI247
aa.""")
format_info = cPickle.loads("""(lp1
(lp2
I8
aI8
aI8
aI8
aI8
aI8
aI8
aI17
aI18
aI19
aI20
aI21
aI22
aI23
aI24
aa(lp3
I24
aI23
aI22
aI21
aI20
aI19
aI18
aI8
aI8
aI8
aI8
aI8
aI8
aI8
aI8
aa.""")
rs_ecc_codewords = 28
rs_block_order = cPickle.loads("""(lp1
I44
a.""")
from qrcode.data.rsc28 import rs_cal_table
from qrcode.data.fr2 import frame_data
