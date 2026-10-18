# shannon information entropy

shannon information entropy (SIE) is a way to measure uncertainty or surprise in an event

SIE is used in compression because data with low entropy can be compressed more

SIE helps ML algorithms decide when they're uncertain or need more data

for a probabilty distribution P(i), H(P) = -summation(p_i*log_2(p_i))

S = sum across all i outcomes

p_i = probability of the ith outcome

p_i*log_2(p_i) = weighted surprise

the negative sign makes the result

H(P) is the average number of bits of information (or yes/no questions) you need to identify which outcome from distribution P will occur.

# problem

calculate the base-2 entropy H(P) = -summation(p_i*log_2(p_i)) for a balanced distribution P1 = [0.5,0.5] and an imbalanced distribution P2 = [0.9,0.1]

H(P1) = -2*0.5*log_2(0.5) = -log_2(0.5) = -log_2(2^-1) = 1

H(P2) = -[ 0.9*log_2(0.9) + 0.1*log_2(0.1) ] = -[ 0.9* { log_2(9) - log_2(10) } + 0.1 * { log_2(1) - log_2(10) }]

= -[ (0.9*-0.152) + (0.1*-3.321) ]

= 0.4689
