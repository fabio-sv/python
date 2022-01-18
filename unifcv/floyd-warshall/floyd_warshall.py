import numpy as np
#pip install numpy

def floydwarshall(D, S):
    n = len(D)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    S[i][j] = S[k][j]

    npd = np.array(D) # formatar matriz
    nps = np.array(S) # formatar matriz

    print("Matriz D: ")
    print(npd)
    print("\n")
    print("Matriz S: ")
    print(nps)

if __name__ == '__main__':
    '''
    D = [[0, 3, 8, float("inf"), -4], 
         [float("inf"), 0, float("inf"), 1, 7], 
         [float("inf"), 4, 0, float("inf"), float("inf")], 
         [2, float("inf"), -5, 0, float("inf")], 
         [float("inf"), float("inf"), float("inf"), 6, 0]]
    
    S = [
			[None, 1    , 1     , None  , 1],
			[None, None , None  , 2     , 2],
			[None, 3    , None  , None  , None],
			[4   , None , 4     , None  , None],
			[None, None , None  , 5     , None]
		]
    '''
    D = [
			[0           ,	float("inf"), 	float("inf"), 	float("inf"),	-1          ,		float("inf")],
			[1           ,	0           , 	float("inf"), 	2           ,	0           ,		float("inf")],
			[float("inf"), 	2           , 	0           ,	float("inf"),	float("inf"),	    -8],
			[-4	         ,	float("inf"),	float("inf"),	0           ,	-5          ,		float("inf")],
			[float("inf"),	7           ,	float("inf"),	float("inf"),	0           ,		float("inf")],
			[float("inf"),	5           ,	10          ,	float("inf"),	float("inf"),	    0]
		]
    S = [
			[None,	1   , 1     , 1     , 1     ,   1],
			[2   ,  None, 2     , 2     , 2     ,	2],
			[3   ,	3   , None  , 3     , 3     ,	3],
			[4   ,	4   , 4     , None  , 4     ,	4],
			[5   ,	5   , 5     , 5     , None  ,	5],
			[6   ,	6   , 6     , 6     , 6     ,	None]
		]	
    
    floydwarshall(D, S)
