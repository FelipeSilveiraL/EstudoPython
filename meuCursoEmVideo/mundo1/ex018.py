import math
from math import radians, cos, sin, tan

angulo = float(input('Digite o angulo que você deseja: '))

radian = radians(angulo)

cos = cos(radian)

sen = sin(radian)

tan = tan(radian)

print('O angulo {} tem o cosseno {:.2f} \n tem seno {:.2f}\n e tem a tangente {:.2f}'.format(angulo, cos, sen, tan))