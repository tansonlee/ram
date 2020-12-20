from trie import empty_trie, insert, fetch

# ram
# ram_store(ram, address, value)
# ram_fetch(ram, address)

ram = empty_trie

def ram_store(ram, address, value):
	return insert(ram, address, value)

def ram_fetch(ram, address):
	return fetch(ram, address)

def core_dump(ram):
	def helper(ram):
		for i in range(1001):
			fetched_value = fetch(ram, i)
			if fetched_value is not None:
				print(f"[{i}]: {fetched_value}")

	print("-----------------------")
	helper(ram)
	print("-----------------------")

my_ram = ram_store(ram_store(ram, 77, 1010), 2, 999)
core_dump(my_ram)

my_ram_replace_2 = ram_store(my_ram, 2, 111)
core_dump(my_ram_replace_2)