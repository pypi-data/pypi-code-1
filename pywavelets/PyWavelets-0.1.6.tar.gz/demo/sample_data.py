# -*- coding: utf-8 -*-

ecg = [-86, -87, -87, -89, -89, -90, -91, -93, -96, -97, -97, -94, -93, -95, -97, -97, -95, -94, -95, -93, -97, -97,
 -94, -91, -92, -93, -93, -95, -92, -88, -87, -90, -90, -88, -90, -87, -91, -88, -89, -88, -85, -84, -83, -84,
 -83, -81, -80, -79, -78, -81, -81, -80, -76, -74, -77, -74, -75, -75, -73, -70, -71, -69, -72, -73, -72, -68,
 -69, -68, -69, -72, -70, -69, -69, -67, -70, -71, -67, -67, -65, -64, -66, -65, -63, -61, -62, -62, -68, -70,
 -65, -63, -63, -68, -66, -66, -62, -62, -63, -66, -65, -63, -60, -60, -58, -61, -64, -64, -60, -56, -57, -59,
 -59, -57, -57, -55, -57, -59, -58, -59, -55, -53, -53, -52, -56, -53, -52, -50, -48, -48, -51, -52, -49, -44,
 -37, -33, -25, -22, -18, -19, -23, -24, -25, -25, -26, -26, -29, -32, -35, -37, -34, -29, -32, -36, -41, -45,
 -45, -44, -46, -45, -50, -53, -51, -49, -51, -53, -55, -51, -51, -48, -48, -51, -55, -54, -52, -48, -50, -52,
 -53, -51, -51, -57, -64, -70, -73, -64, -39, -3, 44, 98, 162, 220, 250, 231, 178, 121, 69, 26, 9, 8, 2, -8, -17, -19, -23, -30, -38, -44, -50, -54, -52, -52, -57, -60, -66, -68, -65, -62, -66, -65, -68, -66, -65, -64, -
64, -65, -65, -65, -63, -64, -65, -64, -67, -67, -66, -64, -63, -66, -67, -69, -64, -61, -64, -66, -68, -67, -67, -62, -62, -64, -67, -66, -63, -61, -60, -61, -63, -63, -62, -59, -56, -56, -58, -57, -53, -51, -52, -52, -
53, -52, -49, -46, -46, -47, -45, -43, -39, -33, -34, -36, -38, -40, -36, -28, -24, -22, -23, -23, -19, -17, -16, -14, -13, -14, -14, -14, -13, -14, -12, -10, -8, -8, -14, -15, -16, -14, -15, -18, -25, -28, -32, -36, -34
, -34, -33, -37, -40, -42, -41, -42, -44, -45, -47, -49, -49, -50, -49, -51, -54, -55, -53, -51, -53, -54, -56, -59, -56, -55, -55, -54, -54, -57, -54, -52, -53, -55, -57, -55, -50, -49, -49, -50, -52, -54, -52, -50, -52
, -53, -54, -52, -51, -50, -51, -52, -52, -51, -47, -47, -47, -48, -49, -53, -49, -49, -47, -48, -49, -53, -50, -48, -50, -48, -48, -48, -45, -43, -43, -45, -48, -51, -46, -42, -42, -46, -49, -48, -47, -44, -45, -46, -49
, -52, -49, -48, -47, -48, -49, -48, -46, -45, -44, -46, -51, -48, -46, -44, -48, -50, -49, -51, -50, -48, -47, -49, -49, -50, -49, -46, -48, -49, -50, -51, -49, -43, -46, -47, -50, -49, -48, -46, -47, -50, -55, -54, -53
, -47, -48, -49, -49, -47, -46, -45, -46, -50, -48, -47, -46, -47, -45, -45, -45, -41, -33, -23, -18, -17, -20, -25, -25, -24, -24, -26, -30, -32, -31, -30, -31, -32, -35, -39, -38, -37, -38, -45, -50, -52, -52, -51, -53
, -52, -53, -54, -55, -56, -57, -57, -58, -59, -57, -56, -57, -57, -60, -63, -60, -56, -56, -61, -65, -72, -77, -80, -81, -68, -42, -3, 46, 99, 162, 214, 236, 208, 155, 101, 53, 15, 2, 0, -5, -12, -20, -24, -33, -45, -53
, -58, -65, -72, -75, -75, -77, -77, -78, -78, -81, -83, -84, -80, -79, -82, -82, -84, -82, -80, -79, -84, -84, -84, -79, -80, -78, -80, -82, -80, -78, -76, -74, -78, -81, -82, -83, -79, -80, -82, -79, -82, -80, -81, -81
, -81, -81, -81, -78, -73, -73, -76, -74, -78, -80, -74, -75, -74, -73, -74, -74, -74, -68, -69, -68, -67, -64, -62, -61, -59, -59, -58, -57, -54, -51, -52, -52, -52, -50, -47, -45, -45, -42, -39, -34, -31, -30, -30, -32
, -31, -29, -28, -25, -25, -25, -25, -26, -25, -22, -24, -29, -32, -29, -32, -33, -39, -41, -44, -44, -46, -45, -47, -51, -54, -57, -53, -57, -60, -63, -62, -62, -61, -62, -62, -66, -69, -66, -65, -66, -65, -66, -65, -64
, -63, -62, -65, -65, -66, -62, -62, -62, -66, -66, -67, -66, -63, -64, -65, -67, -67, -64, -63, -61, -63, -64, -66, -66, -62, -60, -61, -64, -64, -62, -58, -57, -59, -63, -65, -64, -61, -61, -62, -64, -63, -64, -60, -57
, -59, -62, -65, -64, -61, -59, -59, -61, -62, -62, -61, -63, -66, -66, -64, -61, -62, -61, -63, -68, -69, -62, -62, -62, -62, -64, -66, -63, -63, -62, -65, -64, -66, -68, -66, -65, -66, -67, -69, -66, -65, -67, -64, -69
, -68, -65, -61, -62, -64, -67, -69, -68, -67, -62, -64, -67, -69, -68, -64, -63, -64, -64, -66, -63, -62, -60, -61, -61, -61, -58, -54, -54, -56, -55, -56, -51, -49, -48, -47, -40, -37, -29, -22, -21, -23, -28, -35, -37
, -35, -36, -39, -43, -44, -44, -43, -44, -47, -50, -53, -53, -53, -55, -65, -71, -71, -69, -64, -66, -73, -77, -77, -74, -73, -72, -73, -74, -77, -77, -79, -81, -82, -80, -79, -81, -79, -81, -87, -88, -87, -87, -85, -86
, -81, -57, -22, 15, 63, 124, 173, 188, 157, 108, 60, 18, -20, -36, -35, -36, -42, -47, -55, -64, -74, -80, -86, -95, -100, -106, -107, -103, -101, -103, -107, -112, -110, -107, -103, -106, -109, -111, -111, -108, -109,
-107, -107, -108, -111, -108, -108, -104, -105, -110, -111, -110, -106, -104, -101, -104, -110, -112, -109, -106, -107, -107, -110, -111, -108, -108, -108, -109, -110, -107, -106, -105, -101, -101, -105, -111, -108, -102
, -99, -105, -104, -103, -100, -97, -98, -99, -99, -97, -94, -93, -95, -94, -94, -89, -87, -89, -92, -93, -88, -85, -80, -79, -79, -77, -80, -75, -72, -69, -69, -70, -70, -68, -65, -63, -63, -61, -64, -61, -60, -56, -56,
 -58, -61, -59, -58, -59, -62, -64, -66, -65, -66, -69, -73, -77, -80, -78, -77, -77, -79, -83, -86, -87, -86, -88, -86, -89, -91, -88, -85, -88, -91, -93, -94, -93, -89, -91, -90, -90, -90, -85, -86, -86, -85, -88, -90,
 -89, -88, -85, -84, -82, -84, -86, -82, -82, -81, -80, -81, -76, -77, -78, -78, -77, -77]

linchirp = [0, 3.007789412461790e-003, 1.203088554210192e-002, 2.706683951521872e-002, 4.810612928136613e-002, 7.512400678460443e-002, 1.080691135128659e-001, 1.468489251105125e-001, 1.913121474025914e-001, 2.412282805206653e-001, 2.962647010840956e-001, 3.559617896752252e-001, 4.197068554236811e-001, 4.867078819423855e-001, 5.559684358872767e-001, 6.262654327139229e-001, 6.961318289685889e-001, 7.638466839768083e-001, 8.274353742067098e-001, 8.846830089250226e-001, 9.331642337013824e-001, 9.702925568674475e-001, 9.933920236638010e-001, 9.997934203258242e-001, 9.869561450484191e-001, 9.526153749805995e-001, 8.949521507885030e-001, 8.127814915099835e-001, 7.057506924858551e-001, 5.745366657875667e-001, 4.210277560624610e-001, 2.484721992169966e-001, 6.157267902829323e-002, -1.334952388619917e-001, -3.291631018887285e-001,
-5.166682143881849e-001, -6.863863425447830e-001, -8.283059320743780e-001, -9.326399673027204e-001, -9.905570454294205e-001, -9.949960419546720e-001, -9.415100516633416e-001, -8.290668744974642e-001, -6.607175607755383e-001, -4.440343271854169e-001, -1.912176749092952e-001, 8.121713220081168e-002, 3.532394448996247e-001, 6.026134573018546e-001, 8.066890348342584e-001, 9.445756382228782e-001, 9.995284980216593e-001, 9.613056423370464e-001, 8.281980642486274e-001, 6.084062154671661e-001, 3.204469388316183e-001, -7.663783956310570e-003, -3.405902169020794e-001, -6.391871730459998e-001, -8.651015405290762e-001, -9.860019620872785e-001, -9.807701675807096e-001, -8.438458924748751e-001, -5.878806357782754e-001, -2.439594759051880e-001, 1.410865073865378e-001, 5.103397559364021e-001, 8.049649647173516e-001, 9.738648831288737e-001, 9.833130867175265e-001, 8.247573264514561e-001, 5.189943096784169e-001, 1.153024186310750e-001, -3.151082180236172e-001, -6.908878377333008e-001, -9.359254818371735e-001, -9.955609795052580e-001, -8.501897510826044e-001, -5.228044837861861e-001, -7.783508798719896e-002, 3.897179826736685e-001,
7.736490442549746e-001, 9.808639771993487e-001, 9.552358810521869e-001, 6.948091358823296e-001, 2.569233202690212e-001, -2.517571531581491e-001, -6.996044845599583e-001, -9.638805557005051e-001, -9.656687144307665e-001, -6.958553822081260e-001, -2.233008763381606e-001, 3.195236517334790e-001, 7.718009712876560e-001, 9.919880473508416e-001, 9.039823003904757e-001, 5.265224167799072e-001, -2.599644186155510e-002, -5.749304897559703e-001, -9.338587447852141e-001, -9.730221040074056e-001,
-6.694145802638251e-001, -1.225296148439667e-001, 4.739396447509804e-001, 8.985142178597478e-001, 9.848645726349685e-001, 6.903309557015613e-001, 1.209891409169086e-001, -5.015499372998722e-001, -9.238732017038523e-001, -9.648324092326215e-001, -5.972617039888690e-001, 3.065063470274572e-002, 6.498667259709371e-001, 9.837328598717922e-001, 8.736379732976350e-001, 3.595906269469231e-001, -3.268672675543495e-001, -8.623122986388434e-001, -9.835073197244207e-001, -6.210363889939856e-001, 5.478659217738370e-002, 7.073258108939412e-001, 9.988396240033057e-001, 7.682161674358605e-001, 1.267673686687481e-001, -5.874036366503110e-001, -9.834877294309661e-001, -8.337066150826492e-001, -2.111813156711696e-001, 5.364586915827642e-001, 9.760005956398086e-001, 8.410781615519729e-001, 2.008328038493807e-001, -5.653627864445258e-001, -9.870952308910393e-001, -7.934830201680115e-001,
-9.523859561210964e-002, 6.681802378307477e-001, 9.999827291371586e-001, 6.724389279986707e-001, -1.074830197909635e-001, -8.185583291807098e-001, -9.700592468434635e-001, -4.459521565939600e-001, 3.958696539256738e-001, 9.586678530366565e-001, 8.293963644566057e-001, 9.060267925811132e-002, -7.191565590995228e-001, -9.914158502629745e-001, -5.092633223075667e-001, 3.681634807011343e-001, 9.620478585726858e-001, 7.978918206803141e-001, -5.618529532880189e-003, -8.081725018197523e-001,
-9.518179933287935e-001, -3.066348798493150e-001, 5.986503437964386e-001, 9.995347571572828e-001, 5.436580643580313e-001, -3.864025715690843e-001, -9.807490291123027e-001, -7.059637508111158e-001, 2.043319702247320e-001, 9.325314013892442e-001, 8.067530213457914e-001, -6.892005244645351e-002, -8.831808838303669e-001, -8.620746036824353e-001, -1.369105029401871e-002, 8.510500542764669e-001, 8.847334833950586e-001, 4.220485622906021e-002, -8.455009852437412e-001, -8.811809412600474e-001, -1.660225980221484e-002, 8.680017255253598e-001, 8.503480658719843e-001, -6.310967393587333e-002, -9.123407720957801e-001, -7.838228252547561e-001,
1.957739370718001e-001, 9.638004040540007e-001, 6.674727922690875e-001, -3.756349879415334e-001, -9.979650022071676e-001, -4.852778694866377e-001, 5.869264333744451e-001, 9.807725155896033e-001, 2.264309301965042e-001, -7.977612587572877e-001,
-8.723646603721967e-001, 1.038101211577825e-001, 9.562869122583988e-001, 6.377055752406520e-001, -4.711085689289528e-001, -9.941920396345902e-001, -2.656448244764200e-001, 8.023588889294226e-001,
8.437490423981796e-001, -2.064160941446615e-001, -9.895450227779339e-001, -4.718194467402090e-001, 6.734267726586052e-001, 9.194009995274739e-001, -7.559188844291870e-002, -9.696752611693211e-001, -5.341010093367646e-001, 6.417834931501441e-001, 9.240296711315128e-001, -9.366955807565144e-002, -9.803285948173459e-001, -4.663367496924762e-001, 7.209681912496565e-001, 8.624219399743781e-001, -2.593409939037438e-001, -9.999999978106685e-001, -2.536545839095256e-001, 8.742869977615728e-001, 6.825093690627866e-001, -5.490792797550861e-001, -9.397376479828612e-001, 1.223146826273702e-001, 9.952335786382538e-001, 3.069211559888114e-001,
-8.677088381815030e-001, -6.612411988463558e-001, 6.068486815931580e-001, 8.952203815947339e-001, -2.741132428593652e-001, -9.950559662728734e-001, -7.262836111834641e-002, 9.716109466463557e-001, 3.884877641905773e-001, -8.508920811633361e-001, -6.451541733476058e-001, 6.649874957673384e-001, 8.301618173113556e-001, -4.451443312260822e-001, -9.436556152234230e-001, 2.175036391187755e-001, 9.942553121699926e-001, -1.239210789212413e-003, -9.951285863133735e-001, -1.915247040312162e-001, 
9.608702625438694e-001, 3.547134840943584e-001, -9.053766712633455e-001, -4.868129785348537e-001, 8.406418639562598e-001, 5.893104066173294e-001, -7.762723505813641e-001, -6.653109127391976e-001, 7.194825136544309e-001, 7.184372280957352e-001, -6.753544938075714e-001, -7.520280133260761e-001, 6.471925933753475e-001, 7.686011406571622e-001,
-6.368525861233547e-001, -7.695316245976611e-001, 6.449703056939523e-001, 7.548994668335974e-001, -6.710485790784676e-001, -7.234812676693965e-001, 7.133888496735926e-001, 6.728840516120553e-001, -7.688781491626653e-001, -5.998446772735564e-001, 8.326687289518039e-001, 5.007378523702569e-001, -8.978212888899633e-001, -3.723433479683010e-001,
9.550256378056723e-001, 2.129096803188334e-001, -9.925625725597962e-001, -2.350675211209042e-002, 9.967183810145807e-001, -1.904263983198386e-001, -9.528894580937863e-001, 4.175653286190774e-001, 8.475888092411783e-001, -6.396126942878484e-001, -6.714498840744407e-001, 8.312134369803003e-001, 4.230782933060704e-001, -9.615637419791820e-001, -1.132107513234262e-001, 9.983609577901258e-001, -2.318648471668809e-001, -9.144126230158363e-001, 5.691773797608133e-001, 6.965031418128042e-001, -8.420529653841040e-001, -3.549946892746749e-001, 9.887586857586245e-001, -6.870400460983063e-002,
-9.572039485261866e-001, 5.007690945646119e-001, 7.238881187837023e-001, -8.437748717722990e-001, -3.122865214525470e-001, 9.980372302095245e-001, -1.969890176395066e-001, -8.937087215852141e-001, 6.729819461350726e-001, 5.257243667815481e-001, -9.641556113861010e-001, 2.247234450078764e-002, 9.493869442674235e-001, -5.831307997372291e-001, -5.965087753158351e-001, 9.479524625924634e-001, 2.947633800232930e-003, -9.479141470381807e-001, 6.109905531375961e-001, 5.432742893422764e-001, -9.738566846389962e-001, 1.217176186253192e-001, 8.873549428070365e-001, -7.462661561599739e-001, -3.514604290603134e-001, 9.998701439508037e-001,
-3.870017127039175e-001, -7.076319133785449e-001, 9.238225461425343e-001, -6.460696453019948e-003, -9.164078291810095e-001, 7.332741450498366e-001, 3.243418966321068e-001, -9.956734948481723e-001, 4.989976758401130e-001, 5.752848174842613e-001, -9.853239982297591e-001, 2.724119734910426e-001, 7.456090941170829e-001, -9.279269707952552e-001, 8.339937600887060e-002, 8.499045906451415e-001, -8.585851375236487e-001, -5.473853968998939e-002, 9.069641563799343e-001, -8.018200091505675e-001, -1.384418027605260e-001, 9.327961539868489e-001, -7.722062746231224e-001, -1.680681198244620e-001, 9.370310178076818e-001, -7.760751175466072e-001, -1.442064390656040e-001, 9.214608930255096e-001, -8.126412882615390e-001, -6.636328197997318e-002, 8.798178468781461e-001, -8.738486384932033e-001, 6.597912816242108e-002, 7.986164831119591e-001, -9.430208358485696e-001, 2.499286509849431e-001, 6.596602775572399e-001, -9.932182972122833e-001, 4.735582112670357e-001, 4.453813309286336e-001, -9.871817834144580e-001, 7.090756028369285e-001, 1.481459796706837e-001, -8.817491123087915e-001, 9.074550982954764e-001, -2.166228149249585e-001, -6.399733088454858e-001, 9.995358573701757e-001, -5.968273862110224e-001, -2.524673483664426e-001, 9.102901221024474e-001, -8.978530748423689e-001, 2.359004775023484e-001, 5.912138996163705e-001, -9.972971113484918e-001, 7.072917913148411e-001, 6.695149843018344e-002, -7.917371140775587e-001, 9.832144498670995e-001, -5.249872942981758e-001, -2.724119734911200e-001, 8.905179762314111e-001, -9.413274690803684e-001, 4.040956375612181e-001, 3.788439568141673e-001, -9.272752681086403e-001, 9.176075389365517e-001, -3.667648000264696e-001,
-3.939684984432698e-001, 9.243788671981604e-001, -9.297544279427814e-001, 4.180681408146794e-001, 3.193982436434875e-001, -8.798235653648152e-001, 9.691407530823780e-001, -5.508276973609131e-001, -1.484434334108138e-001, 7.677538326271015e-001, -9.996912448586758e-001, 7.390391923432056e-001, -1.230430407482151e-001, -5.471169871513028e-001, 9.566205239189279e-001, -9.231440510727329e-001, 4.723497528305857e-001, 1.851796121088337e-001, -7.568293650381738e-001, 9.989343716196576e-001, -8.173540243194947e-001, 2.980567814949483e-001, 3.386438501674491e-001, -8.347018129927993e-001, 9.986013822266144e-001, -7.756956098268664e-001, 2.607002225757702e-001, 3.469396448194475e-001, -8.228134924570721e-001, 9.999987674427988e-001, -8.244442404742725e-001, 3.664849642486225e-001, 2.111460360270267e-001, -7.136585909661422e-001, 9.800378350669510e-001, -9.324053592384157e-001, 5.948659576948514e-001, -7.911845348878524e-002,
-4.552748020866846e-001, 8.513468352824254e-001, -9.999231442122488e-001, 8.671041803081296e-001, -4.982155035317221e-001, -2.646858644167711e-004, 4.934511881574446e-001, -8.551427630053852e-001, 9.991508730568025e-001, -8.975880489612395e-001, 5.831014777597434e-001, -1.364039910766045e-001, -3.361861917201325e-001, 7.287836223479760e-001, -9.592137887149990e-001, 9.847161562459670e-001, -8.076194605841132e-001, 4.710555060655999e-001, -4.686831627630871e-002, -3.808361305462485e-001, 7.326930695674161e-001, -9.482966850458950e-001, 9.953409105916057e-001, -8.726997012215302e-001, 6.077280677391013e-001, -2.490548475451157e-001,
-1.432777528320447e-001, 5.083207887845297e-001, -7.935855180599771e-001, 9.619657381419714e-001, -9.955167079114545e-001, 8.959964186140880e-001, -6.825797123636043e-001, 3.875008722131476e-001, -5.054548441075892e-002, -2.866894673644392e-001, 5.859811642435304e-001, -8.165422187228741e-001, 9.576381151014491e-001, -9.996834232829311e-001, 9.439419267161082e-001, -8.011004873052972e-001, 5.890673782740992e-001, -3.303670697228753e-001, 4.947604970007204e-002, 2.296171965010768e-001,
-4.854251367042416e-001, 7.004292951561666e-001, -8.619648343003107e-001, 9.625485390891141e-001, -9.997252314132256e-001, 9.755372873312771e-001, -8.957344765456916e-001, 7.688396843832148e-001, -6.051738849200526e-001, 4.159248359388380e-001, -2.123218756507606e-001, 4.956824127001429e-003, 1.967295112103968e-001, -3.847929604220655e-001,
5.529747390976882e-001, -6.967534568549781e-001, 8.132858334910806e-001, -9.012635971538189e-001, 9.607134757301720e-001, -9.927647669148285e-001, 9.994053697539646e-001, -9.832429745609397e-001, 9.472838146445666e-001, -8.947373329603033e-001, 8.288515418453855e-001, -7.527808836066096e-001, 6.694860797915907e-001, -5.816637710616051e-001, 4.917026388979410e-001, -4.016620809540832e-001, 3.132692887225427e-001, -2.279306537785284e-001, 1.467537184703781e-001, -7.057631106221726e-002, -8.035315034876644e-014]

