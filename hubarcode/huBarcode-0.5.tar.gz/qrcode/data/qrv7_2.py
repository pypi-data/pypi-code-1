import cPickle

byte_num = 1568
matrix_d = cPickle.loads("""(lp1
(lp2
I44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
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
aI35
aI36
aI35
aI35
aI35
aI35
aI35
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
aI31
aI32
aI31
aI32
aI31
aI30
aI29
aI30
aI29
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
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
aI31
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
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
aI35
aI35
aI35
aI35
aI35
aI36
aI35
aI36
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
aI31
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
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
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
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
aI31
aI30
aI29
aI30
aI29
aI30
aI29
aI30
aI29
aI44
aI43
aI44
aI43
aI44
aI43
aI44
aI43
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
aI42
aI41
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
aI35
aI36
aI35
aI36
aI35
aI36
aI35
aI36
aI36
aI35
aI33
aI33
aI33
aI33
aI33
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
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
aI20
aI19
aI19
aI19
aI19
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
aI19
aI20
aI19
aI20
aI19
aI20
aI19
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
aI20
aI19
aI20
aI19
aI19
aI19
aI19
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
aI20
aI19
aI20
aI19
aI19
aI19
aI19
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
aI19
aI20
aI19
aI20
aI19
aI20
aI19
aI20
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
I44
aI44
aI43
aI43
aI42
aI42
aI41
aI41
aI24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI33
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI41
aI41
aI42
aI42
aI43
aI43
aI44
aI44
aI26
aI25
aI25
aI24
aI23
aI22
aI21
aI20
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI42
aI42
aI41
aI41
aI40
aI40
aI39
aI39
aI22
aI22
aI21
aI21
aI20
aI20
aI19
aI19
aI1
aI1
aI0
aI0
aI0
aI0
aI1
aI1
aI40
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI20
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI17
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI37
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI27
aI27
aI26
aI26
aI25
aI25
aI19
aI19
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI44
aI44
aI43
aI43
aI42
aI42
aI41
aI41
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI31
aI31
aI32
aI32
aI33
aI33
aI34
aI34
aI38
aI38
aI37
aI37
aI36
aI36
aI35
aI35
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI2
aI2
aI3
aI3
aI4
aI4
aI5
aI5
aI36
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI41
aI41
aI42
aI42
aI43
aI43
aI44
aI44
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI19
aI19
aI25
aI25
aI26
aI26
aI27
aI27
aI40
aI39
aI38
aI37
aI36
aI35
aI35
aI34
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI35
aI35
aI36
aI36
aI37
aI37
aI38
aI38
aI34
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI32
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI25
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI44
aI44
aI43
aI43
aI42
aI42
aI41
aI41
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI28
aI28
aI29
aI29
aI30
aI30
aI31
aI31
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI30
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI8
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI39
aI39
aI40
aI40
aI41
aI41
aI42
aI42
aI30
aI30
aI29
aI29
aI28
aI28
aI27
aI27
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI28
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI29
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI32
aI32
aI33
aI33
aI34
aI34
aI35
aI35
aI30
aI29
aI29
aI28
aI28
aI27
aI27
aI26
aI7
aI7
aI0
aI1
aI2
aI3
aI4
aI5
aI23
aI23
aI24
aI24
aI25
aI25
aI26
aI26
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI26
aI26
aI25
aI25
aI24
aI24
aI23
aI23
aI5
aI5
aI4
aI4
aI3
aI3
aI2
aI2
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
aI25
aI25
aI26
aI26
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI26
aI26
aI25
aI25
aI24
aI24
aI23
aI23
aI5
aI5
aI4
aI4
aI3
aI3
aI2
aI2
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI35
aI35
aI36
aI36
aI37
aI37
aI38
aI38
aI29
aI29
aI28
aI28
aI27
aI27
aI26
aI26
aI0
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI9
aI9
aI8
aI7
aI5
aI4
aI3
aI3
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI37
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI43
aI43
aI42
aI42
aI41
aI41
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
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI38
aI38
aI39
aI39
aI40
aI40
aI41
aI41
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI19
aI19
aI25
aI25
aI26
aI26
aI27
aI27
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI20
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI42
aI42
aI41
aI41
aI40
aI40
aI39
aI39
aI22
aI22
aI21
aI21
aI20
aI20
aI19
aI19
aI1
aI1
aI0
aI0
aI0
aI0
aI1
aI1
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI39
aI39
aI40
aI40
aI41
aI41
aI42
aI42
aI25
aI25
aI19
aI19
aI18
aI18
aI17
aI17
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI34
aI34
aI35
aI35
aI41
aI41
aI42
aI42
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI38
aI38
aI39
aI39
aI40
aI40
aI41
aI41
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI8
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI36
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI42
aI42
aI43
aI43
aI44
aI44
aI36
aI36
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI28
aI28
aI29
aI29
aI30
aI30
aI31
aI31
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI31
aI31
aI32
aI32
aI33
aI33
aI34
aI34
aI38
aI38
aI37
aI37
aI36
aI36
aI35
aI35
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI2
aI2
aI3
aI3
aI4
aI4
aI5
aI5
aI23
aI23
aI24
aI24
aI25
aI25
aI26
aI26
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI23
aI22
aI21
aI20
aI19
aI19
aI18
aI18
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI42
aI42
aI43
aI43
aI44
aI44
aI44
aI44
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI24
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI3
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI37
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI32
aI32
aI33
aI33
aI33
aI33
aI32
aI32
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI35
aI35
aI36
aI36
aI37
aI37
aI38
aI38
aI34
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI42
aI42
aI41
aI41
aI35
aI35
aI34
aI34
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI17
aI17
aI18
aI18
aI19
aI19
aI25
aI25
aI42
aI42
aI41
aI41
aI40
aI39
aI38
aI37
aI17
aI17
aI16
aI16
aI15
aI15
aI14
aI14
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI43
aI43
aI42
aI42
aI41
aI41
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
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI38
aI38
aI39
aI39
aI40
aI40
aI41
aI41
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI11
aI11
aI10
aI10
aI9
aI9
aI8
aI8
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI11
aI11
aI10
aI10
aI9
aI9
aI9
aI9
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI39
aI39
aI40
aI40
aI41
aI41
aI42
aI42
aI30
aI30
aI29
aI29
aI28
aI28
aI27
aI27
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI31
aI31
aI32
aI32
aI33
aI33
aI34
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI30
aI30
aI3
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI39
aI39
aI38
aI38
aI37
aI37
aI36
aI36
aI19
aI19
aI18
aI18
aI17
aI17
aI16
aI16
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI42
aI42
aI43
aI43
aI44
aI44
aI44
aI44
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI24
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI3
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI37
aI27
aI27
aI26
aI26
aI25
aI25
aI19
aI19
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI24
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aa(lp4
I19
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI243
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI116
aI137
aI231
aI146
aI108
aI145
aI247
aI74
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI144
aI149
aI243
aI126
aI72
aI133
aI3
aI102
aI128
aI137
aI243
aI114
aI88
aI81
aI3
aI74
aI144
aI153
aI227
aI98
aI72
aI65
aI19
aI90
aI146
aI116
aI137
aI98
aI81
aI90
aI129
aI130
aI144
aI149
aI203
aI102
aI96
aI141
aI19
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI243
aI126
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI203
aI130
aI112
aI145
aI19
aI90
aI72
aI65
aI88
aI81
aI243
aI114
aI255
aI98
aI116
aI137
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI19
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI116
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI116
aI137
aI231
aI146
aI108
aI145
aI247
aI74
aI112
aI157
aI219
aI118
aI128
aI133
aI144
aI149
aI96
aI129
aI219
aI146
aI144
aI153
aI227
aI98
aI247
aI130
aI100
aI153
aI239
aI114
aI116
aI65
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
aI88
aI149
aI227
aI110
aI128
aI133
aI219
aI118
aI144
aI149
aI203
aI102
aI96
aI141
aI19
aI118
aI3
aI74
aI88
aI81
aI243
aI114
aI128
aI137
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI231
aI146
aI108
aI145
aI247
aI74
aI116
aI65
aI243
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI243
aI126
aI72
aI133
aI3
aI102
aI112
aI157
aI72
aI65
aI88
aI81
aI3
aI74
aI96
aI129
aI74
aI145
aI146
aI137
aI98
aI100
aI81
aI231
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI112
aI157
aI3
aI102
aI72
aI133
aI243
aI126
aI88
aI149
aI227
aI110
aI128
aI133
aI219
aI118
aI203
aI130
aI112
aI145
aI19
aI90
aI72
aI65
aI3
aI74
aI88
aI81
aI243
aI114
aI128
aI137
aI100
aI153
aI247
aI130
aI124
aI129
aI231
aI90
aI19
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI243
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI116
aI137
aI231
aI146
aI108
aI145
aI247
aI74
aI203
aI102
aI144
aI149
aI243
aI126
aI72
aI133
aI219
aI118
aI128
aI133
aI227
aI110
aI88
aI149
aI219
aI146
aI144
aI153
aI227
aI98
aI72
aI65
aI90
aI124
aI129
aI247
aI130
aI100
aI153
aI239
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
aI144
aI149
aI203
aI102
aI96
aI141
aI19
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI243
aI126
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI203
aI130
aI112
aI145
aI19
aI90
aI72
aI65
aI100
aI81
aI255
aI98
aI116
aI137
aI231
aI146
aI219
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI124
aI129
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI65
aI239
aI114
aI100
aI153
aI247
aI130
aI88
aI149
aI19
aI118
aI96
aI141
aI203
aI102
aI19
aI118
aI96
aI141
aI112
aI145
aI203
aI130
aI19
aI90
aI112
aI145
aI203
aI130
aI128
aI137
aI114
aI116
aI65
aI247
aI74
aI108
aI145
aI231
aI100
aI153
aI110
aI133
aI118
aI157
aI102
aI133
aI88
aI149
aI227
aI110
aI128
aI133
aI219
aI118
aI144
aI149
aI203
aI102
aI19
aI90
aI72
aI65
aI3
aI74
aI88
aI81
aI243
aI114
aI128
aI137
aI144
aI153
aI219
aI146
aI96
aI129
aI3
aI74
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
aI100
aI153
aI247
aI130
aI203
aI102
aI144
aI149
aI219
aI118
aI128
aI133
aI227
aI110
aI88
aI149
aI72
aI133
aI3
aI102
aI112
aI157
aI219
aI118
aI96
aI129
aI219
aI146
aI144
aI153
aI227
aI98
aI128
aI137
aI243
aI114
aI88
aI81
aI3
aI74
aI116
aI65
aI247
aI74
aI108
aI145
aI231
aI146
aI227
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI243
aI126
aI144
aI149
aI203
aI102
aI96
aI141
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI112
aI145
aI90
aI65
aI153
aI146
aI96
aI129
aI231
aI146
aI108
aI145
aI247
aI74
aI116
aI65
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI137
aI88
aI149
aI19
aI118
aI96
aI141
aI203
aI102
aI112
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI144
aI153
aI72
aI65
aI19
aI90
aI112
aI145
aI3
aI74
aI96
aI129
aI219
aI146
aI144
aI153
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
aI231
aI146
aI116
aI137
aI255
aI98
aI227
aI110
aI243
aI126
aI144
aI149
aI203
aI102
aI96
aI141
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI227
aI98
aI144
aI153
aI219
aI146
aI96
aI129
aI153
aI144
aI137
aI128
aI146
aI219
aI145
aI112
aI149
aI128
aI118
aI203
aI141
aI112
aI102
aI19
aI74
aI231
aI129
aI108
aI146
aI247
aI153
aI116
aI108
aI145
aI247
aI74
aI116
aI65
aI239
aI114
aI243
aI126
aI72
aI133
aI3
aI102
aI112
aI157
aI19
aI118
aI96
aI141
aI203
aI102
aI144
aI149
aI128
aI133
aI227
aI110
aI243
aI114
aI88
aI81
aI72
aI65
aI19
aI90
aI112
aI145
aI203
aI130
aI96
aI129
aI219
aI146
aI144
aI153
aI227
aI98
aI116
aI137
aI100
aI153
aI239
aI114
aI116
aI65
aI96
aI141
aI19
aI118
aI88
aI149
aI227
aI110
aI19
aI118
aI88
aI149
aI72
aI133
aI243
aI126
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI114
aI3
aI74
aI88
aI81
aI243
aI114
aI255
aI98
aI239
aI114
aI100
aI153
aI247
aI130
aI124
aI129
aI231
aI146
aI108
aI145
aI247
aI74
aI116
aI65
aI144
aI149
aI243
aI126
aI72
aI133
aI3
aI102
aI88
aI149
aI19
aI118
aI96
aI141
aI203
aI102
aI203
aI130
aI128
aI137
aI243
aI114
aI88
aI81
aI227
aI98
aI72
aI65
aI19
aI90
aI112
aI145
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
aI128
aI133
aI219
aI118
aI112
aI157
aI3
aI102
aI19
aI118
aI88
aI149
aI227
aI110
aI128
aI133
aI243
aI126
aI144
aI149
aI203
aI102
aI243
aI114
aI3
aI74
aI88
aI81
aI243
aI114
aI128
aI137
aI74
aI3
aI65
aI72
aI114
aI243
aI153
aI144
aI149
aI72
aI126
aI227
aI133
aI144
aI102
aI219
aI98
aI239
aI65
aI100
aI90
aI247
aI145
aI124
aI100
aI153
aI247
aI130
aI124
aI129
aI231
aI90
aI219
aI118
aI128
aI133
aI227
aI110
aI88
aI149
aI243
aI126
aI72
aI133
aI3
aI102
aI112
aI157
aI3
aI74
aI96
aI129
aI219
aI146
aI144
aI153
aI128
aI137
aI243
aI114
aI88
aI81
aI3
aI74
aI72
aI65
aI19
aI90
aI247
aI130
aI100
aI153
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI128
aI133
aI219
aI118
aI112
aI157
aI3
aI102
aI144
aI149
aI203
aI102
aI19
aI90
aI72
aI65
aI137
aI130
aI145
aI90
aI72
aI65
aI227
aI98
aI116
aI137
aI231
aI146
aI108
aI145
aI247
aI74
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI137
aI239
aI114
aI100
aI153
aI247
aI130
aI203
aI102
aI112
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI144
aI149
aI72
aI133
aI3
aI102
aI112
aI157
aI3
aI74
aI96
aI129
aI219
aI146
aI144
aI153
aI203
aI130
aI128
aI137
aI243
aI114
aI88
aI81
aI100
aI81
aI231
aI90
aI124
aI129
aI247
aI130
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI72
aI133
aI144
aI149
aI203
aI102
aI96
aI141
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI128
aI137
aI203
aI130
aI112
aI145
aI19
aI90
aI203
aI130
aI112
aI145
aI129
aI96
aI90
aI19
aI130
aI203
aI129
aI96
aI141
aI112
aI102
aI19
aI157
aI96
aI118
aI3
aI133
aI88
aI110
aI243
aI130
aI231
aI137
aI100
aI114
aI255
aI81
aI116
aI100
aI81
aI255
aI98
aI116
aI137
aI231
aI146
aI19
aI118
aI96
aI141
aI203
aI102
aI144
aI149
aI219
aI118
aI128
aI133
aI227
aI110
aI88
aI149
aI72
aI65
aI19
aI90
aI112
aI145
aI203
aI130
aI96
aI129
aI219
aI146
aI144
aI153
aI227
aI98
aI239
aI114
aI116
aI65
aI100
aI81
aI231
aI90
aI255
aI98
aI100
aI81
aI231
aI90
aI124
aI129
aI72
aI133
aI243
aI126
aI144
aI149
aI128
aI133
aI227
aI98
aI144
aI153
aI146
aI129
aI74
aI81
aI144
aI153
aI219
aI146
aI96
aI129
aI3
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
aI146
aI108
aI145
aI247
aI74
aI116
aI65
aI144
aI149
aI243
aI126
aI72
aI133
aI3
aI102
aI88
aI149
aI19
aI118
aI96
aI141
aI203
aI102
aI219
aI118
aI128
aI133
aI227
aI110
aI243
aI114
aI227
aI98
aI72
aI65
aI19
aI90
aI112
aI145
aI3
aI74
aI96
aI129
aI219
aI146
aI144
aI153
aI100
aI153
aI239
aI114
aI116
aI65
aI247
aI74
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
aI243
aI126
aI144
aI149
aI203
aI102
aI96
aI141
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI146
aI81
aI88
aI98
aI227
aI137
aI128
aI146
aI219
aI149
aI72
aI126
aI227
aI133
aI144
aI102
aI219
aI149
aI128
aI118
aI203
aI141
aI112
aI145
aI124
aI74
aI231
aI129
aI108
aI146
aI247
aI153
aI116
aI108
aI145
aI247
aI74
aI116
aI65
aI239
aI114
aI243
aI126
aI72
aI133
aI3
aI102
aI112
aI157
aI19
aI118
aI96
aI141
aI203
aI102
aI144
aI149
aI128
aI137
aI243
aI114
aI88
aI81
aI3
aI74
aI72
aI65
aI19
aI90
aI112
aI145
aI203
aI130
aI124
aI129
aI247
aI130
aI100
aI153
aI239
aI114
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI19
aI88
aI81
aI243
aI114
aI128
aI137
aI203
aI130
aI231
aI90
aI100
aI81
aI255
aI98
aI116
aI137
aI239
aI114
aI100
aI153
aI247
aI130
aI124
aI129
aI112
aI157
aI219
aI118
aI128
aI133
aI227
aI110
aI144
aI149
aI243
aI126
aI72
aI133
aI3
aI102
aI88
aI81
aI3
aI74
aI96
aI129
aI219
aI146
aI203
aI130
aI128
aI137
aI243
aI114
aI88
aI81
aI227
aI98
aI72
aI65
aI19
aI90
aI247
aI130
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI100
aI153
aI116
aI65
aI247
aI74
aI108
aI145
aI219
aI118
aI112
aI157
aI3
aI102
aI72
aI133
aI19
aI118
aI88
aI149
aI227
aI110
aI128
aI133
aI96
aI129
aI3
aI74
aI88
aI81
aI72
aI65
aI145
aI112
aI74
aI3
aI65
aI72
aI114
aI243
aI157
aI96
aI118
aI3
aI133
aI88
aI110
aI243
aI130
aI231
aI137
aI100
aI114
aI255
aI81
aI116
aI98
aI239
aI65
aI100
aI90
aI247
aI145
aI124
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
aI37
aI38
aI39
aI40
aI41
aI42
aI43
aI44
aa(lp3
I44
aI43
aI42
aI41
aI40
aI39
aI38
aI8
aI8
aI8
aI8
aI8
aI8
aI8
aI8
aa.""")
rs_ecc_codewords = 26
rs_block_order = cPickle.loads("""(lp1
I39
aI39
aI39
aI39
aI40
a.""")
from qrcode.data.rsc26 import rs_cal_table
from qrcode.data.fr7 import frame_data
