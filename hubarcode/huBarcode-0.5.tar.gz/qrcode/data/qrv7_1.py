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
aI35
aI35
aI35
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
aI20
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
aI35
aI35
aI35
aI35
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
aI1
aI0
aI1
aI0
aI1
aI0
aI1
aI0
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
aI36
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI28
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI20
aI20
aI19
aI19
aI18
aI18
aI17
aI17
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI21
aI21
aI22
aI22
aI23
aI23
aI24
aI24
aI29
aI29
aI30
aI30
aI31
aI31
aI32
aI32
aI37
aI37
aI38
aI38
aI39
aI39
aI40
aI40
aI44
aI44
aI43
aI43
aI42
aI42
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
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI28
aI28
aI29
aI29
aI30
aI30
aI31
aI31
aI41
aI41
aI42
aI42
aI43
aI43
aI44
aI44
aI40
aI39
aI38
aI37
aI36
aI35
aI35
aI34
aI30
aI29
aI29
aI28
aI28
aI27
aI27
aI26
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
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI23
aI23
aI24
aI24
aI25
aI25
aI26
aI26
aI31
aI31
aI32
aI32
aI33
aI33
aI34
aI34
aI39
aI39
aI40
aI40
aI41
aI41
aI42
aI42
aI42
aI42
aI41
aI41
aI40
aI40
aI39
aI39
aI34
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI26
aI26
aI25
aI25
aI24
aI24
aI23
aI23
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI1
aI1
aI0
aI0
aI0
aI0
aI1
aI1
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI23
aI23
aI24
aI24
aI25
aI25
aI26
aI26
aI31
aI31
aI32
aI32
aI33
aI33
aI34
aI34
aI39
aI39
aI40
aI40
aI41
aI41
aI42
aI42
aI42
aI42
aI41
aI41
aI40
aI40
aI39
aI39
aI34
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI26
aI26
aI25
aI25
aI24
aI24
aI23
aI23
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI10
aI10
aI9
aI9
aI8
aI8
aI7
aI7
aI1
aI1
aI0
aI0
aI0
aI0
aI1
aI1
aI7
aI7
aI8
aI8
aI9
aI9
aI10
aI10
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI23
aI23
aI24
aI24
aI25
aI25
aI26
aI26
aI31
aI31
aI32
aI32
aI33
aI33
aI34
aI34
aI39
aI39
aI40
aI40
aI41
aI41
aI42
aI42
aI42
aI42
aI41
aI41
aI35
aI35
aI34
aI34
aI29
aI29
aI28
aI28
aI27
aI27
aI26
aI26
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI3
aI3
aI2
aI2
aI1
aI1
aI0
aI0
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI17
aI17
aI18
aI18
aI19
aI19
aI25
aI25
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI36
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI28
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI17
aI17
aI16
aI16
aI15
aI15
aI14
aI14
aI9
aI9
aI8
aI7
aI5
aI4
aI3
aI3
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI37
aI42
aI42
aI43
aI43
aI44
aI44
aI44
aI44
aI39
aI39
aI38
aI38
aI37
aI37
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
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI20
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI3
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI37
aI42
aI42
aI43
aI43
aI44
aI44
aI44
aI44
aI39
aI39
aI38
aI38
aI37
aI37
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
aI40
aI40
aI39
aI39
aI38
aI38
aI37
aI37
aI32
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI24
aI24
aI23
aI23
aI22
aI22
aI21
aI21
aI16
aI16
aI15
aI15
aI14
aI14
aI13
aI13
aI9
aI9
aI10
aI10
aI11
aI11
aI12
aI12
aI17
aI17
aI18
aI18
aI19
aI19
aI20
aI20
aI25
aI25
aI26
aI26
aI27
aI27
aI28
aI28
aI33
aI33
aI34
aI34
aI35
aI35
aI36
aI36
aI41
aI41
aI42
aI42
aI43
aI43
aI44
aI44
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI27
aI27
aI26
aI26
aI25
aI25
aI19
aI19
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI19
aI19
aI25
aI25
aI26
aI26
aI27
aI27
aI32
aI32
aI33
aI33
aI34
aI34
aI35
aI35
aI44
aI44
aI43
aI43
aI42
aI42
aI41
aI41
aI34
aI33
aI33
aI32
aI32
aI31
aI31
aI30
aI26
aI25
aI25
aI24
aI23
aI22
aI21
aI20
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI7
aI7
aI0
aI1
aI2
aI3
aI4
aI5
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI35
aI35
aI36
aI36
aI37
aI37
aI38
aI38
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI38
aI38
aI37
aI37
aI36
aI36
aI35
aI35
aI30
aI30
aI29
aI29
aI28
aI28
aI27
aI27
aI22
aI22
aI21
aI21
aI20
aI20
aI19
aI19
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI5
aI5
aI4
aI4
aI3
aI3
aI2
aI2
aI2
aI2
aI3
aI3
aI4
aI4
aI5
aI5
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI35
aI35
aI36
aI36
aI37
aI37
aI38
aI38
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI38
aI38
aI37
aI37
aI36
aI36
aI35
aI35
aI30
aI30
aI29
aI29
aI28
aI28
aI27
aI27
aI22
aI22
aI21
aI21
aI20
aI20
aI19
aI19
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI5
aI5
aI4
aI4
aI3
aI3
aI2
aI2
aI2
aI2
aI3
aI3
aI4
aI4
aI5
aI5
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI19
aI19
aI20
aI20
aI21
aI21
aI22
aI22
aI27
aI27
aI28
aI28
aI29
aI29
aI30
aI30
aI35
aI35
aI36
aI36
aI37
aI37
aI38
aI38
aI43
aI43
aI44
aI44
aI44
aI44
aI43
aI43
aI33
aI33
aI32
aI32
aI31
aI31
aI30
aI30
aI25
aI25
aI19
aI19
aI18
aI18
aI17
aI17
aI12
aI12
aI11
aI11
aI10
aI10
aI9
aI9
aI0
aI0
aI1
aI1
aI2
aI2
aI3
aI3
aI13
aI13
aI14
aI14
aI15
aI15
aI16
aI16
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI34
aI34
aI35
aI35
aI41
aI41
aI42
aI42
aI42
aI42
aI41
aI41
aI40
aI39
aI38
aI37
aI32
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI23
aI22
aI21
aI20
aI19
aI19
aI18
aI18
aI13
aI13
aI12
aI12
aI11
aI11
aI10
aI10
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI38
aI38
aI39
aI39
aI40
aI40
aI41
aI41
aI43
aI43
aI42
aI42
aI41
aI41
aI40
aI40
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI24
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
aI10
aI10
aI9
aI9
aI8
aI8
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI38
aI38
aI39
aI39
aI40
aI40
aI41
aI41
aI43
aI43
aI42
aI42
aI41
aI41
aI40
aI40
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI27
aI27
aI26
aI26
aI25
aI25
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
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI7
aI7
aI5
aI5
aI4
aI4
aI3
aI3
aI1
aI1
aI2
aI2
aI3
aI3
aI4
aI4
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
aI34
aI34
aI35
aI35
aI36
aI36
aI37
aI37
aI42
aI42
aI43
aI43
aI44
aI44
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
aI18
aI18
aI17
aI17
aI16
aI16
aI15
aI15
aI10
aI10
aI9
aI9
aI9
aI9
aI10
aI10
aI15
aI15
aI16
aI16
aI17
aI17
aI18
aI18
aI28
aI28
aI29
aI29
aI30
aI30
aI31
aI31
aI31
aI31
aI30
aI30
aI29
aI29
aI28
aI28
aI23
aI23
aI22
aI22
aI21
aI21
aI20
aI20
aI15
aI15
aI14
aI14
aI13
aI13
aI12
aI12
aI10
aI10
aI11
aI11
aI12
aI12
aI13
aI13
aI18
aI18
aI19
aI19
aI20
aI20
aI21
aI21
aI26
aI26
aI27
aI27
aI28
aI28
aI29
aI29
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
aI10
aI10
aI9
aI9
aI8
aI8
aI2
aI2
aI1
aI1
aI0
aI0
aI0
aI0
aI5
aI5
aI7
aI7
aI8
aI8
aI9
aI9
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
aI30
aI30
aI31
aI31
aI32
aI32
aI33
aI33
aI38
aI38
aI39
aI39
aI40
aI40
aI41
aI41
aI35
aI35
aI34
aI34
aI33
aI33
aI32
aI32
aI27
aI27
aI26
aI26
aI25
aI25
aI19
aI19
aI14
aI14
aI13
aI13
aI12
aI12
aI11
aI11
aI11
aI11
aI12
aI12
aI13
aI13
aI14
aI14
aI19
aI19
aI25
aI25
aI26
aI26
aI27
aI27
aI32
aI32
aI33
aI33
aI33
aI33
aI32
aI32
aI27
aI27
aI26
aI26
aI25
aI25
aI24
aI24
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
aI10
aI10
aI9
aI9
aI9
aI9
aI14
aI14
aI15
aI15
aI16
aI16
aI17
aI17
aI22
aI22
aI23
aI23
aI24
aI24
aI25
aI25
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
aI203
aI102
aI144
aI149
aI243
aI126
aI72
aI133
aI144
aI149
aI243
aI126
aI72
aI133
aI3
aI102
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
aI219
aI146
aI144
aI153
aI227
aI98
aI72
aI65
aI144
aI153
aI227
aI98
aI72
aI65
aI19
aI90
aI74
aI145
aI146
aI137
aI98
aI100
aI81
aI231
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
aI100
aI153
aI247
aI130
aI124
aI129
aI231
aI90
aI108
aI145
aI247
aI74
aI116
aI65
aI239
aI114
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
aI124
aI129
aI231
aI90
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
aI116
aI65
aI247
aI74
aI108
aI145
aI231
aI146
aI247
aI74
aI108
aI145
aI231
aI146
aI116
aI137
aI108
aI145
aI231
aI146
aI116
aI137
aI255
aI98
aI96
aI141
aI19
aI118
aI88
aI149
aI227
aI110
aI72
aI133
aI243
aI126
aI144
aI149
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
aI144
aI149
aI203
aI102
aI19
aI90
aI72
aI65
aI114
aI128
aI137
aI203
aI130
aI112
aI145
aI19
aI146
aI96
aI129
aI3
aI74
aI88
aI81
aI114
aI144
aI153
aI219
aI146
aI96
aI129
aI3
aI74
aI112
aI145
aI90
aI65
aI153
aI146
aI96
aI129
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
aI239
aI114
aI116
aI65
aI247
aI74
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
aI112
aI157
aI219
aI118
aI128
aI133
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
aI88
aI81
aI3
aI74
aI96
aI129
aI19
aI90
aI112
aI145
aI203
aI130
aI128
aI137
aI247
aI130
aI100
aI153
aI239
aI114
aI116
aI65
aI90
aI124
aI129
aI247
aI130
aI100
aI153
aI239
aI146
aI116
aI137
aI98
aI81
aI90
aI129
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
aI231
aI146
aI108
aI145
aI247
aI74
aI116
aI65
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
aI124
aI129
aI231
aI90
aI108
aI145
aI247
aI74
aI116
aI65
aI239
aI114
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
aI124
aI129
aI247
aI130
aI100
aI153
aI239
aI114
aI116
aI137
aI100
aI153
aI239
aI114
aI116
aI65
aI255
aI98
aI100
aI81
aI231
aI90
aI124
aI129
aI227
aI110
aI128
aI133
aI219
aI118
aI112
aI157
aI128
aI133
aI219
aI118
aI112
aI157
aI3
aI102
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
aI72
aI133
aI243
aI126
aI227
aI98
aI144
aI153
aI146
aI129
aI74
aI81
aI90
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI137
aI130
aI145
aI90
aI72
aI65
aI227
aI98
aI88
aI81
aI243
aI114
aI128
aI137
aI203
aI130
aI3
aI74
aI88
aI81
aI243
aI114
aI255
aI98
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
aI72
aI65
aI227
aI98
aI144
aI153
aI219
aI146
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
aI129
aI96
aI90
aI19
aI145
aI112
aI74
aI3
aI65
aI72
aI114
aI243
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
aI149
aI128
aI118
aI203
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
aI98
aI239
aI65
aI100
aI90
aI247
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
aI96
aI129
aI3
aI74
aI88
aI81
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
aI81
aI88
aI98
aI227
aI137
aI128
aI146
aI219
aI153
aI144
aI137
aI128
aI146
aI219
aI145
aI112
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
rs_ecc_codewords = 20
rs_block_order = cPickle.loads("""(lp1
I98
aI98
a.""")
from qrcode.data.rsc20 import rs_cal_table
from qrcode.data.fr7 import frame_data
