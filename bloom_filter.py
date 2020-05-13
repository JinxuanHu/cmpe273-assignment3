
import math 
import mmh3 
from bitarray import bitarray 

class BloomFilter(object): 

	def __init__(self, key_nums,probablity): 
        # self.key_nums = key_nums
		self.probablity = probablity 
		self.array_size = self.get_array_size(key_nums,probablity) 
		self.hashes = self.get_hash_count(self.array_size,key_nums) 
		self.bit_array = bitarray(self.array_size) 
		self.bit_array.setall(0) 

	def add(self, key): 
		
		value_list = [] 
		for i in range(self.hashes): 
			value = mmh3.hash(key,i) % self.array_size 
			value_list.append(value) 
			self.bit_array[value] = True

	def is_member(self, key): 
		for i in range(self.hashes): 
			value = mmh3.hash(key,i) % self.array_size
			if self.bit_array[value] == False: 
				return False
		return True

	
	def get_array_size(self,n,p): 
		m = -(n * math.log(p))/(math.log(2)**2) 
		return int(m) 

	def get_hash_count(self, m, n): 
		k = (m/n) * math.log(2) 
		return int(k) 
