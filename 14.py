a < b == case
(a < b) and (b == c)
# a 가 b 보다 작고, 동시에 b 가 c 와 같은지 검사합니다.

(a < b) == case

A and (not B) or C
# A는 B이거나 C가 같지 않느냐?

(a < b) == c

(A and (not B)) or C
T           T     T    T
                  F    T->F
            F     T    T
                  F    F=>T
F           T     T    T
                  F    F
            F     T    T
                  F    F