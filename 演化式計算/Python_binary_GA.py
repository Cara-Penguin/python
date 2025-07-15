from numpy.random import randint
from numpy.random import rand

# Customized your objective function in the following where x is binary chromosome in n-bits
# if you desire a CONTINUOUS function optimization, you need to encode your continuous variables into binary bits

# 定義一個函數叫onemax，裡面參數x接受一個二進制染色體
# sum 是計算染色體中二進制值的總和

def onemax(x):
	return -sum(x)




# Southwestern Airways Crew Scheduling Problem
import numpy as np

#定義優化問題
def southwest(x): # x is chromosome
  cost = [2,3,4,6,7,5,7,8,9,9,8,9] # 每個航段的成本
  # flight sequence
  flight_segment = [[1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,1,0,0,1,0,1,1,0,1],[1,0,0,0,0,1,0,0,0,1,1,0],[0,0,0,1,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,1,0,1,1,1],[0,1,0,1,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,0,1,1,0,0,0,1],[0,0,0,0,0,1,0,0,1,1,1,1]]
  # 0、1表示是否有搭乘該航段。[1,0,0,1,0,0,1,0,0,1,0,0] 表示搭乘第1、4、7、11航段。
  
  TotalCost = 0 # 初始化總成本為 0

  # compute the scheduling cost of the crew assignment
  # np.dot 函式來計算兩個向量的內積
  TotalCost = TotalCost + np.dot(x,cost) # using inner product between two vectors

  # check if all local flights are included
  for i in range(11):
	# 檢查是否有航段未被搭乘。如果機組員分配中存在某個航段未被搭乘，則將成本增加 10。
	# 如果某個航段未被搭乘，機組員分配不完整，所以要逞罰
    if np.dot(x,flight_segment[i])<1:
      TotalCost = TotalCost + 10 # penalty of not including one local flight

	
	  

# check if at most three crew members are assigned
# 是否超過三人。如果超過三人，超過三人的機組員數量乘以 10。
# 機組員人數是足夠但又不過多，超過需要進行逞罰
  if sum(x)>3:
    TotalCost = TotalCost + (sum(x)-3)*10 # penalty of more than three crew member assignments

  return TotalCost #最終計算出的總成本。


# tournament selection

# 天擇(選擇)
# 隨機的方式
# pop代表族群，score代表對應的分數或適應度值的列表，k代表選擇的個體數目
def selection(pop, scores, k=3):
	# first random selection
	selection_ix = randint(len(pop))   # 0 到 len(pop) 之間的隨機整數到selection_ix
	for ix in randint(0, len(pop), k-1):  # 
		# check if better (e.g. perform a tournament)
		#ix是否比目前selection_ix 更好(根據scores)
		#如果是，就將 selection_ix 更新為 ix，以選擇更優秀的個體。
		if scores[ix] < scores[selection_ix]:  
			selection_ix = ix
	return pop[selection_ix]



# crossover two parents to create two children

# 交配
def crossover(p1, p2, r_cross): #p1 和 p2 兩個個體（染色體 --> 父跟母）r_cross 是交配的機率
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()  # 複製基因
	# check for recombination
	if rand() < r_cross: # 產生隨機數，如果隨機數小於交配的機率，發生交配
		# select crossover point that is not on the end of the string
		#隨機選擇一個交配點
		# -2 確保選擇的交配點不在基因的末端
		#如果染色體的長度為 10，那麼 len(p1)-2 就是 8
		pt = randint(1, len(p1)-2) 
		# perform crossover
		#基因分割，將分割的片段組合在一起，形成兩個新的子代。
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]

# mutation operator
# 突變
def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mut: #隨機數小於突變率r_mut
			# flip the bit
			bitstring[i] = 1 - bitstring[i] #將 0 變為 1，或將 1 變為 0

# genetic algorithm
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
	# initial population of random bitstring
	pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
	# keep track of best solution
	best, best_eval = 0, objective(pop[0])
	# enumerate generations
	for gen in range(n_iter):
		# evaluate all candidates in the population
		scores = [objective(c) for c in pop]
		# check for new best solution
		for i in range(n_pop):
			if scores[i] < best_eval: # assume smaller the score the better
				best, best_eval = pop[i], scores[i]
				print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))
		# select parents
		selected = [selection(pop, scores) for _ in range(n_pop)]
		# create the next generation
		children = list()
		for i in range(0, n_pop, 2):
			# get selected parents in pairs
			p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
			for c in crossover(p1, p2, r_cross):
				# mutation
				mutation(c, r_mut)
				# store for next generation
				children.append(c)
		# replace population
		pop = children
	return [best, best_eval]



# define the total iterations
n_iter = 100
# bits
n_bits = 20
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)


# perform the genetic algorithm search
best, score = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
print('f(%s) = %f' % (best, score))




# GA parameterization for the Southwestern Airways Crew Scheduling Problem

# define the total iterations
n_iter = 30
# bits
n_bits = 12
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)

# perform the genetic algorithm search
best, score = genetic_algorithm(southwest, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
print('f(%s) = %f' % (best, score))