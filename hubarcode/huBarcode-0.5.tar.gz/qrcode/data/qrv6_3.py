import cPickle

byte_num = 1383
matrix_d = cPickle.loads("""(lp1
(lp2
I40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI32
aI31
aI32
aI31
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
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
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI32
aI31
aI32
aI31
aI31
aI31
aI31
aI31
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
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
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI40
aI39
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI38
aI37
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI34
aI33
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI31
aI32
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI27
aI28
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
aI25
aI26
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
aI16
aI15
aI16
aI15
aI16
aI15
aI16
aI15
aI16
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
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI23
aI24
aI23
aI24
aI23
aI24
aI23
aI24
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
aI20
aI19
aI20
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
aI8
aI4
aI5
aI4
aI5
aI4
aI5
aI4
aI5
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
aI3
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aI1
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
aI18
aI17
aI18
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
aI7
aI8
aI7
aI8
aI7
aI8
aI7
aI8
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
aI5
aI2
aI3
aI2
aI3
aI2
aI3
aI2
aI3
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
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
aa(lp3
I40
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI25
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI40
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI30
aI30
aI31
aI31
aI37
aI37
aI38
aI38
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI40
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI40
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI36
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI20
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI29
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI39
aI39
aI40
aI40
aI40
aI40
aI39
aI39
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI32
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI17
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI33
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI24
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI9
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI38
aI38
aI37
aI37
aI36
aI35
aI34
aI33
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI28
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI37
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI20
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
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
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI40
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI40
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI40
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI4
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI8
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aa(lp4
I3
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
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
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
aI128
aI133
aI219
aI118
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
aI19
aI74
aI116
aI65
aI100
aI153
aI247
aI130
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
aI247
aI74
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
aI88
aI149
aI19
aI118
aI96
aI141
aI203
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
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI255
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
aI243
aI126
aI72
aI133
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
aI243
aI126
aI144
aI149
aI203
aI102
aI96
aI141
aI112
aI157
aI3
aI102
aI219
aI146
aI96
aI129
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI19
aI90
aI72
aI65
aI144
aI153
aI219
aI146
aI96
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
aI247
aI74
aI116
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
aI203
aI102
aI144
aI149
aI243
aI126
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
aI3
aI74
aI88
aI81
aI114
aI137
aI130
aI145
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI129
aI3
aI74
aI88
aI81
aI243
aI114
aI255
aI137
aI231
aI146
aI108
aI145
aI247
aI74
aI116
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI124
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
aI243
aI126
aI72
aI133
aI3
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI243
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
aI88
aI149
aI19
aI118
aI96
aI141
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
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
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
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI243
aI98
aI116
aI137
aI231
aI146
aI108
aI145
aI247
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI102
aI144
aI149
aI243
aI126
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
aI114
aI88
aI81
aI3
aI74
aI96
aI129
aI219
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
aI88
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
aI19
aI74
aI116
aI65
aI100
aI153
aI247
aI130
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
aI247
aI74
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
aI88
aI149
aI19
aI118
aI96
aI141
aI203
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
aI19
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI128
aI146
aI219
aI145
aI112
aI74
aI3
aI65
aI72
aI114
aI243
aI153
aI144
aI130
aI203
aI102
aI19
aI149
aI72
aI126
aI227
aI133
aI144
aI102
aI116
aI74
aI231
aI129
aI108
aI146
aI247
aI153
aI130
aI100
aI153
aI116
aI65
aI247
aI74
aI108
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
aI19
aI90
aI72
aI65
aI144
aI153
aI219
aI146
aI96
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
aI247
aI74
aI116
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
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI243
aI72
aI114
aI243
aI153
aI144
aI130
aI203
aI129
aI19
aI149
aI72
aI126
aI227
aI133
aI144
aI102
aI219
aI157
aI96
aI118
aI3
aI133
aI88
aI110
aI116
aI98
aI239
aI65
aI100
aI90
aI247
aI145
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI227
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
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI19
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI129
aI3
aI74
aI88
aI81
aI243
aI114
aI255
aI137
aI231
aI146
aI108
aI145
aI247
aI74
aI116
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI124
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
aI243
aI126
aI72
aI133
aI3
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI243
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
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI227
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
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI3
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
aI128
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI243
aI98
aI116
aI137
aI231
aI146
aI108
aI145
aI247
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI102
aI144
aI149
aI243
aI126
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
aI114
aI88
aI81
aI3
aI74
aI96
aI129
aI219
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
aI88
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
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI3
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
aI128
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI19
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
aI65
aI243
aI149
aI128
aI118
aI203
aI141
aI112
aI102
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
aI153
aI116
aI98
aI239
aI65
aI100
aI90
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
aI33
aI34
aI35
aI36
aI37
aI38
aI39
aI40
aa(lp3
I40
aI39
aI38
aI37
aI36
aI35
aI34
aI8
aI8
aI8
aI8
aI8
aI8
aI8
aI8
aa.""")
rs_ecc_codewords = 24
rs_block_order = cPickle.loads("""(lp1
I43
aI43
aI43
aI43
a.""")
from qrcode.data.rsc24 import rs_cal_table
from qrcode.data.fr6 import frame_data
